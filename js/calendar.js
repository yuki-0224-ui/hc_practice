class Calendar {
        static DAYS_IN_WEEK = 7;

        static DISPLAY = {
                SPACE_PER_DAY: 3, // 日付の表示幅（2桁 + 空白1文字）
                DATE_PADDING: 2, // 日付を2桁で右寄せ表示するためのパディング幅
        };

        static MONTH_NAMES = [
                "1月",
                "2月",
                "3月",
                "4月",
                "5月",
                "6月",
                "7月",
                "8月",
                "9月",
                "10月",
                "11月",
                "12月",
        ];

        // 指定された年月の1日の曜日を取得
        static getFirstDay(year, month) {
                return new Date(year, month - 1, 1).getDay();
        }

        // 指定された年月の最終日を取得
        static getLastDate(year, month) {
                return new Date(year, month, 0).getDate();
        }

        static generate(year, month) {
                const firstDay = Calendar.getFirstDay(year, month);
                const lastDate = Calendar.getLastDate(year, month);

                // ヘッダー部分の生成（年月と曜日）
                let calendar = `      ${
                        Calendar.MONTH_NAMES[month - 1]
                } ${year}\n`;
                calendar += "日 月 火 水 木 金 土\n";

                // カレンダー本体の生成
                let currentDay = 1;
                let line = "".padStart(
                        firstDay * Calendar.DISPLAY.SPACE_PER_DAY,
                );

                for (let i = firstDay; currentDay <= lastDate; i++) {
                        // i > 0：最初の週での不要な改行を防ぐ（firstDayが0の場合）
                        if (i > 0 && i % Calendar.DAYS_IN_WEEK === 0) {
                                calendar += line.trimEnd() + "\n";
                                line = "";
                        }
                        line += currentDay.toString().padStart(
                                Calendar.DISPLAY.DATE_PADDING,
                        ) + " ";
                        currentDay++;
                }

                // 最終行の処理
                if (line) {
                        calendar += line.trimEnd() + "\n";
                }
                return calendar;
        }
}

// -m オプションで月の指定が可能。省略時はmain()でシステムの現在の月が使用される
function parseArgs() {
        const args = process.argv.slice(2);
        const options = { month: null };

        if (args.length === 0) return options;

        if (args[0] !== "-m" || args.length !== 2) {
                throw new Error("Usage: node calendar.js [-m month]");
        }

        const month = parseInt(args[1]);
        if (isNaN(month) || month < 1 || month > 12) {
                throw new Error("月は1から12の整数で指定してください");
        }

        options.month = month;
        return options;
}

function main() {
        try {
                const options = parseArgs();
                const currentDate = new Date();
                const month = options.month || currentDate.getMonth() + 1;
                const year = currentDate.getFullYear();
                process.stdout.write(Calendar.generate(year, month));
        } catch (error) {
                console.error(`Error: ${error.message}`);
                process.exit(1);
        }
}

main();

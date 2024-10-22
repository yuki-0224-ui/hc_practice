import argparse
from datetime import datetime, timedelta
import sys


class Calendar:
    WEEK_DAYS = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    HIGHLIGHT_CODE = "\033[7m"
    RESET_CODE = "\033[0m"

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_first_day(self):
        return datetime(self.year, self.month, 1)

    def get_last_day(self):
        first_day = self.get_first_day()
        return (first_day.replace(day=28) + timedelta(days=4)).replace(
            day=1
        ) - timedelta(days=1)

    def get_year_month_string(self):
        return self.get_first_day().strftime("%B %Y")

    def format_day(self, current_day, today):
        if current_day.date() == today:
            return f"{self.HIGHLIGHT_CODE}{current_day.day:2d}{self.RESET_CODE}"
        else:
            return f"{current_day.day:2d}"

    def generate_first_week(self, current_day, today):
        SUNDAY = 6
        # 月の最初の週の空白部分を埋める
        first_week = ["  "] * current_day.weekday()

        while current_day.weekday() != SUNDAY:
            day_str = self.format_day(current_day, today)
            first_week.append(day_str)
            current_day += timedelta(days=1)

        day_str = self.format_day(current_day, today)
        first_week.append(day_str)
        current_day += timedelta(days=1)
        return first_week, current_day

    def generate_week(self, current_day, last_day, today):
        week = []

        while len(week) < 7 and current_day <= last_day:
            day_str = self.format_day(current_day, today)
            week.append(day_str)
            current_day += timedelta(days=1)
        return week, current_day

    def generate_calendar(self):
        first_day = self.get_first_day()
        last_day = self.get_last_day()
        year_month = self.get_year_month_string()
        width = len(" ".join(self.WEEK_DAYS))

        calendar_lines = [
            year_month.center(width),
            " ".join(self.WEEK_DAYS),
        ]

        current_day = first_day
        today = datetime.now().date()

        first_week, current_day = self.generate_first_week(current_day, today)
        calendar_lines.append(" ".join(first_week))

        while current_day <= last_day:
            week, current_day = self.generate_week(current_day, last_day, today)
            calendar_lines.append(" ".join(week))

        return "\n".join(calendar_lines)


class CustomArgParser(argparse.ArgumentParser):
    def error(self, message):
        message = message.replace("argument -m/--month: ", "")
        print(message, file=sys.stderr)
        sys.exit(2)


def validate_month(month):
    if not month.isdigit() or not (1 <= int(month) <= 12):
        raise argparse.ArgumentTypeError(
            f"{month} is neither a month number (1..12) nor a name"
        )
    return int(month)


def parse_arguments():
    parser = CustomArgParser(description="Display a calendar for a specific month")
    parser.add_argument(
        "-m",
        "--month",
        type=validate_month,
        help="Month to display (1-12)",
        default=datetime.now().month,
    )

    return parser.parse_args()


def main():
    try:
        args = parse_arguments()
        now = datetime.now()
        c = Calendar(now.year, args.month)
        calendar = c.generate_calendar()
        print(calendar)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

NUM_HOLES = 18
SCORE_NAMES = {
    0: "パー",
    1: "バーディ",
    2: "イーグル",
    3: "アルバトロス",
    4: "コンドル",
}

par_scores = list(map(int, input().split(",")))
actual_scores = list(map(int, input().split(",")))


def get_score_name(score):
    if score in SCORE_NAMES:
        return SCORE_NAMES[score]
    elif score == -1:
        return "ボギー"
    else:
        return f"{-score}ボギー"


results = []
for i in range(NUM_HOLES):
    if par_scores[i] - actual_scores[i] == par_scores[i] - 1 and par_scores[i] != 5:
        results.append("ホールインワン")
        continue
    score = par_scores[i] - actual_scores[i]
    results.append(get_score_name(score))

print(",".join(results))

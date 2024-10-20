import sys

# 循環インポート回避のため、標準ライブラリのパス(Dockerコンテナ内)を先頭に追加
STDLIB_PATH = "/usr/local/lib/python3.9"
if STDLIB_PATH in sys.path:
    sys.path.remove(STDLIB_PATH)
sys.path.insert(0, STDLIB_PATH)

import random


def shuffle_groups(members):
    shuffled_members = members.copy()
    random.shuffle(shuffled_members)
    group_size = random.randint(2, 3)
    group1 = sorted(shuffled_members[:group_size])
    group2 = sorted(shuffled_members[group_size:])
    return group1, group2


test_members = ["A", "B", "C", "D", "E", "F"]

group1, group2 = shuffle_groups(test_members)
print("Group1:", group1)
print("Group2:", group2)

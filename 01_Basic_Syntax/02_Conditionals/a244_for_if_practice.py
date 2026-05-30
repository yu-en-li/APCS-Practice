# APCS Title: a244. 完全奇數
# APCS Complexity: O(1)
# APCS Tag: 條件判斷, 數學與數論, 基礎語法
# APCS Difficulty: 1

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == 1:
        print(b + c)
    elif a == 2:
        print(b - c)
    elif a == 3:
        print(b * c)
    elif a == 4:
        print(b // c)

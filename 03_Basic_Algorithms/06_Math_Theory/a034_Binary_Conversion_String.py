# APCS Title: a034. 二進位制轉換
# APCS Complexity: O(log N)
# APCS Tag: 基礎語法, 數學與數論
# APCS Difficulty: 1
# APCS Note: 

import sys
while True:
    try:
        n = int(input())
        ans = bin(n)[2:]
        print(ans)

    except EOFError:
        break
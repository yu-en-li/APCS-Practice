# APCS Title: a453. TOI2010 第一題：一元二次方程式
# APCS Complexity: O(M)
# APCS Tag: Math_Theory, Conditionals
# APCS Difficulty: 1
# APCS Note:

import math

n = int(input())
for _ in range(n):

    a, b, c = map(int, input().split())

    if (b * b - 4 * a * c) >= 0:
        if math.isqrt(b * b - 4 * a * c) **2 == (b * b - 4 * a * c) :
                   
            print("Yes")

        else:
                    
            print("No")

    else:
                
        print("No")

  


import sys;

while True:
    try:

        n = int(input())
        ans = []

        if (n == 0):
            print(0)
            continue

        while (n > 0):
            ans.append(n % 2)
            n //= 2                #從末位讀入

        ans.reverse()
        print(*ans,end="")

        print()

    except EOFError:
        break
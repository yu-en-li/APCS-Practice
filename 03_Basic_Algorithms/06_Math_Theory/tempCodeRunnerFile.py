n = int(input())
first = 1
cnt = 0

for i in range(2, int(n**0.5 + 1)):
    if n % i == 0:
        cnt = 0

        while n % i == 0:
            n //= i
            cnt += 1

        if first == 0:
            print(" * ", end="")

        print(i)

        if cnt >= 1:
            print(f"^{cnt}", end="")

        first = 0

        if n != 1:
            if first == 0:
                print(" * ", end="")

            print(n, end="")

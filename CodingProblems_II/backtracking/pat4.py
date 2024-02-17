def pattern(n):
    for i in range(0, n):
        for _ in range(0, i + 1):
            print("*  ", end="")
        print("\r")

pattern(5)


def pattern2(n):
    for i in range(n, -1, -1):
        for _ in range(0, i + 1):
            print("*  ", end="")
        print("\r")

pattern2(5)

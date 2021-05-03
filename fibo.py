def recursive_nth_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    n = int(input("Type in n:"))
    result = recursive_nth_fibo(n)
    fib_seq = []

    for num in range(n + 1):
        fib_seq.append(recursive_nth_fibo(num))

    fib_seq = [recursive_nth_fibo(num) for num in range(n + 1)]
    print(fib_seq)

if __name__ == '__main__':
    main()

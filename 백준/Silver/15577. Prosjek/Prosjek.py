def calculateAverage(arr):
    if len(arr) == 2:
        return (arr[0] + arr[1])/2
    else:
        return calculateAverage([(arr[0] + arr[1])/2] + arr[2:])


def main():
    n = int(input())
    num = [float(input()) for _ in range(n)]
    num.sort()

    print(calculateAverage(num))

if __name__ == "__main__":
    main()

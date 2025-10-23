def solution(n: int, arr: list[int]):
    summed = sum(arr)
    if (not summed % 3 == 0):
        return 0

    target_sum = summed / 3
    accum = 0
    start = 0
    ways = 0

    for i in range(n):
        accum += arr[i]
        if (accum == target_sum):
            ways+=1

        while (accum > target_sum and start <= i):
            accum -= arr[start]
            start += 1

    return ways

def main():
    n = int(input())
    arr = list(map(int, input().split())) 
    print(solution(n, arr))

if __name__ == "__main__":
    main()

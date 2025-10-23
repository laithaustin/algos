# so key insight here:
# firstly we need to know whether the solution is feasible
# then we need to basically figure out how much each "section" needs to sum to, T
# first section has total sum of T / 3
# second is 2 T / 3
# okay with the above in mind we also need to figure out the number of ways we can get the first sum # amount and the second sum amount.
# nice heuristic to realize is that if we know that the final possible position where sum is 2 T / 3 - the rest has to add up to T / 3 for that last section (proof is by the fact that we checked that our total sum is divisible by 3).
# why this maps to a prefix sum problem:
# prefix sum is all about computing p[i] where we describe the number of ways we satisfy a condition
# here p[i] represents the number of ways we can get T/3 * i

def solution(n: int, arr: list[int]):
    # pre compute the split sum target
    total = sum(arr)
    res = 0
    ways = 0
    if (total % 3):
        return res
    else:
        target = total / 3

        accum = 0
        start = 0
        # count the number of ways from the first pivot
        for i in range(len(arr) - 1): # second pivot should not be inclusive 
            accum += arr[i]
            # print(f"iteration {i}: {accum}")
            if (accum == 2 * target):
                # print(f"incrementing by {ways}")
                res += ways
            # new possible first pivot
            if (accum == target):
                ways += 1

    return res



def main():
    n = int(input())
    arr = list(map(int, input().split())) 
    print(solution(n, arr))

if __name__ == "__main__":
    main()

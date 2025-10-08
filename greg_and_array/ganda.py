def solution(operations: list[list[int]], arr: list[int], queries: list[list[int]], n: int, m: int, k: int):
    # diff array for the operations
    diff_arr_ops = [0] * (m + 2)
    for q in queries:
        diff_arr_ops[q[0]] += 1
        diff_arr_ops[q[1] + 1] -= 1

    # compute presum for ops
    p = [0] * (m + 1)
    for i in range(1, m+1):
        p[i] = p[i-1] + diff_arr_ops[i]

    # diff array for input 
    diff_arr = [0] * (n + 2)
    for i in range(len(operations)):
        op = operations[i]
        op_num = i + 1  # Convert 0-indexed to 1-indexed operation number
        diff_arr[op[0]] += op[2] * p[op_num]
        diff_arr[op[1] + 1] -= op[2] * p[op_num]

    # compute presum
    p = [0] * (n + 1)
    for i in range(1, n+1):
        p[i] = p[i-1] + diff_arr[i]
    
    # return final array
    for i in range(len(arr)):
        print(arr[i] + p[i+1], end=" ")

def main():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    operations = []
    for i in range(m):
        operations.append(list(map(int, input().split())))
    
    queries = []
    for i in range(k):
        queries.append(list(map(int, input().split())))
    
    solution(operations, arr, queries, n, m, k)

if __name__ == "__main__":
    main()

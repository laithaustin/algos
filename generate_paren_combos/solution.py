def generate_combinations(n):

    result = []

    # for a given index i place an op. if op == cp == n we have a solution

    # if op or cp > n this is not a viable solution

    dfs(n, result, 0, 0, "")

    return result

    

def dfs(n, result, op, cp, curr):

    if (n < op or n < cp or op < cp):

        return

    elif (len(curr) == n*2 and curr[0] == ')'):

        return

    elif (len(curr) == n*2 and curr[n*2 - 1] == '('):

        return

    elif (n == op and cp == op):

        result.append(curr)

        return

    

    dfs(n, result, op+1, cp, curr + "(")

    dfs(n, result, op, cp+1, curr + ")")

    



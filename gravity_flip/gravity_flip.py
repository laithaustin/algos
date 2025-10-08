def gravity_flip(n, columns):
    """
    Given n columns of toy cubes, simulate a gravity flip.

    Initially, gravity pulls cubes downwards. After the gravity switch,
    it pulls all cubes to the right side of the box.

    Args:
        n: Number of columns (1 ≤ n ≤ 100)
        columns: List of n integers, where columns[i] is the number of cubes
                 in the i-th column (1 ≤ columns[i] ≤ 100)

    Returns:
        List of n integers representing the number of cubes in each column
        after the gravity switch

    Examples:
        >>> gravity_flip(4, [3, 2, 1, 2])
        [1, 2, 2, 3]

        >>> gravity_flip(2, [3, 8])
        [3, 8]
    """
    # naive solution iterate backwards and swap with next biggest number
    # but if we think about this for long enough the real heuristic is that we are effectvely
    # sorting the array
    columns.sort()
    return columns


if __name__ == "__main__":
    #parse two inputs: col_num and arr
    col_num = int(input())
    arr = list(map(int, input().split()))
    print(*gravity_flip(col_num, arr))

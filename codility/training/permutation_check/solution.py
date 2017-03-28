
def solution(A):

    max_val = len(A)

    idx = 0

    while idx < max_val:

        val = A[idx]

        if val < idx + 1:
            return 0
        if val > max_val:
            return 0

        if val == idx + 1:
            idx = idx + 1
        elif A[idx] == A[val - 1]:
            return 0
        else:
            A[idx] = A[val - 1]
            A[val - 1] = val

    return 1

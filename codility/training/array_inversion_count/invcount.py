

def solution(A):

    inver = 0

    for i in range(len(A) - 1):
        ai = A[i]
        for j in range(i + 1, len(A)):
            if ai > A[j]:
                inver += 1

    return inver


while True:

    print "Enter a list of integers separated by spaces: "

    try:
        array = [int(x) for x in raw_input().split()]
    except ValueError:
        print "Error: invalid integer number found."
        continue

    print "Number of inversions: %d" % solution(array)

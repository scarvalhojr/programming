
def solution(N):

    if N < 5:
        return 0

    while N % 2 == 0:
        N = N >> 1

    gap = max_gap = 0

    while N > 0:

        if N % 2 == 0:
            gap = gap + 1
        else:
            if gap > max_gap:
                max_gap = gap
            gap = 0

        N = N >> 1

    return max_gap


while True:

    print "Enter an integer number: "
    input = raw_input().strip()

    try:
        num = int(input)
    except ValueError:
        print "Invalid integer: '%s'" % input
        continue

    print "Binary representation: %s" % bin(num)
    print "Longest binary gap: %d" % solution(num)

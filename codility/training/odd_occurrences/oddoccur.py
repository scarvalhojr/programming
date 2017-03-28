

def solution(A):

    unpaired = 0

    for n in A:
        unpaired = unpaired ^ n

    return unpaired


while True:

    print "Enter an odd number of integers separated by spaces: "

    try:
        array = [int(x) for x in raw_input().split()]
    except ValueError:
        print "Error: invalid integer number found."
        continue

    if len(array) % 2 == 0:
        print "Error: even number of integers found."
        continue

    print "Unpaired element: %d" % solution(array)

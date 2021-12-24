# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height.
# You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height.
# This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height,
# then return the height.


def equalstacks(h1, h2, h3):
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)
    mnsum = min(sum1, sum2, sum3)
    while sum1 != sum2 and sum2 != sum3:
        while sum1 > mnsum:
            sum1 = sum1 - h1[0]
            h1 = h1[1:]
            if sum1 < mnsum:
                mnsum = sum1
                break
        while sum2 > mnsum:
            sum2 = sum2 - h2[0]
            h2 = h2[1:]
            if sum2 < mnsum:
                mnsum = sum2
                break
        while sum3 > mnsum:
            sum3 = sum3 - h3[0]
            h3 = h3[1:]
            if sum3 < mnsum:
                mnsum = sum3
                break

    return mnsum
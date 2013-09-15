import sys
from math import log10, pow

def brute(n):
    # Counts numbers that do not contain the digit '4'
    # that are less than n
    count=0
    for i in range(0, n):
        temp = i
        nofours = True
        while temp > 0:
            #digit = temp - 10 * (temp/10) # digit is the remainder ...
            digit = temp % 10
            if digit == 4:
                nofours = False
                break
            temp = temp/10
        if nofours:
            count = count+1
    print "There are %d numbers less than %d that do not contain the digit 4" % (count, n)
    print "There are %d numbers less than %d that do contain the digit 4" % (n-count, n)

# works for two digits
def fast(n):
    ex = 0
    if n > 49:
        ex = 10
    if n > 39 and n < 50:
        ex = n-40
    if n > 44:
        ex = ex -1
    r = n - 10 * (n/10)
    rp = 0
    if r > 4:
        rp = 1
    return n/10 + rp + ex
    
n=int(sys.argv[1])

print "Fast: %d number containing 4's under %d" % (fast(n), n)
brute(n)
# Okay, we're going to get this!!!!!
# So for the one's there is ... 
# 1 '4' with one digit
# 10 '4's with two digits
# 100 '4's with three digits ...
# so that is 10^(digits-1)
# but, in the second digit there are 10 '40's
# so with two digits there are 10 '4's in the ones column + 10 '4's in the two's column
# minus the overlap (1)
# Then for three digits there are
# 100 4's in the ones column + 10 groups of 4's in the two's column (10 * 10) + 100 4's 
# in the hundreds column
# n/10 = number of ones columns
# n/100 = number of two's columns (* 10 per set)
# so it does come back to
# n/10 + 10 * n/100 + 100 * n/1000 + ...
# n/10 + (10*(n/100)) + (100*n/1000)
# but this simplifies to ...
# n/10 + n/10 + n/10 ... 
# or d * n/10
# so how about for overlaps ... 
# with one digit there are no overlaps
# with two digits, there is one overlap (44)
# with three digits, there are 10 overlaps (44, 144, 244, ... 944) 
# plus 10 more overlaps (404, 414, 424, ... 494) minus the intersection?
# but its also a "double overlap" aka 444
# with four digits, there are 4004, 4014, 4024, ... or all the overlaps with three digits
# times 10 (so 100 overlaps) plus ... all the overlaps not counted previously caused by the 4000's...
# so 4004, 4014, 4024, 4034, ... there's one of these for every group of 10, so 1000 / 10 = 100
# in summary...
# with three digits, there are 100 overlaps + 100 overlaps
# 
# one digit, 0 
# two digits, 1 (10^0)
# three digits, 10 + 10  (2 * 10^1)
# four digits, 100 + 100 ( 2 * 10^2)



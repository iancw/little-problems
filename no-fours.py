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

def fast(n):
    d = int(log10(n))
    print "%d" % (d*n/10)
    c = 0
    for i in range(0, d):
        tp = int(pow(10, i))
        cp = tp * n/(tp*10)
        print "i=%d, tp=%d, cp=%d" % (i, tp, cp)
        c = c + cp
    print "Counted %d fours below %d" % (c, n)

n=int(sys.argv[1])

fast(n)
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

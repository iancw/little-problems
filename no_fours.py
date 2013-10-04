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
#                print "%d has a 4 in it" % i
                nofours = False
                break
            temp = temp/10
        if nofours:
            count = count+1
    #print "There are %d numbers less than %d that do not contain the digit 4" % (count, n)
    #print "There are %d numbers less than %d that do contain the digit 4" % (n-count, n)
    return n-count

# works for two digits
def fast(n):
    if n == 0:
        return 0
    p = int(log10(n))
    # c - counts the fours up to the order of magnitude
    c = 0
    # loop through each digit in the number (except the most significant)..
    for i in range(0, p):
        # 1 4 in digit 0
        # 19 4's in digit 1
        # 176 4's in digit 2 ... 
        c = 10 * c +  int(pow(10, i)) - c
    # now count just the digits between n and 10^(p-1)
    # omag, eg for 40 would be 10, for 400 would be 100
    omag = int(pow(10, p))
    # So for like 14 .... we'd have a residual of 4
    # Also for like 44, we have a residual of 34 ... 
    omag_residual = n - omag
    # multiple the count for each omag (e.g. if there are 19 4's below 100) 
    # and n is 500, we count 5 * 19
    resid_count = ((n-omag) / omag) * c
    omag4 = 4 * omag
    omag5 = 5 * omag
    # count the extra fours 4's in e.g. the 4xx's for example
    extra_c = 0
    if n >= omag4:
        # The goal of this section is to add in all the fours from this 
        # order of magnitude
        # e.g. for number 4xx, we need to count one for every number
        # greater than 400 less than 500
        # for number 4x, we need to count one for every number over 40
        # and less than 50
        morefours = n - omag4
        extra_c = min(morefours, omag) # don't count more than omag 4's
    # I'm not sure why this is necessary
    # My theory is that really resid_count should have + 1 c, and adding
    # c back in solves that, except when we add all the 4's above omag4
    # that cancels out because we've double counted ...
    # ...except why does it only kick in at omag5 and above?
    # i guess because we subtract omag from n ... 
    if n >= omag5:
        c = 0
    lesser_digits = 0
    if n < omag4 or n >= omag5:
        lesser_digits = fast(omag_residual % omag)
#    print "n=%d, resid_count=%d, c=%d, extra_c=%d, lesser_digits=%d" % (n, resid_count, c, extra_c, lesser_digits)
    result = resid_count + c + extra_c + lesser_digits
    return result 

if __name__ == '__main__':
    n=int(sys.argv[1])
    print "There are %d numbers less than %d that do contain the digit 4" % (brute(n), n)
    print "Fast: %d number containing 4's under %d" % (fast(n), n)
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



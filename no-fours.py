import sys
from math import log10, pow

n=int(sys.argv[1])
count=0

# Counts numbers that do not contain the digit '4'
# that are less than n
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
d = int(log10(n)) # number of digits
print "d is %d" % d

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
# n/10 + 10 * n/100 + 100 * n/1000

def num_fours_in_class(d):
    if d < 0:
        return 0
    if d == 0:
        return 1
    return pow(10, d) + num_fours_in_class(d-1)

#c2 = n * d * pow(10, d-1)/pow(10, d)
#c2 = n - ((n+5)/10 + (10*n/100))
for i in range(0, 5):
    print "Num fours with %d digit = %d" % (int(pow(10, i)), num_fours_in_class(i))
# So every number which has n - 10 * (n/10) = 4 is invalid ...
# what's an efficient way to generalize that...

# So for every set of 10 digits, there is one digit with a four in it
# ... except they start repeating, so for < 10 there is one (4), for < 100 there is
# 4, 14, 24, 34, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 54, 64, 74, 84, 94
# so it's n/10 (for how many sets of 10) + 10 for each set over 100 ... 
# n/10 + (10n/100 - 1) + 
# So it's probably like counting how many sets of 10 are below a number ...
# so like n - (n/10)

# n/10 + 10 * n/100 + 100 * n/1000
# n (1/10 + 10/100 + 100/1000)
# n ( 1/10 ( 1 + 1/10 + 1/100 + ... ))
# n * (10 ^ d-1)/(10 ^ d)
# (log10 n + 1) = how many digits in n
####################################################################
# This scipt calculates the integration over an interval using
# trapezoid rule.
# Author: Pooja Rao
# Command line arguments:
# Referenece: https://en.wikipedia.org/wiki/Trapezoidal_rule 
####################################################################

import numpy as np
import sys

# file name to store the result in
#fileOut = "/work/05375/prao5/stampede2/multiple_serial/out_trapezoid.dat"
fileOut="out_trapezoid.dat"

# command line args
# lower bound of the interval
a = float(sys.argv[1]) 
# upper bound of the interval
b = float(sys.argv[2])
# number of intervals
N = int(sys.argv[3])

# first argument is always the script name
print "Name of script: ", (sys.argv[0])
# number of arguments
print "Number of args: ", len(sys.argv)
# print the list of all the arguments
print "List of all args: ", (sys.argv)

# creates N equally spaced intervals between 0 and 1 
x = np.linspace(a, b, N+1)

# reciprocal of spacing between the intervals 
h = (x[1]-x[0])

# function to calculate square of a function
# this is used for testing
def func_square(x):
  return x*x*x

# main part of the program where the numerical integral is calculated
sum_f = 0.0 # to store the integral
for i in range (0,N):
  sum_f += 0.5* (func_square(x[i]) + func_square(x[i]))*h  

print "integral is: ", sum_f

# save the result into a text file 
np.savetxt(fileOut, [sum_f])

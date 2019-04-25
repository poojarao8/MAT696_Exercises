####################################################################
# This scipt calculates the integration over an interval using
# trapezoid rule.
# Author: Pooja Rao
# Command line args: a (lower bound), b (upper bound), 
#                    N (total num of intervals)
# Referenece: https://en.wikipedia.org/wiki/Trapezoidal_rule 
####################################################################

import numpy as np
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

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

# number of intervals per mpi process
n = N/size
assert(N%size==0), "N is not a multiple of size!!"

# creates N equally spaced intervals between a and b 
h = (b-a)/N

# contains the end point of the intervals for each proc
x = np.linspace(a + rank*n*h, a+(rank+1)*n*h, n+1)

print x

# function to calculate square of a function
# this is used for testing
def f(x):
  return x*x*x

# main part of the program where the numerical integral is calculated
sum_f = 0.0 # to store the integral
for i in range (0, n):
  sum_f += 0.5* ( f(x[i]) + f(x[i+1]) )*h  

print "local integral is: ", sum_f

# collect the result from other processes on process 0
# add everything received on process 0
if (rank==0):
  total_integral = sum_f
  recv_buf = np.zeros(1)
  comm.Recv(recv_buf)
  #print recv_buf
  total_integral += recv_buf[0] 
  print total_integral
else:
  comm.Send(sum_f, dest=0)
  

# save the result into a text file
if (rank==0): 
  np.savetxt(fileOut, [total_integral])

# the purpose of this script is to compare
# with the result from HYPRE
# https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html

import sys
import numpy 
import scipy
from scipy import sparse
from scipy.sparse import linalg
from numpy import linalg
from numpy.linalg import matrix_rank

# if you uncomment this, you can print the whole matrix instead of a 
# truncated version
#np.set_printoptions(threshold=sys.maxsize)

n = 8 # grid size in x-direction
N = n*n # total grid points

# calculate dx
dx = 2*numpy.pi/n

# form matrix A
A = numpy.zeros((N,N))

### First fill each diagonal entry
# fill the diagonal entries
for i in range(0,N):
  A[i][i] = 4.0

### Here we fill the entries corresponding to the right neighbor.  Typically this will be the off-diagonal
###   directly above the diagonal, however because of periodicity, everytime you reach the end of the row,
###   i.e. when matrix row % n == n-1, the right neighbor is through the boundary, so handle that case.
# fill the right entries, keeping in mind the periodicity
for i in range(0,N):
  if ((i % n) == n-1):
    A[i][i-(n-1)] = -1.0
  else:
    A[i][i+1] = -1.0

### Here we fill the entries corresponding to the left neighbor.  Same idea of periodicity, here we are
###   worried about the first entry in each row, i.e the matrix row % n == 0.
# fill the left entries 
for i in range(0,N):
  if ((i % n) == 0):
    A[i][i+(n-1)] = -1.0
  else:
    A[i][i-1] = -1.0

### Here we fill the entries correspond to the upper neighbor.  Periodicity in the y-direction kicks in
###   when we are in the top row, or when we are in the last n matrix rows.
# fill the up entries
for i in range(0,N):
  if (i < n*(n-1)):
    A[i][i+n] = -1.0
  else:
    A[i][i-(n-1)*n] = -1.0

### Here we fill the entries corresponding to the lower neighbor.  We have to handle the first row of
###   entries, associated with the first n matrix rows.
# fill the down entries
for i in range(0,N):
  if (i >= n):
    A[i][i-n] = -1.0
  else:
    A[i][i+(n-1)*n] = -1.0

# take one of the values as 0 to make the matrix non-singular
# set the rest of the values in the correpsonding row to 0
# set the column values in the correspsomfinfg column as 0
for j in range(0,N):
  A[N-1][j] = 0.0

for i in range(0,N):
  A[i][N-1] = 0.0
  
# take one of the values as 0 to make the matrix non-singular
A[N-1][N-1] = 1.0

print "Matrix is: "
print A
print "Rank of matrix is: "
print numpy.linalg.matrix_rank(A)
print A.shape[0]
print "Number of non-zero values is: "
print numpy.count_nonzero(A)

# form vector b
b = numpy.zeros(N)
b = numpy.full(N, 2.0)

def set_b(x, y):
  return numpy.sin(x)*numpy.sin(y)

for i in range(0, N):
  x = (i%n)*dx
  y = (i//n)*dx
  b[i] = dx*dx*set_b(x, y)

# to adjust for singularity, set the last value to 0
b[N-1] = 0.0

print b

# form vector b
x = numpy.zeros(N)

# call the linear solver here
x = scipy.linalg.solve(A, b)
print x*2.0*dx*dx
print numpy.sum(numpy.abs(b - x))/N
#print scipy.sparse.linalg.eigs(A)

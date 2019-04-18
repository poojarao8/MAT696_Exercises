####################################################################
# This scipt demonstrates point to point communication using 
# blocking send and recv
# Author: Pooja Rao
####################################################################

import numpy as np
from mpi4py import MPI

# process id of the current process
rank = MPI.COMM_WORLD.rank

if rank==0:
  # create an array on process 0
  data = np.array([10,20,30])
  MPI.COMM_WORLD.send(data, dest=1, tag=10)
elif rank==1:
  # receive the data that has been sent into data
  data =  MPI.COMM_WORLD.recv(source=0,tag=10)
  print ("Received ", data, " from process rank 0")


from mpi4py import MPI

# process id of the current process
rank = MPI.COMM_WORLD.rank

# total number of mpi processes
size = MPI.COMM_WORLD.size

print ("my rank is ", rank)
print ("total num of procs is ", size)

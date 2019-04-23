####################################################################
# This scipt demonstrates an instance of collective communication
# mpi_scatter
# source: https://buildmedia.readthedocs.org/media/pdf/mpi4py/latest/mpi4py.pdf
####################################################################

from mpi4py importMPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

data = np.array(size)

if rank == 0:
  for i in range(size):
    data[i] = (i+1)**2
else:
  data =None

data = comm.scatter(data, root=0)
assert data == (rank+1)**2

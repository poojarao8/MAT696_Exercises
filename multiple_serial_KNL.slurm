#!/bin/bash
#Launch this job by executing this command on a Stampede2 login node:
# sbatch multiple_serial_KNL.slurm
#
# This script has been adapted from the Stampede2's webpage: https://portal.tacc.utexas.edu/user-guides/stampede2
#---------------------------------------------------------------------

#SBATCH -J multiple_mpi_job     # Job name
#SBATCH -o multiple_mpi_job.o  # name of std output file
#SBATCH -e multiple_mpi_job.e  # name of stderr error file
#SBATCH -p normal               # Queue name
#SBATCH -N 1                    # Total # of nodes 
#SBATCH -n 2                    # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 00:01:00             # Run time (hh:mm:ss)
#SBATCH --mail-user=poojarao12@gmail.com # enter your email (optional)
#SBATCH -A TG-DMS190011         # Allocation name (in case more than one)


# This example will run 3 MPI applications using 32 tasks,
# 16 tasks, and 16 tasks

# Launch each MPI application using the "-o" and "-n" flags
# in the background
#Application 1 (serial)
ibrun -o 0 -n 1 python trapezoid.py 0 0.5 10000 &

#Application 2 (serial)
ibrun -o 1 -n 1 python trapezoid.py 0.5 1 10000 &

#Wait for all the MPI applications to finish
wait

#----------------------------------------------------------------------


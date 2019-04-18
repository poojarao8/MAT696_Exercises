#!/bin/bash
#Launch this job by executing this command on a Stampede2 login node:
# sbatch mpi_KNL.slurm
#
# This script has been adapted from the Stampede2's webpage: https://portal.tacc.utexas.edu/user-guides/stampede2
#---------------------------------------------------------------------

#SBATCH -J mympijob     # Job name
#SBATCH -o mympijob.o  # name of std output file
#SBATCH -e mympijob.e  # name of stderr error file
#SBATCH -p normal    # Queue name
#SBATCH -N 1         # Total # of nodes (must be 1 for serial)
#SBATCH -n 5         # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 00:00:30  # Run time (hh:mm:ss)
#SBATCH --mail-user=myname@myschool.edu
#SBATCH -A TG-DMS190011 # Allocation name (in case more than one)

# other commands as necessary after #SBATCH driectives
module list
module load python3 # in case you need python3 and it's not in your env
pwd
date

# Launch parallel code
ibrun -np 2 python3 mpi_p2p.py # change it to python3 if running with it
# if using python3, make sure it is loaded in your environment

#----------------------------------------------------------------------


#!/bin/bash
#Launch this job by executing this command on a Stampede2 login node:
# sbatch serial_KNL_normal.slurm
#
# This script has been adapted from the Stampede2's webpage: https://portal.tacc.utexas.edu/user-guides/stampede2
#---------------------------------------------------------------------

#SBATCH -J myjob     # Job name
#SBATCH -o myjob.o%  # name of std output file
#SBATCH -e myjob.e%  # name of stderr error file
#SBATCH -p normal    # Queue name
#SBATCH -N 1         # Total # of nodes (must be 1 for serial)
#SBATCH -n 1         # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 00:01:00  # Run time (hh:mm:ss)
#SBATCH --mail-user=myname@myschool.edu
#SBATCH -A TG-DMS190011 # Allocation name (in case more than one)

# other commands as necessary after #SBATCH driectives
module list
pwd
date

# Laaunch serial code
python hello_world.py

#----------------------------------------------------------------------


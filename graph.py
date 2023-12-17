from mpi4py import MPI
import numpy as np
import time

M = 20
N = 5

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

A = np.full((N, M), 3.0)
B = np.full(M, 2.0)
C = np.zeros(N)

t1 = time.time()
for j in range(N):
    C[j] = np.sum(A[j] * B)

comm.Allgather([C, MPI.DOUBLE], [B, MPI.DOUBLE])

t2 = time.time()
rt = t2 - t1

print(f"rank = {rank} Time = {rt}")

if rank == 0:
    for i in range(M):
        print(f"B = {B[i]}")

from mpi4py import MPI
import numpy as np
M = 20
N = 5

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

cart_comm = comm.Create_cart(dims=[size], periods=[True])
sour, dest = cart_comm.Shift(0, -1)
A = np.full((N, M), 3.0)
B = np.full(N, 2.0)
C = np.zeros(N)
t1 = MPI.Wtime()
for k in range(size):
    d = ((rank + k) % size) * N
    local_C = np.zeros(N)

    for j in range(N):
        for i1, i in enumerate(range(d, d + N)):
            local_C[j] += A[j, i] * B[i1]
    comm.Allreduce(local_C, C, op=MPI.SUM)
    B = np.roll(B, -N)
t2 = MPI.Wtime()
rt = t2 - t1
print(f"rank = {rank} Time = {rt}")
for i in range(N):
    print(f"rank = {rank} RM = {C[i] / size}")
cart_comm.Free()
MPI.Finalize()

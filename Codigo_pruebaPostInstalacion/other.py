import argparse
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

ps = argparse.ArgumentParser()
ps.add_argument('--pos1', required=True)
ps.add_argument('--pos2', required=True)

args = ps.parse_args()
pos1 = args.pos1
pos2 = args.pos2

if rank ==0:
    k = []
    k.append('r1')
    k.append(pos1)
    k.append(pos2)
    comm.send(k, dest=3, tag=14)

elif rank == 1:
    k = []
    k.append('r2')
    k.append(pos1)
    k.append(pos2)
    comm.send(k, dest=3, tag=24)

elif rank == 2:
    k = []
    k.append('r3')
    k.append(pos1)
    k.append(pos2)
    comm.send(k, dest=3, tag=34)

elif rank == 3:
    data=[]
    data.append(comm.recv(source=0, tag=14))
    data.append(comm.recv(source=1, tag=24))
    data.append(comm.recv(source=2, tag=34))

    print(data)


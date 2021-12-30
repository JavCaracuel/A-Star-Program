from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

class Node():
    def __init__(self, parent=None):
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0
        self.X = 0
        self.Y = 0

pepe=1

if rank == 0:
    data = Node(None)
    data.g=1
    data.h=2
    data.f=3
    data.X=4
    data.Y=5
    comm.send(data, dest=3, tag=11)
    #data es el dato que mandamos
    #dest es el numero de proceso que recibe data
    #el tag es el identificador para poder enviar mas de un mensaje al mismo proceso
elif rank == 2:
    data2 = Node(None)
    data2.g=6
    data2.h=7
    data2.f=8
    data2.X=9
    data2.Y=10
    
    comm.send(data2, dest=3, tag=12)
elif rank == 3:
    data = comm.recv(source=0, tag=11)
    data2 = comm.recv(source=2,tag=12)
    print("Soy el proceso:",comm.rank,"y he recibido",data)
    print("Soy el proceso:",comm.rank,"y he recibido",data2.f)


import Aestrella_MPI
from mpi4py import MPI
import time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#1,3,5,6

#1,5,2,9


print("Proceso:"+ str(rank))
inicio=time.time()
if(rank==0 ):
    Aestrella_MPI.A_estrella(1,5,2,9)
elif(rank==1 ):
    Aestrella_MPI.A_estrella(1,5,2,9)
elif(rank==2 ):
    Aestrella_MPI.A_estrella(1,5,2,9)
elif(rank==3):
    Aestrella_MPI.A_estrella(1,5,2,9)
fin=time.time()

print("Tiempo:" + str((fin-inicio)))

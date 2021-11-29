import AestrellaSERIAL
from mpi4py import MPI
import time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#1,3,5,6

#1,5,2,9


print("Proceso:"+ str(rank))
inicio=time.time()
if(rank==0 ):
    AestrellaSERIAL.A_estrella(15,0,0,15)
elif(rank==1 ):
    AestrellaSERIAL.A_estrella(0,0,15,15)
elif(rank==2 ):
    AestrellaSERIAL.A_estrella(0,15,15,15)
elif(rank==3):
    AestrellaSERIAL.A_estrella(10,10,15,15)
fin=time.time()

print("Tiempo:" + str((fin-inicio)))

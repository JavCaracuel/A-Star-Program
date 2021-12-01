from mpi4py import MPI
import csv

comm = MPI.COMM_WORLD
rank = comm.Get_rank()



if rank == 0:
    with open('data.csv', newline='\n') as f:
        reader = csv.reader(f)
        data = list(reader)

    cat=int(len(data)/4)

    f_aux=int(data[0][1])
    h_aux = int(data[0][2])
    pos=int(data[0][0])
    lista=[]
    for i in range(0,cat):
        if (int(data[i][1]) < f_aux) or (int(data[i][1])==f_aux and int(data[i][2]) == h_aux) :
            f_aux = int(data[i][1])
            h_aux = int(data[i][2])
            pos = int(data[i][0])

    lista.append(pos)
    lista.append(f_aux)
    lista.append(h_aux)      
    comm.send(lista, dest=4, tag=10)
elif rank == 1:
    with open('data.csv', newline='\n') as f:
        reader = csv.reader(f)
        data = list(reader)
    cat=int(len(data)/4)
    
    f_aux=int(data[0][1])
    h_aux = int(data[0][2])
    pos=int(data[0][0])
    lista=[]
    for i in range(cat+1,cat*2):
        if (int(data[i][1]) < f_aux) or (int(data[i][1])==f_aux and int(data[i][2]) == h_aux) :
            f_aux = int(data[i][1])
            h_aux = int(data[i][2])
            pos = int(data[i][0])
            
    lista.append(pos)
    lista.append(f_aux)
    lista.append(h_aux)     
    comm.send(lista, dest=4, tag=11)
elif rank == 2:
    with open('data.csv', newline='\n') as f:
        reader = csv.reader(f)
        data = list(reader)

    cat=int(len(data)/4)
    f_aux=int(data[0][1])
    h_aux = int(data[0][2])
    pos=int(data[0][0])
    lista=[]
    for i in range((cat*2)+1,cat*3):
        if (int(data[i][1]) < f_aux) or (int(data[i][1])==f_aux and int(data[i][2]) == h_aux) :
            f_aux = int(data[i][1])
            h_aux = int(data[i][2])
            pos = int(data[i][0])
            
    lista.append(pos)
    lista.append(f_aux)
    lista.append(h_aux)     
    comm.send(lista, dest=4, tag=12)

elif rank == 3:
    with open('data.csv', newline='\n') as f:
        reader = csv.reader(f)
        data = list(reader)
    cat=int(len(data)/4)
    f_aux=int(data[0][1])
    h_aux = int(data[0][2])
    pos=int(data[0][0])
    lista=[]
    for i in range(cat*3+1,len(lista)-1):
        if (int(data[i][1]) < f_aux) or (int(data[i][1])==f_aux and int(data[i][2]) == h_aux) :
            f_aux = int(data[i][1])
            h_aux = int(data[i][2])
            pos = int(data[i][0])
            
    lista.append(pos)
    lista.append(f_aux)
    lista.append(h_aux)     
    comm.send(lista, dest=4, tag=13)

elif rank == 4:
    esta0 = comm.recv(source=0,tag=10)
    esta1 = comm.recv(source=1,tag=11)
    esta2 = comm.recv(source=2,tag=12)
    esta3 = comm.recv(source=3,tag=13)
    lista_final=[]
    lista_final.append(esta0)
    lista_final.append(esta1)
    lista_final.append(esta2)
    lista_final.append(esta3)

    f_aux=lista_final[0][1]
    h_aux = lista_final[0][2]
    pos= lista_final[0][0]

    for i in range(0,3):
        if (lista_final[i][1]< f_aux) or (lista_final[i][1]==f_aux and lista_final[i][2] == h_aux) :
            f_aux = lista_final[i][1]
            h_aux = lista_final[i][2]
            pos = lista_final[i][0]
               

    print(pos)

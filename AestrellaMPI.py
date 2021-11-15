import numpy as np
import time

posiciones= [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

Matriz = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]]

Nodes = []
NodesSel = []

def GetDistance(StartNode, EndNode):
    DistX = abs(StartNode.X - EndNode.X)
    DistY = abs(StartNode.Y - EndNode.Y)

    '''
    return np.sqrt((DistX**2) + (DistY**2))
    '''
    
    if DistX > DistY:
        return 14*DistY + 10*(DistX - DistY)
    else:
        return 14*DistX + 10*(DistY - DistX)

def NewPosition(children, matriz):
    children0=children
    children1=children
    children2=children
    children3=children
    children_final=children
    for new_position in posiciones:
        if(rank==0 and (new_position==posiciones[0] or new_position==posiciones[1])):

            if (current_node.X + new_position[0]) < 0 or (current_node.Y + new_position[1]) < 0 or (current_node.X + new_position[0]) >= (len(matriz) - 1) or (current_node.Y + new_position[1]) >= (len(matriz[len(matriz)-1])):
                continue

            # Make sure walkable terrain
            if matriz[(current_node.X + new_position[0])][(current_node.Y + new_position[1])] != 1:
                continue

            New_Node0 = Node(current_node)
            New_Node0.X = current_node.X + new_position[0]
            New_Node0.Y = current_node.Y + new_position[1]
            children0.append(New_Node)
        elif(rank==1 and (new_position==posiciones[2] or new_position==posiciones[3])):

            if (current_node.X + new_position[0]) < 0 or (current_node.Y + new_position[1]) < 0 or (current_node.X + new_position[0]) >= (len(matriz) - 1) or (current_node.Y + new_position[1]) >= (len(matriz[len(matriz)-1])):
                continue

            # Make sure walkable terrain
            if matriz[(current_node.X + new_position[0])][(current_node.Y + new_position[1])] != 1:
                continue

            New_Node = Node(current_node)
            New_Node.X = current_node.X + new_position[0]
            New_Node.Y = current_node.Y + new_position[1]
            children1.append(New_Node)
        elif(rank==2 and (new_position==posiciones[4] or new_position==posiciones[5])):

            if (current_node.X + new_position[0]) < 0 or (current_node.Y + new_position[1]) < 0 or (current_node.X + new_position[0]) >= (len(matriz) - 1) or (current_node.Y + new_position[1]) >= (len(matriz[len(matriz)-1])):
                continue

            # Make sure walkable terrain
            if matriz[(current_node.X + new_position[0])][(current_node.Y + new_position[1])] != 1:
                continue

            New_Node = Node(current_node)
            New_Node.X = current_node.X + new_position[0]
            New_Node.Y = current_node.Y + new_position[1]
            children2.append(New_Node)
        elif(rank==3 and (new_position==posiciones[6] or new_position==posiciones[7])):

            if (current_node.X + new_position[0]) < 0 or (current_node.Y + new_position[1]) < 0 or (current_node.X + new_position[0]) >= (len(matriz) - 1) or (current_node.Y + new_position[1]) >= (len(matriz[len(matriz)-1])):
                continue

            # Make sure walkable terrain
            if matriz[(current_node.X + new_position[0])][(current_node.Y + new_position[1])] != 1:
                continue

            New_Node = Node(current_node)
            New_Node.X = current_node.X + new_position[0]
            New_Node.Y = current_node.Y + new_position[1]
            children3.append(New_Node)

    children_final.append(children0)
    children_final.append(children1)
    children_final.append(children2)
    children_final.append(children3)
    return children_final
    '''
    if newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] == 0 or newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] == 2:
        
        New_Node = Node(current_node)
        New_Node.X = current_node.X + new_position[0]
        New_Node.Y = current_node.Y + new_position[1]
        Children.append(New_Node)
    '''
class Node():
    def __init__(self, parent=None):
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0
        self.X = 0
        self.Y = 0
        self.Diagonal = False

Temp = Node(None)

pos = 0

Temp = Node(None)
NodesSel.append(Temp)

print("Inicio:")
print("Coordenadas nodo inicial:")
print("X:")
NodesSel[len(Nodes)-1].Y = input()
print("Y:")
NodesSel[len(Nodes)-1].X = input()

current_node = NodesSel[0]     


End_Node = Node(None)
print("Final:")
print("Coordenadas nodo final:")
print("X:")
End_Node.Y = input()
print("Y:")
End_Node.X = input()

print("buscando")

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

while True:

    NodesSel[len(Nodes)-1].g = 0
    NodesSel[len(Nodes)-1].h = GetDistance(NodesSel[len(Nodes)-1], End_Node)
    NodesSel[len(Nodes)-1].f = NodesSel[len(Nodes)-1].g + NodesSel[len(Nodes)-1].h

    current_node = NodesSel[0]  

    pos = 0

    for index, item in enumerate(NodesSel):
        if item.f < current_node.f:
            current_node = item
            pos = index
        elif item.f == current_node.f:
            if item.h < current_node.h:
                current_node = item
                pos = index

    NodesSel.pop(pos)
    Nodes.append(current_node)
    
    
    if current_node.X == End_Node.X and current_node.Y == End_Node.Y:
        print("Hemos llegado")
        path=[]
        current = current_node
        while current is not None:
            Matriz[current.X][current.Y] = 8
            path.append("[" + str(current.X) + ", " + str(current.Y) + "]")
            current = current.parent
        print(path[::-1])
        print(np.array(Matriz))
        break

    Children = []

    Children.append(NewPosition(Children, Matriz))
    for child in Children:


        for closed_child in Nodes:
            if child == closed_child:
                continue

        NewCost = current_node.g + GetDistance(child, current_node)

        # Create the f, g, and h values
        child.g = NewCost

        #child.h = ((child.X - End_Node.X) ** 2) + ((child.Y - End_Node.Y) ** 2)
        child.h = GetDistance(child, End_Node)
        child.f = child.g + child.h 

        for open_node in NodesSel:
            #if child == open_node and child.g > open_node.g:
            if child == open_node and child.g > open_node.g:
                continue
        NodesSel.append(child)
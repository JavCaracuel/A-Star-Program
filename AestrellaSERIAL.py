import numpy as np
import time

matriz = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
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
NodesSel[len(Nodes)-1].Y = int(input())
print("Y:")
NodesSel[len(Nodes)-1].X = int(input())

current_node = NodesSel[0]     


End_Node = Node(None)
print("Final:")
print("Coordenadas nodo final:")
print("X:")
End_Node.Y = int(input())
print("Y:")
End_Node.X = int(input())

print("buscando")

NodesSel[len(Nodes)-1].g = 0
NodesSel[len(Nodes)-1].h = GetDistance(NodesSel[len(Nodes)-1], End_Node)
NodesSel[len(Nodes)-1].f = NodesSel[len(Nodes)-1].g + NodesSel[len(Nodes)-1].h

Inicio = time.time()

while True:


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
        Fin = time.time()
        print("Hemos llegado")
        path=[]
        current = current_node
        while current is not None:
            matriz[current.X][current.Y] = 8
            path.append("[" + str(current.X) + ", " + str(current.Y) + "]")
            current = current.parent
        print(path[::-1])
        print(np.array(matriz))
        print("Tiempo: " + str(Fin-Inicio))
        break

    Children = []

    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if (current_node.X + new_position[0]) < 0 or (current_node.Y + new_position[1]) < 0 or (current_node.X + new_position[0]) >= (len(matriz) - 1) or (current_node.Y + new_position[1]) >= (len(matriz[len(matriz)-1])):
            continue

        # Make sure walkable terrain
        if matriz[(current_node.X + new_position[0])][(current_node.Y + new_position[1])] != 1:
            continue

        New_Node = Node(current_node)
        New_Node.X = current_node.X + new_position[0]
        New_Node.Y = current_node.Y + new_position[1]
        Children.append(New_Node)

        '''
        if newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] == 0 or newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] == 2:
           
            New_Node = Node(current_node)
            New_Node.X = current_node.X + new_position[0]
            New_Node.Y = current_node.Y + new_position[1]
            Children.append(New_Node)
        '''

    for child in Children:
            
        existe = False
        for i in Nodes:
            if child.X == i.X and child.Y == i.Y:
                existe=True
                break

        if existe:
            continue
        NewCost = current_node.g + GetDistance(child, current_node)

        for open_node in NodesSel:                    
            if child.X == open_node.X and child.Y == open_node.Y and NewCost > open_node.g:
                    existe = True
                    continue
                    print("------------- Problemas -------------")
                
            if existe != True:
                # Create the f, g, and h values
                child.g = NewCost
                child.h = GetDistance(child, End_Node)
                child.f = child.g + child.h
                child.parent = current_node
                
                NodesSel.append(child)
    print(len(NodesSel))
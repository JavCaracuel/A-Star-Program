import numpy as np
import time
def A_estrella(xini,yini,xfin,yfin):
    matriz_3 = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
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

    matriz_5 = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]

    matriz = [[1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

    matriz_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

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

    NodesSel.append(Temp)

    # print("Inicio:")
    # print("Coordenadas nodo inicial:")
    # print("X:")
    NodesSel[0].Y = yini
    # print("Y:")
    NodesSel[0].X = xini

    current_node = NodesSel[0]     


    End_Node = Node(None)
    # print("Final:")
    # print("Coordenadas nodo final:")
    # print("X:")
    End_Node.Y = yfin
    #print("Y:")
    End_Node.X =xfin

    print("buscando")

    NodesSel[len(Nodes)-1].g = 0
    NodesSel[len(Nodes)-1].h = GetDistance(NodesSel[len(Nodes)-1], End_Node)
    NodesSel[len(Nodes)-1].f = NodesSel[len(Nodes)-1].g + NodesSel[len(Nodes)-1].h

    Inicio = time.time()

    while True:



        current_node = NodesSel[0]  

        pos = 0

        #current_node = min(NodesSel, key=lambda o:o.f)
        
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
            if (current_node.X + new_position[0]) < 0 or (current_node.Y + new_position[1]) < 0 or (current_node.X + new_position[0]) >= (len(matriz)) or (current_node.Y + new_position[1]) >= (len(matriz[0])):
                continue

            # Make sure walkable terrain
            if matriz[(current_node.X + new_position[0])][(current_node.Y + new_position[1])] != 1:
                continue

            New_Node = Node(None)
            New_Node.X = current_node.X + new_position[0]
            New_Node.Y = current_node.Y + new_position[1]
            Children.append(New_Node)
        

        for child in Children:
            
            existe = False

            for closed_child in Nodes:
                if (current_node.X + new_position[0])== closed_child.X and (current_node.Y + new_position[1]) == closed_child.Y:
                    continue

            
            NewCost = current_node.g + GetDistance(child, current_node)

            for open_node in NodesSel:
                #if child == open_node and child.g > open_node.g
                    
                if child.X == open_node.X and child.Y == open_node.Y and NewCost >= open_node.g:
                    existe = True
                    break

            if existe == False:
                child.g = NewCost
                #child.h = ((child.X - End_Node.X) ** 2) + ((child.Y - End_Node.Y) ** 2)
                child.h = GetDistance(child, End_Node)
                child.f = child.g + child.h
                child.parent = current_node
                NodesSel.append(child)
                

            # Create the f, g, and h values

            '''
            for closed_child in Nodes:
                if child.X == closed_child.X and child.Y == closed_child.Y:
                    continue

            NewCost = current_node.g + GetDistance(child, current_node)

            for index, open_node in enumerate(NodesSel):
                #if child == open_node and child.g > open_node.g:
                if (child.X == open_node.X and child.Y == open_node.Y) and NewCost < open_node.g:
                    print("[ " + str(child.X) + ", " + str(child.Y) + " ]")
                    print("[ " + str(open_node.X) + ", " + str(open_node.Y) + " ]")
                    NodesSel[index].g = NewCost
                    NodesSel[index].h = GetDistance(child, End_Node)
                    NodesSel[index].f = open_node.g + open_node.h
                    NodesSel[index].parent = current_node
                    continue
                    

                if (child.X == open_node.X and child.Y == open_node.Y) and NewCost >= open_node.g:
                    continue
            
            # Create the f, g, and h values
            child.g = NewCost

            #child.h = ((child.X - End_Node.X) ** 2) + ((child.Y - End_Node.Y) ** 2)
            child.h = GetDistance(child, End_Node)
            child.f = child.g + child.h 
            child.parent = current_node

            
            NodesSel.append(child)
        '''
        '''
        for child in Children:
            
            if child in Nodes:
                print("------------BKJDSFJBDSFBJKbjKSDF-----------------")
                continue
            elif child in NodesSel:
                print("------------hola-----------------")
                #Check if we beat the G score 
                NewCost = current_node.g + GetDistance(child, current_node)
                if child.G > NewCost:
                    #If so, update the node to have a new parent
                    child.G = NewCost
                    child.parent = current_node
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                child.G = current_node.g + GetDistance(child, current_node)
                child.H = GetDistance(child, End_Node)
                #Set the parent to our current item
                child.parent = current_node
                #Add it to the set
                NodesSel.append(child)
            '''
import pygame
import numpy as np
import time

pygame.init()

width, height = 700, 700
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 50,50

dimCW = width/nxC
dimCH = height/nyC

gameState = np.zeros((nxC, nyC))

pauseExect = True
Started = False

EndX = 0
EndY = 0

Nodes = []
NodesSel = []



def GetDistance(StartNode, EndNode):
    DistX = abs(StartNode.X - EndNode.X)
    DistY = abs(StartNode.Y - EndNode.Y)

    #return np.sqrt((DistX**2) + (DistY**2))
    
    
    if DistX > DistY:
        return 14*DistY + 10*(DistX - DistY)
    else:
        return 14*DistX + 10*(DistY - DistX)

    
    '''
    return np.sqrt((DistX**2) + (DistY**2))
    '''
    

class Node():
    def __init__(self, parent=None):
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0
        self.X = 0
        self.Y = 0



Temp = Node(None)

pos = 0

while True:

    newGameState = np.copy(gameState)
    #time.sleep(1)

    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pauseExect = not pauseExect
                print("PAUSED")
            elif event.key == pygame.K_SPACE:
                Started = not Started
                print("SPACE")
                NodesSel[len(Nodes)-1].g = 0
                NodesSel[len(Nodes)-1].h = GetDistance(NodesSel[len(Nodes)-1], End_Node)
                #NodesSel[len(Nodes)-1].f = NodesSel[len(Nodes)-1].g + NodesSel[len(Nodes)-1].h

        mouseClick = pygame.mouse.get_pressed()
        if mouseClick[0] == 1:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX, celY] = 1
            Temp = Node(None)
            NodesSel.append(Temp)
            NodesSel[len(Nodes)-1].X = celX
            NodesSel[len(Nodes)-1].Y = celY
            current_node = NodesSel[0]     

        if mouseClick[2] == 1:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX, celY] = 2
            EndX = celX
            EndY = celY
            End_Node = Node(None)
            End_Node.X = celX
            End_Node.Y = celY
            

        if mouseClick[1] == 1:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX, celY] = 3  

    screen.fill(bg)
    for y in range(0, nxC):
        for x in range(0, nyC):
            poly = [((x)*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    ((x)*dimCW, (y+1)*dimCH)]
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
            elif newGameState[x, y] == 1:
                pygame.draw.polygon(screen, (255,0,0), poly, 0)
            elif newGameState[x, y] == 2:
                pygame.draw.polygon(screen, (0,255,0), poly, 0)
            elif newGameState[x, y] == 3:
                pygame.draw.polygon(screen, (100,100,0), poly, 0)
            elif newGameState[x, y] == 8:
                pygame.draw.polygon(screen, (134,45,89), poly, 0)
            elif newGameState[x, y] == 9:
                pygame.draw.polygon(screen, (0,0,255), poly, 0)
    
    if Started == True and pauseExect == True:
        #print("Nodo 1: " + str(Nodes[len(Nodes)-1].X) + " , " + str(Nodes[len(Nodes)-1].Y))
        #if pauseExect == False:
        
        current_node = NodesSel[0]
        pos = 0

        for index, item in enumerate(NodesSel):
            if (item.f < current_node.f) or (item.f == current_node.f and item.h < current_node.h):
            #if (item.fcost < current_node.fcost) or (item.fcost < current_node.fcost and item.h < current_node.h):
                current_node = item
                pos = index
                
            #elif item.f == current_node.f:
             #   if item.h < current_node.h:
              #      current_node = item
               #     pos = index
                    

        NodesSel.pop(pos)
        Nodes.append(current_node)
        
        #newGameState[current_node.X, current_node.Y] = 1
        
        if current_node.X == End_Node.X and current_node.Y == End_Node.Y:
            print("Hemos llegado")
            current = current_node
            while current is not None:
                newGameState[current.X, current.Y] = 1
                current = current.parent
            for open_node in NodesSel:
                print("[" + str(open_node.X) + ", " + str(open_node.Y) + "]")
            pauseExect = not pauseExect
            Started = not Started

        Children = []

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if (current_node.X + new_position[0]) < 0 or (current_node.Y + new_position[1]) < 0 or (current_node.X + new_position[0]) >= 50 or (current_node.Y + new_position[1]) >= 50:
                continue

            if newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] == 0 or newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] == 2  or newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] == 8:
                newGameState[current_node.X + new_position[0], current_node.Y + new_position[1]] = 8
                New_Node = Node(None)
                New_Node.X = current_node.X + new_position[0]
                New_Node.Y = current_node.Y + new_position[1]
                Children.append(New_Node)


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
                        break
                        
                    
            if existe != True:
                # Create the f, g, and h values
                child.g = NewCost
                child.h = GetDistance(child, End_Node)
                child.f = child.g + child.h
                child.parent = current_node
                
                NodesSel.append(child)



        '''
        for child in Children:                
            existe = False
            if child in Nodes:
                continue
           
            NewCost = current_node.g + GetDistance(child, current_node)

            for open_node in NodesSel:                 
                if child.X == open_node.X and child.Y == open_node.Y:
                    if NewCost < open_node.g:
                        open_node.g = NewCost
                        #child.h = ((child.X - End_Node.X) ** 2) + ((child.Y - End_Node.Y) ** 2)
                        open_node.h = GetDistance(child, End_Node)
                        open_node.f = open_node.g + open_node.h
                        open_node.parent = current_node
                    existe = True
                    break
                    

            if existe == False:
                child.g = NewCost
                #child.h = ((child.X - End_Node.X) ** 2) + ((child.Y - End_Node.Y) ** 2)
                child.h = GetDistance(child, End_Node)
                child.f = child.g + child.h
                child.parent = current_node
                NodesSel.append(child)
        '''
        '''   
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
        '''

        '''
            for child in Children:

                if child in Nodes:
                    continue
                
                for closed_child in Nodes:
                    if child.X == closed_child.X and child.Y == closed_child.Y:
                        continue
                        print("------------- Problemas -------------")               

                NewCost = current_node.g + GetDistance(child, current_node)
                
                if child not in NodesSel or NewCost < child.g:
                    child.g = NewCost
                    child.h = GetDistance(child, End_Node)
                    child.f = child.g + child.h
                    child.parent = current_node

                    if child not in NodesSel:
                        NodesSel.append(child)
            
        '''           

        '''
            for open_node in NodesSel:
                existe = False

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
                
        '''
        print(len(NodesSel))
        
        #print("[ " + str(child.X) + ", " + str(child.Y) + " ]")
    gameState = np.copy(newGameState)
    pygame.display.flip()



def imprimir_ruta( sol ):       
    for i in sol: 
        for j in i: 
            print(str(j) + " ") 
        print("")  
def verifica( C, x, y ):      
    if x >= 0 and x < len(C) and y >= 0 and y < len(C[1]) and C[x][y] == 0: 
        return True
      
    return False

def encontrar_ruta( C ): 
    sol = [ [ 0 for j in range(len(C[1])) ] for i in range(len(C)) ]      
    if bucar_ruta(C, 0, 0, sol) == False:  
        return []
      
    #imprimir_ruta(sol) 
    return sol
      
def bucar_ruta(C, x, y, sol):      
    if x == len(C) - 1 and y == len(C[1]) - 1: 
        sol[x][y] = 1
        return True
          
    if verifica(C, x, y) == True: 
        sol[x][y] = 1
        #print("x: ",x, "y: ",y)
        #imprimir_ruta(sol)
          

        if bucar_ruta(C, x + 1, y, sol) == True: 
            return True
              
        if bucar_ruta(C, x, y + 1, sol) == True: 
            return True
        sol[x][y] = 0
        return False
'''
C = [[0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 1],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 1, 0]]
               
encontrar_ruta(C) 
'''

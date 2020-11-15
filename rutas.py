def verifica( C, x, y ):      
    if x >= 0 and x < len(C) and y >= 0 and y < len(C[1]) and C[x][y] == 0: 
        return True 
    return False

def encontrar_ruta( C ): 
    sol = [ [ 0 for j in range(len(C[1])) ] for i in range(len(C)) ]      
    if buscar_ruta(C, 0, 0, sol) == False and sol[len(C)-1][len(C[1])-1]==0:
    	return [] 
    return sol
      
def buscar_ruta(C, x, y, sol):
    if x == len(C) - 1 and y == len(C[1]) - 1:
        sol[x][y] = 1
        return True
          
    if verifica(C, x, y) == True: 
        sol[x][y] = 1

        if buscar_ruta(C, x + 1, y, sol) == True: 
            return True
              
        if buscar_ruta(C, x, y + 1, sol) == True: 
            return True
        
        if sol[x][y-1]==0 and y-1 >=0 and sol[len(C)-1][len(C[1])-1]==0:
        	while buscar_manual(C,x,y,sol) ==True:
        		return True

        if sol[len(C)-1][len(C[1])-1]==0:
        	sol[x][y] = 0

        return False

def buscar_manual(C, x, y, sol):
    if x == len(C) - 1 and y == len(C[1]) - 1: 
        sol[x][y] = 1
        return False      
    if verifica(C, x, y) == True: 
        sol[x][y] = 1          

        if buscar_manual(C, x , y-1, sol) == True and C[X+1][Y]==1:
        	return True

        buscar_ruta(C,x+1,y,sol)



#@author: cristian

def funcion(n):
    
   iter=0
   error=0.1
   result=0
   suma=0
   while(iter<=n):
        num=iter*iter
        suma=suma+num
       
        iter=iter+1
   print("N(equivale a la cantidad de naturales a sumar):",n)
   print("Solucion",suma)
   errorrela=(error/suma)*100
   print("Error Relativo",errorrela)
   print("iteraciones",iter)
   
funcion(10)

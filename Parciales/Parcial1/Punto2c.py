#Cristian Contreras
import math
import decimal
import matplotlib.pyplot as plot
x = []
y = []
def funcion(fun,xn,xn1,tol):

    it = 0
    error = 0.01
    x0=xn
    x1=xn1
    while(it<100 and error>tol):
        if((fun(x1)-fun(x0))==0):
            break
        x2= x1-(fun(x1)*((x1-x0))/(fun(x1)-fun(x0)))
        error = abs((fun(x2)-fun(x1)/fun(x2)))
        y.append(error)
        it= it+1
        x.append(it)
        x0=x1
        x1=x2
        print(x2,error)
    
    print("Respuesta Final:",fun(x2),error)
  
def fun(x):
    vcos = math.cos(x)
    return x**2 - vcos

funcion(fun,2.0,1.0,10**-9)
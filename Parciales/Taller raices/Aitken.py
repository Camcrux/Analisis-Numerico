# -*- coding: utf-8 -*-



def aitken(x0,g,nmax,tol):
    i=0
    while i<nmax:
        x1=g(x0)
        if abs(x1-x0)<tol:
            xg=x1
            i=i+1
            print ("Raiz: " + str(xg) , str (i))
            return
        
        x2=g(x1)
        if abs(x2-x1)<tol:
            xg=x2
            i=i+1
            print("Raiz:  "+ str(xg) , str(i))
            return
        
        x0=x0-((x1-x0)**2)/(x2-2*x1*x0) #Metodo de aitken 
        if abs(x2-x0)<tol:
            xg=x0
            i=i+1
            print("Raiz:  "+ str(xg) , str(i))
            return        
        i=i+1
        
    xg=x0
    print("Raiz:  "+ str(xg) , str(i))
    return

import time
# n termino
N=35

#ESTA FUNCION DEVUELVE EL ENECIMO TERMINO DE la serie de fibonacci
def fibonacci(N):
	if(N < 2):
        	return N
	else:
		return fibonacci(N-1) + fibonacci(N-2)

#esta funcion devuelve el tiempo que se demora en calcular la maquina el enecimo termino de la serie de fibonacci
  	
def get_time(N):
	
	t0 = time.time()
	fibonacci(N)
	t1 = time.time()-t0
	return t1

for i in range (N+1):
	print i, get_time(i)

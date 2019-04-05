def cribaErastostenes(n):
    L = range(2, n+1)
    i = 0
    while(L[i]**2 < n):
       
        j = i + 1
                
        while(j < len(L)):
            if((L[j] % L[i]) == 0):
                del L[j]
            else:
                j += 1
    
        i += 1
        
    return L
  
def CribaFabio():
  n=100
  #crear lista
  #criba=[]
  criba = range (2, n) 
  print (criba)
  i=0
  l=len(criba)
  print l
  while ((criba[i]**2) <n):
      #print criba[i]
      for k in range(i+1, l):
          #print criba[k]
          if (criba[k] != None and criba[i]!= None):
              if ((criba[k] % criba[i]) == 0):
                  criba [k] = None
      #print criba[i]
      i=i+1
      while criba[i]==None:
          i=i+1
  print (criba)
  l=len(criba)
  print l
  primos = []
  for i in range (l):
      if (criba[i] != None):
          primos.append(criba[i])
  print (primos)
  print (len(primos))
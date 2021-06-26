
def canBeSplited(vec):
    try:
        lis = vec  
        left = sum(lis[:len(lis)//2])
        right = sum(lis[len(lis)//2:])
        if len(lis) == 0 and left == right:
            return print(0)
        elif left == right:
            return print(1)  
         
        else:
            return print(-1) 
    except (TypeError, NameError): 
        print('¡No es un tipo de datos correcto!')

vect = [1,3,3,8,4,3,2,3,3]

canBeSplited(vect)

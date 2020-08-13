def is_divisible(n,x,y):
    """
    Create a function that checks if a number n is divisible by two numbers x AND y. 
    All inputs are positive, non-zero digits
    """
    dev_x = n / x 
    dev_y = n / y 
    if dev_x and dev_y:
        if dev_x == int(dev_x) and dev_y == int(dev_y):
            return True
        else:  
            return False
    else:
        return False
    
print(is_divisible(20,4,5)) #True
print(is_divisible(200,8,16)) #False
print(is_divisible(2,3,1))

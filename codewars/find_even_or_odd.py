def find_outlier(integers):
    """
    You are given an array containing integers.
    The array is either entirely comprised of odd integers
    or entirely comprised of even integers except for a single integer N. 
    Write a method that takes the array as an argument and returns this "outlier" N.
    """
    
    count_even = 0
    count_odd = 0
    
    for number in integers:
        if number % 2 == 0: #check if even
            count_even += 1
            even_number = number
           
        else:               #else is odd
            count_odd += 1
            odd_number = number
                   
                
    if count_even == 1:
        return even_number        
    if count_odd == 1:
        return odd_number
            



print(find_outlier([2,3,4,6,10]))


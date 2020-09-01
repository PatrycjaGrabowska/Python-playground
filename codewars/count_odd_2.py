from collections import defaultdict
def find_it(seq):

    appearances = defaultdict(int)

    for curr in seq:
        appearances[curr] += 1
        
    appear_dictionary = {curr: appearances[curr] for curr in appearances }
     
    
    for number, app in appear_dictionary.items():
        if app % 2 == 1:
            return number
    
    
    

    
print(find_it([10,11,12,13,10,10]))

print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([10,11,10]))
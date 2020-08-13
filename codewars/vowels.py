
def get_count(input_str):
    """
    Return the number (count) of vowels in the given string. (Without 'y')
    """
    
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in input_str:
        if char not in vowels:
            pass
        else:
            num_vowels += 1
    
    return num_vowels
print(get_count('Test 123 test'))


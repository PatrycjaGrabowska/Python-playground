def fake_bin(x):
    
    """
    Given a string of digits, 
    you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
    """
    fbin = ""
    for digit in x:
        if int(digit) < 5:
            fbin += '0'
        else:
            fbin += '1'   
    
    return fbin

print(fake_bin('157'))
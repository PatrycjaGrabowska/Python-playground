def rgb(r, g, b):
    global hr
    global hg
    global hb
    
    if r <= 0:
        hr = '00'
    elif r > 9 and r <= 255:
        hr = hex(r).strip('0x')
    elif r > 255:
        hr = 'FF'
    elif r >= 1 and r < 10:
        hr = '0' + str(r) 
        
    if g <= 0:
        hg = '00'
    elif g > 9 and g <= 255:
        hg = hex(g).strip('0x')
    elif g > 255:
        hg = 'FF'
    elif g >= 1 and g < 10:
        hg = '0' + str(g)   
        
    if b <= 0:
        hb = '00'
    elif b > 9 and b <= 255:
        hb = hex(b).strip('0x')
    elif b > 255:
        hb = 'FF'
    elif b >= 1 and b < 10:
        hb = '0' + str(b)
        
        
    string = str(hr) + str(hg) + str(hb)

    return string.upper()

print(rgb(255,-20,300))

assert rgb(255,255,255) == 'FFFFFF', 'Wrong max values' #check if maximum values are ok
assert rgb(0,0,0) == '000000', 'Wrong min values' #chceck if minumim values are ok
assert rgb(1,2,3) == '010203', 'Should have "0" before a number' #chceck if values between 1 and 9 are correct
assert rgb(-20, 275, 125) == '00FF7D', 'Minimum can be only "00", and maximum "FF"' #check if out of range values are ok

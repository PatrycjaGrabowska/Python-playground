def good_vs_evil(good, evil):
    
    Hobbits = 1
    Men = 2
    Elves = 3
    Dwarves = 3
    Eagles = 4
    Wizards = 10
    
    Orcs = 1
    Wargs = 2
    Goblins = 2
    Uruk_Hai = 3
    Trolls = 5
    
    list_good = list(good.split())
    good_units = []
    list_evil = list(evil.split())
    evil_units = []
    
    sum_of_good_value = 0
    sum_of_evil_value = 0
    
    #print(list_good)
    for x in list_good:
        if x.strip():
            good_units.append(x)
    print(good_units)
    
    for y in list_evil:
        if y.strip():
            evil_units.append(y)
    print(evil_units)
    
    
    sum_of_good_value += Hobbits * int(good_units[0])
    sum_of_good_value += Men * int(good_units[1])
    sum_of_good_value += Elves * int(good_units[2])
    sum_of_good_value += Dwarves * int(good_units[3])
    sum_of_good_value += Eagles * int(good_units[4])
    sum_of_good_value += Wizards * int(good_units[5])
    
    sum_of_evil_value += Orcs  * int(evil_units[0])
    sum_of_evil_value += Men * int(evil_units[1])
    sum_of_evil_value += Wargs * int(evil_units[2])
    sum_of_evil_value += Goblins * int(evil_units[3])
    sum_of_evil_value += Uruk_Hai * int(evil_units[4])
    sum_of_evil_value += Trolls * int(evil_units[5])
    sum_of_evil_value += Wizards * int(evil_units[6])
    
    print(sum_of_good_value)
    print(sum_of_evil_value)

    if sum_of_good_value > sum_of_evil_value:
        print("Battle Result: Good triumphs over Evil")
    elif sum_of_good_value < sum_of_evil_value:
        print("Battle Result: Evil eradicates all trace of Good")
    else:
        print("Battle Result: No victor on this battle field")
    
good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0')
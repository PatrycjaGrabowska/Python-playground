def DNA_strand(dna):
    """
    in DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA
    you need to get the other complementary side. DNA strand is never empty or there is no DNA at all 
    """  
    complementary = ""
    for nukleotide in dna:
        if nukleotide == 'A':
            complementary += 'T'
        if nukleotide == 'T':
            complementary += 'A'
        if nukleotide == 'C':
            complementary += 'G'
        if nukleotide == 'G':
            complementary += 'C'
    
    return(complementary)
            

    
print(DNA_strand('ATCGTCCC'))

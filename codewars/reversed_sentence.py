def spin_words(sentence):
    words = sentence.split(' ')
    rev_sentence = []
  
    for word in words:
        if len(word) >= 5:
            new_word = word[::-1]    
            
            rev_sentence.append(new_word)
        else:
            rev_sentence.append(word)
                 
    return ' '.join(rev_sentence)

print(spin_words('This is a test sentence'))

from Bio import SeqIO
for seq_record in SeqIO.parse(r"C:\Users\pati8\Desktop\ug\magisterka\program_do_wycinki\lambda_grupa_0.fasta", "fasta"):
    print(seq_record.id) #zwraca numer w bazie
    print('Długosc:')
    print(len(seq_record)) #zwraca długoć sekwencji
    
    
    start_position, end_position = map(int, input('Podaj zakres:').split())
    start_position = start_position - 1 # zmniejszenie o 1 ze wzgledu na to ze numerowanie zaczyna się od 0
    end_position = end_position - 1 
    final_size = print(start_position, end_position)
    my_sequence = seq_record.seq[start_position:end_position]
    
    with open("trimmed_lambda_grupa_0.fasta", "a") as trimmed:
        identifier_line = ">" + seq_record.id + "\n"
        trimmed.write(str(identifier_line))
        trimmed.write(str(my_sequence + "\n"))
    
    

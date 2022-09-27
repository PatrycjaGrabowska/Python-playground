from Bio import SeqIO
for seq_record in SeqIO.parse(r"C:\fakepath\fasta_file.fasta", "fasta"):
    print(seq_record.id)
    print('Długosc:')
    print(len(seq_record)) 
    
    
    start_position, end_position = map(int, input('Podaj zakres:').split())
    start_position = start_position - 1 
    end_position = end_position - 1 
    final_size = print(start_position, end_position)
    my_sequence = seq_record.seq[start_position:end_position]
    
    with open("trimmed_sequence.fasta", "a") as trimmed:
        identifier_line = ">" + seq_record.id + "\n"
        trimmed.write(str(identifier_line))
        trimmed.write(str(my_sequence + "\n"))
    
    

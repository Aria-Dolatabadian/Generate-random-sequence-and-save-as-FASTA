from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import random
# Define the length of the sequence
seq_length = 5000
# Define the nucleotides to choose from
nucleotides = ["A", "C", "G", "T"]
# Generate the random sequence
seq = "".join([random.choice(nucleotides) for _ in range(seq_length)])
# Print the sequence
print(seq)

seq_record = SeqRecord(Seq(seq))

# Add metadata to the sequence record
seq_record.id = "RandomSequence"
seq_record.description = "A random DNA sequence"

# Write the sequence record to a FASTA file
with open("Sequence.fasta", "w") as output_handle:
    SeqIO.write(seq_record, output_handle, "fasta")

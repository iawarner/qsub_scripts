#For running MAFFT on the IMB HPC cluster 
# drawn mostly from 
# https://biopython.org/DIST/docs/api/Bio.Align.Applications._Mafft.MafftCommandline-class.html
# 30 July 2019
# Isabel Warner 

#Import Mafft Command Line from Bio.Align.Applications 
from Bio.Align.Applications import MafftCommandline

#name the executable mafft and use from your local bin directory 
mafft_exe = "/home/i.warner/bin/mafft"

#in file as the input file 
in_file = "/shares/common/users/i.warner/FASTA_seqeuences/Ecoli_genomes_all.fasta"

#set your output 
output = MafftCommandline(mafft_exe, input = in_file)

#make a function that will print the output into a file in the chosen directory 
f = open('/shares/common/users/i.warner/output_mafft/Ecoli_genomes_aligned_mafft.fasta','w')

#make the funciton f run the variable output, the product of your mafft alignment 
#this will put your 
f(output) 

#close the f function (and the file)
f.closed


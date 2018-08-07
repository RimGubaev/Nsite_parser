import sys
import re

a = sys.argv[1] # reading of input filename (first argument)

b = sys.argv[2] # reading of output filename (second argument)

ouf = open(b, 'w+') # open output file for writing

ouf.write('GeneID\tLength\tFactorID\tStrand\tMean_exp_value\tFound\n') # set the columns names

with open(a) as inf:
    for line in inf:
        line = line.strip()
        if line[0:5] == 'QUERY':
            GeneID = (line[7:len(line)]) # saving gene name into GeneID variable untill next gene name
            #print(GeneID)
        if line[0:4] == 'TFBS':
            FactorID = line[9:17] # saving TF binding site ID name into FactorID variable untill next TF binding site
            #print(FactorID)
        if line[0:25] == 'Length of Query Sequence:':
            Length = re.search('\d+\sbp', line).group(0) # saving the promoter sequence length (by regex)
        if 'Motifs' in line:
            Strand = line[line.find('" Strand:')-1] # saving TF binding site ID name into FactorID variable until next TF binding site
            #print(Strand)
            Mean_exp_value = re.search('\d\.\d+',line).group(0) # saving the Mean Exp. Number
            #print(Mean_exp_value)
            Found = re.search('Found\s*\d+', line) 
            Found = re.search('\d+', Found.group(0)).group(0) # saving the number of TF binding sites
            #print(Found)
            ouf.write(GeneID + '\t' + Length + '\t' + FactorID + '\t' 
                      + Strand + '\t' + Mean_exp_value + '\t' + Found +'\n') # adding a string in tab-separated format          
ouf.close()

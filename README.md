# Nsite_parser

Rim Gubaev, 2018

[Nsite](http://www.softberry.com/berry.phtml?topic=nsite&group=programs&subgroup=promoter) is a program that allows to search regulatory elements within promoter sequences of the genes. The Nsite output represents HTML page with text which is quite uncomfortable to use for subsequent analysis. 
This script takes Nsite output as text copied from HTML page and converts it to a tab-delimited text file.

**Usage**
```
python3 Nsite_parser.py Nsite_output.txt Nsite_table.txt
```
* 1<sup>st</sup> argument is text copied from HTML page (Nsite output)
* 2<sup>nd</sup> argument is a tab-delimited text file (Nsite_parser.py output)


**Sample input**

```
Program   Nsite | Version 6.2014
   Search for motifs of   3032 Transcription Factor Binding Sites (TFBS)
   SET of TFBSs: REGSITE DB: 3032 Plant Transcription Factor Binding Sites [Last update: 13.07.2016]; Softberry Inc.

 Search PARAMETRS:
     Expected  Mean  Number                      :  0.0100000
     Statistical Siginicance Level               :  0.9500000
     Level of homology between known TFBS and motif:   80%
     Variation of Distance between TFBS Blocks     :   20%

 NOTE: Mism. - Mismatches   | Mean. Exp. Number - Mean Expected Number   | Up.Conf.Int. - Upper Confidence Interval
       Mismatches are given in Lower case
____________________________________________________________

 QUERY: 1466315
 Length of Query Sequence:       1000 bp     | Nucleotide Frequencies:  A -  0.35   G -  0.20   T -  0.30   C -  0.14


 TFBS AC: RSP00039//OS: tomato (Lycopersicon esculentum), Lycopersicon esculentum /GENE: LAT56; LAT59;/TFBS: 56/59 box /BF: GT-1 related transcription factors
 Motifs on "+" Strand: Mean Exp. Number   0.00202     Up.Conf.Int.  1     Found   1
     324  TGAAATTGTGA      334 (Mism.= 0)

 TFBS AC: RSP00314//OS: arabidopsis (Arabidopsis thaliana) /GENE: GA3/TFBS: rbe /BF: RSG, a bZIP transcriptional activator;
 Motifs on "+" Strand: Mean Exp. Number   0.00554     Up.Conf.Int.  1     Found   1
     906  TCCAAaTTGGA      916 (Mism.= 1)

 Motifs on "-" Strand: Mean Exp. Number   0.00754     Up.Conf.Int.  1     Found   1
     916  TCCAAtTTGGA      906 (Mism.= 1)
```


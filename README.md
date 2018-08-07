# Nsite_parser

Rim Gubaev, 2018

[Nsite](http://www.softberry.com/berry.phtml?topic=nsite&group=programs&subgroup=promoter) is a program that allows to search regulatory elements within promoter sequences of the genes. The Nsite output represents HTML page with text which is quite uncomfortable to use for subsequent analysis. 
This script takes Nsite output as text copied from HTML page and converts it to a tab-delimited text file.

**Sample input**

**Usage**

```
python3 Nsite_parser.py Nsite_output.txt Nsite_table.txt
```
* 1<sup>st</sup> argument is text copied from HTML page (Nsite output)
* 2<sup>nd</sup> argument is a tab-delimited text file (Nsite_parser.py output)

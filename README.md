# .txt To Latex

Let's face it; making tables in LaTeX is awful.
This is a simple Python script I wrote to make the conversion go a little smoother. 
The script reads in data (from a txt file by default) and outputs to a txt file for an easy copy-and-paste LaTeX table.
Right now it is capable of generating a LaTeX table in tabular or longtable format.
Note: the longtable format assumes you are using both the longtable and booktabs packages in LaTeX.

## Getting Started

Just download the txttolatex.py file and the style directory (containing tabular.py, longtable.py, and __init__.py).
Open txttolatex.py with your favorite text editor and substitute your input and output files.

### Prerequisites

This should work if you have either python 2 or 3 installed

### Installing

Download files into the directory of your choice

Open txttolatex.py and substitute input and output file names.

### Running
Replace these with your file names
```
datafile = "./test.txt"
outputfile = "./latexout.txt"
```
Set the format: tabular or longtable
```
tableFormat = 'tabular'
```
Set the alignment: 'c','l', or 'r'
```
align = 'l'
```
### Sample input

```
0	1	2	3
a	b	c	d	
e	f	g	h
i	j	k	l
```
### Sample output (tabular)
```
\begin{table}[htbp]
\begin{center}
\label{tb:addlabel}
\caption{add caption}
\begin{tabular}{llll}
\hline\hline
0&1&2&3\\
\hline
a&b&c&d\\
e&f&g&h\\
i&j&k&l\\
\hline\hline
\end{tabular}
\end{center}
\end{table}
```

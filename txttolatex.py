#converts simple text data file to a copy and paste-able LaTeX table

#Note: 'longtable' style assumes the longtable and booktabs LaTeX packages


from style import longtable, tabular

datafile = "./test.txt"
outputfile = "./latexout.txt"

#Change tableFormat to set an alternative format (e.g. 'longtable') 
#Default is 'tabular'; currently 'tabular' or 'longtable' are available
tableFormat = 'tabular'

#set alignment of columns: 'l', 'c', 'r'
align = 'l'

def convert(datafile, outputfile, colnums= [-1], align = align, style = tableFormat):
    if style == 'tabular':
        tabular.out(datafile=datafile, outputfile=outputfile, colnums=colnums, align= align)
    elif style == 'longtable':
        longtable.out(datafile=datafile, outputfile=outputfile, colnums=colnums, align=align)


convert(datafile, outputfile)


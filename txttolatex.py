#converts simple text data file to a copy and paste-able LaTeX table

#Note: 'longtable' style assumes the longtable and booktabs LaTeX packages


from style import longtable, tabular

datafile = "./test.txt"
outputfile = "./latexout.txt"

#Change tableFormat to set an alternative format (e.g. 'longtable') 
#Default is 'tabular'; currently only 'longtable' is available
tableFormat = 'tabular'

def convert(datafile, outputfile, colnums= [-1], align = 'l', style = 'tabular'):
    if style == 'tabular':
        tabular.out(datafile=datafile, outputfile=outputfile, colnums=colnums, align= align)
    elif style == 'longtable':
        longtable.out(datafile=datafile, outputfile=outputfile, colnums=colnums, align=align)


convert(datafile, outputfile, style = tableFormat)


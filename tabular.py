def ign_blank(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def out(datafile, outputfile, colnums= [-1], align = 'l'):
    with open(datafile) as file:
        lines = list(line for line in ign_blank(file))
        #header
        header = lines.pop(0)
        headcols = header.split()
        headerfmt = ""
        if colnums != [-1]:
            for c in colnums:
                headerfmt = headerfmt +str(headcols[c].strip())+"&"
            headcols = [headcols[c] for c in colnums]
        else:
            for c in headcols:
                headerfmt = headerfmt + str(c.strip())+"&"
        header = headerfmt[:-1] + "\\\\\n"
        datafmt = []
        for line in lines:
            cols = line.split()
            tmp = ""        
            cols = [str(x) for x in cols]
            for n,i in enumerate(cols):
                if i.find("_") != -1:
                    cols[n] = i.replace("_","-")
            if colnums != [-1]:
                for c in colnums:
                    tmp = tmp + str(cols[c])+"&"
            else:
                for i,c in enumerate(cols):
                    tmp = tmp + str(c)+"&"
            tmp = tmp[:-1] + "\\\\\n"
            datafmt.append(tmp)
        with open(outputfile, "w") as out:
            out.write("\\begin{table}[htbp]\n")
            out.write("\\begin{center}\n")
            out.write("\\label{tb:addlabel}\n")
            out.write("\\caption{add caption}\n")
            tblcols = ""
            for i in range(len(headcols)):
                tblcols += align
            out.write("\\begin{tabular}{"+tblcols+"}\n")
            

            out.write("\\hline\\hline\n")
            out.write(header+"\\hline\n")

            for x in datafmt:
                out.write(x)
            out.write("\\hline\\hline\n")
            out.write("\\end{tabular}\n")
            out.write("\\end{center}\n")
            out.write("\\end{table}\n")

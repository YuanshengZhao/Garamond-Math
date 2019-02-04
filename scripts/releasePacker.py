import datetime
now = datetime.datetime.now()
verN=now.strftime("%Y-%m-%d")
print (verN)


def writeFile(fname, textti, texttf):
    fp=open(fname)
    strr=""
    gll=len(textti)
    while(True):
        strrx=fp.readline()
        if(strrx[:gll]==textti):
            strr=strr+textti+verN+texttf
            break
        else:
            strr=strr+strrx
        if(strrx==""):
            print("Warning: ",fname)
            break
    strr=strr+fp.read()
    fp.close()
    fp=open(fname,"w")
    fp.write(strr)
    fp.close()


writeFile("./docs/README.md", "# Garamond-Math Ver. ", "\n")
writeFile("./README.md", "# Garamond-Math Ver. ", "\n")
writeFile("./docs/Garamond-Math.tex", "\\title{Garamond-Math, Ver. ", "}\n")
writeFile("./Garamond-Math.sfdir/font.props", "Version: ", "\n")


import os
os.system("cd ./scripts/ & build.bat")
os.system("xelatex ./docs/Garamond-Math.tex")


def mvFile(fsrc,ftgt):
    fp=open(fsrc,"rb")
    gss=fp.read()
    fp.close()

    fp=open(ftgt,"wb")
    gss=fp.write(gss)
    fp.close()

    print("file copied: ", fsrc, " to " ,ftgt)

mvFile("./docs/Garamond-Math.tex","../Release/garamond-math/Garamond-Math.tex")
mvFile("./docs/README.md","../Release/garamond-math/README.md")
mvFile("./Garamond-Math.otf","../Release/garamond-math/Garamond-Math.otf")
mvFile("./Garamond-Math.pdf","../Release/garamond-math/Garamond-Math.pdf")

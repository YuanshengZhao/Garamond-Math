import os

def TransferGlyph(g_fname_in,g_fname_out):
    hfile = open(g_fname_in)
    lpstr=hfile.readline()   
    g_ic=0.0
    while (lpstr[:9]!="SplineSet"):
        lpstr=hfile.readline()
        if(lpstr==""):
            return 0
        elif (lpstr[:5]=="Width"):
            g_wd=(int)(lpstr[7:])
        elif (lpstr[:16]=="ItalicCorrection"):
            g_ic=(int)(lpstr[18:])
            if(g_ic==0):
                return 2
        elif (lpstr[:18]=="IsExtendedShape: 1"):
            return 0
    
    hfile.seek(0)

    lpstr=opr=hfile.readline()   
    while (lpstr[:9]!="SplineSet"):
        lpstr=hfile.readline()
        if(lpstr==""):
            return 0
        elif (lpstr[:5]=="Width"):
            opr=opr+"Width: "+str(g_wd+g_ic)+"\n"
            opr=opr+"BottomRightVertex: 1  0,"+str(-g_ic)+"\n"
        elif (lpstr[:16]!="ItalicCorrection"):
            opr+=lpstr
    opr+=hfile.read()
    hfile.close()

    hfile=open(g_fname_out,"w",newline='')
    hfile.write(opr)
    hfile.close()
    return 1

def cpFile(fsrc,ftgt):
    fp=open(fsrc,"rb")
    gss=fp.read()
    fp.close()

    fp=open(ftgt,"wb")
    gss=fp.write(gss)
    fp.close()

dirrr_in="./Garamond-Math.sfdir"
dirrr_out="../Garamond-Math-Word.sfdir"

fnum=0

for path, subdirs, files in os.walk(dirrr_in):
    for filename in files:
        fnum+=1
print(fnum)

for path, subdirs, files in os.walk(dirrr_in):
    for filename in files:
        lResult=TransferGlyph(dirrr_in+"/"+filename,dirrr_out+"/"+filename)
        if(lResult!=1):
            cpFile(dirrr_in+"/"+filename,dirrr_out+"/"+filename)
        if(lResult==0):
            print("Copied without processing: ", filename)

print("Done!")\

import os
import numpy as np
# dirrr="../gtemp/lettersname.sfdir/"
dirrr="./Garamond-Math.sfdir/"

enc=[]

for path, subdirs, files in os.walk(dirrr):
    for filename in files:
        if(filename[-1]!="h"):
            continue
        hfile = open(dirrr+filename)
        lnstr=hfile.readline()
        lnstr=hfile.readline()
        ii=10
        jj=11
        while (lnstr[jj]!=" "):
            jj+=1
        enc=enc+[int(lnstr[ii:jj])]
        # ii=jj+1
        # jj=ii+1
        # while (lnstr[jj]!=" "):
        #     jj+=1;
        # print(int(lnstr[ii:jj]))
        # ii=jj+1
        # jj=ii+1
        # while (lnstr[jj]!="\n"):
        #     jj+=1;
        # print(int(lnstr[ii:jj]))
        hfile.close()

enc.sort()

print("Table generated, N=",len(enc))

lth=len(enc)
def lookUp(tgt):
    ist=0
    ied=lth
    icc=int(lth/2)
    while (enc[icc]!=tgt):
        if(enc[icc]<tgt):
            ist=icc
        else:
            ied=icc
        icc=int((ist+ied)/2)
    return icc

for path, subdirs, files in os.walk(dirrr):
    for filename in files:
        if(filename[-1]!="h"):
            continue
        hfile = open(dirrr+filename)
        lnstr=hfile.readline()
        lwstr=lnstr
        lnstr=hfile.readline()
        ii=10
        jj=11
        while (lnstr[jj]!=" "):
            jj+=1
        enc1=int(lnstr[ii:jj])
        ii=jj+1
        jj=ii+1
        while (lnstr[jj]!=" "):
            jj+=1
        enc2=int(lnstr[ii:jj])
        lwstr=lwstr+"Encoding: "+str(enc1)+" "+str(enc2)+" "+str(lookUp(enc1))+"\n"+hfile.read()
        hfile.close()
        # print(dirrr+filename)
        hfile = open(dirrr+filename,"w")
        hfile.write(lwstr)
        hfile.close()

print("Finished")
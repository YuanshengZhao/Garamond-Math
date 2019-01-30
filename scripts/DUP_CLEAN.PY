import os
import numpy as np
# dirrr="../gtemp/lettersname.sfdir/"
dirrr="./Garamond-Math.sfdir/"

enc=[]

def lookUp(tgt):
    ist=0
    lth=len(enc)
    while (ist<lth):
        if(enc[ist]==tgt):
            return 1
        ist+=1
    return 0

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
        hfile.close()
        encx=int(lnstr[ii:jj])
        if(lookUp(encx)==1):
            os.remove(dirrr+filename)
            print("Remove ",dirrr,filename)
        else:
            enc=enc+[encx]

print("Finished")
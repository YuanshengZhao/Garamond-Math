import os
import numpy as np
dirin="C:/Users/yuans/Desktop/opr_large.sfdir/"
dirrr="./Garamond-Math.sfdir/"

# enc=[]
# 
# for path, subdirs, files in os.walk(dirin):
#     for filename in files:
#         if(filename[-1]!="h"):
#             continue
#         hfile = open(dirin+filename)
#         lnstr=hfile.readline()
#         lnstr=hfile.readline()
#         ii=10
#         jj=11
#         while (lnstr[jj]!=" "):
#             jj+=1
#         enc=enc+[int(lnstr[ii:jj])]
#         hfile.close()

# enc.sort()

# print("Table generated, N=",len(enc))

# lth=len(enc)
# def lookUp(tgt):
#     ist=0
#     ied=lth
#     icc=int(lth/2)
#     while (enc[icc]!=tgt):
#         if(enc[icc]<tgt):
#             ist=icc
#         else:
#             ied=icc
#         icc=int((ist+ied)/2)
#     return icc
## Copy
# for path, subdirs, files in os.walk(dirin):
#     for filename in files:
#         if(filename[-1]!="h"):
#             continue
#         # if(filename[:4]!="plus"):
#         #     continue
#         hfile = open(dirin+filename)
#         lnstr=hfile.readline()
#         lwstr=lnstr[:-1]+".large\n"
#         lnstr=hfile.readline()
#         ii=10
#         jj=11
#         while (lnstr[jj]!=" "):
#             jj+=1
#         enc1=int(lnstr[ii:jj])
#         enc2=lookUp(enc1)
#         lwstr=lwstr+"Encoding: "+str(enc2+1116614+1)+" -1 "+str(enc2+4970+1)+"\n"+hfile.read()
#         hfile.close()
#         print(dirrr+filename[:-6]+".large.glyph")
#         # print(lwstr)

#         hfile = open(dirrr+filename[:-6]+".large.glyph","w")
#         hfile.write(lwstr)
#         hfile.close()

## Add lookup
for path, subdirs, files in os.walk(dirin):
    for filename in files:
        if(filename[-1]!="h"):
            continue
        # if(filename[:5]!="plusm"):
        #     continue
        if(not os.path.isfile(dirrr+filename)):
            print("file not found: "+ filename)
            continue
        # hfile = open(dirin+filename)
        # lpstr=hfile.readline()
        # hfile.close()
        # jj=-1
        # while (lpstr[jj]!=" "):
        #     jj-=1
        # tgtname=lpstr[jj:-1]
        # hfile = open(dirrr+filename)
        # lwstr=lnstr=hfile.readline()
        # while (lnstr[:12]!="EndSplineSet"): # assume map all have splineset!
        #     lnstr=hfile.readline()
        #     lwstr+=lnstr
        # lwstr+=("Substitution2: \"\'ss11\' Style Set 11\" "+tgtname+".large\n")
        # lnstr=hfile.readline()
        # if(lnstr[:37]!="Substitution2: \"\'ss11\' Style Set 11\" "):
        #     lwstr+=lnstr
        # while (lnstr!=""):
        #     lnstr=hfile.readline()
        #     if(lnstr[:37]!="Substitution2: \"\'ss11\' Style Set 11\" "):
        #         lwstr+=lnstr
        # hfile.close()
        # print(lwstr)

        # hfile = open(dirrr+filename,"w")
        # hfile.write(lwstr)
        # hfile.close()

print("Finished")
#clean redundency
import os
path="./Garamond-Math.sfdir"
for path, subdirs, files in os.walk(path):
    for filename in files:
        if(filename[-8:-6]==".s" or filename[-9:-6]==".ss"):
                hfl=open(path+"/"+filename)
                strg=""
                isex=0
                while(True):
                    strr=hfl.readline()
                    if(strr==""):
                        break
                    elif(strr[:52]!="AlternateSubs2: \"\'ssty\' Script Style in Mathematical"):
                        strg+=strr
                    else:
                        isex=1
                
                hfl.close()

                if(isex==1):
                    print(filename)
                    hfl=open(path+"/"+filename,"w")
                    hfl.write(strg)
                    hfl.close()

print("Finished.")
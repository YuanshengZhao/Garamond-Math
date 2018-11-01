#!/usr/bin/env python
import os

def ReadGlyph(g_fname):
    hfile = open(g_fname)
    lnstr="begin"
    #Get Width, ItalicCor, TopAccentPos
    tpach=itacor=0 # init, in case of no info provided

    while (lnstr[:4]!="Fore"):
        lnstr=hfile.readline()
        if (lnstr[:5]=="Width"):
            wd=float(lnstr[7:])
            continue
        if (lnstr[:16]=="ItalicCorrection"):
            itacor=float(lnstr[18:])
            continue
        if (lnstr[:19]=="TopAccentHorizontal"):
            tpach=float(lnstr[21:])
            continue

    #Move to SplineSet
    while (lnstr[:9]!="SplineSet"):
        lnstr=hfile.readline()

    lnstr=hfile.readline()
    cdmin=10000
    cdmax=-10000
    #Find left and right bearing
    while (lnstr[:12]!="EndSplineSet"):
        j=-1
        cnt=0
        while (cnt<3):
            j-=1
            if(lnstr[j]==" "):
                cnt+=1
        i=j-1
        lth=len(lnstr)+1
        while (lnstr[i]!=" "):
            i-=1
            if(i==-lth):
                break
        i+=1
        temp=float(lnstr[i:j])
        if (temp>cdmax):
            cdmax=temp
        if (temp<cdmin):
            cdmin=temp

        lnstr=hfile.readline()

    hfile.close()
    return (wd,itacor,tpach,cdmin,wd-cdmax)

def WriteGlyph(g_fname,g_wd,g_itacor,g_tpach,g_xmove):
    hfile = open(g_fname)
    lpstr=opr=hfile.readline()
    
    #Write Info
    while (lpstr[:9]!="SplineSet"):
        lpstr=hfile.readline()
        if(lpstr==""):
            return 0
        if (lpstr[:5]=="Width"):
            opr=opr+"Width: "+str(g_wd)+"\n"
            if(g_itacor!=0):
                opr=opr+"ItalicCorrection: "+str(g_itacor)+"\n"
            if(g_tpach!=0):
                opr=opr+"TopAccentHorizontal: "+str(g_tpach)+"\n"
            continue
        if (lpstr[:16]!="ItalicCorrection" and lpstr[:19]!="TopAccentHorizontal"):
            opr+=lpstr
    # Move Spline
    lpstr=hfile.readline()
    while (lpstr[:12]!="EndSplineSet"):
        if(lpstr[0]==" "):
            i=1
            opr+=" "
        else:
            i=0
            opr+=""
        j=i
    
        adb=True
        while (True):
            j+=1
            if(lpstr[j]==" "):
                if(lpstr[i:j]!="c" and lpstr[i:j]!="m" and lpstr[i:j]!="l"):
                    temp=float(lpstr[i:j])
                    if adb:
                        temp+=g_xmove
                    adb=not adb
                    if(int(temp)==temp):
                        temp=int(temp)
                    opr=opr+str(temp)+" "
                else:
                    opr+=lpstr[i:]
                    break
                i=j+1
        lpstr=hfile.readline()
    
    opr=opr+lpstr+hfile.read()
    hfile.close()
    hfile=open(g_fname,"w")
    hfile.write(opr)
    hfile.close

for path, subdirs, files in os.walk("./fname"):
    for filename in files:
        if(filename[-1]!="h"):
            continue
        fn_i=0
        while (filename[fn_i]!="."):
           fn_i+=1
        filenameSource=filename[:fn_i]+".glyph"
        destGlyphInfo=ReadGlyph("./Garamond-Math.sfdir/"+filename)
        sourceGlyphInfo=ReadGlyph("./Garamond-Math.sfdir/"+filenameSource)
        tgtGlyphInfo=(
            destGlyphInfo[0]+sourceGlyphInfo[-1]+sourceGlyphInfo[-2]-destGlyphInfo[-1]-destGlyphInfo[-2],
            sourceGlyphInfo[1],
            (sourceGlyphInfo[2]-sourceGlyphInfo[3])*(destGlyphInfo[0]-destGlyphInfo[-1]-destGlyphInfo[-2])/(sourceGlyphInfo[0]-sourceGlyphInfo[-1]-sourceGlyphInfo[-2])+sourceGlyphInfo[3],
            sourceGlyphInfo[3]-destGlyphInfo[3]
            )
        WriteGlyph("./Garamond-Math.sfdir/"+filename,tgtGlyphInfo[0],tgtGlyphInfo[1],tgtGlyphInfo[2],tgtGlyphInfo[3])
        print(filename, "Done!")

# print ReadGlyph("./Garamond-Math.sfdir/u1D72_E.s.glyph")
# print ReadGlyph("./Garamond-Math.sfdir/u1D72_E.glyph")
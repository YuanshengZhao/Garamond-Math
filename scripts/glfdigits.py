cwd=490

def gen(htc,ita,afx=""):
    global enc,encd,lim,glfdat
    encloop=enc
    while(encloop<=encd):
        nm=("u%X" % (encloop))
        if(nm[-1]=="A" or nm[-1]=="B" or nm[-1]=="C" or nm[-1]=="D" or nm[-1]=="E" or nm[-1]=="F"):
            nm=nm[:-1]+"_"+nm[-1]
        if(encloop<lim): 
            ht=-1
        else:
            ht=htc
        glfdat=glfdat+[[nm+afx, ht, ita]]
        encloop=encloop+1

gdtemp=[
    ["zero"       , -1    , 0      ],
    ["one"        , -1    , 0      ],
    ["two"        , -1    , 0      ],
    ["three"      , -1    , 0      ],
    ["four"       , -1    , 0      ],
    ["five"       , -1    , 0      ],
    ["six"        , -1    , 0      ],
    ["seven"      , -1    , 0      ],
    ["eight"      , -1    , 0      ],
    ["nine"       , -1    , 0      ],
]

glfdat=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".s",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".ss",gdtemp[idx][1],gdtemp[idx][2]]]

enc= int("1D7CE",base=16);
encd=int("1D7F5",base=16);
lim= int("1D7FF",base=16);
gen(-1,0)
gen(-1,0,".s")
gen(-1,0,".ss")
gen(-1,0,".eb")
gen(-1,0,".sb")
gen(-1,0,".gm")

# print(len(glfdat),glfdat[0],glfdat[-1])


# hand
# glf, Xheight, itaslope
import math

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


glfdat=[# Latin
    ["_A"             , -1    , 0      ],
    ["_B"             , -1    , 0      ],
    ["_C"             , -1    , 0      ],
    ["_D"             , -1    , 0      ],
    ["_E"             , -1    , 0      ],
    ["_F"             , -1    , 0      ],
    ["_G"             , -1    , 0      ],
    ["_H"             , -1    , 0      ],
    ["_I"             , -1    , 0      ],
    ["_J"             , -1    , 0      ],
    ["_K"             , -1    , 0      ],
    ["_L"             , -1    , 0      ],
    ["_M"             , -1    , 0      ],
    ["_N"             , -1    , 0      ],
    ["_O"             , -1    , 0      ],
    ["_P"             , -1    , 0      ],
    ["_Q"             , -1    , 0      ],
    ["_R"             , -1    , 0      ],
    ["_S"             , -1    , 0      ],
    ["_T"             , -1    , 0      ],
    ["_U"             , -1    , 0      ],
    ["_V"             , -1    , 0      ],
    ["_W"             , -1    , 0      ],
    ["_X"             , -1    , 0      ],
    ["_Y"             , -1    , 0      ],
    ["_Z"             , -1    , 0      ],
    ["a"              , 450   , 0      ],
    ["b"              , 450   , 0      ],
    ["c"              , 450   , 0      ],
    ["d"              , 450   , 0      ],
    ["e"              , 450   , 0      ],
    ["f"              , 450   , 0      ],
    ["g"              , 450   , 0      ],
    ["h"              , 450   , 0      ],
    ["i"              , 450   , 0      ],
    ["j"              , 450   , 0      ],
    ["k"              , 450   , 0      ],
    ["l"              , 450   , 0      ],
    ["m"              , 450   , 0      ],
    ["n"              , 450   , 0      ],
    ["o"              , 450   , 0      ],
    ["p"              , 450   , 0      ],
    ["q"              , 450   , 0      ],
    ["r"              , 450   , 0      ],
    ["s"              , 450   , 0      ],
    ["t"              , 450   , 0      ],
    ["u"              , 450   , 0      ],
    ["v"              , 450   , 0      ],
    ["w"              , 450   , 0      ],
    ["x"              , 450   , 0      ],
    ["y"              , 450   , 0      ],
    ["z"              , 450   , 0      ],
    ["dotlessi"       , 450   , 0      ],
    ["dotlessj"       , 450   , 0      ],
]

glfdat+=[# Greek
    ["_Gamma"     , -1    , 0      ],
    ["_Delta"    , -1    , 0      ],
    ["_Theta"     , -1    , 0      ],
    ["_Lambda"    , -1    , 0      ],
    ["_Xi"        , -1    , 0      ],
    ["_Pi"        , -1    , 0      ],
    ["_Sigma"     , -1    , 0      ],
    ["_Upsilon"   , -1    , 0      ],
    ["_Phi"       , -1    , 0      ],
    ["_Psi"       , -1    , 0      ],
    ["_Omega"     , -1    , 0      ],
    ["uni03F4"    , -1    , 0      ],
    ["alpha"      , 450   , 0      ],
    ["beta"       , 450   , 0      ],
    ["gamma"      , 450   , 0      ],
    ["delta"      , 450   , 0      ],
    ["epsilon"    , 450   , 0      ],
    ["zeta"       , 450   , 0      ],
    ["eta"        , 450   , 0      ],
    ["theta"      , 450   , 0      ],
    ["iota"       , 450   , 0      ],
    ["kappa"      , 450   , 0      ],
    ["lambda"     , 450   , 0      ],
    ["mu"         , 450   , 0      ],
    ["nu"         , 450   , 0      ],
    ["xi"         , 450   , 0      ],
    ["pi"         , 450   , 0      ],
    ["rho"        , 450   , 0      ],
    ["uni03C2"    , 450   , 0      ],
    ["sigma"      , 450   , 0      ],
    ["tau"        , 450   , 0      ],
    ["upsilon"    , 450   , 0      ],
    ["phi"        , 450   , 0      ],
    ["chi"        , 450   , 0      ],
    ["psi"        , 450   , 0      ],
    ["omega"      , 450   , 0      ],
    ["uni03D1"    , 450   , 0      ],
    ["uni03D5"    , 450   , 0      ],
    ["uni03D6"    , 450   , 0      ],
    ["uni03F0"    , 450   , 0      ],
    ["uni03F1"    , 450   , 0      ],
    ["uni03F5"    , 450   , 0      ],
    ["nabla"   , -1    , 0      ],
    ["partialdiff"    , 450   , 0      ],
    ["partialdiff.x"  , 450   , 0      ],

]

for idx in range(len(glfdat)):
    glfdat=glfdat+[[glfdat[idx][0]+".s",glfdat[idx][1],glfdat[idx][2]]]
    glfdat=glfdat+[[glfdat[idx][0]+".ss",glfdat[idx][1],glfdat[idx][2]]]


# bf ltn
enc= int("1D400",base=16);
encd=int("1D433",base=16);
lim= int("1D41A",base=16);
gen(461,0)
gen(461,0,".s")
gen(461,0,".ss")
gen(461,0,".sb")
gen(461,0,".eb")

# it ltn
slp=math.tan(17.2*math.pi/180.0)
enc= int("1D434",base=16);
encd=int("1D467",base=16);
lim= int("1D44E",base=16);
gdtemp=[# Italic Latin
    ["uni210E"           , 450   , slp    ],
    ["uni210F"           , 450   , slp    ],
    ["uni210E.var"       , 450   , slp    ],
    ["uni210F.var"       , 450   , slp    ],
    ["uni210F.var.bar"   , 450   , slp    ],
    ["uni210F.bar"       , 450   , slp    ],
    # ["u1D456"    , 450   , slp    ], # h
    ["u1D6A4"            , 450   , slp    ], # dotless i
    ["u1D6A5"            , 450   , slp    ],
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".s",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".ss",gdtemp[idx][1],gdtemp[idx][2]]]
gen(450,slp)
gen(450,slp,".s")
gen(450,slp,".ss")



# bf it ltn
slp=math.tan(17.2*math.pi/180.0)
enc= int("1D468",base=16);
encd=int("1D49B",base=16);
lim= int("1D482",base=16);
gdtemp=[
    ["u1D489.var"   , 461   , slp    ],
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".s",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".ss",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".eb",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".sb",gdtemp[idx][1],gdtemp[idx][2]]]
gen(461,slp)
gen(461,slp,".s")
gen(461,slp,".ss")
gen(461,slp,".sb")
gen(461,slp,".eb")

# scr ltn
slp=math.tan(17.2*math.pi/180.0)
enc= int("1D49C",base=16);
encd=int("1D4CF",base=16);
lim= int("1D4B6",base=16);
gdtemp=[
    ["uni212C"   , -1    , slp   ],
    # ["u1D49_D"   , -1    , slp   ], # B
    ["uni2130"   , -1    , slp   ],
    # ["u1D4A0"    , -1    , slp   ], # E
    ["uni2131"   , -1    , slp   ],
    # ["u1D4A1"    , -1    , slp   ], # F
    ["uni210B"   , -1    , slp   ],
    # ["u1D4A3"    , -1    , slp   ], # H
    ["uni2110"   , -1    , slp   ],
    # ["u1D4A4"    , -1    , slp   ], # I
    ["uni2112"   , -1    , slp   ],
    # ["u1D4A7"    , -1    , slp   ], # L
    ["uni2133"   , -1    , slp   ],
    # ["u1D4A8"    , -1    , slp   ], # M
    ["uni211B"   , -1    , slp   ],
    # ["u1D4A_D"   , -1    , slp   ], # R
    ["uni2113"   , 450   , slp   ], # l
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".c",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".gm",gdtemp[idx][1],gdtemp[idx][2]]]
gen(450,slp)
gen(450,slp,".c")
gen(450,slp,".gm")

# bf scr ltn
slp=math.tan(17.2*math.pi/180.0)
enc= int("1D4D0",base=16);
encd=int("1D503",base=16);
lim= int("1D4EA",base=16);
gen(461,slp)
gen(461,slp,".c")

# frk ltn
enc= int("1D504",base=16);
encd=int("1D537",base=16);
lim= int("1D51E",base=16);
glfdat+=[
    ["uni212D"   , -1    , 0      ],
    # ["u1D506"    , -1    , 0      ], # C
    ["uni210C"   , -1    , 0      ],
    # ["u1D50_B"   , -1    , 0      ], # H
    ["_Ifraktur"  , -1    , 0      ],
    # ["u1D50_C"   , -1    , 0      ], # I
    ["_Rfraktur"  , -1    , 0      ],
    # ["u1D515"    , -1    , 0      ], # R
    ["uni2128"   , -1    , 0      ],
    # ["u1D51_D"   , -1    , 0      ], # Z
]
gen(510,0)


# bb ltn
enc= int("1D538",base=16);
encd=int("1D56B",base=16);
lim= int("1D552",base=16);
gdtemp=[
    ["uni2102"   , -1    , 0      ],
    # ["u1D53_A"   , -1    , 0      ], # C
    ["uni210D"   , -1    , 0      ],
    # ["u1D53_F"   , -1    , 0      ], # H
    ["uni2115"   , -1    , 0      ],
    # ["u1D545"    , -1    , 0      ], # N
    ["uni2119"   , -1    , 0      ],
    # ["u1D547"    , -1    , 0      ], # P
    ["uni211A"   , -1    , 0      ],
    # ["u1D548"    , -1    , 0      ], # Q
    ["uni211D"   , -1    , 0      ],
    # ["u1D549"    , -1    , 0      ], # R
    ["uni2124"   , -1    , 0      ],
    # ["u1D551"    , -1    , 0      ], # Z
    ["uni213C"   , 450    , 0      ],
    ["uni213D"   , 450    , 0      ],
    ["uni213E"   , -1     , 0      ],
    ["uni213F"   , -1     , 0      ],
    ["uni2145"   , -1     , slp    ],
    ["uni2148"   , 450    , slp    ],
    ["uni2149"   , 450    , slp    ],
    ["uni2147"   , 450    , slp    ],
    ["uni2146"   , 450    , slp    ],
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".gm",gdtemp[idx][1],gdtemp[idx][2]]]
gen(450,0)
gen(450,0,".gm")

# bf frk ltn
enc= int("1D56C",base=16);
encd=int("1D59F",base=16);
lim= int("1D586",base=16);
gen(540,0)

# sf ltn
enc= int("1D5A0",base=16);
encd=int("1D5D3",base=16);
lim= int("1D5BA",base=16);
gen(480,0)

# bf sf ltn
enc= int("1D5D4",base=16);
encd=int("1D607",base=16);
lim= int("1D5EE",base=16);
gen(480,0)

# it sf ltn
slp=math.tan(12.0*math.pi/180.0)
enc= int("1D608",base=16);
encd=int("1D63B",base=16);
lim= int("1D622",base=16);
gen(480,slp)

# bf it sf ltn
enc= int("1D63C",base=16);
encd=int("1D66F",base=16);
lim= int("1D656",base=16);
gen(480,slp)

# tt ltn
enc= int("1D670",base=16);
encd=int("1D6A3",base=16);
lim=int("1D68A",base=16);
gen(480,0)

# bf grk
enc= int("1D6A8",base=16);
encd=int("1D6E1",base=16);
lim=int("1D6C2",base=16);
gdtemp=[
    ["u1D6DB.x"  , 461   , slp    ],
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".s",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".ss",gdtemp[idx][1],gdtemp[idx][2]]]
gen(461,0)
gen(461,0,".s")
gen(461,0,".ss")
gen(461,0,".eb")
gen(461,0,".sb")

# it grk
slp=math.tan(17.2*math.pi/180.0)
enc= int("1D6E2",base=16);
encd=int("1D71B",base=16);
lim=int("1D6FC",base=16);
gdtemp=[
    ["u1D715.x"  , 450   , slp    ],
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".s",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".ss",gdtemp[idx][1],gdtemp[idx][2]]]
gen(450,slp)
gen(450,slp,".s")
gen(450,slp,".ss")

# bf it grk
slp=math.tan(17.2*math.pi/180.0)
enc= int("1D71C",base=16);
encd=int("1D755",base=16);
lim=int("1D736",base=16);
gdtemp=[
    ["u1D74F.x"  , 461   , slp    ],
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".s",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".ss",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".eb",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".sb",gdtemp[idx][1],gdtemp[idx][2]]]
gen(461,slp)
gen(461,slp,".s")
gen(461,slp,".ss")
gen(461,slp,".eb")
gen(461,slp,".sb")

# bf sf grk
enc= int("1D756",base=16);
encd=int("1D76E",base=16);
lim=int("1D76E",base=16);
gen(450,0)

# digits
enc= int("1D7CE",base=16);
encd=int("1D7D7",base=16);
lim= int("1D7FF",base=16);
gdtemp=[
    ["zero.prp"       , -1    , 0      ],
    ["one.prp"        , -1    , 0      ],
    ["two.prp"        , -1    , 0      ],
    ["three.prp"      , -1    , 0      ],
    ["four.prp"       , -1    , 0      ],
    ["five.prp"       , -1    , 0      ],
    ["six.prp"        , -1    , 0      ],
    ["seven.prp"      , -1    , 0      ],
    ["eight.prp"      , -1    , 0      ],
    ["nine.prp"       , -1    , 0      ],
]
glfdat+=gdtemp
for idx in range(len(gdtemp)):
    glfdat=glfdat+[[gdtemp[idx][0]+".s",gdtemp[idx][1],gdtemp[idx][2]]]
    glfdat=glfdat+[[gdtemp[idx][0]+".ss",gdtemp[idx][1],gdtemp[idx][2]]]

gen(-1,0,".prp")
gen(-1,0,".prp.s")
gen(-1,0,".prp.ss")
gen(-1,0,".prp.sb")
gen(-1,0,".prp.eb")

enc= int("1D7F6",base=16);
encd=int("1D7FF",base=16);
lim= int("1D7FF",base=16);
gen(-1,0)

# print(len(glfdat),glfdat[0],glfdat[-1])
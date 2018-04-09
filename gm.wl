(* ::Package:: *)

ClearAll["Global`*"];
X[t_]:=(1-t)^3 X0+3 t (1-t)^2 X1+3 t^2 (1-t) X2+t^3 X3;
Y[t_]:=(1-t)^3 Y0+3 t (1-t)^2 Y1+3 t^2 (1-t) Y2+t^3 Y3;
NX[t_]:=(1-t)^3 X[u]+3 t (1-t)^2 NX1+3 t^2 (1-t) NX2+t^3 X3;
NY[t_]:=(1-t)^3 Y[u]+3 t (1-t)^2 NY1+3 t^2 (1-t) NY2+t^3 Y3;
GN[z_]:=(u=z;dsr=FindRoot[{Derivative[1][Y][u] Derivative[1][NX][0]==Derivative[1][NY][0] Derivative[1][X][u],Derivative[1][Y][1] Derivative[1][NX][1]==Derivative[1][NY][1] Derivative[1][X][1],(Y^\[Prime]\[Prime])[u] (NX^\[Prime]\[Prime])[0]==(NY^\[Prime]\[Prime])[0] (X^\[Prime]\[Prime])[u],(Y^\[Prime]\[Prime])[1] (NX^\[Prime]\[Prime])[1]==(NY^\[Prime]\[Prime])[1] (X^\[Prime]\[Prime])[1]},{{NX1,0},{NY1,0},{NX2,0},{NY2,0}}];{{X[u],Y[u]},{NX1,NY1}/. dsr,{NX2,NY2}/. dsr,{X[1],Y[1]}});
GS[$L1_,$L2_]:=t/. FindRoot[(Y[t]-$L2[[2]]) ($L1[[1]]-$L2[[1]])==(X[t]-$L2[[1]]) ($L1[[2]]-$L2[[2]]),{t,0}]
TRR1[{{x1_,y1_},{x2_,y2_}},\[Theta]1_,\[Theta]2_]:=Module[{$v1,$v2,$v,$x,$y,$l,$ctr,$P1,$P2,$P3,$V12,$l1,$l2,$lt,MP1,MP2,$1P1,$1P2,$2P1,$2P2},$v1={Cos[\[Theta]1],Sin[\[Theta]1]};$v2={Cos[\[Theta]2],Sin[\[Theta]2]};$v=Normalize[$v1+$v2];{$x,$y}=1/2 ({x1,y1}+{x2,y2});$l=Norm[{x1,y1}-{x2,y2}];$ctr={$x,$y}+($l $v)/10;If[Abs[y1-y2]<Abs[x1-x2],
$P1={x1+($ctr[[2]]-y1) Cot[\[Theta]1],$ctr[[2]]};$P2={x2+($ctr[[2]]-y2) Cot[\[Theta]2],$ctr[[2]]};If[Abs[$v[[1]]]>.1,$P3=$ctr+1/4 Sign[$v[[1]]] $l {1,0},$P3=$ctr+($P1-$P2)/5];,

$P1={$ctr[[1]],y1+($ctr[[1]]-x1) Tan[\[Theta]1]};$P2={$ctr[[1]],y2+($ctr[[1]]-x1) Tan[\[Theta]2]};If[Abs[$v[[2]]]>.1,$P3=$ctr+1/4 Sign[$v[[2]]] $l {0,1},$P3=$ctr+($P1-$P2)/5];];$V12=$P2-$P1;$l=Norm[$V12];$V12=Normalize[$V12];$l1=Norm[$P1-$P3];$l2=Norm[$P2-$P3];$lt=If[2 $l1>$l,.8,1.25];MP1=$P1-$v1 $l1 $lt;MP2=$P2-($v2 $l2)/$lt;$1P1=MP1+($v1 $l1 $lt)/2*(If[$lt>1,1.0,1.3]);$2P1=$P3-($V12 $l1)/2;$1P2=MP2+($v2 $l2)/(2 $lt)*(If[$lt<1,1.0,1.3]);$2P2=$P3+($V12 $l2)/2;N[{MP1,$1P1,$2P1,$P3,$2P2,$1P2,MP2}]];
Crs[$vc1_,$vc2_]:=Module[{$nvc1,$nvc2},$nvc1=Normalize[$vc1];$nvc2=Normalize[$vc2];$nvc1[[1]] $nvc2[[2]]-$nvc1[[2]] $nvc2[[1]]];
Opr[$n_,$gcrs_]:=Module[{$w,prv,nxt},$w=StringReplace[s[[$n]],{" "->","}];$w=ToExpression["{{"<>StringReplace[$w,{"\n"->"},\n{","0x"->"OX"}]<>"}}"];tl[[$n]]=(Take[#1,-2]&)/@$w;
tl[[$n]]=Array[{tl[[$n,#,1]],Interpreter["HexInteger"][StringReplace[ToString[tl[[$n,#,2]]],"OX"->""]]}&,Length[tl[[$n]]]];
$w=(Drop[#1,-2]&)/@$w;$w=(ArrayReshape[#1,{Length[#1]/2,2}]&)/@$w;$w=Array[Join[{Last[$w[[#1]]]},$w[[#1+1]]]&,Length[$w]-1];ow[[$n]]=$w;nln=Length[$w];For[$id=nln+1,$id>1,$id--;If[Length[$w[[$id]]]==2&&Norm[$w[[$id]][[1]]-$w[[$id]][[2]]]<66,prv=If[$id>1,$id-1,-1];nxt=If[$id==nln,1,$id+1];If[$gcrs Crs[$w[[$id,1]]-$w[[prv,-2]],$w[[$id,2]]-$w[[$id,1]]]>.1&&$gcrs Crs[$w[[$id,2]]-$w[[$id,1]],$w[[nxt,2]]-$w[[$id,2]]]>.1,cgrst=TRR1[$w[[$id]],ArcTan[$w[[$id,1,1]]-$w[[prv,-2,1]],$w[[$id,1,2]]-$w[[prv,-2,2]]],ArcTan[$w[[$id,2,1]]-$w[[nxt,2,1]],$w[[$id,2,2]]-$w[[nxt,2,2]]]];If[Length[$w[[prv]]]==4,{X0,Y0}=$w[[prv,-1]];{X1,Y1}=$w[[prv,-2]];{X2,Y2}=$w[[prv,-3]];{X3,Y3}=$w[[prv,-4]];$w[[prv]]=Reverse[GN[GS[cgrst[[1]],cgrst[[4]]]]];cgrst[[2]]+=$w[[prv,-1]]-cgrst[[1]];cgrst[[1]]=$w[[prv,-1]],$w[[prv,-1]]=cgrst[[1]];];If[Length[$w[[nxt]]]==4,{X0,Y0}=$w[[nxt,1]];{X1,Y1}=$w[[nxt,2]];{X2,Y2}=$w[[nxt,3]];{X3,Y3}=$w[[nxt,4]];$w[[nxt]]=GN[GS[cgrst[[7]],cgrst[[4]]]];cgrst[[-2]]+=$w[[nxt,1]]-cgrst[[-1]];cgrst[[-1]]=$w[[nxt,1]];,$w[[nxt,1]]=cgrst[[-1]];];$w=Insert[$w,Take[cgrst,-4],$id+1];$w[[$id]]=Take[cgrst,4];
tl[[$n,If[$id==1,-1,$id]]]={tl[[$n,If[$id==1,-1,$id],1]],BitSet[BitClear[tl[[$n,If[$id==1,-1,$id],2]],0],1]};
tl[[$n,$id+1]]={"c",0};
tl[[$n]]=Insert[tl[[$n]],{"c",2},$id+2];]]];
cw[[$n]]=$w;]
TRR2[ptv1_,ptv2_,lth_]:=Module[{$v1,$v2},$v1=Normalize[ptv1];$v2=Normalize[ptv2];N[{lth $v1,(lth $v1)/3,(lth $v2)/3,lth $v2}]];
Oprs[$n_,$gcrs_]:=Module[{$w,prv,temp},(*$w=StringReplace[s\[LeftDoubleBracket]$n\[RightDoubleBracket],{" "\[Rule]","}];$w=ToExpression["{{"<>StringReplace[$w,{"\n"\[Rule]"},\n{","0x"\[Rule]"OX"}]<>"}}"];tl\[LeftDoubleBracket]$n\[RightDoubleBracket]=(Take[#1,-2]&)/@$w;$w=(Drop[#1,-2]&)/@$w;$w=(ArrayReshape[#1,{Length[#1]/2,2}]&)/@$w;$w=Array[Join[{Last[$w\[LeftDoubleBracket]#1\[RightDoubleBracket]]},$w\[LeftDoubleBracket]#1+1\[RightDoubleBracket]]&,Length[$w]-1];*)
$w=cw[[$n]];
nln=Length[$w];For[$id=nln+1,$id>1,$id--;prv=If[$id>1,$id-1,-1];
temp=Crs[$w[[$id,1]]-$w[[prv,-2]],$w[[$id,2]]-$w[[$id,1]]];
If[$gcrs temp>.1||$gcrs temp<-.1,
If[$gcrs temp>.1,temp=30,temp=8];
cgrst=TRR2[$w[[prv,-2]]-$w[[$id,1]],$w[[$id,2]]-$w[[$id,1]],temp]/.{x_,y_}->{x,y}+$w[[$id,1]];If[Length[$w[[prv]]]==4,{X0,Y0}=$w[[prv,-1]];{X1,Y1}=$w[[prv,-2]];{X2,Y2}=$w[[prv,-3]];{X3,Y3}=$w[[prv,-4]];$w[[prv]]=Reverse[GN[t/. FindMinimum[{(X[t]-cgrst[[1,1]])^2+(Y[t]-cgrst[[1,2]])^2,0<t<1},{t,.1}][[2]]]];cgrst[[2]]+=$w[[prv,-1]]-cgrst[[1]];cgrst[[1]]=$w[[prv,-1]],$w[[prv,-1]]=cgrst[[1]];];If[Length[$w[[$id]]]==4,{X0,Y0}=$w[[$id,1]];{X1,Y1}=$w[[$id,2]];{X2,Y2}=$w[[$id,3]];{X3,Y3}=$w[[$id,4]];$w[[$id]]=GN[t/. FindMinimum[{(X[t]-cgrst[[-1,1]])^2+(Y[t]-cgrst[[-1,2]])^2,0<t<1},{t,.1}][[2]]];cgrst[[-2]]+=$w[[$id,1]]-cgrst[[-1]];cgrst[[-1]]=$w[[$id,1]];,$w[[$id,1]]=cgrst[[-1]];];$w=Insert[$w,cgrst,$id];
tl[[$n,If[$id==1,-1,$id]]]={tl[[$n,If[$id==1,-1,$id],1]],2};
tl[[$n]]=Insert[tl[[$n]],{"c",2},$id+1];
]];cw[[$n]]=$w;]


SetDirectory[NotebookDirectory[]];
str=Import["g.glyph"];
str=StringCases[str,"SplineSet\n"~~splineSet__~~"\nEndSplineSet"->splineSet][[1]];
s=StringReplace[str,"\n "->"#"];
s="(*"<>StringReplace[s,"\n"->"*)(*"]<>"*)";
s=StringCases[s,"(*"~~ShortestMatch[___]~~"*)"];
s=Array[StringReplace[s[[#]],{"#"->"\n","(*"->"","*)"->""}]&,Length[s]];
tl=Array[1,Length[s]];
G[$_]:=(
w=StringReplace[s[[$]],{"  "->" ","\n "->"\n"}];
w=StringReplace[w,{" "->","}];
w="{{"<>StringReplace[w,{"\n"->"},\n{","0x"->"OX"}]<>"}}"//ToExpression;
Print[tl=Take[#,-2]&/@w];
w=Drop[#,-2]&/@w;
w=ArrayReshape[#,{Length[#]/2,2}]&/@w;
w=Array[Join[{w[[#]]//Last},w[[#+1]]]&,Length[w]-1];
Graphics[Array[If[Length[w[[#]]]==2,If[Norm[w[[#]][[1]]-w[[#]][[2]]]<69,{Red,Thick,Line[w[[#]]]},Line[w[[#]]]],BezierCurve[w[[#]]]]&,Length[w]]]
);
gr=Array[G,Length[s]]//Show
tl


SetDirectory[NotebookDirectory[]];
fname="g.glyph";
str=Import[fname];
s=StringCases[str,"SplineSet\n"~~splineSet__~~"\nEndSplineSet"->splineSet][[1]];
s=StringReplace[s,"\n "->"#"];
s=StringSplit[s,"\n"];
s=StringReplace[#,"#"->"\n"]&/@s;
ow=cw=tl=Range[Length[s]];
Opr[#,-1]&/@Range[Length[s]];
Oprs[#,-1]&/@Range[Length[s]];
OW=Flatten[ow,1];
CW=Flatten[cw,1];
(tl[[#,1,2]]=tl[[#,-1,2]])&/@Range[Length[s]];
Show[Graphics[Array[{Red,BezierCurve[OW[[#1]]]}&,Length[OW]]],Graphics[Array[{Black,BezierCurve[CW[[#1]]]}&,Length[CW]]]]


Jn[x_,bs_]:=Module[{$xx},
$xx=" "<>#&/@x;
If[bs,$xx[[1]]=x[[1]]];
StringJoin[$xx]<>"\n"
]
Tstr[$n_]:=Module[{$w},
$w=cw[[$n]];
$w=Join[{{$w[[1]][[1]]}},Drop[#,1]&/@$w];
$w=Array[Join[$w[[#]]//Flatten,tl[[$n]][[#]]]&,Length[$w]];
$w=Array[ToString/@$w[[#]]&,Length[$w]];
Array[Jn[$w[[#]],#==1]&,Length[$w]]//StringJoin]
str=StringCases[str,__~~"\nSplineSet\n"]<>
(Tstr/@Range[Length[cw]]//StringJoin)<>
StringCases[str,"EndSplineSet"~~__];
Export[fname,str,"Text"];

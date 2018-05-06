(* ::Package:: *)

SetDirectory[NotebookDirectory[]]


Opr[$n_] :=
  Module[{$w,prv,nxt},
    $w = StringReplace[s[[$n]],{" "->","}];
    $w = ToExpression["{{"<>
      StringReplace[$w,
        {"\n"->"},\n{","0x"->"OX","1x"->"OX","2x"->"OX","3x"->"OX","4x"->"OX"}]<>"}}"
    ];
    tl[[$n]] = (Take[#1,-2]&)/@$w;
    tl[[$n]] = Array[
      {tl[[$n,#,1]],Interpreter["HexInteger"][StringReplace[ToString[tl[[$n,#,2]]],"OX"->""]]}&,
      Length[tl[[$n]]]
    ];
    $w = (Drop[#1,-2]&)/@$w;
    $w = (ArrayReshape[#1,{Length[#1]/2,2}]&)/@$w;
    $w = Array[Join[{Last[$w[[#1]]]},$w[[#1+1]]]&,Length[$w]-1];ow[[$n]]=$w;
  ];


fname = "backslash.glyph";
str   = Import[fname,"Text"];
s     = First @
  StringCases[str,"SplineSet\n"~~splineSet__~~"\nEndSplineSet" -> splineSet];
s     = StringReplace[s,"\n "->"#"];
s     = StringSplit[s,"\n"];
s     = StringReplace[#,"#"->"\n"]& /@ s;
ow = tl = Range[Length[s]];
Opr /@ Range[Length[s]];


bz[cr_,t_] := (1 - t)^3 * cr[[1]]
  + 3 * t   * (1 - t)^2 * cr[[2]]
  + 3 * t^2 * (1 - t)   * cr[[3]]
  +     t^3             * cr[[4]];
dist[cr_,pt_] := First @ SortBy[
  {
    FindMinimum[Plus @@ ((bz[cr, t] - pt)^2), {t, 0}, AccuracyGoal -> 3],
    FindMinimum[Plus @@ ((bz[cr, t] - pt)^2), {t, 1}, AccuracyGoal -> 3]
  }, First];


cnt[bzc1_,bzc2_] := (
    (*
      If[
        Min[
          Plus @@ ((bzc1[[1]]  - bzc2[[1]])^2),
          Plus @@ ((bzc1[[1]]  - bzc2[[-1]])^2),
          Plus @@ ((bzc1[[-1]] - bzc2[[1]])^2),
          Plus @@ ((bzc1[[-1]] - bzc2[[-1]])^2)
        ] > 800^2,
        Return[{}]
      ];
    *)
    t1 = dist[bzc2, bzc1[[1]]][[1]];
    t2 = dist[bzc2, bzc1[[2]]][[1]];
    tg = Min[t1, t2];
    t1 = dist[bzc1, bzc2[[1]]];
    t2 = dist[bzc1, bzc2[[2]]];
    If[Min[tg, t1[[1]], t2[[1]]] > 40, Return[{}]];
    t1 = t /. t1[[2]];
    t2 = t /. t2[[2]];
    If[t2 > t1 > 1,
      p1  = bzc1[[1]];
      p2  = bzc1[[2]];
      p3  = bzc2[[-2]];
      p4  = bzc2[[-1]];
      mp1 = bzc1[[-1]];
      mp2 = bzc2[[1]]; ,
      If[t1 > t2 > 1,
        p1  = bzc1[[1]];
        p2  = bzc1[[2]];
        p3  = bzc2[[2]];
        p4  = bzc2[[1]];
        mp1 = bzc1[[-1]];
        mp2 = bzc2[[-1]]; ,
        If[t2 < t1 < 0,
          p1  = bzc1[[-1]];
          p2  = bzc1[[-2]];
          p3  = bzc2[[-2]];
          p4  = bzc2[[-1]];
          mp1 = bzc1[[1]];
          mp2 = bzc2[[1]]; ,
          p1  = bzc1[[-1]];
          p2  = bzc1[[-2]];
          p3  = bzc2[[2]];
          p4  = bzc2[[1]];
          mp1 = bzc1[[1]];
          mp2 = bzc2[[-1]];
        ]
      ]
    ];
    bzcc = {p1, p1 + u(p2 - p1), p4+v(p3-p4), p4};
    bzcc /. FindRoot[{bz[bzcc,t]==mp1,bz[bzcc,r]==mp2},
      {{u,1},{v,1},{r,.7},{t,.3}}]
  )


gr = Flatten[If[#[[1,1]] != #[[-1,-1]], {#[[1]],#[[-1]]},{}] & /@ ow,1];
gs = Flatten[If[#[[1,1]] != #[[-1,-1]], Drop[Drop[#, {1}], {-1}], {}] & /@ ow,1];
Graphics @ {BezierCurve[gr[[#]]] & /@ Range[Length[gr]]}[[1]]


n = Length[gr];
For[i1 = 1, i1 <= n,
  For[j1 = i1 + 1, j1 <= n,
    Print[i1, " ", j1, " ", rst = cnt[gr[[i1]], gr[[j1]]]];
    If[rst != {},
      gr = Drop[gr,{j1}];
      n--;
      gr[[i1]] = rst;
      Break;];
    j1++];
  i1++]


gr = Join[gr, gs];
Graphics @ {BezierCurve[gr[[#]]] & /@ Range[Length[gr]]}


gr // MatrixForm


n = Length[gr];
For[i1 = 1, i1 < n,
  For[j1 = i1 + 1, j1 <= n,
  (*
    Print[i1, " ", j1, " ",
      gr[[i1, -1]] == gr[[j1,1]], " ", gr[[i1, -1]] == gr[[j1, -1]]]
  *)
  If[gr[[i1, -1]] == gr[[j1, 1]],
    temp=gr[[i1 + 1]];
    gr[[i1 + 1]] = gr[[j1]];
    gr[[j1]] = temp;
    Break;];
  If[gr[[i1, -1]] == gr[[j1, -1]],
    temp = gr[[i1 + 1]];
    gr[[i1 + 1]] = Reverse@(gr[[j1]]);
    gr[[j1]] = Reverse@temp;
    Break;];
  j1++];
i1++]
gr // MatrixForm

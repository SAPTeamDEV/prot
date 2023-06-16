import base64 as __cmethst__
import os
import random
import sys

from . import Database, list2str, printErr, printMsg, printWarn

__spec__.data = Database()
__spec__.data.codeType = [
    {
        "codes": [
            "D=u*JdO7&//+g7fsH33Xk*M*$7*u_.",
            "=ev1=5u?$?-W5gf0n%w#5_7$%h__kq",
            "Uc20dMPeVFq/~_+#&&fXugV_i&iA3Y",
            "S50&+z5Z46#=1-Vh6Qt9jA@J1#4=!2",
            "_4Jb&v22749_+Ei9&Oq1_!qcu*92r0",
            "%$/fe9/y8q-j0A02pd9kk*IDGu20%_",
            "Lqd4_8_%PrIP9oZC&uc3?K-A~Bp34U",
            "6~8_nf=/xcQ01GiKKd@68MVWO$.9o7",
            "h#sFad1l-Br497W654q7Ye95e.4I4k",
            "74&UJR@cq!_9YekY/h-n~a$/!E+Q5Z",
            "$2#B?@5AP2IEUjxpDC@*ZYl=8+e/Ab",
            "701a_!*E#I.778my0!z877kBxCp-z=",
            "K*uVq-=Z*8iY59/2c+aX3_MV.@*#Z_",
            "?2~5kA!eXu_cT--N$?T-*.+9NY947Z",
            ".!Wjz5NVOX3j7P1.bpC79.v24ls*K9",
            "1pr&Ll0giv/lBA$B_18!i$1@232-%/",
            "a-@99ii9&Z84zN.kh/!8-5f&rqvj98",
            "jvS#5d6?Rt=u!NJ1!2UDX4?*=5R%8v",
            "ENr.T+8i37*ZKMS*UM4=jq=56*12H1",
            "j6D-SWshO/p4Yc87wr.Hq40j81_KG7",
            "?23g7IBa9U4/9Xc4!o%438l&/46ZuG",
            "Z1uLv&@058Oi_$50b?ox#3N4$_t4k0",
            "0w?Q!Gs27JY#RbW6li4zS+9&T5j_##",
            "37UHI5Q4AFV=v0A4P!zn!e_JTc9S93",
            "72zH338x?7s3cAe/l@.W6J%WO#Z@/$",
            "35fy*zV5w@ACWO3=S5u#Gj5l6beN@2",
            "RGt86&1926@69_u95=4wyXI?=kHLJ6",
            "U1qE!OC21*r+W0nm7k.X48+6k+&$l#",
            "MU07fwRm1HdK00UZ2Jiu$_=I5t-2$X",
            "!1k6*a_7SD/20~*/xCn#.*C8uu.X~D",
            "v66A4U.a$?E8W_xXR$*=@90r6_9&Dp",
            "u+G!#4WbG$h=4.p5._9OWZ6143h.8R",
            "Wz77@!#yZ@5W27g23?6r@2~7l515X~",
            "3~_p9CTPrJ.H9*TG370u#3rY6~ar=@",
            "/=t+%p7hy&nkuhnsHiK#=oG~DuAX~4",
            "w!!x?_U6X96QpKx937jb8DFNv1.lU0",
            "~~!Y#78T95@3fV#DrB9$@9i6I?p39%",
            "$f@CD$Y6Ov1+1#w9.*?8I2x?bafsu.",
            "dzkRN=7w59dk9_#e&?4L#Nj@?+Tpl!",
            "0d6X5_81GF-+/~2?wb=0?RPXqP952q",
            "8s2z%5r5da4vm0J8dn@Km7y0dL!*te",
            "+b#fG7*oVs4rN*1&.G+=G1%zO?#i/2",
            "MxKR#-6ep@#Q+29kH5883XK=AJ#.H7",
            "&1$z4$+44E79tn?2$@_.6.bU&8?RVw",
            "@JF+pT55ydzR_5?Y_l@6S8_a/108$#",
            "mD3e#5~13Z6s+V_cx7nm1Y/M4U=e.0",
            "L9_VTQ.s7U=VRbC-#J5$7CE5-*9@vm",
            "072#3n./b11eh-Q_*Q$G_r6?!&P0PY",
            "kMkdLA=+h%C40D8uoC7/7_!X&Mb%=4",
            "b68cXM25q6GJ4s5N#g$062+0.WrT9_",
            "_5=9@avDV~UKbDod9~gw1g7A_jRb5_",
            "JI%!ln.FNWNbqmDbo8=se+dJvo.W96",
            "gNJamX*B!l/l#p9ag9Xi3Y%dy?j!NM",
            "e=1=1bHh&n6.Sm3J8~1zU-g&o0?2rO",
            "?uO50+d.9.j7H8HFw0aBP21$$1qt~i",
            "#O!6uIse=7__DL-m-h9e88HdLj2jzm",
            "OS~+5TtfjP5-kQecPM5Q+22Vhu!kY0",
            "DVFEX14?U~b@t476VK72O&@ap.aB@V",
            "n5dh!H-/-0W-%8?Q3X+_=26bNt=4@D",
            "46KKmbX-R6N~-9l=&5f1k0#E4PIm71",
            "!b$E9Typ#p+rM?#yQB50C442*gNMUs",
            "TomYNZ-d3&i_%ySFi72WhY3L@-d~19",
            "B31aV2!%ASH#q=19#tF6@1~j$BO69*",
            "@.TF_*xhfzC!BggwP7N47/*_#dZekt",
            "K.@B#*/A*Q8I-IG1qcRqD_4O%D1s?v",
            "lfs58h2Mn_O!@8=4ip/393?=L!0@4g",
            "pjTb*?f4*Xn1.B3ZLV3Y30r21M@L%L",
            "XeUh/86@F.-7Gf6&WT2cCP%7%x@~a.",
            "-/y.W6@*+H0M~kY@s$W0YXn&$2rjoh",
            "1y82N28LC!6_7$9k49K4X5/1$1Kw63",
            "pXYEJ09tu0cd#9#Lf/3w4u7R0c?i3p",
            "9l6O$4rJD9/O82*6+wwiV#sBS9EV8I",
            "QcL&tYKh4Q$cG1tx8.uM?0hth%E8O2",
            "6$+Q@HZElj2csmX_OzGi5A-BR8i++_",
            "Ie/a8ph=Y_1%l=DC!du~e61A8qMUu7",
            "_nj%KGoz9&q-5V1=~&MnfYns1E171/",
            "hg98U6oT$3Mq==97Hk9RVu#HtM$F+i",
            "K=N409AL8~67fpL1IcT*6-9f4B125N",
            "&AX4U3A0~hh%4%P11%y10$batOcf!~",
            "UaKC$b$%uzk?0#-/0Zs18q6+1s8ImF",
            "~7e$d#7!#QSw229hdM!3xFwI1_%/.q",
            "xE6D12326RlIxi63j$&901w--GE9.1",
            "ZZe*?23102IhIg4U&4$48f8OJ0+03w",
            "_kT&!9*VZ1sE-OtZ71L?x4$@P272EC",
            "uJ35g6gHiQky+gs60_h8+f=~t1-tF7",
            "3Lu2O7Z%ZL2#/*z9_pFY=_7e-#qGOx",
            "I0%2Phdd~I?6/Lw#MO98Jl7A*Cbv2W",
            "D@s0qyF$aFl8/$53GWqA=1.&av#@!1",
            "MG4%ZmhIod-e.0eqGO#VkfER8T2ttN",
            "2q#f@8arUE8Uu?V56c&76jWR9#!2?0",
            "4O5MQGM&h04=cH?P1!80dt+4&!a3d/",
            "1oBK%s9/h2j!0+d08uAT9-_v_pMu=0",
            "fC9ioP-I9/l2?wJH42W4#1+y5r-pe7",
            "*x3PF8!@9_Jf5NUk@u4Zp-t@Fl0d_k",
            "M!8gu53l92*O-R0F6W9$7~H%1/-025",
            "0Dhm.%2~0R$/Db428x3YBv7ZB4/KYF",
            "E=E&VuP&J$snh5D8kn1vz0.4mYsNh8",
            "974KTXO3D6xJRkV/x$4.8+Q/xBnu%.",
            "@78/cNGHf4i3i?2A~Q0p3RXUwI5!h1",
            "46F6u.D1K1VNlywu9A5%_!xr?1y&CU",
        ],
        "decoder": __cmethst__.b64decode,
        "encoder": __cmethst__.b64encode,
    },
    {
        "codes": [
            "3#$1/0?#a783BL0M.y?FIva06-MqOo",
            "7Kcx#x?.F77C+F3B*SSCa$$+M*l9T7",
            "oUGl8D__QhM.6Z&FA7-a8??34&Bmwe",
            "7#U0+p#y4T4ke4&2*9vVDgp3OGn&+~",
            "41IUP7HO0ENnT78v9%oU=m9a7NYM42",
            "Mo5B$Q3jlNEtnQL1!fx2j.tvbI2c?X",
            "#3z940+Z7%aqRy_3176@66B1m4?duK",
            "2*Y177k1XHT=u%o!cT$#7e=Nv9V_g!",
            "bK%4?K1?nQCzT45!!Fi0j7/%Q3YzaP",
            "RI$Sv*4$@D@+V7X9~DRtcP5_8=8=+1",
            "UIj8$Tgi&@sRk$34H55TP5*lN2gd2O",
            "/&B&n8s011!26u@NL?XDZ*t5LtVP39",
            "WtPT~r5D*#10o2-p4N_JvxxgD%@8FC",
            "Nk2u4aljuFVm%+_P~W=L8969VDi_gj",
            "W931W7Us#&B@2-@05oTJ9d&f66!JF8",
            "?1Q#Ue-5!CUUmB+-jes1N8NzRHtS.i",
            "%9G$Pq7UrN1.#!6&!W056=Z-70_Nu7",
            "P0?l#3zh5BOB8pF2JVS*pF+d79cL0k",
            "=1%.=@/A9D-=*EX0/Y#V#d8~Tyx?7G",
            "P?/q@An*c.%U~81_36f+~k.=-6=6I6",
            "5vf1@_=!&92-3X?=DWW.Xxk@JU56-0",
            "6P8h0v?+IK?4FV23n.6o8T8my!M4_?",
            "xD~p2?Mc/zSg+EZnQ$vG338b0P.3+l",
            "6B_BVso6Z0l$TQ.q_wdkHs?lAE=TJ8",
            "RsmMkc96SF_VG~=FN~UHWV1?8B7bGq",
            "89N/5C9R6!+D!C9*-!393/WS1%rSUC",
            "/76AEesbv-y7M#sRb/6d?U+65F$bh@",
            "=6l5d5lRK4DIF6g.!qc3MP+U8_SB8c",
            "Qy#$&S.50TJ3X5Ht0%5CS6v!=Zjf5J",
            "avS&8BzVQ66HLA=_UbZDs1d=O+Fj.&",
            "&Y!D43x8=N54S*M=?NF2o9_/2J=RRM",
            "A0Ru9mq36&.z5z!5/zMD?j7PVW~sf.",
            "0#Acz*yNpw8aOW&72sN!lPlaZ~%%u1",
            "Zsq61qL44!IYZ!+*/2O4/5JZ4=4T#$",
            "_&o_V~/+M&@3%04d9gKnb-81.XJQ@D",
            "6953~~fF?Sj7KS107-m8vc7ykeSM~0",
            "_M5s3LxmWO6.c$3?*IDHKjMpL?4nv9",
            "S+3=0n14Oc+Yg?h31$7X/WF~jr8/4j",
            "P~?3.-0-8O=9%xCt+Uyg$TfyX%5537",
            "B%z-r!nS-z4DPIb4@11#c*fI=0?5+9",
            "lTAUgd%fy+gNZ5Il9nFj?=98+~6Z!D",
            "Wr9G_J=s?Yqkjs*G854?y$z_Z_=*AY",
            "-e_@qQT&#uKQY7@LSD~q%G26-!m_qA",
            "x_UcRS85r-N/KF*Cqarr+34~5+DpGV",
            "0+C4#@TUxFv0qK@h513Qxo1nko6t2e",
            "&=eU/1RCy_u+r+_is9Gx~S#PmS8I=_",
            "9@8P5kWt73$Mq7WI/tc91!/4b9?+61",
            "P20@_G02Vy4uZ8~.249&25ZMq-n&0g",
            "d~#.23yZ%CR1OsS5ER3V&jp/!M13Hv",
            "N-5Ae1f/0$6H872FU_7/o7iDY!5nn*",
            "-m0?/?RUx55.@BH$1v0-S84Y@P2~2v",
            "uX2deXaWU2#j@2K.@$AJJl2xz2KH!4",
            "6eeK@@p7b/!L!#?u~F7+O5A1j7V?#e",
            "G078b!4lQ3j79AK0=8~puE!0hDCFX7",
            "E7k98P9Vq3L3yf?v.@qWGk&KBh-y8K",
            "l8y%f3Lts3Ze*m4=R_!0Tiw/~r9%Ag",
            "Slj&1Fs0.las22t2R=~N6Xhk7Md0Mt",
            "GlB1dk*j8oGYJMhb*R1?m#lpsDhGQ+",
            "--VhH+8y#XlA@H.53o1+.X$hRcZ8_t",
            "hnMK0=VJ-&5e6?j34D3?/8?$5$xg8~",
            "xhz!x0wN0p47B6v4W#3UC4%4#&6Y@=",
            "a%*vBP_&5+650R#IzR0ylQ/14$6ykY",
            "7KZ8YP68%dPm8S6FL3?A-f0eZ-8bPo",
            "RF%g519j1R?84%*94tc87JfL$~Obpn",
            "wd52IW87=&066MiW$#811ikXtHiB#Z",
            "a6Wv~3rGn-u#4$133=dN$p5g9_?f48",
            "%0!gazTjbg/02lAj_6g!3u9*a=r%6.",
            "792Ha3@qHBKvdg#F@dlxDaw7L8*+!l",
            "-/zCQG-81@e9v7Z7288**+%874nK8.",
            "/9P=x5*&23~sB-mVNk%4?.T1d6Y.$c",
            "1hi?2I5ylhYkhwcb@&3AMb.~1_EkCe",
            "i92eYR69wV06B&j2a.q/KEKQtKk?2c",
            "X6wCs4s#MDF_99D1No$~O$J22A4/q2",
            "7m50Z7+~gHD_bT&X=vT@m32/D.q!%e",
            "846?&zK=FIQd3.~5T6O?775.bQ=IC%",
            "ht!3yKP9/Jmbdz!ikT-Ea$gTY3t_Q5",
            "GUTd5Qe@6/NKv5=I3_I_u$DNmaN!A~",
            "HGJi9%wAt~CZ@5=NPe~=F.5B6vnm7o",
            "8r0+99-4.h8A3wG75vtvTlBJ18uXdV",
            "B&*M74*@JdIMI.~L9f$d40r+s82o5b",
            "NMH35$Ai0d_$==3%2#HySRuSE_.Q%Q",
            "2o!7T~e?*H0m32?5?nS2C0k01o4pG?",
            "=6_DM5EL68E*du%DrH6/261d7G9W0j",
            "X~00jdxTeNnxA79nBKm9RCb1L5+L2=",
            "h-*jAKP_2_cgkm3pKpg2~NFh2bNmFn",
            "w~PXi_?4=9K648@=r814h$gYj=._/C",
            "~f+fh0xfH/Zcf7iVj4L!4654S0s!r9",
            "%e27TK7uj$7J$V*&?Y~5D3W7BA.n_3",
            "NqclBn%q4t707110/@k40957o&438g",
            "03P/NvSP0~QUSf_/Wm/&I76zTi2Oqv",
            "D6C72l8_997~@Gt9aK9x$74qL~xqk_",
            "5.-J2I6w22O4&n.4y3DzF3g#w~.*-4",
            "_4/ct4v@b231yR.ZP6~590NXh4z-iD",
            "sUBb90-Y4EEMq469K*Kj/w5Z8GU4P_",
            "U7o=z$0!6Ous4EE+K+3?Yh08H6+dm&",
            "7&OI6sTl7P8k$%U$0r+6RPw7la8A9V",
            "z272?7XO1F@#kW7nPS&5r?+3--xG17",
            "A5u+mXY_R.f0iz?7MwP1-4d$R#I_+X",
            "4oGa84&H5ap8HA.U983~DQ_?8QDUgh",
            "=U9V4Bs6z+t@BS74yHPl@8d490467o",
        ],
        "decoder": __cmethst__.b32decode,
        "encoder": __cmethst__.b32encode,
    },
    {
        "codes": [
            "&ABCRe05$nxlulY%UrX3@$1C5=~5H_",
            "k2RyF9FfXXm5NKRM03_r4b*2N5..m&",
            "B!vX7NATP6V@8F3%S7~hRm%P&+vH%2",
            "l_1=jP6W8lk43vQZ4Ye3$Jzm1_ut$B",
            "cmOp/*a@U*#86wSzULM++e2Us4jsZU",
            "3*nXuaxG2BklNE&uVPPw94AK4$oA5~",
            "pv9Qe37_T_/K_xs*?ay6fWgy1-MKVW",
            "BZf~d80Z2gFqX2K6ViG5yt4274R4Ob",
            ".ELB/7o!U#JSt7c%9.0*s747Agz~/7",
            "ichai&GndO62QB449WgkD*2O0CouR~",
            "4#0F@@=S?R#-.780Jq1N885XNeVOAw",
            "ic@$fBtCb+Ft5M~o%lR3~wBaVYgB&@",
            "Ad4Mc4CeW/SR1q-$&izaC+!Q@043W9",
            "!*Mv*eTL*2R+$W7XT7@@@L+00JolBf",
            "XK*B4#Pfu79LJ0Nlup9=$Vx3@@n!t6",
            "hV*kcP&%j3K!b3=~E6I?gOP3=!$PqQ",
            "4%W.o@GaUO+Oj1Z3Py1#6A3%F2z5~7",
            "eqU#&b0_=1dc-8@/89X7RK=CItn*6~",
            "91fqX2=tK3t9H!7&PvUg4V31JhrUrg",
            "KX4m49q5NhZj/*8a#x&8#w8W#5MZ$+",
            "N@B7pU2?ph$GC3JLHq/p3q!0jI%L+i",
            "$COEn+6f?=1tR7At!8I9#.NW-rO71u",
            "07xo/!lf*UFr33i$1?_@FH=PWwcE/#",
            "4qe5.%Cq5R6/EE_-h0=3c90xT&ZT3!",
            "gKP4!Q.=S9jcgho8A&1uA53xk24Go8",
            "8@D6*-l7orPocT9_mhj84O1_i5-85!",
            "7MoFFl0k/t~cA%H8Tg0+ELJLa1.T12",
            "f~#3!k2D#Q1M~zP&6H7~*$3w/A48N4",
            ".s=9_rA/*V?=Z19P1F65uiJSpl.@84",
            "@h7=j3hd+-oLHy$%8Zw?Ha+=u118F/",
            ".8WWn4xZd*VvU%TE5a%3OYb=_$%2Vz",
            "U?@2VW87NE8jXf73M=~-67p#A%X?_5",
            "=T-EZ3nv#?7M9V2Y~0EsucV@KR0&/v",
            "63k537I35=1Qp~L_J2K1so+z.aG9Og",
            "1$Ch#F*OrHDnHR74#90K@9=8_6Z23m",
            "J1&R4j1uV4b2F72Y=&l#Eizr3E-%-U",
            "RD/+!vvxOg1VR~UDbz&CJ%f+9l5LVN",
            "m23snf5p?g3ilf9LlB.32A3JM!6g!Y",
            "+kR8a+jF!s@pO#290qM/DZ5_hO3K4G",
            "~6D%~F&2t=*c+acg+l17y+sQp6q#P_",
            "96!sui9z1FG/Y9b+Z5G0zMO5CHCam=",
            "6?7036Z-!@F2yH1Y/4rTl-#VDy?~nI",
            "Uci!*1XeT?0*p-&8m!m3LS!@!fXmx!",
            "Rzz%o9WZ!=4kMDS1-_Od=9-s+09fk8",
            "&~Q6_!8T/_#67b4G.FkZ.8qaR9IS%m",
            "4o$=9n614UnT3nP3Q~x!@9F9W8$2_d",
            "2w/~+O*cd~dtqgC.Ma865475zo/T%Q",
            "l9Oy16254TTb~Gd9k?irU#+8QR=7K0",
            "!J.Y730=5GPplJGh8e7&z0*8jJWO65",
            "@&$Y&@q#Y73z06pQ&4A.+jnx56%Tvc",
            "~jy=Wnp#_3LiuKNV5C5eB33V!M@lC!",
            "c5=O#+#H6d48.$A2se4!2A7wm6Tlzs",
            "=48zt4+54TO1246r5yL!gb4Mb046W%",
            "00cVm6-$7Ow2.#B*1@&+M45_uf73_x",
            "wjYy$5%TO.w68E7_6T*x1C~2CstuqG",
            ".?j5nUmd!J18t2y&467D9~3ju9~m_w",
            "nRx/_qM//ADs4uBS32$S45Q-%nSiLH",
            "M~FK6P2%tG$2V3hM7c6&4@$jszw@&V",
            "+DWwppWyUr/@/C=7fz7pa%4+@-6RT9",
            ".~38V0!SKv1LoSW67+vCC33n7%LWHZ",
            "%T&?4A*.j6JTHI=.+_423voK3xr$D.",
            "Qqei6cbTHa0@408Zqn8_U8xm$GfX%=",
            "$3GkC-Z2.V_4#zs+_I6PVO&fvEc.Dw",
            "9z-k6EnE1g%*&_vpY!91/wO1h$30JC",
            "N%2BOL_+#8J8-CFfB-_!~%7QM73?H9",
            "pdq9i+be&YRhes8t%3y=i5R9%#C755",
            "8+_H9~Z--%?M3$wp323qWP*UsT7d.g",
            "R%10jFaGS5BQTF_?Mq0_+E%gx6aJK3",
            "=.UrzP736$t.S7q5vO+r1uxf@G9bm4",
            "acsQ.H&/e=~6QuN/j1130x*#w738SD",
            "vW3e_*0Zblz2-4w2V+6P9ewZ*@+2~J",
            "yae210jf8Wd945YH2qD9iHTHgJ4-?7",
            "5c69*-H!7$W0vh/f91@g687Kl$1Im0",
            "5#5QRB.5IW9h*7zzxMj@@L8o6s7=82",
            "Mgkxsi=$k1PfWBQYSFcOCo8*$8/BMe",
            "7XvN+2v4Vo7ux9I3Ob584u7J99T8Mu",
            "28/3%-u5d?*KpK6SK%5.f?Ug!7yKT0",
            "!4zv3X8ElbSF8IK?69//_F+L*ZYyVl",
            "3.oax6YRKf&zJbyf@w-pX@#n?qMxZ1",
            "dK!8n0_-S72xqyr26R6HL$N59~o97D",
            "Sm6SeY~mGT%j1306z=hQ@7MPcr?k2v",
            "~A.*6Ln7am57&A/6sXJO~ih3no6J7x",
            "X5hi7?=U35%D7j-@8wU4X9w7*z9soI",
            "O5W/V!QO.wh6$DA92mM!+h*Wrr7Z8T",
            "5#?!04#e5W25EH2GS-?#5fED89J75g",
            "RRg%WpcpHz%QVd6c331$/?3?@4v=e.",
            "1q8C&P088X7b7033gA4c-Ud&BF&ZJ/",
            "Dr3X=sP=/L8K3G~6v?ulRVMtZ27NB5",
            "Dj#dF/bEG*--9UR.4Me3fu262!f6*K",
            "&TZ+qA?7JaU&rtp?e0?54-+NY21x2.",
            "QKN657uSAk4j601?wF*5/MQ1dHUQgI",
            "6fy?jTV+dN.Z6to_c.+8_Ds32e83QV",
            "7QFb?hE%fE6mb01~4*2D_Pw$po_741",
            "Vw9.2PE_t687L$=47W5wQMxTcE487#",
            "ClL%$i16iCi1F0073ki*2G1%Z3y$&&",
            "6Ot&/W?7fqg?65!XM433$7l4mh84x+",
            "8@Gf6O+ip&n?qzR@EjeN8ZgB.0SsDj",
            "~a_uwUo=+O!5tk49m96tQ/X%unFz??",
            "0KKlGz$7wR%.VF3086n_&@454_l_7O",
            "K0r.44XK5@N~NF*9K2+5b+Hnml_A*3",
        ],
        "decoder": __cmethst__.b16decode,
        "encoder": __cmethst__.b16encode,
    },
]

__spec__.data.compilerData = {
    "name": "protStringCompiler",
    "version": "1.1",
    "codeListID": "9611699982",
}

__spec__.data.compileOptions = [
    {"name": "type", "options": ["py", "data"], "default": "py"}
]


def encode(input, type="file"):
    if type == "file":
        pyFile = open(input)
        pyData = pyFile.read()
        pyFile.close()
    elif type in ["string", "str"]:
        pyData = input
    else:
        printErr("type is invalid")
        return
    encType = random.choice(__spec__.data.codeType)
    encCode = random.choice(encType["codes"])
    encFunc = encType["encoder"]
    encData = encCode + "\n" + str(encFunc(bytes(pyData, "utf-8")))[2:-1]
    return encData


def encrypt(input, output):
    encData = encode(input)
    encFile = open(output, "w")
    encFile.write(encData)
    encFile.flush()
    encFile.close()


def execute(input, type="file"):
    output = "exec"
    if type.startswith("out$"):
        output = "return"
        type = type[4:]
    if type == "file":
        pyFile = open(input)
        pyData = pyFile.read()
        pyFile.close()
    elif type in ["string", "str"]:
        pyData = input
    else:
        printErr("type is invalid")
        return
    pyLines = pyData.splitlines()
    encCode = pyLines[0]
    encData = pyLines[-1]
    encFunc = None
    for t in __spec__.data.codeType:
        for c in t["codes"]:
            if c == encCode:
                encFunc = t["decoder"]
    decData = list2str(str(encFunc(bytes(encData, "utf-8")))[2:-1].splitlines(), "\n")
    if output == "exec":
        decFile = open("decodedfile.py", "w")
        decFile.write(decData)
        decFile.flush()
        decFile.close()
        decMod = __import__("decodedfile")
        del decMod
        del sys.modules["decodedfile"]
        os.remove("decodedfile")
    else:
        return decData

import random
import math
from turtle import *
from tkinter import *



def timp0(szel,mag): # nem rajzol semmit
    up()
    down()

def timp1(szel,mag): # ablak fölötti egyszerű timpanon (2*szel*1.2 széles)
    alfa_t=math.radians(20)
    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    forward(szel*1.2)
    right(160)
    forward((szel*1.2)/math.cos(alfa_t))
    right(40)
    forward((szel*1.2)/math.cos(alfa_t))
    right(160)
    forward(szel*1.2)

    up()
    left(90)
    forward(mag*0.2)
    right(90)
    down()

def timp1b(szel,mag): # ablak fölötti egyszerű timpanon (2*szel*1.6 széles) ///összevonni az előzővel, +1 paraméter!///
    alfa_t=math.radians(20)
    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    forward(szel*1.6)
    right(160)
    forward((szel*1.6)/math.cos(alfa_t))
    right(40)
    forward((szel*1.6)/math.cos(alfa_t))
    right(160)
    forward(szel*1.6)

    up()
    left(90)
    forward(mag*0.2)
    right(90)
    down()

def timp2(szel,mag): # ablak fölötti egyszerű lunetta (2*szel*1.2 széles) 
    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    backward(szel*1.2)
    right(30)
    circle(szel*2.4,60)
    setheading(0)
    forward(szel*1.2)

    up()
    right(90)
    forward(mag*0.2)
    right(90)
    down()

def timp2b(szel,mag): # ablak fölötti egyszerű lunetta (2*szel*1.6 széles) ///összevonni az előzővel, +1 paraméter!///
    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    backward(szel*1.6)
    right(30)
    circle(szel*3.2,60)
    setheading(0)
    forward(szel*1.6)

    up()
    right(90)
    forward(mag*0.2)
    right(90)
    down()


def timp3(szel,mag): # ablak fölötti összetett timpanon (2*szel*1.2 széles)

    alfa_t=math.radians(20)
    x=((szel*1.2)/math.cos(alfa_t))
    y=(1.2*szel*math.tan(alfa_t)/9)


    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    forward(szel*1.2)
    right(160)
    forward(x)
    right(40)
    forward(x)
    right(160)
    forward(szel*1.2)

    forward(szel*1.2*0.8)
    right(160)
    forward(x*0.8)
    right(40)
    forward(x*0.8)
    right(160)
    forward(szel*1.2*0.8)

    up()
    left(90)
    forward(mag*0.06)
    right(90)
    down()

    forward(szel*1.2)
    right(90)
    forward(mag*0.06)
    left(20)
    forward(1.2*szel/9)
    right(90)
    forward(x+y)
    right(40)
    forward(x+y)
    right(90)
    forward(1.2*szel/9)
    left(20)
    forward(mag*0.06)
    right(90)
    forward(szel*1.2)


    up()
    left(90)
    forward(mag*0.14)
    right(90)
    down()

def timp3b(szel,mag): # ablak fölötti összetett timpanon (2*szel*1.6 széles) ///összevonni az előzővel, +1 paraméter!///
    alfa_t=math.radians(20)
    x=((szel*1.6)/math.cos(alfa_t))
    y=(1.6*szel*math.tan(alfa_t)/9)


    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    forward(szel*1.6)
    right(160)
    forward(x)
    right(40)
    forward(x)
    right(160)
    forward(szel*1.6)

    forward(szel*1.6*0.8)
    right(160)
    forward(x*0.8)
    right(40)
    forward(x*0.8)
    right(160)
    forward(szel*1.6*0.8)

    up()
    left(90)
    forward(mag*0.06)
    right(90)
    down()

    forward(szel*1.6)
    right(90)
    forward(mag*0.06)
    left(20)
    forward(1.6*szel/9)
    right(90)
    forward(x+y)
    right(40)
    forward(x+y)
    right(90)
    forward(1.6*szel/9)
    left(20)
    forward(mag*0.06)
    right(90)
    forward(szel*1.6)

    up()
    left(90)
    forward(mag*0.14)
    right(90)
    down()

def timp4(szel,mag): # ablak fölötti összetett lunetta (2*szel*1.2 széles) 
    x=1.2
    r1=szel*2*x #(r1: radius1)
    r2=math.sqrt(r1**2-(r1/2)**2+(0.8*x*szel)**2) #(r2: radius2)
    alpha=math.degrees(math.asin(r1*0.4/r2))

    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    backward(szel*x)
    right(30)
    circle(r1,60)
    right(30)
    backward(szel*x+szel*x*0.8)

    right(alpha)
    circle(r2,alpha*2)
    right(alpha)
    backward(szel*x*0.8)


    up()
    left(90)
    forward(mag*0.06)
    right(90)
    down()

    backward(szel*x)
    right(90)
    forward(mag*0.06)

    right(30)
    forward(x*szel/9) #legfelső körívnél ennyivel nő a sugár
    left(90)
    circle(r1+x*szel/9,60)
    left(90)
    forward(x*szel/9)
    right(30)

    forward(mag*0.06)
    right(90)
    backward(szel*x)

    up()
    left(90)
    forward(mag*0.14)
    right(90)
    down()

def timp4b(szel,mag): # ablak fölötti összetett lunetta (2*szel*1.6 széles) ///összevonni az előzővel, +1 paraméter!///
    x=1.6
    r1=szel*2*x #(r1: radius1)
    r2=math.sqrt(r1**2-(r1/2)**2+(0.8*x*szel)**2) #(r2: radius2)
    alpha=math.degrees(math.asin(r1*0.4/r2))

    up()
    right(90)
    forward(mag*0.2)
    left(90)
    down()

    backward(szel*x)
    right(30)
    circle(r1,60)
    right(30)
    backward(szel*x+szel*x*0.8)

    right(alpha)
    circle(r2,alpha*2)
    right(alpha)
    backward(szel*x*0.8)

    up()
    left(90)
    forward(mag*0.06)
    right(90)
    down()

    backward(szel*x)
    right(90)
    forward(mag*0.06)

    right(30)
    forward(x*szel/9) # legfelső körívnél ennyivel nő a sugár
    left(90)
    circle(r1+x*szel/9,60)
    left(90)
    forward(x*szel/9)
    right(30)

    forward(mag*0.06)
    right(90)
    backward(szel*x)

    up()
    left(90)
    forward(mag*0.14)
    right(90)
    down()

def win1(szel,mag,timpanon): # téglalap ablak
    forward(szel)
    left(90)
    forward(mag*2)
    left(90)
    forward(szel)

    timpanonrajz=timpanon  ###### /// ezt itt lehet máshogy kéne /// lásd pillar vagy ajtó
    timpanonrajz(szel,mag) ###### /// ezt itt lehet máshogy kéne /// lásd pillar vagy ajtó

    forward(szel)
    left(90)
    forward(mag*2*0.33)
    left(90)
    forward(szel*2)
    right(90)
    forward(mag*2*0.67)
    right(90)
    forward(szel)
    right(90)
    forward(mag*2*0.67)
    left(90)
    forward(szel)
    left(90)
    forward(mag*2*0.67)
    left(90)
    forward(szel)

def win2(szel,mag,timpanon): # félköríves ablak (most nem aktív)
    forward(szel)
    left(90)
    forward(mag*2-szel)
    circle(szel,180)
    forward(mag*2-szel)
    left(90)
    forward(szel)
    left(90)
    forward(mag*2*0.67)
    right(90)
    forward(szel)
    backward(szel*2)
    forward(szel)
    right(90)
    forward(mag*2*0.67)
    left(90)

def baluster(bwd,bht): # (bwd: baluster width, bht: baluster height)
    alfa_b=math.radians(15)
    forward(bwd)
    left(90)
    forward(bht/2)
    left(90)
    forward(bwd)
    backward(bwd)
    right(60)
    forward(bwd)
    right(90)
    circle(bwd,60)
    left(15)
    forward(3*bwd/(4*math.sin(alfa_b)))
    right(105)
    backward(bwd/4)
    forward(bwd/4)
    circle(bwd/8,180)

    forward(bwd/4)
    backward(bwd/4)
    right(120)
    forward(bwd/2)
    left(120)
    forward(bwd/2)
    backward(bwd)
    right(90)
    forward(bht/4)
    left(90)

    forward(bwd*2)

    left(90)
    forward(bht/4)
    right(90)
    backward(bwd)
    forward(bwd/2)
    left(120)
    forward(bwd/2)
    right(120)
    backward(bwd/4)
    forward(bwd/4)

    circle(bwd/8,180)
    forward(bwd/4)
    backward(bwd/4)
    right(105)
    forward(3*bwd/(4*math.sin(alfa_b)))
    left(15)
    circle(bwd,60)
    right(90)
    forward(bwd)
    right(60)
    backward(bwd)
    forward(bwd)
    left(90)
    forward(bht/2)
    left(90)
    forward(bwd)

def balustrade(bwd,bht,bdb): # (bwd: baluster width, bht: baluster height, bdb: baluster darab)
    for steps in range(bdb):
        forward(bwd*5/4)
        baluster(bwd,bht)
        forward(bwd*5/4)

def balustrade_under_window(szel,mag,bdb): # (bdb: baluster darab)
   bwd=szel/8
   bht=mag/8
   up()
   backward(bwd*bdb*5/4) # ///szel*35/32///
   right(90)
   forward(mag*10/16)
   down()
   for steps in range(2):
       forward(mag*2/16)
       left(90)
       forward(bwd*bdb*5/2)
       left(90)
   left(90)
   balustrade(bwd,bht,bdb)
   up()
   backward(bwd*bdb*5/4)
   right(90)
   backward(mag*10/16)
   left(90)
   down()


def phead1(pwd,pht): # pillarhead (dór oszlopfő) (pwd: pillar width, pht: pillar height)
    forward(pwd/4)
    circle(pwd/8,90)
    right(90)
    backward(pwd*6/8)
    forward(pwd*7/8)
    left(90)
    forward(pwd/8)
    left(90)
    forward(pwd)
    left(90)
    forward(pwd/8)
    left(90)
    forward(pwd*1/8)
    right(90)
    circle(pwd/8,90)
    forward(pwd/4)

def phead2(pwd,pht): # pillarhead (ión oszlopfő) (pwd: pillar width, pht: pillar height)
    up()
    left(90)
    forward(pwd/3.5)
    right(90)
    down()

    forward(pwd/4)
    w=1
    while w<50:
        forward((50-w)*pwd/800)
        right(20+w/4)
        w=w+1
    w=49
    while w>0:
        left(20+w/4)
        backward((50-w)*pwd/800)
        w=w-1
    backward(pwd/2)
    w=1
    while w<50:
        backward((50-w)*pwd/800)
        left(20+w/4)
        w=w+1
    w=49
    while w>0:
        right(20+w/4)
        forward((50-w)*pwd/800)
        w=w-1
    forward(pwd/4)

    up()
    left(90)
    backward(pwd/3.5)
    right(90)
    down()

def pleg(pwd,pht): # pillarleg (pwd: pillar width, pht: pillar height)
    forward(pwd*0.34)
    left(90)
    forward(pwd*0.68)
    left(90)
    forward(pwd*0.34)
    backward(pwd*0.34)

    right(math.degrees(math.asin(3/5)))
    forward(pwd*0.05)
    left(math.degrees(math.asin(3/5)))
    forward(pwd*0.30*2)
    left(math.degrees(math.asin(3/5)))
    forward(pwd*0.05)
    right(math.degrees(math.asin(3/5)))

    backward(pwd*0.34)
    forward(pwd*0.34)
    left(90)
    forward(pwd*0.68)
    left(90)
    forward(pwd*0.34)

def pillarornament0(pwd,pht): # (nincs barázda)
    up()
    down()

def pillarornament1(pwd,pht):   # ritka oszlopbarázda  ///(values_pillarorn, n, m, a)///
    up()                        
    forward(pwd/4)
    left(90)
    forward(pht*19/10)
    left(90)
    down()
    values_pillarorn=(0.07,0.18,0.25,0.25,0.18,0.07)   #barázdatávolságok
    n=1
    for steps in range(6):
        m=values_pillarorn[n-1]
        right(30)
        circle(0.5*pwd*m,60)
        right(30)
        n=n+1

    left(90)
    forward(pht*18/10)
    left(90)

    n=1
    for steps in range(6):
        m=values_pillarorn[n-1]
        right(30)
        circle(0.5*pwd*m,60)
        right(30)
        n=n+1

    n=1
    a=1
    for steps in range(6):
        m=values_pillarorn[n-1]
        up()
        backward(0.5*pwd*m)
        down()
        left(90*a)
        forward(pht*18/10)
        right(90*a)
        n=n+1
        a=a*-1
    right(90)
    forward(pht*1/10)
    left(90)
    forward(pwd/4)

def pillarornament2(pwd,pht): # sűrű oszlopbarázda  ///(values_pillarorn, n, m, a)///
    up()
    forward(pwd/4)
    left(90)
    forward(pht*19/10)
    left(90)
    down()
    values_pillarorn=(0.05,0.10,0.15,0.20,0.20,0.15,0.10,0.05) #barázdatávolságok
    n=1
    for steps in range(8):
        m=values_pillarorn[n-1]
        right(30)
        circle(0.5*pwd*m,60)
        right(30)
        n=n+1

    left(90)
    forward(pht*18/10)
    left(90)

    n=1
    for steps in range(8):
        m=values_pillarorn[n-1]
        right(30)
        circle(0.5*pwd*m,60)
        right(30)
        n=n+1

    n=1
    a=1
    for steps in range(8):
        m=values_pillarorn[n-1]
        up()
        backward(0.5*pwd*m)
        down()
        left(90*a)
        forward(pht*18/10)
        right(90*a)
        n=n+1
        a=a*-1
    right(90)
    forward(pht*1/10)
    left(90)
    forward(pwd/4)

def pillarbody(pwd,pht,pheadtype): # oszloptest + oszlopfő
    forward(pwd/4)
    left(90)
    forward(pht*2)
    right(90)
    backward(pwd/4)
    pillarhead=pheadtype
    pillarhead(pwd,pht)
    backward(pwd/4)
    right(90)
    forward(pht*2)
    left(90)
    forward(pwd/4)

def pillar(pwd,pht,pheadtype,pillarornament):
    pleg(pwd,pht)
    up()
    left(90)
    forward(pwd*0.71)
    right(90)
    down()
    pillarbody(pwd,pht,pheadtype)
    pillarornament(pwd,pht)
    up()
    right(90)
    forward(pwd*0.71)
    left(90)
    down()

def pilaster(szel,mag,blokkemelet,blokkdb):
    pwd=(szel*2)
    pht=(mag*blokkemelet*5/3)
    pheadtype=phead1
    pillarornament=pillarornament1

    for steps in range(blokkdb-1):
        backward(szel*5)
        pillar(pwd,pht,pheadtype,pillarornament)
    forward(szel*5*(blokkdb-1))




def window0(szel,mag,timptype0): #dísztelen vertikális tag (blokk) ablaka
    timpanon=timptype0
    win1(szel,mag,timpanon)

def window0b(szel,mag,timptype0): #dísztelen vertikális tag (blokk) ablaka balusztráddal
    bdb=7
    timpanon=timptype0
    win1(szel,mag,timpanon)
    balustrade_under_window(szel,mag,bdb)

def window1(szel,mag,timptype1): #díszes vertikális tag (blokk) ablaka
    timpanon=timptype1
    win1(szel,mag,timpanon)
    pwd=(szel/2)
    pht=(mag*0.90)
    pheadtype=phead1
    pillarornament=pillarornament0
    backward(szel*1.3)
    pillar(pwd,pht,pheadtype,pillarornament)
    forward(szel*2.6)
    pillar(pwd,pht,pheadtype,pillarornament)
    backward(szel*1.3)

def window1b(szel,mag,timptype1): #díszes vertikális tag (blokk) ablaka balusztráddal
    bdb=9
    timpanon=timptype1
    win1(szel,mag,timpanon)
    balustrade_under_window(szel,mag,bdb)
    pwd=(szel/2)
    pht=(mag*0.90)
    pheadtype=phead1
    pillarornament=pillarornament0
    backward(szel*1.3)
    pillar(pwd,pht,pheadtype,pillarornament)
    forward(szel*2.6)
    pillar(pwd,pht,pheadtype,pillarornament)
    backward(szel*1.3)

#def ajto0(szel,mag): # egyszerű íves ajtó (most nem aktív)
#	forward(szel*1.5)
#	right(90)
#	forward(mag*2.5)
#	circle(szel,180)
#	forward(mag*2.5)
#	right(90)
#	forward(szel*1.5)

def ajto1(szel,mag):
        s=1
        forward(szel*1.5)
        right(90)
        for steps in range(8):
                right(90)
                forward(szel*1.5)
                backward(szel*1.5)
                left(90)
                forward(mag/4)
        right(90)
        forward(szel*1.5)
        backward(szel*1.5)
        left(90)
        while s<7:
                alfa=math.radians(s*180/13)
                sinalfa=math.sin(alfa)
                tanalfa=math.tan(alfa)
                circle(szel,(180/13))
                right(90)
                forward((s*mag)/(4*sinalfa)-szel)
                right(s*180/13)
                forward(2.5*szel-(s*mag)/(4*tanalfa))
                backward(2.5*szel-(s*mag)/(4*tanalfa))
                left(s*180/13)
                backward((s*mag)/(4*sinalfa)-szel)
                left(90)
                s=s+1
        s=6
        while s>0:
                alfa=math.radians(s*180/13)
                sinalfa=math.sin(alfa)
                tanalfa=math.tan(alfa)
                circle(szel,(180/13))
                right(90)
                forward((s*mag)/(4*sinalfa)-szel)
                left(s*180/13)
                forward(2.5*szel-(s*mag)/(4*tanalfa))
                backward(2.5*szel-(s*mag)/(4*tanalfa))
                right(s*180/13)
                backward((s*mag)/(4*sinalfa)-szel)
                left(90)
                s=s-1

        circle(szel,(180/13))
        right(90)
        forward(szel*1.5)
        backward(szel*1.5)
        left(90)
        for steps in range(8):
                forward(mag/4)
                right(90)
                forward(szel*1.5)
                backward(szel*1.5)
                left(90)
        right(90)
        forward(szel*1.5)

        up()                #+1 sor
        right(90)
        forward(3.75*mag)
        left(90)
        down()
        backward(5*szel)
        forward(5*szel)
        up()
        left(90)
        forward(3.75*mag)
        right(90)
        down()

def ajto2(szel,mag):
        s=1
        forward(szel*1.5)
        right(90)
        for steps in range(8):
                right(90)
                forward(szel*1.5)
                backward(szel*1.5)
                left(90)
                forward(mag/4)
        right(90)
        forward(mag/0.95-szel)
        left(90)
        forward(mag/4)
        backward(mag/4)
        right(90)
        forward(szel*1.5-(mag/0.95-szel))
        backward(szel*1.5)
        left(90)
        while s<7:
                alfa=math.radians(s*180/13)
                sinalfa=math.sin(alfa)
                tanalfa=math.tan(alfa)
                circle(szel,(180/13))
                right(90)
                forward((s*mag)/(4*sinalfa)-szel)
                right(s*180/13)
                forward(2.5*szel-(s*mag)/(4*tanalfa))
                backward(2.5*szel-(s*mag)/(4*tanalfa))
                if s<6:
                        left(90)
                        forward(mag/4)
                        backward(mag/4)
                        right(90)
                if s==6:
                        backward(szel/3)
                        forward(szel/3)
                left(s*180/13)
                backward((s*mag)/(4*sinalfa)-szel)
                left(90)
                s=s+1
        s=6
        while s>0:
                alfa=math.radians(s*180/13)
                sinalfa=math.sin(alfa)
                tanalfa=math.tan(alfa)
                circle(szel,(180/13))
                right(90)
                forward((s*mag)/(4*sinalfa)-szel)
                left(s*180/13)
                forward(2.5*szel-(s*mag)/(4*tanalfa))
                backward(2.5*szel-(s*mag)/(4*tanalfa))
                if s<6:
                        right(90)
                        forward(mag/4)
                        backward(mag/4)
                        left(90)
                if s==6:
                        backward(szel/3)
                        forward(szel/3)
                right(s*180/13)
                backward((s*mag)/(4*sinalfa)-szel)
                left(90)
                s=s-1

        circle(szel,(180/13))
        right(90)
        forward(mag/0.95-szel)
        right(90)
        forward(mag/4)
        backward(mag/4)
        left(90)
        forward(szel*1.5-(mag/0.95-szel))
        backward(szel*1.5)
        left(90)
        for steps in range(8):
                forward(mag/4)
                right(90)
                forward(szel*1.5)
                backward(szel*1.5)
                left(90)
        right(90)
        forward(szel*1.5)

        up()                #+1 sor
        right(90)
        forward(3.75*mag)
        left(90)
        down()
        backward(5*szel)
        forward(5*szel)
        up()
        left(90)
        forward(3.75*mag)
        right(90)
        down()

def ajto3(szel,mag):
        forward(szel*1.5)
        right(90)
        t=1
        for steps in range(8):
                forward(mag/4)
                right(90)
                forward((szel/2)+(t*szel/6))
                right(90)
                forward(mag/4)
                right(90)
                forward((szel/2)+(t*szel/6))
                right(90)
                forward(mag/4)
                t=t*-1


        right(90)
        forward((mag/0.98591145-szel)*1.1)
        left(90)
        forward(mag/4)
        left(90)
        forward((mag/0.98591145-szel)*0.1)
        backward((mag/0.98591145-szel)*0.1)
        right(90)
        backward(mag/4)
        right(90)
        backward((mag/0.98591145-szel)*1.1)
        left(90)
        s=1
        while s<7:
                alfa=math.radians(s*180/13)
                sinalfa=math.sin(alfa)
                tanalfa=math.tan(alfa)
                alfa2=math.radians((s+1)*180/13)
                tanalfa2=math.tan(alfa2)
                x=2.5*szel-(s*mag)/(4*tanalfa)
                y=2.5*szel-((s+1)*mag)/(4*tanalfa2)
                circle(szel,(180/13))
                right(90)
                forward((s*mag)/(4*sinalfa)-szel)
                right(s*180/13)
                if s<6:
                        left(90)
                        forward(mag/4)
                        left(90)
                        forward(y-x)
                        backward(y-x)
                        right(90)
                        backward(mag/4)
                        right(90)
                if s==6:
                        backward(szel/3)
                        forward(szel/3)
                left(s*180/13)
                backward((s*mag)/(4*sinalfa)-szel)
                left(90)
                s=s+1

        s=6
        while s>0:
                alfa=math.radians(s*180/13)
                sinalfa=math.sin(alfa)
                tanalfa=math.tan(alfa)
                alfa2=math.radians((s+1)*180/13)
                tanalfa2=math.tan(alfa2)
                x=2.5*szel-(s*mag)/(4*tanalfa)
                y=2.5*szel-((s+1)*mag)/(4*tanalfa2)
                circle(szel,(180/13))
                right(90)
                forward((s*mag)/(4*sinalfa)-szel)
                left(s*180/13)
                if s<6:
                        right(90)
                        forward(mag/4)
                        right(90)
                        forward(y-x)
                        backward(y-x)
                        left(90)
                        backward(mag/4)
                        left(90)
                if s==6:
                        backward(szel/3)
                        forward(szel/3)
                right(s*180/13)
                backward((s*mag)/(4*sinalfa)-szel)
                left(90)
                s=s-1

        circle(szel,(180/13))
        right(90)
        forward((mag/0.98591145-szel)*1.1)
        right(90)
        forward(mag/4)
        right(90)
        forward((mag/0.98591145-szel)*0.1)
        backward((mag/0.98591145-szel)*0.1)
        left(90)
        backward(mag/4)
        left(90)
        backward((mag/0.98591145-szel)*1.1)
        left(90)
        t=-1
        for steps in range(8):
                forward(mag/4)
                right(90)
                forward((szel/2)+(t*szel/6))
                right(90)
                forward(mag/4)
                right(90)
                forward((szel/2)+(t*szel/6))
                right(90)
                forward(mag/4)
                t=t*-1
        right(90)
        forward(szel*1.5)

def ajto(szel,mag,doortype):
	up()
	forward(szel*2.5)
	right(90)
	forward(mag)
	right(90)
	down()
	doortype(szel,mag)
	up()
	right(90)
	forward(mag)
	right(90)
	forward(szel*2.5)
	down()

#def tegla1(emelet,szel,mag):
#	for steps in range(emelet*8+10):
#			backward(szel)
#			left(90)
#			forward(mag/4)
#			right(90)
#			forward(szel)
#			backward(szel/2)
#			left(90)
#			forward(mag/4)
#			right(90)
#			forward(szel/2)

#def tegla2(emelet,szel,mag):
#	for steps in range(emelet*8+10):
#			backward(szel/2)
#			left(90)
#			forward(mag/4)
#			right(90)
#			forward(szel/2)
#			backward(szel)
#			left(90)
#			forward(mag/4)
#			right(90)
#			forward(szel)

def brick1(blokkemelet,szel,mag):
	for steps in range(blokkemelet*8):
			backward(szel/2)
			left(90)
			forward(mag/4)
			right(90)
			forward(szel/2)
			backward(szel/4)
			left(90)
			forward(mag/4)
			right(90)
			forward(szel/4)

def brick2(blokkemelet,szel,mag): # ///össze lehet vonni az előzővel///
	for steps in range(blokkemelet*8):
			backward(szel/4)
			left(90)
			forward(mag/4)
			right(90)
			forward(szel/4)
			backward(szel/2)
			left(90)
			forward(mag/4)
			right(90)
			forward(szel/2)

def tetoalj0(szel,mag,dbsum,xtra_sum):
    forward(5*szel*dbsum+szel*xtra_sum)
    left(90)
    forward(3*mag/4)
    left(90)
    forward(5*szel*dbsum+szel*xtra_sum)
    right(90)
    backward(3*mag/4)
    forward(3*mag/4)
    right(90)

#def tetoalj1(szel,mag,dbsum,xtra_sum):
#    tetoalj0(szel,mag,dbsum,xtra_sum)
#    for steps in range(dbsum*5+2):
#        forward(szel/4)
#        right(90)
#        forward(mag/2)
#        left(90)
#        forward(szel/2)
#        left(90)
#        forward(mag/2)
#        right(90)
#        forward(szel/4)
#    right(90)
#    forward(3*mag/4)

def tetoalj2(szel,mag,dbsum,xtra_sum):
    tetoalj0(szel,mag,dbsum,xtra_sum)
    v=(5*dbsum+xtra_sum)
    for steps in range(int(v)):             # ///floatból integert csinál az int(v), osztás miatt lett float az xtra_sum (?)///
        forward(3*szel/8)
        right(90)
        forward(mag/2)
        left(90)
        forward(szel/4)
        left(90)
        forward(mag/2)
        right(90)
        forward(3*szel/8)
    right(90)
    forward(3*mag/4)

#def tetoalj3(szel,mag,dbsum,xtra_sum):
#    tetoalj0(szel,mag,dbsum,xtra_sum)
#    forward(7*szel/8)
#    for steps in range(dbsum*2):
#        right(90)
#        forward(mag/2)
#        left(90)
#        forward(szel/4)
#        left(90)
#        forward(mag/2)
#        right(90)
#        forward(18*szel/8)
#    right(90)
#    forward(mag/2)
#    left(90)
#    forward(szel/4)
#    left(90)
#    forward(mag/2)
#    right(90)
#    forward(7*szel/8)
#    right(90)
#    forward(3*mag/4)

def tetoalj(szel,mag,dbsum,xtra_sum): 
    #values_j=(tetoalj2,tetoalj3)
    #tetoaljx=(random.choice(values_j))
    #tetoaljx(szel,mag,dbsum,xtra_sum)
    tetoalj2(szel,mag,dbsum,xtra_sum)

def ablakok0(szel,mag,blokkdb,blokkemelet,wintype0,timptype0,hpos,doortype): # dísztelen vertikális tag (blokk) ablaksorait rajzolja, egy teljes blokkot 
        e=1
        while e<=blokkemelet:
            for steps in range(blokkdb): # ablaksort rajzol
                    up()
                    forward(szel*2.5)
                    down()
                    if e==1 and hpos==1:
                        ajto(szel,mag,doortype)
                    else:
                        wintype0(szel,mag,timptype0)   # ////hiba!!! itt window0 volt.............////
                    up()
                    forward(szel*2.5)
                    down()
            if e==blokkemelet:  # kész a blokk, elmegy a blokk jobb alsó sarkába
                up()
                right(90)
                forward(4*mag*(blokkemelet-1)+mag)
                left(90)
                down()
                e=e+1
            else:               # új ablaksor megkezdéséhez visszamegy a sor kezdőpontjára
                up()
                backward(blokkdb*szel*5)
                left(90)
                forward(mag*4)
                right(90)
                down()
                e=e+1

def ablakok1(szel,mag,blokkdb,blokkemelet,wintype1,timptype1,hpos,doortype): # dísztelen vertikális tag (blokk) ablaksorait rajzolja, egy teljes blokkot 
        f=1
        while f<=blokkemelet:
            for steps in range(blokkdb): # ablaksort rajzol
                    up()
                    forward(szel*2.5)
                    down()
                    if f==1 and hpos==1:
                        ajto(szel,mag,doortype)
                    else:
                        wintype1(szel,mag,timptype1)      # ////hiba!!! itt window1 volt.............////
                    up()
                    forward(szel*2.5)
                    down()
            if f==blokkemelet:  # kész a blokk, elmegy a blokk jobb alsó sarkába
                up()
                right(90)
                forward(4*mag*(blokkemelet-1)+mag)
                left(90)
                down()
                f=f+1
            else:               # új ablaksor megkezdéséhez visszamegy a sor kezdőpontjára
                up()
                backward(blokkdb*szel*5)
                left(90)
                forward(mag*4)
                right(90)
                down()
                f=f+1

def blokkkeret0(szel,mag,blokkdb,blokkemelet): # dísztelen vertikális tag (blokk) keretét rajzolja
    forward(5*blokkdb*szel)
    left(90)
    forward(4*blokkemelet*mag)
    left(90)
    forward(5*blokkdb*szel)
    left(90)
    forward(4*blokkemelet*mag)
    left(90)

def blokkkeret1(szel,mag,blokkdb,blokkemelet,xtrawd): # díszes vertikális tag (blokk) keretét rajzolja (szélesebb ennyivel: xtrawd*szel)
    forward(5*blokkdb*szel+xtrawd*szel)
    left(90)
    forward(4*blokkemelet*mag)
    left(90)
    forward(5*blokkdb*szel+xtrawd*szel)
    left(90)
    forward(4*blokkemelet*mag)
    left(90)

def blokk0(szel,mag,blokkdb,blokkemelet,wintype0,timptype0,hpos,doortype,hblokksum,pilaster_yn): # dísztelen
    blokkkeret0(szel,mag,blokkdb,blokkemelet)
    left(90)
    forward(mag)
    right(90)
    ablakok0(szel,mag,blokkdb,blokkemelet,wintype0,timptype0,hpos,doortype)
    if blokkemelet==2 and blokkdb>2 and hpos>1 and hpos!=hblokksum and pilaster_yn==1:
        pilaster(szel,mag,blokkemelet,blokkdb)
        
    

def blokk1(szel,mag,blokkdb,blokkemelet,wintype1,timptype1,hpos,doortype,xtrawd): # díszes
    blokkkeret1(szel,mag,blokkdb,blokkemelet,xtrawd)
    forward(5*blokkdb*szel+xtrawd*szel)
    brick1(blokkemelet,szel,mag)
    left(180)
    forward(5*blokkdb*szel+xtrawd*szel)
    brick2(blokkemelet,szel,mag)
    left(180)

    left(90)
    forward(mag)
    right(90)
    up()
    forward(szel*0.5*xtrawd)
    down()
    ablakok1(szel,mag,blokkdb,blokkemelet,wintype1,timptype1,hpos,doortype)
    up()
    forward(szel*0.5*xtrawd)
    down()

def blokkhaz(szel,mag,dbsum,emsum):

        #dbsum=int(var_db.get()) #start_haz-nal van
        #emsum=int(var_em.get()) #start_haz-nal van

        b_em1=([1],[1])         #tagolástípusok
        b_db1=([1],[1])
        b_em2=([1,1],[2])
        b_db2=([2],[2])
        b_em3=([1,1,1],[1,2],[2,1],[3])
        b_db3=([3],[3],[1,1,1],[1,1,1],[1,1,1],[1,1,1])
        b_em4=([1,2,1],[1,1,2],[2,2],[1,3],[3,1],[4],[1,2,1],[1,2,1],[1,2,1],[1,2,1],[1,2,1],[1,2,1])
        b_db4=([1,2,1],[4],[1,2,1],[1,2,1],[1,2,1],[1,2,1],[1,2,1])
        b_em5=([1,2,2],[1,3,1],[1,1,3],[3,1,1],[1,2,1,1],[1,4],[4,1],[2,3],[5],[1,2,2],[1,2,2],[1,2,1,1],[1,2,1,1],[1,2,1,1],[1,2,1,1],[1,2,1,1],[1,2,1,1])
        b_db5=([1,3,1],[5],[1,3,1],[1,3,1],[1,3,1],[1,3,1],[1,3,1])
        b_em6=([2,2,1,1],[1,2,2,1],[2,2,2],[2,3,1],[1,4,1],[1,1,4],[2,4],[1,5],[6],[2,2,1,1],[1,2,2,1],[2,2,2],[2,3,1],[1,4,1],[1,2,2,1],[1,2,2,1],[1,2,2,1],[1,2,2,1],[1,2,2,1])       
        b_db6=([1,4,1],[2,2,2],[6],[1,4,1],[1,4,1])
        b_db7=([1,5,1],[2,3,2],[1,5,1],[2,3,2])
        b_db8=([1,6,1],[2,4,2],[1,6,1],[2,4,2])
        b_db9=([1,7,1],[2,5,2],[3,3,3],[1,7,1],[2,5,2],[2,5,2],[2,5,2],[3,3,3],[2,1,3,1,2],[2,1,3,1,2])
        b_db10=([1,8,1],[2,6,2],[3,4,3],[1,8,1],[2,6,2],[3,4,3],[2,6,2],[1,8,1],[2,1,4,1,2],[2,1,4,1,2],[1,3,2,3,1],[1,3,2,3,1],[1,3,2,3,1],[1,3,2,3,1],[1,3,2,3,1],[1,3,2,3,1])
        b_db11=([1,9,1],[2,7,2],[3,5,3],[1,9,1],[2,7,2],[3,5,3],[1,9,1],[2,7,2],[2,1,5,1,2],[2,1,5,1,2],[2,1,5,1,2],[2,1,5,1,2],[1,3,3,3,1],[1,3,3,3,1],[1,3,3,3,1],[1,3,3,3,1])
        b_db12=([1,10,1],[2,8,2],[3,6,3],[1,10,1],[2,8,2],[3,6,3],[1,10,1],[2,8,2],[3,6,3],[2,1,6,1,2],[2,1,6,1,2],[1,3,4,3,1],[1,3,4,3,1],[1,3,4,3,1],[1,3,4,3,1],[1,3,4,3,1],[1,3,4,3,1],[1,3,4,3,1],[1,3,4,3,1],[1,3,4,3,1])



        blokkdb_x=[b_db1,b_db2,b_db3,b_db4,b_db5,b_db6,b_db7,b_db8,b_db9,b_db10,b_db11,b_db12]
        blokkem_x=[b_em1,b_em2,b_em3,b_em4,b_em5,b_em6]
        blokkdbsor=(random.choice(blokkdb_x[dbsum-1]))          # kisorsolja hogy melyik típusú vertikális tagolás legyen, a szintenkénti ablakszámtól (db) függően   
        blokkemeletsor=(random.choice(blokkem_x[emsum-1]))      # kisorsolja hogy melyik típusú horizontális tagolás legyen, a szintek számtól (em) függően 


        #dbsum=sum(blokkdbsor)           #elemek összegét adja meg, ennyi ablak (ajtó) van a házon szintenként  ///nem aktív, mert most a user eleve ezt adja meg és nem a tagolástípust/// 
        #emsum=sum(blokkemeletsor)       #elemek összegét adja meg, ennyi szintes a ház                         ///nem aktív, mert most a user eleve ezt adja meg és nem a tagolástípust/// 
        vblokksum=len(blokkdbsor)       #elemek számát adja meg, ennyi részre van tagolva vertikálisan a ház
        hblokksum=len(blokkemeletsor)   #elemek számát adja meg, ennyi részre van tagolva horizontálisan a ház
        values_op=(1,1,1,1,1,1,1,0)
        ornamentparity=(random.choice(values_op))   #ez alapján lesz majd eldöntve hogy a páratlan vpos legyen-e díszesebb vagy a páros
        vpos=1                                      #vertikális pozíciója a blokknak, a bal alsó sarokban rajzolja az elsőt, ennél a vpos=1
        hpos=1                                      #horizontális pozíciója a blokknak, a bal alsó sarokban rajzolja az elsőt, ennél a hpos=1
        xtrawd=1
        blokkdb=blokkdbsor[vpos-1]
        blokkemelet=blokkemeletsor[hpos-1]
        if vblokksum%2!=0 and ornamentparity==1:        #___________________________________________
                    xtra_sum=(vblokksum+1)/2

        elif vblokksum%2!=0 and ornamentparity==0:      #kiszámolja hogy hány extra széles blokk van
                    xtra_sum=(vblokksum-1)/2
        else:
                    xtra_sum=(vblokksum)/2              #___________________________________________

        v_t1=(timp4,timp4,timp4)
        v_t2=(timp4,timp4,timp4,timp4,timp4,timp3,timp3)# ///timp4 próba van, ettől sok a timp4///
        v_t3=(timp0,timp3,timp3,timp3)
        v_t4=(timp0,timp0,timp1)
        v_t5=(timp0,timp0)
        v_t6=(timp0,timp0)
        v_a1=(window0b,window0b) ### ///vpos.....///
        v_a2=(window0b,window0b)
        v_a3=(window0b,window0)
        v_a4=(window0,window0)
        v_a5=(window0,window0)
        v_a6=(window0,window0)
        v_p=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0)                   # (ilyen eséllyel lesz a pilaszter_yn értéke 1-es)
        valuelist_a=[v_a1,v_a2,v_a3,v_a4,v_a5,v_a6]
        valuelist_t=[v_t1,v_t2,v_t3,v_t4,v_t5,v_t6]
        values_d=(ajto1,ajto1,ajto2,ajto2,ajto3,ajto3)
        doortype=(random.choice(values_d))                      # ajtótípust sorsol
        wintype0=(random.choice(valuelist_a[hpos-1]))           # ablaktípust sorsol
        timptype0=(random.choice(valuelist_t[hpos-1]))          # timpanontípust sorsol
        pilaster_yn=random.choice(v_p)
        if wintype0==window0:                                   # hozzárendel díszes párokat a dísztelenekhez
                wintype1=(window1)
        if wintype0==window0b:
                wintype1=(window1b)
        if timptype0==timp0:
                timptype1=(timp3b)
        if timptype0==timp1:
                timptype1=(timp3b)
        if timptype0==timp2:
                timptype1=(timp2b)
        if timptype0==timp3:
                timptype1=(timp3b)
        if timptype0==timp4:
                timptype1=(timp4b)

        while vpos<=vblokksum:                              #____________________________________________________________________________________
                if (vpos%2==0) and (ornamentparity==1):
                    ornament=0
                elif (vpos%2!=0) and (ornamentparity==0):   #eldönti ornamentparity és vpos paritás alapján hogy melyik blokkok legyenek díszesek
                    ornament=0
                else:
                    ornament=1                              #____________________________________________________________________________________
                blokkdb=blokkdbsor[vpos-1]
                blokkemelet=blokkemeletsor[hpos-1]


                if ornament==1:
                                blokk1(szel,mag,blokkdb,blokkemelet,wintype1,timptype1,hpos,doortype,xtrawd)
                else:
                                blokk0(szel,mag,blokkdb,blokkemelet,wintype0,timptype0,hpos,doortype,hblokksum,pilaster_yn)

                if vpos==vblokksum and hblokksum==hpos:                     # kész, tetőaljat rajzol és elmegy a ház jobb alsó sarkába
                                up()
                                backward(5*szel*dbsum+szel*xtra_sum)
                                left(90)
                                forward(4*blokkemelet*mag)
                                right(90)
                                down()
                                tetoalj(szel,mag,dbsum,xtra_sum)            
                                up()
                                forward(4*mag*emsum)
                                left(90)
                                down()
                                vpos=vpos+1
                                hpos=hpos+1 
                elif vpos==vblokksum and hblokksum>hpos:                    # köv emeletet kezdi
                                up()
                                backward(5*szel*dbsum+szel*xtra_sum)
                                left(90)
                                forward(4*blokkemelet*mag)                  
                                right(90)
                                down()
                                vpos=1
                                hpos=hpos+1                                 
                                wintype0=(random.choice(valuelist_a[hpos-1]))               #sorsol
                                timptype0=(random.choice(valuelist_t[hpos-1]))              #sorsol
                                pilaster_yn=random.choice(v_p)                              #sorsol
                                if wintype0==window0:
                                    wintype1=(window1)
                                if wintype0==window0b:
                                    wintype1=(window1b)
                                if timptype0==timp0:
                                    timptype1=(timp3b)
                                if timptype0==timp1:
                                    timptype1=(timp3b)
                                if timptype0==timp2:
                                    timptype1=(timp2b)
                                if timptype0==timp3:
                                    timptype1=(timp3b)
                                if timptype0==timp4:
                                    timptype1=(timp4b)

                else:                                                       #   tovább rajzolja a blokksort
                                vpos=vpos+1

#def sel():
#    selection = 'Value = ' + str(var1.get())
#    label.config(text = selection)

def start_ablak():
    reset()
    bgcolor('black')
    color('grey')
    speed(0)
    szel=int(var1.get())*2
    mag=szel*1.5
    timpanon=timp0
    win2(szel,mag,timpanon)
    up()
    forward(1400)
    down()

def start_oszlop():
    reset()
    bgcolor('black')
    color('grey')
    speed(0)

    szel=int(var1.get())*2
    mag=szel*1.5
    pwd=(szel*2)
    pht=(mag*3)
    pheadtype=phead2
    pillarornament=pillarornament1
    up()
    right(90)
    forward(mag*3)
    left(90)
    down()
    pillar(pwd,pht,pheadtype,pillarornament)
    up()
    forward(1400)
    down()

def start_ajto():
    reset()
    bgcolor('black')
    color('grey')
    speed(0)
    szel=int(var1.get())*2
    mag=szel*1.5
    up()
    forward(szel*2.5)
    right(90)
    forward(mag*1.5)
    right(90)
    down()
    ajto3(szel,mag)
    up()
    forward(1400)
    down()

def start_haz():
    tracer(0, 0)
    dbsum=int(var_db.get())
    emsum=int(var_em.get())
    szel=int(var1.get())*2
    mag=szel*1.5
    if float(entry1.get())>float(entry2.get()):
            resxdiv2=float(entry1.get())/2
            resydiv2=float(entry2.get())/2
    else:
            resxdiv2=float(entry2.get())/2
            resydiv2=float(entry1.get())/2
    if resxdiv2*2 > (5*szel*dbsum+szel*2) and resydiv2*2 > (4*mag*emsum):
           reset()
           bgcolor('black')
           color('grey')
           speed(0)
           up()
           backward((5*szel*dbsum+szel*3)/2)
           right(90)
           forward((4*mag*emsum)/2)
           left(90)
           down()
           blokkhaz(szel,mag,dbsum,emsum)
           up()
           forward(1400)
           down()
    #elif xcor()==0 and ycor()==0 :
    else:
        reset()
        bgcolor('black')
        color('grey')
        speed(0)
        up()
        goto(-1*int(resxdiv2)+30,-1*int(resydiv2)+60)
        down()
        blokkhaz(szel,mag,dbsum,emsum)
        up()
        forward(1400)
        down()

def visszaallit():
    reset()
    bgcolor('black')
    color('grey')
    speed(0)

root = Tk()
var1 = IntVar()
var_em = IntVar()
var_db = IntVar()
entry1 = IntVar()
entry2 = IntVar()


txt1 = Label(root, text = 'Rajzoljunk klasszicista stílusú házakat!')
txt1.grid(row=0, sticky=W, padx=30, pady=10)

txt2 = Label(root, text = 'Írd ide a képernyőd felbontását:')
txt2.grid(row=1, sticky=W, padx=30, pady=10)

entry1 = Entry(root, width=5)
entry1.grid(row=2, column=0, sticky=W, padx=80, pady=10)

txt3 = Label(root, text = 'X')
txt3.grid(row=2, column=0)

entry2 = Entry(root, width=5)
entry2.grid(row=2, column=0, sticky=E, padx=80, pady=10)



scale1 = Scale(root, variable = var1, length=320, label='Állítsd be a rajz méretét!', from_=4, to=40, orient=HORIZONTAL)
scale1.grid(row=3, padx=20, pady=10)

scale2 = Scale(root, variable = var_em, length=160, label='Hány szintes legyen a ház?', from_=1, to=6, orient=HORIZONTAL)
scale2.grid(row=4, sticky=W, padx=20, pady=10)

scale3 = Scale(root, variable = var_db, length=320, label='Hány db ablak legyen a házon szintenként?', from_=1, to=12, orient=HORIZONTAL)
scale3.grid(row=5, padx=20, pady=10)

#button = Button(root, text='Get Scale Value', command=sel)
#button.pack(anchor=CENTER)

gomb01 = Button(root, text='INDULJON A HÁZRAJZOLÁS!', command = start_haz)
gomb01.grid(row=6, padx=20, pady=30)

gomb02 = Button(root, text='Csak egy ablakot szeretnék!', command=start_ablak)
gomb02.grid(row=7, padx=20, pady=7)

gomb03 = Button(root, text='Hadd lássam a ión oszlopot!', command=start_oszlop)
gomb03.grid(row=8, padx=20, pady=7)

gomb04 = Button(root, text='Mutass nekem ajtót!', command=start_ajto)
gomb04.grid(row=9, padx=20, pady=7)

gomb05 = Button(root, text='Reset', command=visszaallit)
gomb05.grid(row=10, padx=20, pady=30)

root.mainloop()












#def updateLabel(xx):
#    lab.configure(text='szélesség =' + str(xx))

#szel=xx
#mag=szel*1.5

#GUI = Tk()
#szoveg = Label(GUI, text='RAJZOLJUNK HÁZAT!', fg='red')
#szoveg.pack(side=TOP, padx=30, pady=10) #ablakbeli elrendezésre hat
#szel = Entry(GUI)
#szel.bind("<Return>", szin)
#szel.pack()
#Scale(GUI, length=250, orient=HORIZONTAL, label='Állítsd be a szélességet:', troughcolor ='dark grey', sliderlength=20, showvalue=0, from_=10, to=100, tickinterval=10, command=updateLabel).pack()
#lab = Label(GUI)
#lab.pack


#setheading(0)


#GUI.mainloop() #eseményfogadót elindítja(kattintást figyel)











## szel, mag, db, emelet
## e, values_t, values_a   (ablakok)
## values_d, ajtok (ajtosor)
## cserepsor (teto)
## s, alfa, sinalfa, tanalfa
## t, (t=+-1)
## x, y
## values_j,  (tetoalj)
## f, g (blokkhaz)

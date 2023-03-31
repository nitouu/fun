import turtle


fenetre = turtle.Turtle()

# Theorem of Pythagore - To understand under python language.

#
#[TO REMEMBER] In a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other 2 sides.
#

#Soon:
#-Float and Int
#-Trigonometry's Function (Cos,Tan,Sin) [For the calculations of the Angle's (Euler's Angle, Quaternion ?)]
#...


# [B](Adjacent)' (Cm)
#              ' '
#              '   '
#              '     '
#              '       '
#              '_        '
#              '-|---------'[C](Hypotenuse)(Cm)
#   (Opposite)[A](Cm)


AB=int(input())
AC=int(input())

#AB = Adjacent
#AC = Opposite
#BC = Hypotenuse

#Beta = CAB's angle
#Alpha = BAC's angle

def multiplication(a,b):
    s=0
    if a==0 or b==0:
        return 0
    if a<0:
        return -multiplication(-a,b)
    if b<0:
        return -multiplication(a,-b)
    for i in range(a):
        s = s+b
    return s

def square(n):
    s=1
    s=s*multiplication(n,n)
    return s

def square_root(x):
    x=x**(1/2)
    return x

def Pythagore(AB,AC,CAB,BAC):

    BC=0.0 #Distance AB+AC

    BC = square(AB)+square(AC)+BC

    BC = square_root(BC)

    print("BC : ",BC,"cm.")

    print("Angle(CAB):", CAB,"°", "Angle(BAC):", BAC,"°")

    #Will draw the right triangle.

    #fenetre.forward(AC)

    #fenetre.left(CAB)
    #fenetre.forward(BC)

    #fenetre.left(BAC)
    #fenetre.forward(AB)

    #turtle.done()



print(Pythagore(AB,AC,90,90))

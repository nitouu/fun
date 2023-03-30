import math
import turtle


fenetre = turtle.Turtle()

# Theorem of Pythagore

#
#[TO REMEMBER] In a right triangle, the square of the hypotenuse is equal to the sum of the squares of the other 2 sides.
#



# [B](Adjacent)' (Cm)
#              ' '
#              '   '
#              '     '
#              '       '
#              '_        '
#              '-|---------'[C](Hypotenuse)(Cm)
#   (Opposite)[A](Cm)


AB=float(input())
AC=float(input())

#AB = Adjacent
#AC = Opposite
#BC = Hypotenuse

#Beta = CAB's angle
#Alpha = BAC's angle

def Pythagore(AB,AC,CAB,BAC):

    BC=0 #Distance AB+AC

    BC = AB**2+AC**2+BC
    BC = math.sqrt(BC)

    print("BC : ",BC,"cm.")

    print("Angle(CAB):", CAB, "Angle(BAC):", BAC)

    #Will draw the right triangle.

    fenetre.forward(AC)

    fenetre.left(CAB)
    fenetre.forward(BC)

    fenetre.left(BAC)
    fenetre.forward(AB)

    turtle.done()



print(Pythagore(AB,AC))

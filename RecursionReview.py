# def blast(n):
#     if n == 0:
#         print("Blask Off")
#     else:
#         print(n)
#         blast(n-1)
# # blast(5)

# def sum(L):
#     if len(L) == 0:
#         return 0
#     else:
#         return L[0] + sum(L[1:])

# # print(sum([2,3,4]))

# # LOL
# '''
# def maxSS(L):
#     LOL = [[],[],[],[]]
#     bestpair = max(LOL)
#     return bestpair[1]


# '''

# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*recur_factorial(n-1)
# print(recur_factorial(3))


import time
from turtle import *
from random import *


clr = choice(['darkgreen', 'red', 'blue'])

# def tri(n):
#     """Draws n 100-pixel sides of an equilateral triangle.
#        Note that n doesn't have to be 3 (!)
#     """
#     if n == 0:
#         return      # No sides to draw, so stop drawing
#     else:
#         forward(100)
#         left(120)
#         tri(n-1)    # Recur to draw the rest of the sides!



# def spiral(initialLength, angle, multiplier):
#     """Spiral-drawing function.  Arguments:
#        initialLength = the length of the first leg of the spiral
#        angle = the angle, in degrees, turned after each spiral's leg
#        multiplier = the fraction by which each leg of the spiral changes
#     """
#     if initialLength <= 1:          
#         return      # No more to draw, so stop this call to spiral
#     else:
#         # You will want a call to forward here...
#         # You will want a turn here...
#         # You will want to recur here! That is, make a new call to spiral...
#         forward(initialLength)
#         left(angle)
#         spiral(initialLength*multiplier,angle, multiplier)


def svtree(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        # Draw the original trunk (1 line)
        # Turn a little bit to position the first subtree (1 line)
        # Recur! with both a smaller trunk and fewer levels (1 line)
        # Turn the other way to position the second subtree (1 line)
        # Recur again! (1 line)
        # Turn and go BACKWARDS (2 steps: 2 lines)
        forward(trunklength)
        left(45)
        svtree(trunklength*0.7,levels-1)
        right(90)
        svtree(trunklength*0.7,levels-1)
        left(45)
        backward(trunklength)

def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)


def flakeside(sidelength, levels):
    if levels == 0:
        forward(sidelength)
        return
    else:
        flakeside(sidelength/3,levels-1)
        right(60)
        flakeside(sidelength/3,levels-1)
        left(120)
        flakeside(sidelength/3,levels-1)
        right(60)
        flakeside(sidelength/3,levels-1)






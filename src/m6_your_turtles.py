"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Will Detterman.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

joe = rg.SimpleTurtle('turtle')
joe.pen = rg.Pen('purple', 10)

sal = rg.SimpleTurtle('turtle')
sal.pen = rg.Pen('black', 10)

size = 120
angle = 90

for k in range(10):
    joe.left(angle)
    joe.forward(size)
    joe.right(angle+90)
    joe.forward(size)
    sal.left(45)
    sal.backward(size)
    sal.left(90)
    sal.backward(size)

    size = size-10
    angle = angle-5

window.close_on_mouse_click()
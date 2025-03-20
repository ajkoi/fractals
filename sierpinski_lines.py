from turtle import *
import sys
def mid(pt1, pt2):
    return (pt1[0]+pt2[0])/2, (pt1[1]+pt2[1])/2
def sierpinski(pt1, pt2, pt3, depth ):
    p1 = mid(pt1, pt2)
    p2 = mid(pt1, pt3)
    p3 = mid(pt2, pt3)
    penup()
    goto(p1[0], p1[1])
    pendown()
    goto(p2[0], p2[1])
    goto(p3[0], p3[1])
    goto(p1[0], p1[1])
    if depth <= 0 :
        return
    sierpinski(pt1, p1, p2, depth-1)
    sierpinski(p1, pt2, p3, depth-1)
    sierpinski(p2, p3, pt3, depth-1)
def dessiner_triangle(cote=300, depth=3):
    penup()
    goto(0-cote/2, 0-cote/2)
    pendown()
    goto(cote-cote/2, 0-cote/2)
    goto(cote/2-cote/2, cote-cote/2)
    goto(0-cote/2, 0-cote/2)
    sierpinski([0-cote/2, 0-cote/2], [cote-cote/2, 0-cote/2], [cote/2-cote/2, cote-cote/2], depth=depth)
if __name__=="__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        depth = 3
    else:
        depth = int(sys.argv[1])
    try:
        cote = int(sys.argv[2])
    except:
        cote=300
    print(sys.argv)
    speed(0)
    if type(int(sys.argv[1]))!= int:
        raise TypeError("Use an int pls.")
    dessiner_triangle(cote, depth)
    exitonclick()

# Create a function that takes three points (x,y) lying on a circle in 2 dimensional cartesion plane 
import math
def MP2(x1, y1, x2, y2, x3, y3):
# The coefficients of a,b,c, and d can be solved with the determinant of a circle with three points passing 
    a = (x1*(y2-y3))-(y1*(x2-x3))+((x2*y3-x3*y2))
    b = int((pow(x1,2)+pow(y1,2))*(y3-y2)+(pow(x2,2)+pow(y2,2))*(y1-y3)+(pow(x3,2)+pow(y3,2))*(y2-y1))
    c = int((pow(x1,2)+pow(y1,2))*(x2-x3)+(pow(x2,2)+pow(y2,2))*(x3-x1)+(pow(x3,2)+pow(y3,2))*(x1-x2))
    d = int((pow(x1,2)+pow(y1,2))*(x3*y2-x2*y3)+(pow(x2,2)+pow(y2,2))*(x1*y3-x3*y1)+(pow(x3,2)+pow(y3,2))*(x2*y1-x1*y2))
# The Center can be found with the formula 
    h = int(-b/(2*a))
    k = int(-c/(2*a))
# The Radius of the circle is given as:
    r = int(math.sqrt(((h-x1)**2)+((k-y1)**2)))
# The coefficients of the equation of the circle 
    D = int(b/a)
    E = int(c/a)
    F = int(d/a)
# Store the coefficients "D", "E", and "F" to variable "vector"
    vector = [D,E,F]
# Output the Center, Radius, and Vector[D,E,F]
    print("Center:",(h,k))
    print("Radius:", r)
    print("Vector[D,E,F]:", vector)
   


  

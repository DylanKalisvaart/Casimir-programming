import numpy as np

def circumference_circle(r):
    return 2*np.pi*r

def area_circle(r):
    '''
    area = area_circle(r) computes the area of a circle, given its radius r
    
    Inputs:
       :param float r: radius of circle
       
    Outputs:
       :param float area: area of circle
    '''
    return np.pi*r**2

def area_triangle(base, height): 
    '''
    This function computes the area of a triangle, given its base length and height
    
    Inputs:
       :param float base: base length of the triangle
       :param float height: height of the triangle
       
    Outputs:
       :param float area: area of triangle
    '''
    return 1/2*base*height


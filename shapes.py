import numpy as np
import math
import random


def spiro(a, b, d):
    dt = 0.01
    t = 0
    pts = []
    while t < 2 * math.pi * b/math.gcd(a, b):
        t += dt
        x = (a - b) * math.cos(t) + d * math.cos((a - b)/b * t)
        y = (a - b) * math.sin(t) - d * math.sin((a - b)/b * t)
        pts.append((x, y))
    return pts


def circle(radius, step_size=0.1, x_offset=0, y_offset=0):
    points = []
    position = 0
    #step_size = .1

    while position < 361:        
        x = radius * math.cos(math.radians(position))
        y = radius * math.sin(math.radians(position))
        position += step_size
        points.append((x + x_offset, y + y_offset))

    return points


def square(x_size, y_size, x_offset=0, y_offset=0):
    points = []
    points.append((x_offset + (-x_size/2), y_offset + (-y_size/2)))
    points.append((x_offset + (x_size/2), y_offset + (-y_size/2)))
    points.append((x_offset + (x_size/2), y_offset + (y_size/2)))
    points.append((x_offset + (-x_size/2), y_offset + (y_size/2)))    

    return points


def right_triangle(size, x_offset=0, y_offset=0):
    points = []
    points.append((x_offset, y_offset))
    points.append((size + x_offset, y_offset))
    points.append((x_offset, size + y_offset))
    
    return points


def equilateral_triangle(size, x_offset=0, y_offset=0):
    R = size/math.sqrt(3)
    rads = math.radians(60)
    
    points = []
    points.append((R * math.cos(rads + math.pi*2/3)+x_offset, R * math.sin(rads + math.pi*2/3)+y_offset))
    points.append((R * math.cos(rads)+x_offset, R * math.sin(rads)+y_offset))
    points.append((R * math.cos(rads + math.pi*4/3)+x_offset, R * math.sin(rads + math.pi*4/3)+y_offset))
   
    return points


def vertical_line(length, x_offset=0, y_offset=0):
    points = []
    points.append((x_offset, y_offset))
    points.append((x_offset, y_offset + length))
    
    return points


def arc(radius, x_sign=1, y_sign=1):
    points = []
    position = .0001
    step_size = .1

    while position <= 90:        
        x = radius * math.cos(math.radians(position))
        y = radius * math.sin(math.radians(position))
        position += step_size
        points.append(((x_sign * x), (y_sign * y)))

    return points


def ellipse(a, b, x_offset=0, y_offset=0):
    points = []
    position = 0
    step_size = 1

    while position <= 360:        
        x = a * math.cos(math.radians(position))
        y = b * math.sin(math.radians(position))
        position += step_size
        points.append((x+x_offset, y+y_offset))

    return points


def angle_line(distance_from_zero, x_sign=1, y_sign=1):
    center_point = (distance_from_zero * x_sign, distance_from_zero * y_sign)
    x_int = (2 * distance_from_zero * x_sign, 0)
    y_int = (0, 2 * distance_from_zero * y_sign)

    return (x_int, center_point, y_int)


def parabola(width, x_offset=0, y_offset=0):
    coords = []
    density = 10
    for x in range(-width*density, width*density+1):
        coords.append((x/density, (x/density)**2))
    return coords


def asymp(width, x_offset=0, y_offset=0):
    coords = []
    for i in range(-width, width):
        x = i/100
        if x == 0:
            pass
        else:
            y = 1/x
            coords.append((x, y))
    return coords


def feeder(width, x_offset=0, y_offset=0):
    coords = []
    for x in range(-width, width+1):
        coords.append((x + x_offset, abs(x) + y_offset))
    return coords


def diamond(width, x_offset=0, y_offset=0):
    coords = []
    for x in range(-width, width+1):
        coords.append((x + x_offset, abs(x) + y_offset))
    for x in range(width, - width, -1):
        coords.append((x + x_offset, -abs(x)+width*2  + y_offset))
    return coords


def jesus_fish(radius, x_offset=0, y_offset=0):
    points = []
    position = 0
    step_size = .1

    while position < 360:        
        x = math.cos(radius * math.cos(math.radians(position)))
        y = math.cos(radius * math.sin(math.radians(position)))
        position += step_size
        points.append((x + x_offset, y + y_offset))

    return points


def wide_parabola(radius, x_offset=0, y_offset=0):
    points = []
    position = 0
    step_size = .1

    while position < 360:        
        x = radius * math.cos(math.radians(position))
        y = math.sqrt(abs(radius * math.sin(math.radians(position))))
        position += step_size
        points.append((x + x_offset, y + y_offset))

    return points


def wavy_circle(radius, num_sinusoids, delta, x_offset=0, y_offset=0):
    points = []
    position = 0
    step_size = 1

    while position <= 360:        
        x = (radius + delta * math.sin(num_sinusoids * math.radians(position))) * math.cos(math.radians(position)) + x_offset
        y = (radius + delta * math.sin(num_sinusoids * math.radians(position))) * math.sin(math.radians(position)) + y_offset
        position += step_size
        points.append((x, y))

    return points


def random_line(length, max_height, variability, granularity, y_offset):

    points = []
    for x in range(0, length * granularity):
        y = ((random.uniform(0, 1) * variability) * max_height) + y_offset
        
        points.append((x/granularity, y))
        
    return points  


def fibonacci(n_terms):
    phi = (1 + 5 ** 0.5) / 2
    n1 = 0
    n2 = 1
    count = 0
    points = []
    
    while count < n_terms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        points.append((n1, n1))
        
    return points  


def golden(a, b, density, length):
    # a is arbitrary scaling factor
    # b is growth rate
    theta = 0
    points = []
    
    while theta < length:
        theta += density
        x = a * math.cos(math.radians(theta)) * math.exp(b*theta)
        y = a * math.sin(math.radians(theta)) * math.exp(b*theta)
        points.append((x,y))
    
    return points


def line_h(length, left_crooked_factor=0, right_crooked_factor=0, x_offset=0, y_offset=0):
    points = []
    points.append((x_offset, y_offset + left_crooked_factor))
    points.append((x_offset + length, y_offset + right_crooked_factor))
    
    return points


def sin_h(x_start, x_end, y_scale, x_off=0, y_off=0):
    points = []
    for point in range(x_start*100, x_end*100):
        points.append((point/100, y_off+math.sin(math.radians(point))/y_scale))
        
    return points


def cube(size, x_offset=0, y_offset=0):
    points = []
    #square 1
    points.append((x_offset + (-size/2), y_offset + (-size/2))) #1
    points.append((x_offset + (size/2), y_offset + (-size/2))) #2
    points.append((x_offset + (size/2), y_offset + (size/2))) #3
    points.append((x_offset + (-size/2), y_offset + (size/2)))  #4 

    points.append((x_offset + (-size/2), y_offset + (-size/2))) #back to 1

    # #square 2
    points.append((x_offset + (-size/2) + size/3, y_offset + (-size/2)+ size/3)) #5
    points.append((x_offset + (size/2)+ size/3, y_offset + (-size/2)+ size/3)) #6
    points.append((x_offset + (size/2)+ size/3, y_offset + (size/2)+ size/3)) #7
    points.append((x_offset + (-size/2)+ size/3, y_offset + (size/2)+ size/3)) #8

    points.append((x_offset + (-size/2) + size/3, y_offset + (-size/2)+ size/3)) # back to 5
    points.append((x_offset + (size/2)+ size/3, y_offset + (-size/2)+ size/3)) #6
    points.append((x_offset + (size/2), y_offset + (-size/2))) #2
    points.append((x_offset + (size/2), y_offset + (size/2))) #3
    points.append((x_offset + (size/2)+ size/3, y_offset + (size/2)+ size/3)) #7
    points.append((x_offset + (-size/2)+ size/3, y_offset + (size/2)+ size/3)) #8
    points.append((x_offset + (-size/2), y_offset + (size/2)))  #4 
    
    return points


def heart(width):

    t = np.arange(0,2*np.pi, 0.1)
    x = width*np.sin(t)**3
    y = (15*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))/2
    
    return list(zip(x,y))


def polygon(radius, sides, x_offset=0, y_offset=0):
    points = []
    position = 0
    step_size = 360/sides

    while position < 360:        
        x = radius * math.cos(math.radians(position))
        y = radius * math.sin(math.radians(position))
        position += step_size
        points.append((x + x_offset, y + y_offset))

    return points


def caret(height, width, x_offset=0, y_offset=0):
    points = []

    points.append((-width/2 + x_offset, 0 + y_offset))
    points.append((x_offset, height + y_offset))
    points.append((width/2 + x_offset, 0 + y_offset))

    return points


def wavy_ellipse(a, b, num_sinusoids, delta, x_off=0, y_off=0):
    points = []
    position = 0
    step_size = 1  
    
    while position <= 360:        
        x = a * math.cos(math.radians(position)) + (delta * math.sin(num_sinusoids * math.radians(position))) * math.cos(math.radians(position)) + x_off
        y = b * math.sin(math.radians(position)) + (delta * math.sin(num_sinusoids * math.radians(position))) * math.sin(math.radians(position)) + y_off
        position += step_size
        points.append((x, y))

    return points

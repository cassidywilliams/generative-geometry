import cairo
import math
from shapely.geometry import Point, Polygon


def plot(ctx, coords, line_width=0.05, color=(0,0,0), transparent=1, fill=0, connect_last=False):
    """ This function is used for all basic plotting operations.
    args:
    - ctx: pass in the canvas
    - coords: list of coordinates to plot
    - line width: default is 0.05
    - color: tuple (R, G, B) values between 0-1
    - transparent: between 0 and 1
    - fill: boolean
    - connect_last: if the last point should be connected to the first point, boolean
    """ 
    
    ctx.set_line_width(line_width)
    ctx.set_line_cap(cairo.LINE_CAP_BUTT)
    ctx.set_source_rgba(*color, transparent)

    ctx.move_to(coords[0][0], coords[0][1])
    for x, y in coords[0:]:
        ctx.line_to(x, y)
    if connect_last:
        ctx.line_to(coords[0][0], coords[0][1])
        ctx.line_to(coords[1][0], coords[1][1])
    if fill:    
        ctx.fill() 
    else:
        ctx.stroke() 


def shader(coords, density):
    
    """This function iterates through the polygon and returns a point if it's within the bounds.
    The density can be adjusted as needed to shade more intricately.
    requires two arguments:
    - coords: this is a list of points defining the polygon
    - density: this is how tightly to shade, even numbers only"""
   
    points = []  
    
    x_min = int(min([x[0] for x in coords])-1)*density
    x_max = int(max([x[0] for x in coords])+1)*density
    y_min = int(min([y[1] for y in coords])-1)*density
    y_max = int(max([y[1] for y in coords])+1)*density 
        
    for y in enumerate(range(y_min, y_max)):
        
        if y[0]%2 == 0:
        
            for x in range(x_max, x_min, -1): 
                
                if Point(x/density, y[1]/density).within(Polygon(coords)):
                    points.append((x/density,y[1]/density))
        else:        
            
            for x in range(x_min, x_max):
            
                if Point(x/density, y[1]/density).within(Polygon(coords)):
                    points.append((x/density,y[1]/density))
                
    return points


def linear_interpolate(point1, point2, density=1):
    
    """ This takes in two points and returns equidistant points in between.
    Density can be changed as needed, default is one unit.
    
    """
    points = []
    points.append(point1)
    x_diff = point2[0] - point1[0]
    y_diff = point2[1] - point1[1]
    
    d = math.sqrt((x_diff)**2+ (y_diff)**2)
    
    for n in range(0, math.ceil(d*density)):
        
        xn = point1[0] + (n/density)/d*(x_diff)
        yn = point1[1] + (n/density)/d*(y_diff)
        points.append((xn, yn))
    points.append(point2)
        
    return points


def shape_interpolate(shape, density):

    """This function interpolates between all points in a shape list and returns
    a new list with greater density"""

    points = []

    for index, obj in enumerate(shape):
        if index > 0:
            previous = shape[index - 1]
            points += linear_interpolate(previous, obj, density)
        else:
            points.append(obj)

    points += linear_interpolate(shape[0], shape[len(shape)-1], density)
    
    return points


def tuple_translater(coords, new_origin, y_sign=-1):

    """ This function translates a list of coords at any x,y and centers on 
    the new origin input arg. The y_sign arg should be 1 or -1 in the case
    that you want to flip the shape across the x axis. """
    
    x_min = min(coords, key=lambda t: (t[0], t[1]))[0]
    x_max = max(coords, key=lambda t: (t[0], t[1]))[0]
    y_min = min(coords, key=lambda t: (t[1], t[0]))[1]
    y_max = max(coords, key=lambda t: (t[1], t[0]))[1]
    
    x_off = -(x_max + x_min)/2 + new_origin[0]
    y_off = -(y_max + y_min)/2 + new_origin[1]

    return [(point[0] + x_off, y_sign *(point[1] + y_off)) for point in coords]

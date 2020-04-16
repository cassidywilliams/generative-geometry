import cairo


class Generate:
    
    """ 
    width: width of the surface in pixels
    height: height of the surface in pixels
    scale: multiplier for width and height
    start_x: x coordinate to set to 0,y
    start_y: y coordinate to set to x,0
    transparent: boolean
    background: tuple (R, G, B) values between 0-1
    filename: name to save file as with extension
    """

    def __init__(self, width, height, scale=100, start_x=0, start_y=0, transparent=0, background=(0, 0, 0),
                 filename=None, filetype='svg'):

        self.width = width
        self.height = height
        self.scale = scale
        self.start_x = start_x
        self.start_y = start_y
        self.transparent = transparent
        self.background = background
        self.filename = filename
        self.filetype = filetype

    def setup_canvas(self):
        if self.filetype == 'pdf':
            surface = cairo.PDFSurface(self.filename, self.width, self.height)

        elif self.filetype == 'svg':
            surface = cairo.SVGSurface(self.filename, self.width, self.height)

        elif self.filetype == 'png':
            surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.width * self.scale, self.height * self.scale)

        ctx = cairo.Context(surface)
        ctx.scale(self.scale, self.scale)

        if not self.transparent:
            ctx.set_source_rgb(*self.background)
            ctx.rectangle(0, 0, self.width, self.height)
            ctx.fill()

        ctx.translate(self.start_x, self.start_y)

        return surface, ctx

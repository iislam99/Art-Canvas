import tkinter as tk

# Previous and current positions
prev_x = None
prev_y = None
curr_x = None
curr_y = None

# Default color and line thickness
color = 'black'
width = 1

# Color changing functions
def change2black(event):
    global color
    color = 'black'
    currColor.config(bg = color)

def change2red(event):
    global color
    color = 'red'
    currColor.config(bg = color)

def change2orange(event):
    global color
    color = 'orange'
    currColor.config(bg = color)

def change2yellow(event):
    global color
    color = 'yellow'
    currColor.config(bg = color)

def change2green(event):
    global color
    color = 'green'
    currColor.config(bg = color)

def change2blue(event):
    global color
    color = 'blue'
    currColor.config(bg = color)

def change2purple(event):
    global color
    color = 'purple'
    currColor.config(bg = color)

def change2white(event):
    global color
    color = 'white'
    currColor.config(bg = color)

def change2pink(event):
    global color
    color = 'pink'
    currColor.config(bg = color)

def change2sienna(event):
    global color
    color = 'sienna'
    currColor.config(bg = color)

def change2gold(event):
    global color
    color = 'gold'
    currColor.config(bg = color)

def change2greenyellow(event):
    global color
    color = 'green yellow'
    currColor.config(bg = color)

def change2skyblue(event):
    global color
    color = 'deep sky blue'
    currColor.config(bg = color)

def change2magenta(event):
    global color
    color = 'magenta'
    currColor.config(bg = color)

# Drawing functions
def init(event):
    global curr_x
    global curr_y
    global prev_x
    global prev_y

    curr_x = event.x
    curr_y = event.y
    prev_x = event.x
    prev_y = event.y

def draw(event):
    global curr_x
    global curr_y
    global prev_x
    global prev_y
    global color

    curr_x = event.x
    curr_y = event.y
    w = event.widget
    w.create_line(prev_x, prev_y, curr_x, curr_y, fill = color, width = width)
    prev_x = curr_x
    prev_y = curr_y
    
def increaseSize():
    global width
    if width != 11:
        width += 2

def decreaseSize():
    global width
    if width != 1:
        width -= 2

def clearCanvas():
    cav.delete('all')

win = tk.Tk()
win.title('Art Canvas')

# Frame that holds color palette
colorFrm = tk.Frame(win)
colorFrm.pack(anchor = 'w')

# Color labels
w = 4
h = int(w/2)
brd = 'ridge'

currColor = tk.Label(colorFrm, bg = color, height = w, width = w*2, relief = 'sunken')
currColor.pack(anchor = 'nw', side = tk.LEFT)


###############################################################################
# Top Row Frame
###############################################################################

top = tk.Frame(colorFrm)
top.pack()

black = tk.Label(top, bg = 'black', height = h, width = w, relief = brd)
black.pack(side = tk.LEFT)
black.bind('<Button-1>', change2black)

red = tk.Label(top, bg = 'red', height = h, width = w, relief = brd)
red.pack(side = tk.LEFT)
red.bind('<Button-1>', change2red)

orange = tk.Label(top, bg = 'orange', height = h, width = w, relief = brd)
orange.pack(side = tk.LEFT)
orange.bind('<Button-1>', change2orange)

yellow = tk.Label(top, bg = 'yellow', height = h, width = w, relief = brd)
yellow.pack(side = tk.LEFT)
yellow.bind('<Button-1>', change2yellow)

green = tk.Label(top, bg = 'green', height = h, width = w, relief = brd)
green.pack(side = tk.LEFT)
green.bind('<Button-1>', change2green)

blue = tk.Label(top, bg = 'blue', height = h, width = w, relief = brd)
blue.pack(side = tk.LEFT)
blue.bind('<Button-1>', change2blue)

purple = tk.Label(top, bg = 'purple', height = h, width = w, relief = brd)
purple.pack(side = tk.LEFT)
purple.bind('<Button-1>', change2purple)


###############################################################################
# Bottom Row Frame
###############################################################################

bottom = tk.Frame(colorFrm)
bottom.pack()

white = tk.Label(bottom, bg = 'white', height = h, width = w, relief = brd)
white.pack(side = tk.LEFT)
white.bind('<Button-1>', change2white)

pink = tk.Label(bottom, bg = 'pink', height = h, width = w, relief = brd)
pink.pack(side = tk.LEFT)
pink.bind('<Button-1>', change2pink)

sienna = tk.Label(bottom, bg = 'sienna', height = h, width = w, relief = brd)
sienna.pack(side = tk.LEFT)
sienna.bind('<Button-1>', change2sienna)

gold = tk.Label(bottom, bg = 'gold', height = h, width = w, relief = brd)
gold.pack(side = tk.LEFT)
gold.bind('<Button-1>', change2gold)

greenyellow = tk.Label(bottom, bg = 'green yellow', height = h, width = w, relief = brd)
greenyellow.pack(side = tk.LEFT)
greenyellow.bind('<Button-1>', change2greenyellow)

skyblue = tk.Label(bottom, bg = 'deep sky blue', height = h, width = w, relief = brd)
skyblue.pack(side = tk.LEFT)
skyblue.bind('<Button-1>', change2skyblue)

magenta = tk.Label(bottom, bg = 'magenta', height = h, width = w, relief = brd)
magenta.pack(side = tk.LEFT)
magenta.bind('<Button-1>', change2magenta)


###############################################################################
# Drawing canvas
###############################################################################

cav = tk.Canvas(win, width=500, height=500, bg = 'white')
cav.pack()

cav.bind('<Button-1>', init)
cav.bind('<B1-Motion>', draw)

# Clear button
clearButton = tk.Button(colorFrm, text = 'Clear', command = clearCanvas)
clearButton.pack(side = tk.LEFT)

# Size buttons
increaseButton = tk.Button(top, text = '+', command = increaseSize, width = w)
increaseButton.pack(side = tk.LEFT)
decreaseButton = tk.Button(bottom, text = '-', command = decreaseSize, width = w)
decreaseButton.pack(side = tk.LEFT)

win.mainloop()

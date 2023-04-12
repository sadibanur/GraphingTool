from tkinter import *
""""-------------------------------------------------------------
Author: Sadiba Nusrat Nur
File: graph.txt
Assignment: 3- Graphing Tool
Course: CSC343, Spring 2022
Purpose: The purpose of the program is to create a graphing tool 
         where the user could draw vertices and edges to represent
         a networks pf sensors.
--------------------------------------------------------------"""

# Create a new window with a title
root = Tk()
root.title("Graphing Tool")
# Set the dimension of the window
root.geometry("600x500")
# Create a canvas object
canvas = Canvas(root, height = 500, width = 600)
canvas.pack()
COUNT = 0

# Create an entry field
color_input = Label(root, text="Enter a color:",font = ("Arial", 15, "bold"))
color_input.place(x=10, y=20)
color_entry = StringVar()
color_box = Entry(root,textvariable=color_entry)
color_box.place(x=10,y=40)


def draw_vertex(event):
    """
    The function draw the vertices everytime the user left click
    on the mouse.
    :param event: An event object describing the event
    :return: a list of all vertex object
    """
    v = []
    global COUNT
    x = event.x
    y = event.y
    color = color_box.get()
    vertex=canvas.create_oval(x, y, x+50, y+50, fill = color, width = 2)
    v.append(vertex)
    canvas.create_oval(x+25, y+25, x + 25, y + 25, fill="black",width = 2)
    num = canvas.create_text(x+20, y+20, text = COUNT)
    canvas.itemconfig(num, text = COUNT + 1)
    COUNT += 1
    return v

# Create a left click
canvas.bind("<Button-1>", draw_vertex)


def draw_edge(event):
    """
    The function draws a straigh line(edge) between
    two vertices.
    :param event: An event object describing the event
    :return: a list of all edge object
    """
    global click_number
    global x1, y1
    global COUNT
    e = []
    color = color_box.get()
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        click_number = 1
    else:
        x2 = event.x
        y2 = event.y
        edge = canvas.create_line(x1, y1, x2, y2, fill=color, width = 2)
        e.append(edge)
        click_number = 0
    return e

# Create a right click
canvas.bind("<Button-2>", draw_edge)
click_number = 0

#----------------------------------------------------------------------
# start main event loop
root.mainloop()


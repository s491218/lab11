from Tkinter import *
root = Tk () 
drawpad = Canvas(root, width=800,height=600, background='purple')
drawpad.grid(row=0, column=0)

circle = drawpad.create_oval(20, 20, 100, 100, fill='green')
direction = 1

def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(circle)
    if y2 > drawpad.winfo_height():
        direction = -5
    elif y1 < 0:
        direction = 5
    drawpad.move(circle,0,direction)
    drawpad.after(1, animate)
animate()
root.mainloop()
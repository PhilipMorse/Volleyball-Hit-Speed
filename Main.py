from tkinter import *

root = Tk()
canvas = Canvas(master=root, width=500, height=500)
court1 = PhotoImage(file="Court1.png")
court1 = court1.subsample(2,2)
court2 = PhotoImage(file="Court2.png")
court2 = court2.subsample(2,2)
ball = PhotoImage(file="ball.png")
ball = ball.subsample(3,3)
canvas.create_image(0, 0, image=court1, anchor=NW)
canvas.create_image(250, 250, image=ball, tags=['ball'])
canvas.create_text(250,475,text="Please select contact point",tags=['info'])
canvas.lift(ball)

contact = [0,0,2.45]
hit = [0,0,0]

click_loc_label = Label(root, text="(0,0)")


def contact_event(event):
    click_loc_label.config(text="(" + str((event.x-50) / 50) + "," + str((event.y-450) / 50) + ")")
    canvas.coords('ball',event.x,event.y)
    contact[0] = (event.x-50)/50
    contact[1] = (event.y-450)/50


def hit_event(event):
    click_loc_label.config(text="(" + str((event.x-50) / 50) + "," + str((event.y-50) / 50) + ")")
    canvas.coords('ball',event.x,event.y)
    hit[0] = (event.x-50)/50
    hit[1] = (event.y-50)/50


def confirm_hit():
    confirm_button.destroy()
    canvas.unbind("<Button 1>")
    canvas.delete('all')
    distance = ((hit[0]-contact[0])**2+(hit[1]-contact[1])**2+(hit[2]-contact[2])**2)**0.5
    click_loc_label.config(text="The distance is " + "{:.2f}".format(distance) + " m")



def confirm_contact():
    confirm_button.config(command=confirm_hit)
    canvas.delete("all")
    canvas.create_image(0, 0, image=court2, anchor=NW)
    canvas.create_image(250, 250, image=ball, tags=['ball'])
    canvas.create_text(250,25,text="Please select spike landing location",tags=['info'])
    canvas.bind("<Button 1>", hit_event)



speed = Entry(root)
canvas.bind("<Button 1>", contact_event)
confirm_button = Button(root, text="Confirm Selection", command=confirm_contact)
click_loc_label.pack()
confirm_button.pack()
canvas.pack()

root.mainloop()

import random
import tkinter

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White', 'Pink', 'Brown']
points = 0 # points gained
time = 30  # time left to complete

def start(e): # start game method
    
    if time == 30:
        timer()
    
    nextColor()

def nextColor(): # array traverse to find next color

    global time
    global points

    if time > 0: # game is going on

        e.focus_set()

        if e.get().lower() == colors[1].lower():

            points += 1

        e.delete(0, tkinter.END)

        random.shuffle(colors)

        label.config(fg = str(colors[1]), text = str(colors[0]))
        Ptlabel.config(text= 'POINTS : ' + str(points))

def timer():
    global time

    if time  > 0:

        time -= 1

        tlabel.config(text = 'Time Left : '+ str(time))

        tlabel.after(1000,timer)#run after 1 second


root = tkinter.Tk()

root.title('Color it')

root.geometry('360x240')

instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word text!",font = ('Helvetica', 12)) 

instructions.pack() 

Ptlabel = tkinter.Label(root, text = "Press enter to start",
									font = ('Helvetica', 12))
Ptlabel.pack()

# add a time left label
tlabel = tkinter.Label(root, text = "Time left: " +
			str(time), font = ('Helvetica', 12))

tlabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', start)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()

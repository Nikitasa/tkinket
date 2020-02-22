import tkinter 
import random

colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 30
def startGame(event):
  if timeleft == 30: 
    countdown()
  nextColour() 
def nextColour():
  global score 
  global timeleft
  if timeleft > 0:
    e.focus_set() 
    if e.get().lower() == colours[1].lower():
      score += 1
    e.delete(0, tkinter.END) 
          
    random.shuffle(colours)
    label.config(fg = str(colours[1]), text = str(colours[0])) 
    scoreLabel.config(text = "Score: " + str(score))
def countdown():
  global timeleft 
  if timeleft > 0: 
    timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
  timeLabel.after(1000, countdown)
root = tkinter.Tk() 
  
# set the title 
root.title("COLORGAME") 
  
# set the size 
root.geometry("375x200") 
  
# add an instructions label 
instructions = tkinter.Label(root, text = "Type in the colour"
                        "of the words, and not the word text!", 
                                      font = ('Helvetica', 12)) 
instructions.pack()  
  
# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                      font = ('Helvetica', 12)) 
scoreLabel.pack() 
  
# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12)) 
                
timeLabel.pack() 
  
# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Helvetica', 60)) 
label.pack() 
  
# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root) 
  
# run the 'startGame' function  
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 
  
# set focus on the entry box 
e.focus_set() 
  
# start the GUI 
root.mainloop()
#Rohan Sonakya Last edit: 1/14/2022

#Import libraries
from tkinter import *
from tkinter.ttk import Combobox
import moving_functions as mf

#Hard values from gearing and stepper motor
STEP_PER_DEGREE = (512*225)/360

#GUI
class MyWindow:
  def __init__(self, win):
    self.lbl=Label(window, text="Pitch", fg='red', font=("Helvetica", 16))
    self.lbl.place(x=15, y=10)
    self.lbl=Label(window, text="Yaw", fg='red', font=("Helvetica", 16))
    self.lbl.place(x=270, y=10)
    
    self.var = StringVar()
    self.var.set("one")
    self.data=("Right", "Left")
    self.cb=Combobox(window, values=self.data)
    self.cb.place(x=270, y=50)
    
    self.txtfld1=Entry(window, text="Dgrees?", bd=5)
    self.txtfld1.place(x=270, y=80)
    
    self.var2 = StringVar()
    self.var2.set("one")
    self.data2=("Up", "Down")
    self.cb2=Combobox(window, values=self.data2)
    self.cb2.place(x=15, y=50)

    self.txtfld2=Entry(window, text="Dees?", bd=4)
    self.txtfld2.place(x=15, y=80)

    self.btn=Button(window, text="Run", fg='blue')
    self.btn=Button(win, text='Add', command=self.add)
    self.btn.place(x=200, y=125)

    self.txtfld3=Entry(window, text="Degrees?", bd=8)
    self.txtfld3.place(x=155, y=150)

  #Backend
  def add(self):
        #Pull values
        pitch_direction = self.cb2.get()
        yaw_direction = self.cb.get()
        pitch_degrees = self.txtfld2.get()
        yaw_degrees = self.txtfld1.get()

        #Print val moves in GUI
        self.txtfld3.insert(END, str(str(pitch_direction) +str(pitch_degrees + str(yaw_direction) )+ str(yaw_degrees)))

        #Vals for motor to move
        pitch_degree_to_step = float(pitch_degrees) * STEP_PER_DEGREE
        yaw_degree_to_step = float(yaw_degrees) * STEP_PER_DEGREE


        #Move up
        if pitch_direction == "Up":
          control_pins = [7,11,13,15]
          mf.move_up_or_left(control_pins,pitch_degree_to_step)
          print (str(pitch_degree_to_step) + "up")
        #Move down
        else:
          control_pins = [7,11,13,15]
          mf.move_down_or_right(control_pins,pitch_degree_to_step)
          print (str(pitch_degree_to_step) + "down")
        #Move left
        if yaw_direction == "Left":
          control_pins = [31,33,35,37]
          mf.move_up_or_left(control_pins,pitch_degree_to_step)
          print (str(yaw_degree_to_step) + "Left")
        #Move right
        else:
          control_pins = [31,33,35,37]
          mf.move_down_or_right(control_pins,pitch_degree_to_step)
          print (str(yaw_degree_to_step) + "Right")
                


  
  
#Display GUI
window = Tk()
mywin=MyWindow(window)
window.title('Star Locator Program')
window.geometry("450x200+10+20")
window.mainloop()

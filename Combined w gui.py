from tkinter import *
from tkinter.ttk import Combobox


STEP_PER_DEGREE = (512*225)/360


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

  def add(self):
        pitch_direction = self.cb2.get()
        yaw_direction = self.cb.get()
        pitch_degrees = self.txtfld2.get()
        yaw_degrees = self.txtfld1.get()
        self.txtfld3.insert(END, str(str(pitch_direction) +str(pitch_degrees + str(yaw_direction) )+ str(yaw_degrees)))
        pitch_degree_to_step = float(pitch_degrees) * STEP_PER_DEGREE
        if pitch_direction == "Up":
          GPIO.setmode(GPIO.BOARD)
          control_pins = [7,11,13,15]
          for pin in control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0) 
          halfstep_seq = [
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1]
          ]
          for i in range(int(pitch_degree_to_step)):
            for halfstep in range(8):
              for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
              time.sleep(0.0015)
          GPIO.cleanup()
          print (str(pitch_degree_to_step) + "up")
        else:
          GPIO.setmode(GPIO.BOARD)
          control_pins = [7,11,13,15]
          for pin in control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0) 
          halfstep_seq = [
          [1,0,0,1],
          [0,0,0,1],
          [0,0,1,1],
          [0,0,1,0],
          [0,1,1,0],
          [0,1,0,0],
          [1,1,0,0],
          [1,0,0,0]
          ]
          for i in range(int(pitch_degree_to_step)):
            for halfstep in range(8):
              for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
              time.sleep(0.0015)
          GPIO.cleanup()
          print (str(pitch_degree_to_step) + "down")

        yaw_degree_to_step = float(yaw_degrees) * STEP_PER_DEGREE
        if yaw_direction == "Left":
          GPIO.setmode(GPIO.BOARD)
          control_pins = [31,33,35,37]
          for pin in control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0) 
          halfstep_seq = [
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1]
          ]
          for i in range(int(yaw_degree_to_step)):
            for halfstep in range(8):
              for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
              time.sleep(0.0015)
          GPIO.cleanup()
          print (str(yaw_degree_to_step) + "Left")
        else:
          GPIO.setmode(GPIO.BOARD)
          control_pins = [31,33,35,37]
          for pin in control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0) 
          halfstep_seq = [
          [1,0,0,1],
          [0,0,0,1],
          [0,0,1,1],
          [0,0,1,0],
          [0,1,1,0],
          [0,1,0,0],
          [1,1,0,0],
          [1,0,0,0]
          ]
          for i in range(int(yaw_degree_to_step)):
            for halfstep in range(8):
              for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
              time.sleep(0.0015)
          GPIO.cleanup()
        print (str(yaw_degree_to_step) + "Right")
                


  
  

window = Tk()
mywin=MyWindow(window)
window.title('Star Locator Program')
window.geometry("450x200+10+20")
window.mainloop()
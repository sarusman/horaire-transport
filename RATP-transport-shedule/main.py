import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import os, datetime
from api import api


window=tk.Tk()
window.title('TIME REAL')
window.geometry('1350x1000')



class f:
	def __init__(self):
		self.Label_middle = tk.Label(window, text ="")
		self.h = tk.Label(window, text ="HEURE : "+datetime.datetime.now().strftime('%H : %M'))

	def texte_Render(self,text):
		self.Label_middle = tk.Label(window, text =text)
		self.Label_middle.config(font=("Courier", 28))
		self.Label_middle.place(relx = 0.5, rely = 0.5,anchor = 'center')

		self.h = tk.Label(window, text ="HEURE : "+datetime.datetime.now().strftime('%H : %M'))
		self.h.config(font=("Courier", 50))
		self.h.place(relx = 0.29, rely = 0.7)
		
	def kill(self):
		self.Label_middle.destroy()
		self.h.destroy()



gtr=f()

def ligne_235():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("bus", "235", "Solferino"))


def ligne_366():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("bus", "366", "Solferino"))

def ligne_140():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("bus", "140", "Solferino"))




def ligne_13():
	gtr.kill()
	gtr.texte_Render(api.get_horaire("metro", "13", "asnieres+gennevilliers+les+courtilles"))




ligne_235_logo = PhotoImage(file = os.getcwd()+"/images/lignes/235.png")
ligne_140_logo = PhotoImage(file = os.getcwd()+"/images/lignes/140.png")
ligne_13_logo = PhotoImage(file = os.getcwd()+"/images/lignes/13.png")
ligne_366_logo = PhotoImage(file = os.getcwd()+"/images/lignes/366.png")

Button(window, image = ligne_235_logo, command=ligne_235).place(x=170, y=100)
Button(window, image = ligne_140_logo, command=ligne_140).place(x=420, y=100)
Button(window, image = ligne_13_logo, command=ligne_13).place(x=670, y=100)
Button(window, image = ligne_366_logo, command=ligne_366).place(x=820, y=100)




window.mainloop()

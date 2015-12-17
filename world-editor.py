#!/usr/bin/env python

try:
	from tkinter import *
except:
	from Tkinter import *

import pickle

toplevel=Tk()

outerPane=Frame(toplevel)

buttonPane=Frame(outerPane)

addStateButton=Button(buttonPane, text="Add state")
stateNameEntry=Entry(buttonPane, text="Name of new state")
addStateButton.pack(side="left")
stateNameEntry.pack(side="left")
buttonPane.pack(side="top")

bottomPane=Frame(outerPane, width=800, height=600)
stateListPane=Frame(bottomPane, width=300, height=600)
stateList=Listbox(stateListPane)
stateList.pack(fill="both", expand="y")
stateInfo=Frame(bottomPane, width=500, height=600)
stateListPane.pack(side="left", fill="y")
stateInfo.pack(side="right")
bottomPane.pack(side="bottom")

outerPane.pack()

world={}

def handleCreateState(*args):
	global world
	stateName=stateNameEntry.get()
	if (not (stateName in world.keys())):
		world[stateName]={}
		refreshStateList()
	else:
		selectState(stateName)

addStateButton.configure(command=handleCreateState)


toplevel.mainloop()


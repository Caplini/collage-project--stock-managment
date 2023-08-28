from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter

from waste import WasteMenuFunc
from Findstock import FindStockMenuFunc
from AddNewStock import AddNewItemMenuFunc
from EditCheckStock import EditItemFunc
from Settings import SettingsMenuFunc

f = open("wasted.txt")

# main menu


root = customtkinter.CTk() # Stock managment system main menu
root.title("Stock Managment system")
root.configure(fg_color='#2b2b2b')

font = customtkinter.CTkFont(family="Helvetica")



# frame so setting button can fit in same area
MainMenuLabelFrame = customtkinter.CTkFrame(master=root)
MainMenuLabelFrame.grid(column=0, row=0)

# main menu label
MainMenuLabel = customtkinter.CTkLabel(master=MainMenuLabelFrame, 
                                       text="Stock Managment System",
                                       font=customtkinter.CTkFont(family="Helvetica", size=30),
                                       corner_radius=20,
                                       anchor="center"
                                       )

MainMenuLabel.grid(column=1,
                   row=0,
                   pady=4,
                   padx=4,
                   )

# locate settings icon image and resieze 
SettingsIcon = PhotoImage(file=r"setting.png")
SettingsIcon = SettingsIcon.subsample(20,20)

# settings button
SettingsButton = customtkinter.CTkButton(master=MainMenuLabelFrame,
                                      text="",
                                      image=SettingsIcon,
                                      font=font,
                                      width=10,
                                      height=10,
                                      corner_radius=20,
                                      fg_color="transparent",
                                      hover_color="#3d3d3d",
                                      command=SettingsMenuFunc
                                      )

SettingsButton.grid(column=2,
                  row=0,
                  pady=1,
                  padx=4,
                  sticky="e"
                  )

# Frame so buttons can be fit in along side main menu
MainButtonsFrame = customtkinter.CTkFrame(master=root)
MainButtonsFrame.grid(column=0, row=1)

# button to open waste menu
WasteButton = customtkinter.CTkButton(master=MainButtonsFrame,
                                      text="Waste",
                                      font=font,
                                      width=140,
                                      height=200,
                                      corner_radius=20,
                                      fg_color="#828282",
                                      hover_color="#3d3d3d",
                                      command=WasteMenuFunc
                                      )

WasteButton.grid(column=0,
                  row=1,
                  pady=40,
                  padx=25
                  )

# button to open find stock menu
FindStockButton = customtkinter.CTkButton(master=MainButtonsFrame,
                                      text="Find Stock",
                                      font=font,
                                      width=140,
                                      height=200,
                                      corner_radius=20,
                                      fg_color="#828282",
                                      hover_color="#3d3d3d",
                                      command=FindStockMenuFunc)
FindStockButton.grid(column=1,
                 row=1,
                 pady=40,
                 padx=25,
                 )

# button to open add stock menu
AddStockButton = customtkinter.CTkButton(master=MainButtonsFrame,
                                      text="Add New Stock",
                                      font=font,
                                      width=140,
                                      height=200,
                                      corner_radius=20,
                                      fg_color="#828282",
                                      hover_color="#3d3d3d",
                                      command=AddNewItemMenuFunc)
AddStockButton.grid(column=2,
                 row=1,
                 pady=40,
                 padx=25,
                 )

# button to open edit stock menu
EditCheckButton = customtkinter.CTkButton(master=MainButtonsFrame,
                                      text="Edit/Check Stock",
                                      font=font,
                                      width=140,
                                      height=200,
                                      corner_radius=20,
                                      fg_color="#828282",
                                      hover_color="#3d3d3d",
                                      command=EditItemFunc)
EditCheckButton.grid(column=3,
                 row=1,
                 pady=40,
                 padx=25,
                 )

root.mainloop()

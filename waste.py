from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter

# Menus

# waste menu

def WasteMenuFunc():
    WasteMenu = customtkinter.CTkToplevel() # window for waste menu
    WasteMenu.configure(height=800,
                   width=600,
                   fg_color='#2b2b2b')
    WasteMenu.title("Stock Managment system - Waste")



    # label waste menu at the top
    WastMenuLabel = customtkinter.CTkLabel(master=WasteMenu, 
                                       text="Waste Menu",
                                       font=customtkinter.CTkFont(family="Helvetica", size=30),
                                       corner_radius=20,
                                       anchor="center")
    
    WastMenuLabel.grid(column=0,
                       row=0)
    
    
    # filler gray line for formatting
    Filler = customtkinter.CTkFrame(master=WasteMenu,
                                    fg_color="#828282",
                                    height=15,
                                    width=600,
                                    corner_radius=0)
    Filler.grid(column=0,
                row=1)


    # frame to fit item tags and add item button
    WasteFunctionsFrame = customtkinter.CTkFrame(master=WasteMenu)
    WasteFunctionsFrame.grid(column=0, row=2, sticky="w")


    # Item label
    ItemLabel = customtkinter.CTkLabel(master=WasteFunctionsFrame, 
                                       text="Item:                ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")
    
    ItemLabel.grid(column=0,
                   row=0,
                   sticky="w")
    

    # tags label
    TagsLabel = customtkinter.CTkLabel(master=WasteFunctionsFrame, 
                                       text="Tags:                                        ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")
    
    TagsLabel.grid(column=1,
                   row=0
                   )
    
    # Button to add item

    AddItemButton = customtkinter.CTkButton(master=WasteFunctionsFrame,
                                        text="Add Item",
                                        font=customtkinter.CTkFont(family="Helvetica", size=20),
                                        width=100,
                                        height=30,
                                        corner_radius=6,
                                        fg_color="#828282",
                                        hover_color="#3d3d3d")
    
    AddItemButton.grid(column=2,
                         row=0,
                         pady=3,
                         padx=0,
                         sticky="e"
                         )
    

    # filler gray line for formatting
    Filler = customtkinter.CTkFrame(master=WasteMenu,
                                    fg_color="#828282",
                                    height=3,
                                    width=600,
                                    corner_radius=0)
    
    Filler.grid(column=0,
                row=3)
from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter

def EditCheckItemsMenuFunc():
    EditCheckItemsMenu = customtkinter.CTkToplevel() # Edit/check stock window
    EditCheckItemsMenu.configure(height=800,
                   width=600,
                   fg_color='#2b2b2b')
    
    EditCheckItemsMenu.title("Stock Managment system - Edit/Check Stock")

     # label waste menu at the top
    EditCheckItemsLabel = customtkinter.CTkLabel(master=EditCheckItemsMenu, 
                                       text="Edit/Check Stock",
                                       font=customtkinter.CTkFont(family="Helvetica", size=30),
                                       corner_radius=20,
                                       anchor="center")
    
    EditCheckItemsLabel.grid(column=0,
                       row=0)
    
    
    # filler gray line for formatting
    Filler = customtkinter.CTkFrame(master=EditCheckItemsMenu,
                                    fg_color="#828282",
                                    height=15,
                                    width=600,
                                    corner_radius=0)
    Filler.grid(column=0,
                row=1,
                pady=20,
                padx=0)
    
    # Name label
    EditCheckItemsLabel = customtkinter.CTkLabel(master=EditCheckItemsMenu, 
                                       text="Name: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    EditCheckItemsLabel.grid(column=0,
                                  row=2,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Name label entry field 
    EditCheckItemsNameEnt = customtkinter.CTkEntry(master=EditCheckItemsMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    EditCheckItemsNameEnt.grid(column=0,
                                row=2,
                                pady=8,
                                padx=4
                                )
                                


    # Code label
    EditCheckItemsCodeLabel = customtkinter.CTkLabel(master=EditCheckItemsMenu, 
                                       text="Code: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    EditCheckItemsCodeLabel.grid(column=0,
                                  row=3,
                                  pady=8,
                                  padx=4,
                                  sticky="w"
                                  )


    # Code label entry field 
    EditCheckItemsCodeEnt = customtkinter.CTkEntry(master=EditCheckItemsMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    EditCheckItemsCodeEnt.grid(column=0,
                                  row=3,
                                  pady=8,
                                  padx=4
                                  )
    

    # Class label
    EditCheckItemsClassLabel = customtkinter.CTkLabel(master=EditCheckItemsMenu, 
                                       text="Class: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    EditCheckItemsClassLabel.grid(column=0,
                                  row=4,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Class label entry field 
    EditCheckItemsClassEnt = customtkinter.CTkEntry(master=EditCheckItemsMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    EditCheckItemsClassEnt.grid(column=0,
                                  row=4,
                                  pady=8,
                                  padx=4
                                  )

    # Type label
    EditCheckItemsTypeLabel = customtkinter.CTkLabel(master=EditCheckItemsMenu, 
                                       text="Type: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")
    
    EditCheckItemsTypeLabel.grid(column=0,
                                  row=5,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Class label entry field 
    EditCheckItemsTypeEnt = customtkinter.CTkEntry(master=EditCheckItemsMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    EditCheckItemsTypeEnt.grid(column=0,
                                  row=5,
                                  pady=8,
                                  padx=4
                                  )
                                  
    
    # Amount label
    EditCheckItemsAmountLabel = customtkinter.CTkLabel(master=EditCheckItemsMenu, 
                                       text="Amount: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    EditCheckItemsAmountLabel.grid(column=0,
                                  row=6,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Class label entry field 
    EditCheckItemsAmountEnt = customtkinter.CTkEntry(master=EditCheckItemsMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    EditCheckItemsAmountEnt.grid(column=0,
                                  row=6,
                                  pady=8,
                                  padx=4
                                  )
    
    
    # Add item button
    EditCheckItemsButton = customtkinter.CTkButton(master=EditCheckItemsMenu,
                                        text="Change",
                                        font=customtkinter.CTkFont(family="Helvetica", size=30),
                                        width=300,
                                        height=60,
                                        corner_radius=6,
                                        fg_color="#828282",
                                        hover_color="#3d3d3d")
    
    EditCheckItemsButton.grid(column=0,
                         row=7,
                         pady=20,
                         padx=25,
                         sticky="NS"
                         )
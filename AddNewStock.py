from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter
import ctypes

import sqlite3

 # Add item to the database
def AddItemToDataBase():
    
    conn = sqlite3.connect("Stock.db") # call which data base we are working with 
    
    cur = conn.cursor() # add cursor 
    
    
    # get each entry and give it a variable 
    ItemCode = AddNewItemMenuCodeEnt.get()
    ItemName = AddNewItemMenuNameEnt.get()
    Count = AddNewItemMenuAmountEnt.get()
    ClassID = AddNewItemMenuClassEnt.get()
    TypeID = AddNewItemMenuTypeEnt.get()
    
    def AddItem():
        # command to add each entry to data base on button click 
        cur.execute("INSERT INTO Item (ItemName, ItemCode, Count, ClassID, TypeID) VALUES (?,?,?,?,?)", (ItemName, ItemCode, Count, ClassID, TypeID))     
    
    def ResetBoxesError():
        print(f"Make sure all box's are present and the code is not already in the database")
        
        ctypes.windll.user32.MessageBoxW(0, f"Error, Make sure all box's are present, all data is the correct type and the code is not already in the database", "Error", 1) # show error messge if item code is already present
        
        # reset boxes
        AddNewItemMenuCodeEnt.delete(0, END)
        AddNewItemMenuCodeEnt.insert(0, "")

        AddNewItemMenuNameEnt.delete(0, END)
        AddNewItemMenuNameEnt.insert(0, "")

        AddNewItemMenuAmountEnt.delete(0, END)
        AddNewItemMenuAmountEnt.insert(0, "")

        AddNewItemMenuClassEnt.delete(0, END)
        AddNewItemMenuClassEnt.insert(0, "")

        AddNewItemMenuTypeEnt.delete(0, END)
        AddNewItemMenuTypeEnt.insert(0, " ")

    
    # get code list into list
    cur.execute("SELECT ItemCode FROM Item") # select teh column 
    rows = cur.fetchall() # get all in list
    
    ColumnList = [row[0] for row in rows] # put all from column into list

            
    if any(x== ""  for x in (ItemName, ItemCode, ClassID, TypeID, Count)) or Count.isnumeric() == False or ItemCode in ColumnList:
        ResetBoxesError()
        
    else:
        AddItem()
            
    
    
    
        conn.commit() # update data base with changes
        conn.close() # close data base

 # function for window 
def AddNewItemMenuFunc():
    
    
    # define entrys as global variables
    global AddItemToDataBase
    global AddNewItemMenuNameEnt
    global AddNewItemMenuCodeEnt
    global AddNewItemMenuClassEnt 
    global AddNewItemMenuTypeEnt
    global AddNewItemMenuAmountEnt
    
    AddNewItemMenu = customtkinter.CTkToplevel() # window for waste menu
    AddNewItemMenu.configure(height=800,
                   width=600,
                   fg_color='#2b2b2b')
    AddNewItemMenu.title("Stock Managment system - Add New Item")

     # label waste menu at the top
    AddNewItemMenuLabel = customtkinter.CTkLabel(master=AddNewItemMenu, 
                                       text="Add New Item",
                                       font=customtkinter.CTkFont(family="Helvetica", size=30),
                                       corner_radius=20,
                                       anchor="center")
    
    AddNewItemMenuLabel.grid(column=0,
                       row=0)
    
    
    # filler gray line for formatting
    Filler = customtkinter.CTkFrame(master=AddNewItemMenu,
                                    fg_color="#828282",
                                    height=15,
                                    width=600,
                                    corner_radius=0)
    Filler.grid(column=0,
                row=1,
                pady=20,
                padx=0)
    
    # Name label
    AddNewItemMenuNameLabel = customtkinter.CTkLabel(master=AddNewItemMenu, 
                                       text="Name: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    AddNewItemMenuNameLabel.grid(column=0,
                                  row=2,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Name label entry field 
    AddNewItemMenuNameEnt = customtkinter.CTkEntry(master=AddNewItemMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    AddNewItemMenuNameEnt.grid(column=0,
                                row=2,
                                pady=8,
                                padx=4
                                )
                                


    # Code label
    AddNewItemMenuCodeLabel = customtkinter.CTkLabel(master=AddNewItemMenu, 
                                       text="Code: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    AddNewItemMenuCodeLabel.grid(column=0,
                                  row=3,
                                  pady=8,
                                  padx=4,
                                  sticky="w"
                                  )


    # Code label entry field 
    AddNewItemMenuCodeEnt = customtkinter.CTkEntry(master=AddNewItemMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    AddNewItemMenuCodeEnt.grid(column=0,
                                  row=3,
                                  pady=8,
                                  padx=4
                                  )
    

    # Class label
    AddNewItemMenuClassLabel = customtkinter.CTkLabel(master=AddNewItemMenu, 
                                       text="Class: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    AddNewItemMenuClassLabel.grid(column=0,
                                  row=4,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Class label entry field 
    AddNewItemMenuClassEnt = customtkinter.CTkEntry(master=AddNewItemMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    AddNewItemMenuClassEnt.grid(column=0,
                                  row=4,
                                  pady=8,
                                  padx=4
                                  )

    # Type label
    AddNewItemMenuTypeLabel = customtkinter.CTkLabel(master=AddNewItemMenu, 
                                       text="Type: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")
    
    AddNewItemMenuTypeLabel.grid(column=0,
                                  row=5,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Class label entry field 
    AddNewItemMenuTypeEnt = customtkinter.CTkEntry(master=AddNewItemMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    AddNewItemMenuTypeEnt.grid(column=0,
                                  row=5,
                                  pady=8,
                                  padx=4
                                  )
                                  
    
    # Amount label
    AddNewItemMenuAmountLabel = customtkinter.CTkLabel(master=AddNewItemMenu, 
                                       text="Amount: ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")

    AddNewItemMenuAmountLabel.grid(column=0,
                                  row=6,
                                  pady=8,
                                  padx=4,
                                  sticky="w")
    

    # Class label entry field 
    AddNewItemMenuAmountEnt = customtkinter.CTkEntry(master=AddNewItemMenu,
                                          width=350,
                                          height=20,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=20),
                                          corner_radius=4
                                          )

    AddNewItemMenuAmountEnt.grid(column=0,
                                  row=6,
                                  pady=8,
                                  padx=4
                                  )
    
    
    # Add item button
    AddNewItemMenuButton = customtkinter.CTkButton(master=AddNewItemMenu,
                                        text="Add Item",
                                        font=customtkinter.CTkFont(family="Helvetica", size=30),
                                        width=300,
                                        height=60,
                                        corner_radius=6,
                                        fg_color="#828282",
                                        hover_color="#3d3d3d",
                                        command=AddItemToDataBase)
    
    AddNewItemMenuButton.grid(column=0,
                         row=7,
                         pady=20,
                         padx=25,
                         sticky="NS"
                         )
    
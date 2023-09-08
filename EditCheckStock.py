from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter
import sqlite3
import ctypes

# Update Button
def update_item():
     # grab the values that will be updated
    new_values = (
        EditCheckItemsCodeEnt.get(),
        EditCheckItemsNameEnt.get(),
        EditCheckItemsAmountEnt.get(),
        EditCheckItemsClassEnt.get(),
        EditCheckItemsTypeEnt.get()
    )
    
    cur.execute("UPDATE Item SET ItemCode = ?, ItemName = ?, Count = ?, ClassID = ?, TypeID = ? WHERE ItemCode = ?", (*new_values, item_code)) # send changes to database
    conn.commit() # save database
    conn.close() # close data base
    ctypes.windll.user32.MessageBoxW(0, f"{new_values[1]} updated successfully", "Item Updated!", 1) # show user that the changes went through
    EditCheckItemsMenu.destroy()  # Close the Tkinter window to reduce errors 


def EditCheckItemsMenuFunc():
    global EditCheckItemsNameEnt
    global EditCheckItemsCodeEnt
    global EditCheckItemsClassEnt
    global EditCheckItemsTypeEnt
    global EditCheckItemsAmountEnt
    global EditCheckItemsMenu
    global item_code
    global cur
    global conn


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
    
        # submit Edit
    EditCheckItemsButton = customtkinter.CTkButton(master=EditCheckItemsMenu,
                                        text="Change",
                                        font=customtkinter.CTkFont(family="Helvetica", size=30),
                                        width=300,
                                        height=60,
                                        corner_radius=6,
                                        fg_color="#828282",
                                        hover_color="#3d3d3d",
                                        command=update_item)
    
    EditCheckItemsButton.grid(column=0,
                         row=7,
                         pady=20,
                         padx=25,
                         sticky="NS"
                         )
    
    item_code = FindStockEnt.get()

    # Database stuff
    conn = sqlite3.connect("Stock.db")
    cur = conn.cursor()

    # Fetch data based on item_code
    cur.execute("SELECT * FROM Item WHERE ItemCode = ?", (item_code,))
    item = cur.fetchone()




    # If item exists, populate the fields
    if item:
        EditCheckItemsNameEnt.insert(0, item[2])  # Name from DB
        EditCheckItemsCodeEnt.insert(0, item[1])  # Code from DB
        EditCheckItemsClassEnt.insert(0, item[4])  # Class from DB
        EditCheckItemsTypeEnt.insert(0, item[5])  # Type from DB
        EditCheckItemsAmountEnt.insert(0, item[3])  # Count from DB
    else:
        ctypes.windll.user32.MessageBoxW(0, f"No item found with code {item_code}", "Error", 1)
        return


def EditItemFunc():
    global FindStockEnt
    
    EditItem = customtkinter.CTkToplevel() # window for waste menu
    EditItem.configure(height=150,
                   width=300,
                   fg_color='#2b2b2b')
    EditItem.title("Stock Managment system - Edit Item")

    # find stock entry field 
    FindStockEnt = customtkinter.CTkEntry(master=EditItem,
                                          width=200,
                                          height=35,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=14),
                                          corner_radius=4,
                                          placeholder_text="Item Code"
                                          )

    FindStockEnt.grid(column=0,
                      row=0,
                      pady=10,
                      padx=25,
                      sticky="NS")
    

    # Button Edit
    FindStockSubmitButton = customtkinter.CTkButton(master=EditItem,
                                        text="Edit",
                                        font=customtkinter.CTkFont(family="Helvetica", size=20),
                                        width=100,
                                        height=30,
                                        corner_radius=6,
                                        fg_color="#828282",
                                        hover_color="#3d3d3d",
                                        command=EditCheckItemsMenuFunc)
    
    FindStockSubmitButton.grid(column=0,
                         row=1,
                         pady=10,
                         padx=25,
                         sticky="NS"
                         )
    
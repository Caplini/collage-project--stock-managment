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

# Menus

WastedItemsFile = open("wasted.txt", "r+")

# take count off amount in database
def WasteItemFinal():
    
    # get each entry and give it a variable 
    ItemCodeToWaste = ItemCode.get() # Get the value from the ItemCode Entry field
    CountToWaste = int(ItemCount.get()) # Get the value from the ItemCount Entry field

    conn = sqlite3.connect("Stock.db") # call which database we are working with 
    cur = conn.cursor() # add cursor 
    
    # Prepare SQL query to get 'Count' field of ItemCode
    count_field_query = 'SELECT Count FROM Item WHERE ItemCode = ?'
    cur.execute(count_field_query, (ItemCodeToWaste,)) # Execute the query with ItemCodeToWaste as parameter
    count_field = cur.fetchone() # Fetch the result of the query

    if count_field is None: # If the ItemCode was not found
        print("ItemCode not found in the database")
        ctypes.windll.user32.MessageBoxW(0, f"Error, Make sure the Item code is correct", "Error", 1) # show error messge
    else:
        # Subtract CountToWaste from the current count
        current_count = int(count_field[0])
        new_count = current_count - CountToWaste

        # Update the 'Count' in the database with the new count
        update_query = 'UPDATE Item SET Count = ? WHERE ItemCode = ?'
        cur.execute(update_query, (new_count, ItemCodeToWaste))

        conn.commit()  # commit changes to the database

        # Fetch and print the updated count to verify
        cur.execute(count_field_query, (ItemCodeToWaste,))
        updated_count = cur.fetchone()
        if updated_count is not None:
            print("Updated Count for ItemCode", ItemCodeToWaste, "is", updated_count[0])

    conn.close() # close database

    WastedItems.configure(state="normal")
    WastedItems.insert(END, f"{ItemCodeToWaste.ljust(50)}{updated_count[0]} \n", tags=None)
    WastedItems.configure(state="disabled")
    WastedItemsFile.write(f"{ItemCodeToWaste.ljust(50)}{updated_count[0]}\n")


# add waste button

def Addwaste():
     # global so can be grabbed in other function
    global ItemCount
    global ItemCode


    WasteAdd = customtkinter.CTkToplevel() # window for waste menu
    WasteAdd.configure(height=150,
                   width=300,
                   fg_color='#2b2b2b')
    WasteAdd.title("Waste Item Info")


    # fram for formatting
    WasteInfo = customtkinter.CTkFrame(master=WasteAdd,
                                    fg_color="#2b2b2b",
                                    corner_radius=0)

    WasteInfo.grid(
        column=0,
        row=0)


    # item code ent fielf
    ItemCode = customtkinter.CTkEntry(master=WasteInfo,
                                          width=200,
                                          height=35,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=14),
                                          corner_radius=4,
                                          placeholder_text="Enter Code"
                                          )

    ItemCode.grid(column=0,
                      row=0,
                      pady=10,
                      padx=15,
                      sticky="NS")

    ItemCount = customtkinter.CTkEntry(master=WasteInfo,
                                          width=100,
                                          height=35,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=14),
                                          corner_radius=4,
                                          placeholder_text="Amount"
                                          )

    # item count to waste off
    ItemCount.grid(column=1,
                      row=0,
                      pady=10,
                      padx=15,
                      sticky="NS")


    # Button Submit waste
    WasteItem = customtkinter.CTkButton(master=WasteAdd,
                                        text="Submit",
                                        font=customtkinter.CTkFont(family="Helvetica", size=20),
                                        width=100,
                                        height=30,
                                        corner_radius=6,
                                        fg_color="#828282",
                                        hover_color="#3d3d3d",
                                        command=WasteItemFinal)

    WasteItem.grid(column=0,
                         row=1,
                         pady=10,
                         padx=25,
                         sticky="NS"
                         )

# waste menu
def WasteMenuFunc():
    global WastedItems

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
                                       text="Item:            ",
                                       font=customtkinter.CTkFont(family="Helvetica", size=20),
                                       corner_radius=20,
                                       anchor="center")
    
    ItemLabel.grid(column=0,
                   row=0,
                   sticky="w")
    

    # tags label
    TagsLabel = customtkinter.CTkLabel(master=WasteFunctionsFrame, 
                                       text="Item Count:                                        ",
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
                                        hover_color="#3d3d3d",
                                        command=Addwaste)
    
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
    
    WastedItems = customtkinter.CTkTextbox(master=WasteMenu,
                                           width=600
                                           )

    WastedItems.grid(column=0,
                row=4)
    
    
    WastedItems.insert(END, WastedItemsFile.read())
    WastedItems.configure(state="disabled")

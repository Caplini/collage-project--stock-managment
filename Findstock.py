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

 # function that finds the item postion from the code entered
def LocateAndShowPostion():
    
    # get each entry and give it a variable 
    ItemNameToFind = FindStockEnt.get() # Get the value from the ItemCode Entry field

    conn = sqlite3.connect("Stock.db") # call which database 
    cur = conn.cursor() # add cursor

    ItemCode_query = 'SELECT ItemCode FROM Item WHERE ItemName = ?'
    cur.execute(ItemCode_query, (ItemNameToFind,)) # Execute the query with ItemNameToFind as parameter 

    ItemCode = cur.fetchone()[0]

    if ItemCode_query is None: # If the ItemCode was not found
        print("ItemName not found in the database")
        ctypes.windll.user32.MessageBoxW(0, f"Error, Make sure the item name is correct", "Error", 1) # show error messge
    else:
        ctypes.windll.user32.MessageBoxW(0, f"Item located at isle {ItemCode[0:2]}, position {ItemCode[3::]}", "Item Found!", 1)
        print(cur.fetchone()[0])

 # Find Stock menu 
def FindStockMenuFunc():
    global FindStockEnt
    
    FindStockMenu = customtkinter.CTkToplevel() # window for waste menu
    FindStockMenu.configure(height=150,
                   width=300,
                   fg_color='#2b2b2b')
    FindStockMenu.title("Stock Managment system - Find Stock")

    # find stock entry field 
    FindStockEnt = customtkinter.CTkEntry(master=FindStockMenu,
                                          width=200,
                                          height=35,
                                          fg_color="#828282",
                                          font=customtkinter.CTkFont(family="Helvetica", size=14),
                                          corner_radius=4,
                                          placeholder_text="Item Name"
                                          )

    FindStockEnt.grid(column=0,
                      row=0,
                      pady=10,
                      padx=25,
                      sticky="NS")
    

    # Button Submit search
    FindStockSubmitButton = customtkinter.CTkButton(master=FindStockMenu,
                                        text="Submit",
                                        font=customtkinter.CTkFont(family="Helvetica", size=20),
                                        width=100,
                                        height=30,
                                        corner_radius=6,
                                        fg_color="#828282",
                                        hover_color="#3d3d3d",
                                        command=LocateAndShowPostion)
    
    FindStockSubmitButton.grid(column=0,
                         row=1,
                         pady=10,
                         padx=25,
                         sticky="NS"
                         )
from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter

 # Find Stock menu 
def FindStockMenuFunc():
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
                                          corner_radius=4
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
                                        hover_color="#3d3d3d")
    
    FindStockSubmitButton.grid(column=0,
                         row=1,
                         pady=10,
                         padx=25,
                         sticky="NS"
                         )
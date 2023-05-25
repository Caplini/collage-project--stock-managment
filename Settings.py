from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter


def SettingsMenuFunc():
    SettingsMenu = customtkinter.CTkToplevel() # Edit/check stock window
    SettingsMenu.configure(height=800,
                   width=600,
                   fg_color='#2b2b2b')
    
    SettingsMenu.title("Stock Managment system - Settings")
    
    SettingsMenuLabel = customtkinter.CTkLabel(master=SettingsMenu, 
                                       text="Settings",
                                       font=customtkinter.CTkFont(family="Helvetica", size=30),
                                       corner_radius=20,
                                       anchor="center")
    
    SettingsMenuLabel.grid(column=0,
                           row=0)

    # filler for formatting 
    Filler = customtkinter.CTkFrame(master=SettingsMenu,
                                    fg_color="#828282",
                                    height=7,
                                    width=600,
                                    corner_radius=0)
    Filler.grid(column=0,
                row=1,
                pady=20,
                padx=0)
    

    # frame to allow the formatting
    SettingsMenuFrame = customtkinter.CTkFrame(master=SettingsMenu,
                                    fg_color="#2b2b2b",
                                    corner_radius=0)
    
    SettingsMenuFrame.grid(column=0,
                       row=3,
                       sticky="NESW")
    
    # settings menu theme label 
    SettingsMenuThemeLabel = customtkinter.CTkLabel(master=SettingsMenuFrame,
                                                    text="Theme: ",
                                                    fg_color="#2b2b2b",
                                                    bg_color="#FFFFFF",
                                                    font=customtkinter.CTkFont(family="Helvetica", size=30)
                                                    )
    
    SettingsMenuThemeLabel.grid(column=0,
                                row=0,
                                sticky="W")

    # ligth theme check box to select check light theme
    SettingsMenuLightThemechkbx = customtkinter.CTkCheckBox(master=SettingsMenuFrame,
                                                       text="",
                                                       width=80,
                                                       height=30,
                                                       checkbox_width=50,
                                                       checkbox_height=30,
                                                       corner_radius=20,
                                                       hover_color="#3d3d3d",
                                                       fg_color="#828282")
    
    SettingsMenuLightThemechkbx.grid(column=1,
                                row=0,
                                pady=0,
                                padx=10,
                                sticky="W")
    
    # dark theme check box to select check dark theme
    SettingsMenuDarkThemechkbx = customtkinter.CTkCheckBox(master=SettingsMenuFrame,
                                                       text="",
                                                       width=80,
                                                       height=30,
                                                       checkbox_width=50,
                                                       checkbox_height=30,
                                                       corner_radius=20,
                                                       hover_color="#3d3d3d",
                                                       fg_color="#828282")
    
    SettingsMenuDarkThemechkbx.grid(column=2,
                                row=0,
                                pady=0,
                                padx=0,
                                sticky="W")
    
    # second filler line for formatting 
    Filler2 = customtkinter.CTkFrame(master=SettingsMenu,
                                    fg_color="#828282",
                                    height=7,
                                    width=600,
                                    corner_radius=0)
    Filler2.grid(column=0,
                row=4,
                pady=20,
                padx=0)
    
    # Slect wether you want a custom theme or not

    # custom theme frame for formatting
    CustomThemeFrame = customtkinter.CTkFrame(master=SettingsMenu,
                                    fg_color="#2b2b2b",
                                    corner_radius=0)
    
    CustomThemeFrame.grid(column=0,
                       row=5,
                       sticky="NESW")
    
    # label for custom theme
    CustomThemeLabel = customtkinter.CTkLabel(master=CustomThemeFrame,
                                              text="Custom Theme: ",
                                              fg_color="#2b2b2b",
                                              bg_color="#FFFFFF",
                                              font=customtkinter.CTkFont(family="Helvetica", size=30))
    
    CustomThemeLabel.grid(column=0,
                          row=0,
                          pady=5,
                          padx=5,
                          sticky="NSEW")
    
    # Check box to slect wether you want a custom theme or not
    SettingsMenuCustomThemechkbx = customtkinter.CTkCheckBox(master=CustomThemeFrame,
                                                       text="",
                                                       width=80,
                                                       height=30,
                                                       checkbox_width=30,
                                                       checkbox_height=30,
                                                       corner_radius=10,
                                                       hover_color="#3d3d3d",
                                                       fg_color="#828282")
    
    SettingsMenuCustomThemechkbx.grid(column=1,
                                      row=0,
                                      pady=5,
                                      padx=5,
                                      sticky="NSEW")

    # primary colour frame for formatting
    PrimaryThemeFrame = customtkinter.CTkFrame(master=SettingsMenu,
                                    fg_color="#2b2b2b",
                                    corner_radius=0)
    
    PrimaryThemeFrame.grid(column=0,
                       row=6,
                       sticky="NESW")
    
    # Primary colour label
    PrimaryColourThemeLabel = customtkinter.CTkLabel(master=PrimaryThemeFrame,
                                              text="Primary Colour: ",
                                              fg_color="#2b2b2b",
                                              bg_color="#FFFFFF",
                                              font=customtkinter.CTkFont(family="Helvetica", size=30))
    
    PrimaryColourThemeLabel.grid(column=0,
                          row=0,
                          pady=5,
                          padx=5,
                          sticky="NSEW")
    
    # button to select the primary colour
    PrimaryColourSelectButton = customtkinter.CTkButton(master=PrimaryThemeFrame,
                                                       text="",
                                                       font=customtkinter.CTkFont(family="Helvetica", size=0),
                                                       width=100,
                                                       height=30,
                                                       corner_radius=8,
                                                       fg_color="#828282",
                                                       hover_color="#3d3d3d")

    PrimaryColourSelectButton.grid(column=1,
                                   row=0,
                                   pady=5,
                                   padx=5
                                   )
    
    # Secondary colour frame for formatting
    SecondaryThemeFrame = customtkinter.CTkFrame(master=SettingsMenu,
                                    fg_color="#2b2b2b",
                                    corner_radius=0)
    
    SecondaryThemeFrame.grid(column=0,
                       row=7,
                       sticky="NESW")
    
    # Primary colour label
    SecondaryColourThemeLabel = customtkinter.CTkLabel(master=SecondaryThemeFrame,
                                              text="Secondary Colour: ",
                                              fg_color="#2b2b2b",
                                              bg_color="#FFFFFF",
                                              font=customtkinter.CTkFont(family="Helvetica", size=30))
    
    SecondaryColourThemeLabel.grid(column=0,
                          row=0,
                          pady=5,
                          padx=5,
                          sticky="NSEW")
    
    # button to select the primary colour
    SecondaryColourSelectButton = customtkinter.CTkButton(master=SecondaryThemeFrame,
                                                       text="",
                                                       font=customtkinter.CTkFont(family="Helvetica", size=0),
                                                       width=100,
                                                       height=30,
                                                       corner_radius=8,
                                                       fg_color="#828282",
                                                       hover_color="#3d3d3d")

    SecondaryColourSelectButton.grid(column=1,
                                   row=0,
                                   pady=5,
                                   padx=5
                                   )
    
    
        # Secondary colour frame for formatting
    FontThemeFrame = customtkinter.CTkFrame(master=SettingsMenu,
                                    fg_color="#2b2b2b",
                                    corner_radius=0)
    
    FontThemeFrame.grid(column=0,
                       row=8,
                       sticky="NESW")
    
    # Primary colour label
    FontColourThemeLabel = customtkinter.CTkLabel(master=FontThemeFrame,
                                              text="Font Colour: ",
                                              fg_color="#2b2b2b",
                                              bg_color="#FFFFFF",
                                              font=customtkinter.CTkFont(family="Helvetica", size=30))
    
    FontColourThemeLabel.grid(column=0,
                          row=0,
                          pady=5,
                          padx=5,
                          sticky="NSEW")
    
    # button to select the primary colour
    FontColourSelectButton = customtkinter.CTkButton(master=FontThemeFrame,
                                                       text="",
                                                       font=customtkinter.CTkFont(family="Helvetica", size=0),
                                                       width=100,
                                                       height=30,
                                                       corner_radius=8,
                                                       fg_color="#828282",
                                                       hover_color="#3d3d3d")

    FontColourSelectButton.grid(column=1,
                                   row=0,
                                   pady=5,
                                   padx=5
                                   )
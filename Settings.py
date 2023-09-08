from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter

def set_theme(theme):
    global SettingsMenuLightThemechkbx, SettingsMenuDarkThemechkbx, SettingsMenuCustomThemechkbx
    if theme == 'light':
        SettingsMenuLightThemechkbx.select()
        SettingsMenuDarkThemechkbx.deselect()
        SettingsMenuCustomThemechkbx.deselect()
    elif theme == 'dark':
        SettingsMenuLightThemechkbx.deselect()
        SettingsMenuDarkThemechkbx.select()
        SettingsMenuCustomThemechkbx.deselect()
    elif theme == 'custom':
        SettingsMenuLightThemechkbx.deselect()
        SettingsMenuDarkThemechkbx.deselect()
        SettingsMenuCustomThemechkbx.select()
    save_settings(triggered_by="theme")

def save_settings(triggered_by=""):
    try:
        with open("settings.txt", "r") as f:
            lines = f.readlines()

        if triggered_by == "primary" and PrimaryColourENT is not None:
            lines[3] = f"{PrimaryColourENT.get()}\n"
        elif triggered_by == "secondary" and SecondaryColourENT is not None:
            lines[4] = f"{SecondaryColourENT.get()}\n"
        elif triggered_by == "font" and FontColourENT is not None:
            lines[5] = f"{FontColourENT.get()}\n"
        else:
            # Update everything else or handle an unknown trigger
            pass

        with open("settings.txt", "w") as f:
            f.writelines(lines)
    except Exception as e:
        print(f"An error occurred: {e}")

    if triggered_by == "theme":
        with open("settings.txt", "r") as f:
            lines = f.readlines()
        lines[0] = f"{SettingsMenuLightThemechkbx.get()}\n"
        lines[1] = f"{SettingsMenuDarkThemechkbx.get()}\n"
        lines[2] = f"{SettingsMenuCustomThemechkbx.get()}\n"
        with open("settings.txt", "w") as f:
            f.writelines(lines)
        
def primary_color_select_func():
    global PrimaryColourENT
    
    # create window
    PrimarySelect = customtkinter.CTkToplevel()
    PrimarySelect.configure(height=150, width=300, fg_color='#2b2b2b')
    PrimarySelect.title("Select Primary Color")
    
    # place in entry for primary colour
    PrimaryColourENT = customtkinter.CTkEntry(master=PrimarySelect,  
                                              width=200,
                                              height=35,
                                              fg_color="#828282",
                                              font=customtkinter.CTkFont(family="Helvetica", size=14),
                                              corner_radius=4,
                                              placeholder_text="Enter Primary Color")
    
    PrimaryColourENT.grid(column=0, row=0, pady=10, padx=25, sticky="NS")

    PrimaryColourENT.insert(0, primary_colour) # grab current value and show

    PrimaryColourSubmitButton = customtkinter.CTkButton(master=PrimarySelect,
                                                         text="Submit",
                                                         font=customtkinter.CTkFont(family="Helvetica", size=20),
                                                         width=100,
                                                         height=30,
                                                         corner_radius=6,
                                                         fg_color="#828282",
                                                         hover_color="#3d3d3d",
                                                         command=lambda: save_settings(triggered_by="primary"))
    
    PrimaryColourSubmitButton.grid(column=0, row=1, pady=10, padx=25, sticky="NS")

    

def secondary_color_select_func():
    global SecondaryColourENT
    
    # create window
    SecondarySelect = customtkinter.CTkToplevel()
    SecondarySelect.configure(height=150, width=300, fg_color='#2b2b2b')
    SecondarySelect.title("Select secondary Color")
    
    # place in entry for primary colour
    SecondaryColourENT = customtkinter.CTkEntry(master=SecondarySelect,  
                                              width=200,
                                              height=35,
                                              fg_color="#828282",
                                              font=customtkinter.CTkFont(family="Helvetica", size=14),
                                              corner_radius=4,
                                              placeholder_text="Enter secondary Color")
    
    SecondaryColourENT.grid(column=0, row=0, pady=10, padx=25, sticky="NS")

    SecondaryColourENT.insert(0, secondary_colour) # grab current value and show

    SecondaryColourSubmitButton = customtkinter.CTkButton(master=SecondarySelect,
                                                         text="Submit",
                                                         font=customtkinter.CTkFont(family="Helvetica", size=20),
                                                         width=100,
                                                         height=30,
                                                         corner_radius=6,
                                                         fg_color="#828282",
                                                         hover_color="#3d3d3d",
                                                         command=lambda: save_settings(triggered_by="secondary"))
    
    SecondaryColourSubmitButton.grid(column=0, row=1, pady=10, padx=25, sticky="NS")

def font_color_select_func():
    global FontColourENT

    # create window
    FontSelect = customtkinter.CTkToplevel()
    FontSelect.configure(height=150, width=300, fg_color='#2b2b2b')
    FontSelect.title("Select Font Color")

    FontColourENT = customtkinter.CTkEntry(master=FontSelect,  
                                           width=200,
                                           height=35,
                                           fg_color="#828282",
                                           font=customtkinter.CTkFont(family="Helvetica", size=14),
                                           corner_radius=4,
                                           placeholder_text="Enter Font Color")
    
    FontColourENT.grid(column=0, row=0, pady=10, padx=25, sticky="NS")
    FontColourENT.insert(0, font_colour)

    FontColourSubmitButton = customtkinter.CTkButton(master=FontSelect,
                                                     text="Submit",
                                                     font=customtkinter.CTkFont(family="Helvetica", size=20),
                                                     width=100,
                                                     height=30,
                                                     corner_radius=6,
                                                     fg_color="#828282",
                                                     hover_color="#3d3d3d",
                                                     command=lambda: save_settings(triggered_by="font"))
    
    FontColourSubmitButton.grid(column=0, row=1, pady=10, padx=25, sticky="NS")

def create_default_settings_file():
    with open("settings.txt", "w") as f:
        f.write("0\n")  # light_theme
        f.write("1\n")  # dark_theme
        f.write("0\n")  # custom_theme
        f.write("0\n")  # primary_colour
        f.write("0\n")  # secondary_colour
        f.write("0\n")  # font_colour

def SettingsMenuFunc():
    global SettingsMenuLightThemechkbx
    global SettingsMenuDarkThemechkbx
    global SettingsMenuCustomThemechkbx
    global PrimaryColourSelectButton
    global SecondaryColourSelectButton
    global FontColourSelectButton
    global settings
    global light_theme
    global dark_theme
    global custom_theme
    global primary_colour
    global secondary_colour
    global font_colour

    try:
        with open("settings.txt", "r") as f:
            settings = f.read().splitlines()
            if len(settings) < 6:  # Check if settings has enough lines
                raise IndexError("Settings file is incomplete.")

            light_theme = settings[0]
            dark_theme = settings[1]
            custom_theme = settings[2]
            primary_colour = settings[3]
            secondary_colour = settings[4]
            font_colour = settings[5]


    except (FileNotFoundError, IndexError):  # Handle both exceptions
        create_default_settings_file()  # Create and populate the settings file
        light_theme = "0"
        dark_theme = "1"
        custom_theme = "0"
        primary_colour = "0"
        secondary_colour = "0"
        font_colour = "0"

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
                                                       hover_color="#FFFFFF",
                                                       fg_color="#FFFFFF",
                                                       command=lambda: set_theme('light'))
    
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
                                                       fg_color="#828282",
                                                       command=lambda: set_theme('light'))
    
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
                                                       fg_color="#828282",
                                                       command=lambda: set_theme('light'))
    
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
                                                       hover_color="#3d3d3d",
                                                       command=primary_color_select_func)

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
                                                       hover_color="#3d3d3d",
                                                       command=secondary_color_select_func)

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
                                                       hover_color="#3d3d3d",
                                                       command=font_color_select_func)

    FontColourSelectButton.grid(column=1,
                                   row=0,
                                   pady=5,
                                   padx=5
                                   )
    
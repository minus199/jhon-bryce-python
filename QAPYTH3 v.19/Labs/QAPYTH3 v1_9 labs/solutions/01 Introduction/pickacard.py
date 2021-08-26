#!/usr/local/bin/python

import Showcard

number = input("Pick a card (1-52):")

filename = "BMP"+number+".GIF"
Showcard.display_file(filename)

    

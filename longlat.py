import geocoder
import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv

Point = complex
City  = Point

def X(point): 
    "The x coordinate of a point."
    return point.real

def Y(point): 
    "The y coordinate of a point."
    return point.imag

def distance(A, B): 
    "The distance between two points."
    return abs(A - B)

def plot_lines(points, style='bo-'):
    "Plot lines to connect a series of points."
    plt.plot(map(X, points), map(Y, points), style)
    plt.axis('scaled'); plt.axis('off')

vancity=['33 Acres Brewing Co. , Vancouver, British Columbia   ', 'Big Rock Brewing , Vancouver, British Columbia    ', 'Black Kettle Brewing Co. , North Vancouver, British Columbia  ', 'Bomber Brewing , East Vancouver, British Columbia    ', 'Brassneck Brewery , Vancouver, British Columbia  ', 'Bridge Brewing Co. , North Vancouver BC    ', 'Callister Brewing Company , Vancouver, British Columbia  ', 'Coal Harbour Brewing Company , Vancouver, British Columbia    ', 'Deep Cove Brewers and Distillers , North Vancouver, British Columbia    ', 'Dogwood Brewing , Vancouver, British Columbia  ', 'Dockside Brewing Co. , Vancouver, British Columbia    ', 'Granville Island Brewing , Vancouver, British Columbia    ', 'Green Leaf Brewing , North Vancouver, British Columbia  ', 'Hearthstone Brewing , North Vancouver, British Columbia    ', 'Main Street Brewing Co. , Vancouver, British Columbia    ', 'Off The Rail Brewing Co. , Vancouver, British Columbia    ', 'Powell Street Brewery , East Vancouver, British Columbia    ', 'Parallel 49 Brewing Co. , East Vancouver, British Columbia    ', 'Postmark Brewing Co. , Vancouver, British Columbia    ', 'R&B Brewing Co. , Vancouver, British Columbia  ', 'Red Truck Beer Company , North Vancouver, British Columbia    ', "Sailor Hagar's , North Vancouver, British Columbia", 'Steamworks Brewing Co. , Vancouver, British Columbia    ', 'Storm Brewing Co. , Vancouver, British Columbia    ', 'Strange Fellows Brewing Co. , Vancouver, British Columbia    ', 'Yaletown Brewing Company , Vancouver, British Columbia ']

longlat=[]
for  x in vancity:
	#searches with google
	r = geocoder.osm(x).json  
	if r['ok'] == True:
	#grabs the long/lat from the json as a list
		coord = r['bbox']['northeast']
		longlat.append(coord) 
		print(coord,x)




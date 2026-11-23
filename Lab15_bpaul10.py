"""
Program name: Lab15- Plotting numbers
Author: Bernard Paul
Purpose: make 2 plots showing the cubes of the first 5 numbers and the first 5000 numbers
Starter Code: no starter code
Date: 11/22/26

"""

import matplotlib.pyplot as plt

#creating the list that has the first 5 numbers
input_values = [1, 2, 3, 4, 5]

#making a list where each number is muiltiplied to the power of 3
cubes = [x**3 for x in input_values]

#geeks for geeks matplotlib tutorial was used to help with the plotting of the graphs

#this will make a new figure for where the graph will be drawn
plt.figure()

#will have the plot where x axis is the imput values and y is the cubes of it
plt.plot(input_values, cubes)

#creating title for the graph
plt.title("First 5 cubes")

#creating the lable for the x acis
plt.xlabel("Input Values")

#making lable for the y axis
plt.ylabel("Cubes of Input Values")

#will save the graph bas  a png 
plt.savefig("cubes_5.png")

#will show the graph on teh screen
plt.show()

#going to create a range from 1-5000 for the input values
input_values = list(range(1, 5001))

#gets the cube of the numbers of inputs
cubes = [x**3 for x in input_values]

#creating new figure for the second graph
plt.figure()

# will plot the first 5000 numbers and their cubes to the plot
plt.plot(input_values, cubes)

#giving the graph a title
plt.title("First 5000 cubes")

#putting x axis label
plt.xlabel("Input Values")

#putting y axis label
plt.ylabel("Cubes of Input Values")

#saving graph as png
plt.savefig("cubes_5000.png")

#shows the second graph on screen
plt.show()
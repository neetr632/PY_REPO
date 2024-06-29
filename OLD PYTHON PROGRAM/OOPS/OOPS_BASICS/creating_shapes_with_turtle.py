from turtle import *  # Import all functions and classes from the turtle module

# Function to draw a star shape
def star(t, size, width, color , edges):
    t.color(color)  # Set the color of the turtle's pen
    t.width(width)  # Set the width of the turtle's pen
    t.begin_fill()  # Start recording vertices for a shape to be filled
    for i in range(edges):  # Loop 5 times to draw a 5-pointed star
        t.forward(size)  # Move the turtle forward by the specified size
        t.left(144)  # Turn the turtle left by 144 degrees (exterior angle of a regular pentagon)
    t.end_fill()  # Fill the shape with the current fill color

# Function to draw a circle
def circle(t, radius, color):
    t.color(color)  # Set the color of the turtle's pen
    t.begin_fill()  # Start recording vertices for a shape to be filled
    t.circle(radius)  # Draw a circle with the specified radius
    t.end_fill()  # Fill the shape with the current fill color

t = Turtle()  # Create a new Turtle object
ask = input("Enter the name of the shape you want to create: ")  # Ask the user for the shape

# Loop until the user enters "done"
while ask != "done":
    if ask == 'star':  # If the user entered "star"
        width = int(input("Enter the required width: "))  # Ask for the pen width
        col = input("Enter the desired color: ")  # Ask for the color
        size = int(input("Enter a length: "))  # Ask for the length of the star's sides
        edges = int(input("how many edges do u want:"))
        star(t, size, width, col, edges)  # Call the star function with the user's inputs
    elif ask == 'circle':  # If the user entered "circle"
        radius = int(input("Enter the radius: "))  # Ask for the radius
        col = input("Enter the color: ")  # Ask for the color
        circle(t, radius, col)  # Call the circle function with the user's inputs
    else:
        print('Invalid shape')  # If the user entered something other than "star" or "circle"
    ask = input("Enter shape: ")  # Ask the user for the next shape

# No need to call done() here, as the turtle window will remain open until closed manually
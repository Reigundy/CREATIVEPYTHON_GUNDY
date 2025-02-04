# NOTES
here are my notes for this class, tune in or tune out. 
## Class 1
Homework being, to finish up the github repository. I am a little tired today to say the least.

Using [Jupyter Notebook](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb), to save make sure to click save and export the python file.

Resources. 
[Python Basics](https://automatetheboringstuff.com/2e/chapter1/)

inequalities = means either it matches or it doesn't. If it matches then it returns true, if it doesnt match then it will return a false.
basically numbers here can ilicit a do or dont do function within the code. for instance I want my site to show different content via a different number user provided. I would say blah blah if UI <= 32 then if they input something less than 32 they would be showed one thing (if this specific function is receiving false) versus the other (if this function receives true.)

You can create variables within variables within varibales with pyton. keep this and the numbers based functionalty. 

to create a variable 
"voldemort" = he who should not be named 

type{name of variable} it tells you the type of data the variable is represented by.

python can check if a word starts with something 

"helloworld".startswith("hel")
will return 
True

helloworld.endswith("hel")
will return 
False

List + Array, act to store information, in the code. 

[1,10,15,50]
Creates an array (list) with 5 items, you can also create an empty array (list) with [] 

To create a named list (array) my_number(dont use spaces use_s) = 1,10,15,50 

To access something specific from an Array [my_number][3] should equal 15

you can stack functions on top of functionality for instance, type(my_number[2]), 
TYPE function telling the type of data My number[2] choosing specific answer 

len in python (checks how many items available in a certain list)

3 in MY_Number
gets False, no number 

1 in My_Number

True

My_numbers[1:4]
will go into the list (array titled 'my numbers' and get the entries 1-4 and display them.)

## Class 2

Blah- yes okay code sketches art and ideation are based on a grid system. (you place things on the grid, lines dots etc).

Setup() vs draw ()
Set up, I want these things to just exist... 
Draw, I want this fuction to draw repeatdly  and always draw when your mouth moves.

can add background colors to set up with 
background(hex code)

using
for column in range(6):
 for row in range(6):
 circle(column*80, row * 80, 50)

 This is how you get a grid.... ^^

 In python the name of a "key" in a dictionary needs to be wrapped in double quotes
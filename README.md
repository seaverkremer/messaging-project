# messaging-project


# Introduction to Customer Connector

Customer Connector allows the user to quickly send template messages to their recipient of choice. When the template is selected by the user, the template message will automatically be populated with the correct information, which can then be sent to the recipient. 

Customer Connector's versatile template creator allows the user to easily create their own templates for more detailed messages and further ease of access.

In cases where creating a new template may not be desired, they can also type out a bespoke message to the recipient.


# Requirements

The only module Customer Connector requires outside of the Python Standard Library is **pytz**.

To install **pytz**, enter "pip3 install pytz" into your command line.


# Instructions

Once you have downloaded the necessary module, navigate to the directory Customer Connector's files are located in and run **app.py**.

To run **app.py**, enter "python3 app.py" into your command line.

Once the app is running, it will give you prompts:
You will be prompted to specify your employer’s name, and then will be greeted and taken to the home state. Entering ‘list’ will show you the employers available.

From the home state you can use an existing message template or create your own.  Entering ‘message’ will prompt you for a guest, then to which template to use. Alternatively you may enter a bespoke message instead of using a template. 

If you chose to select a template, you will be asked to enter the name of the template you would like to use. Entering ‘list’ or ‘ls’ will provide a list of substitution variables available.

To create a template, enter ‘template’ when on the home page. Entering ‘list’ or ‘ls’ will show you the supported substitution variables. Type your desired message in plain text using the ‘~’ character before any desired substitution locations.  For example, ‘Hello, ~first_name in Room ~room_number.’ would yield: ‘Hello, Morgan in Room 385.’  Error checking is performed on your template, and if OK, you will be asked to name your template to save for later use.


The main commands are summarized here:
	        ‘q’ or ‘quit’ or ‘exit’	    Terminate the program
            ‘h’ or ‘help’                Shows this message
            ‘b’ or ‘back’                 Return to previous prompt
            ‘home’       		           Return to root prompt
On some pages, you can use:
	‘list’ or ‘ls’			Shows available options		


# Design Process

The first step in Customer Connector's design process was to decide which language to use. I chose Python because of the following:

    -Python is a great enabler for OOP
    -The input() function in Python is intuitive and is useful for the amount of user input required for this project
    -Python lends itself to modular design, which greatly helps the potential for future expansion of the project

The next step was to decide the interface type the program would have. I decided that a command line-based program would suit the basic functionalities of the project well.

Given the language and interface type of the project, I then tested some basic functionality using python's json module. I created classes for Company and Guest, both of which used the output objects from json.load as their constructor argument.

I decided to make a finite state machine to manage the keyboard input, and created the basic capabilities of the State class. 

I then created a state diagram of all the necessary State instances, as well as a diagram of the other main classes and variables.

Using this diagram, I was able to declare each State object's attributes. I was then able to navigate the state machine with user input using the evaluate_default function and each State's children attribute.

I then slowly worked my way through the States, adding more and more functionality, making sure to test edge cases and potential errors along the way.

The only major hurdle along in this process was allowing the user to create their own template, but after enough trial and error, ended up using the  ‘~’ escape character to signify the use of an attribute from a class instance in globaldict. Then all I needed to do was to reformat the user input and add it to the json of templates.

I then tested each functional State by inputting correct values, incorrect values, empty values, and other possible edge cases. I ensured the Greeting class returns the correct greeting for a given time of day. I also tested my template creator by inputting correct, incorrect, and edge case values.

Finally, I gave all messages and prompts proper grammar and style, and did the same for my code.


# Limitations

-The way I created the State class seems a bit messy. I think that using subclasses would help a lot in getting the results I wanted out of it, especially looking at functions like template_case

-The template creator could be several times more intuitive, and could also be made an independent class. The way punctuation is handled at the end of a variable is a weak point and could cause errors.

-I felt like there were more opportunities to dive deeper into OOP principles, especially class inheritance, specifically the template creator and State class. If I were to spend more time with these classes, I would no doubt find many instances of reused code that could be better optimized.


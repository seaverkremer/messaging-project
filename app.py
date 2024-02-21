import json,datetime,pytz,sys
from Company import Company
from Greeting import Greeting
from Guest import Guest
from MessageTemplate import MessageTemplate
from State import State

def main():

    #load in companies, guests, and message templates from json files as python objects
    with open('Companies.json') as companies_json:
        companies_data = json.load(companies_json)
    with open('Guests.json') as guests_json:
        guests_data = json.load(guests_json)
    with open('MessageTemplates.json') as mtemplates_json:
        message_templates_data = json.load(mtemplates_json)

    #create lists to store class instances
    companies_list = []
    guests_list = []
    message_templates_list = []

    #turn json formatted 
    for comp in companies_data:
        companies_list.append(Company(comp))
    for guest in guests_data:
        guests_list.append(Guest(guest))
    for mtemplate in message_templates_data:
        message_templates_list.append(MessageTemplate(mtemplate))


    #globaldict is used in both app.py and State.py, stored in a separate file to prevent cyclical import
    global globaldict
    from globaldict import globaldict

    #storing object lists in globaldict
    globaldict['companies_list'] = companies_list
    globaldict['guests_list'] = guests_list
    globaldict['message_templates_list'] = message_templates_list


    #print welcome message and list basic commands
    print("\n\tWelcome to Customer Connector!\n\nTo navigate this tool, simply enter a response when prompted. At any time, you may also: \
    \n\n\t-Enter 'quit' or 'q' to quit\n\t-Enter 'help' or 'h' for help\n\t-Enter 'back' or 'b' to return to the previous prompt\n\t-Enter 'home' to return to the home screen\n")

    #create new State object for each page
    welcome_state = State('welcome',"Please enter the name of your employer. (Enter 'list' to see a list of employers): ",[],None,[])
    home_state = State('home',"Welcome, {} Employee. Would you like to send a message or create a new template?\n\tPlease enter either 'message' or 'template': ",["company_name"],None,[])
    globaldict['home_state'] = home_state
    message_state = State('message',"Please enter the name of the guest you'd like to message. Enter 'list' to see a list of all current guests: ",[],None,[])
    message_state_guest = State('messageguest',"Would you like to select {} a message from a template or create a bespoke message? Please enter either 'select' or 'bespoke': ",["guest_name"],None,[])
    select_template_state = State('select',"Enter the name of the template you would like to use. Enter 'list' to see a list of templates: ",[],None,[])
    bespoke_message_state = State('bespoke','Please enter your bespoke message to {}: ',["guest_name"],None,[])
    template_state = State('template',"Please enter your template below. To use a variable, type '~' directly before typing the variable name.\n\tEnter 'list' to see a list of supported variables: ",[],None,[])
    create_template_state = State('template_create', "Give your new template a name: ",[],None,[])

    #add children for each State
    welcome_state.add_children([home_state])
    home_state.add_children([message_state,template_state])
    message_state.add_children([message_state_guest])
    message_state_guest.add_children([select_template_state,bespoke_message_state])
    select_template_state.add_children([home_state])
    bespoke_message_state.add_children([home_state])
    template_state.add_children([create_template_state])
    create_template_state.add_children([home_state])

    #start
    welcome_state.evaluate()




if __name__ == "__main__": #ensures singleton
    main()
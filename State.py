import json,sys
from Company import Company
from Greeting import Greeting
from Guest import Guest
from MessageTemplate import MessageTemplate
from globaldict import globaldict

class State():
    def __init__(self,name,message,vars,parent,children):
        #self.message stores the message string, if any formatting is needed, those variables 
        #will be stored in order in the self.vars list
        self.name = name
        self.message = message
        self.vars = vars
        self.parent = parent
        self.children = children
    
    #getters
    def get_name(self):
        return self.name
    def get_message(self):
        return self.message
    def get_vars(self):
        return self.vars
    def get_parent(self):
        return self.parent
    def get_children(self):
        return self.children
    
    #setters
    def set_name(self,val):
        self.name = val
    def set_message(self,val):
        self.message = val
    def set_vars(self,val):
        self.vars = val
    def set_parent(self,val):
        self.name = val
    def set_children(self,val):
        self.name = val

    #additional methods for children list
    def add_children(self,children_list):
        for child in children_list:
            self.children.append(child)
    def remove_child(self,child):
        self.children.remove(child)
    def clear_children(self):
        self.children = []
        
    #find correct evaluator for current object
    def evaluate(self): 
        if self.name == 'welcome':
            self.welcome_state_case()     
        elif self.name == 'message':
            self.message_state_case()
        elif self.name == "template":
            self.template_case()
        elif self.name == 'template_create':
            self.template_create_case()
        elif self.name == 'select':
            self.template_select_case()
        elif self.name == 'bespoke':
            self.bespoke_case()
        else:
            self.default_evaluate()

    #space-saving function to handle exit,help,back,home, and empty/none imputs
    def handle_cases(self,user_input):
        global globaldict
        if user_input in ['q','quit','exit']:
            print('Exiting Program...')
            sys.exit()
        if user_input in ['h','help']:
            print("\nTo navigate this tool, simply enter a response when prompted. At any time, you may also: \
                  \n\n\t-Enter 'quit' or 'q' to quit\n\t-Enter 'help' or 'h' for help\n\t-Enter 'back' or 'b' to return to the previous prompt\n\t-Enter 'home' to return to the home screen\n")
            self.evaluate()
            return True
        if user_input in ['back', 'b']:
            if self.parent:
                print('Returning to previous page...')
                self.parent.evaluate()
                return True
            else:
                pass
        if user_input == '' or user_input.isspace():
            print("Sorry, your input cannot be blank. Enter 'help' for help.\n")
            self.evaluate()
            return True
        if user_input in ['home','cd']:
            if globaldict['company_name']:
                print("Returning to home screen...")
                globaldict['home_state'].evaluate()
                return True
            else: #catches if user is on welcome screen / hasn't entered their company name yet
                print("You must enter your company name first before heading to the home screen: ")
                self.evaluate()
                return True
        return False

    #default evaluator: redirects user to a given child of current State
    def default_evaluate(self):
        global globaldict
        temp = []
        for v in self.vars:             #supports any number of variables in message
            temp.append(globaldict[v])
        print(self.message.format(*temp))
        user_input = input()
        if self.handle_cases(user_input): #handle special inputs
            return
        for child in self.children:
            if child.name == user_input:
                child.parent = self
                child.evaluate()
                return
        print("Sorry, your input was not recognized. Enter 'help' for help.\n")
        self.evaluate()
        return
        
    #evaluates welcome state
    def welcome_state_case(self):
        global globaldict
        print(self.message)
        user_input = input()
        temp = [] #temporary list of company objects
        for comp in globaldict['companies_list']:
                temp.append(comp)
        if self.handle_cases(user_input):
            return
        elif user_input == 'list' or user_input == 'ls':    #handle 'list' input
            print("Here's a list of our current partners: ")
            for comp in temp:
                print(comp.get_company())
            self.evaluate()
            return
        else:
            for comp in temp:
                if user_input[:].casefold() == comp.get_company()[:].casefold():  #not case sensitive
                    globaldict['company_name'] = comp.get_company()
                    globaldict['company_obj'] = comp
                    the_greeting = Greeting(comp.get_timezone())
                    globaldict['the_greeting'] = the_greeting
    
                    child = self.children[0] 
                    child.parent = self
                    child.evaluate()
                    return
            print("Sorry, that company name was not recognized. Enter 'help' for help.\n")
            self.evaluate()
            return

    #evaluate message state
    def message_state_case(self):
        global globaldict
        print(self.message)
        user_input = input()
        temp = [] #temp list of guest objects
        for g in globaldict['guests_list']:
                temp.append(g)
        if self.handle_cases(user_input):
            return
        elif user_input == 'list' or user_input == 'ls': #handle 'list' input
            print("Here's a list of our current guests: ")
            for g in temp:
                print(g.get_name())
            self.evaluate()
            return
        else:
            for g in temp:
                if user_input[:].casefold() == g.get_name()[:].casefold():  # not case sensitive
                    globaldict['guest_name'] = g.get_name()
                    globaldict['guest_obj'] = g
                    
                    child = self.children[0]
                    child.parent = self
                    child.evaluate()
                    return
            print("Sorry, that guest name was not recognized. Enter 'help' for help.\n")
            self.evaluate()
            return
        
    #evaluate template state
    def template_case(self):
        global globaldict

        #create lists for pretty printing and creating args later on
        guest_vars = ['name','first_name','last_name','id','reservation','room_number','start_timestamp','end_timestamp']
        company_vars = ['company','company_id','city','timezone']
        misc_vars = ['greeting', 'time']
        all_vars = guest_vars[:] + company_vars[:] + misc_vars[:]

        print(self.message)
        user_input = input()
        if self.handle_cases(user_input):
            return
        elif user_input == 'list' or user_input == 'ls':
            print("Here's the list of supported variables: ")
            print('\n Guest variables:\t', '\t'.join(guest_vars))
            print(' Company variables:\t', '\t'.join(company_vars))
            print(' Miscellaneous variables:', '\t'.join(misc_vars))
            print(' ')
            self.evaluate()
            return
        else:
            template = user_input[:]
            template = template.split()
            args = []
            out = []
            #extracts variables from template into args, replaces them each with '{}' for string formatting
            for word in template:   #checks if each word (separated by whitespace) starts with escape character '~'
                punc = False #punc will enable punctuation to follow a variable declaration provided it is immediately followed by whitespace
                if word[0] == '~':
                    if word[1:] not in all_vars:
                        if word[1:-1] in all_vars: #check for punctuation
                            punc = word[-1]
                            word = word[:-1]
                        else:
                            print("\nError, {} is not a valid variable\n".format(word))
                            self.evaluate()
                            return
                    #add variable to args and replace the variable's word in the list with {} for string formatting later
                    if word[1:] in guest_vars:
                        args.append(["guest_obj", word[1:]])
                        word = "{}"
                    elif word[1:] in company_vars:
                        if word[1:] == 'company_id': 
                            #guest and company both have variable 'id', in company_vars it was 'company_id' to distinguish them, it is now back to 'id'
                            args.append(["company_obj",'id'])
                            word = "{}"
                        else:
                            args.append(['company_obj' , word[1:]])
                            word = "{}"
                    else:
                            args.append(['the_greeting', word[1:]])
                            word = "{}"
                    if punc:
                        word = word[:] + punc
                out.append(word)
            out = ' '.join(out)

            #put variables into globaldict for next page to add the name to
            temp_template = {"name" : 'placeholder',"message" : out, "args" : args}
            globaldict['message_template_obj'] = temp_template 

            child = self.children[0]
            child.parent = self
            child.evaluate()
            return

    #evaluate template create state
    def template_create_case(self):
            global globaldict
            
            print(self.message)
            user_input = input()
            if self.handle_cases(user_input):
                return
            for mtemplate in globaldict['message_templates_list']: #ensures no two templates will have the same name
                if mtemplate.name == user_input:
                    print('Name already taken, please try another name: ')
                    self.evaluate()
                    return
            temp_obj = globaldict['message_template_obj']
            final_template = {"name" : user_input,"message" : temp_obj['message'],"args" : temp_obj['args']}

            #adds newly created template to list with other templates
            with open("MessageTemplates.json") as templates_file:
                all_templates_data = json.load(templates_file)
                all_templates_data.append(final_template)

            #puts all templates into json file
            with open("MessageTemplates.json",'w') as temp_files:
                json.dump(all_templates_data, temp_files, indent=4)

            print('\nTemplate successfuly created. Returning to the home screen. \n')
            child = self.children[0]
            child.parent = self
            child.evaluate()
            return

    #evaluate template select state
    def template_select_case(self):
        global globaldict
        temp = [] # temp is a list of MessageTemplate objects
        for t in globaldict['message_templates_list']:
            temp.append(t)
        print(self.message)
        user_input = input()
        if self.handle_cases(user_input):
            return
        if user_input == 'list' or user_input == 'ls': #handle 'list' input
            print('Here is a list of all current templates: ')
            for item in temp:
                print(item.get_name())
            self.evaluate()
            return
        else:
            for t in temp:
                if user_input[:].casefold() == t.get_name()[:].casefold(): #not case sensitive
                    globaldict['message_template_obj'] = t

            tempys = [] #tempys will store all attribute values
            final_template=globaldict['message_template_obj']
            for arg in final_template.args: #each arg is stored as [object, attribute]
                #handle errors without halting program
                try:
                    tempy = getattr(globaldict[str(arg[0])],arg[1]) #gets attribute value of given object
                except Exception:
                    tempy = ['ERROR',str(arg)]
                tempys.append(tempy)

            final_message = final_template.message.format(*tempys)
            print("Your message to {} reads: '{}' \n\n\tWould you like to send it? (y/n): ".format(globaldict['guest_name'],final_message))
            user_input = input()
            if self.handle_cases(user_input):
                return
            if user_input in ['yes','y','send']:

                #log activity in the database!

                print('\nYour message has been sent! Returning to home screen: \n')
                child = self.children[0]
                child.parent = self
                child.evaluate()
            if user_input in ['no','n']:
                print("Your message has been erased. ")
                self.evaluate()
                return
            else:
                print("Sorry, your input was not recognized. Enter 'help' for help.\n")
                self.evaluate()
                return
            
    #evaluate bespoke case
    def bespoke_case(self):
        global globaldict
        temp = []
        for v in self.vars:
            temp.append(globaldict[v])
        print(self.message.format(*temp))
        user_input = input()
        if self.handle_cases(user_input):
            return
        print("Your bespoke message to {} reads: '{}' \n\n\tWould you like to send it? (y/n): ".format(globaldict['guest_name'],user_input))
        user_input = input()
        if self.handle_cases(user_input):
            return
        if user_input in ['yes','y','send']:
            print('\nYour message has been sent! Returning to home screen: \n')

            #log activity in the database!

            child = self.children[0]
            child.parent = self
            child.evaluate()
        if user_input in ['no','n']:
            print("Your message has been erased. ")
            self.evaluate()
            return
        else:
            print("Sorry, your input was not recognized. Enter 'help' for help.\n")
            self.evaluate()
            return
        
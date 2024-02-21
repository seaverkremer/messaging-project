class MessageTemplate():
    def __init__(self,mtemplate):
        self.name = mtemplate['name']
        self.message = mtemplate['message']
        self.args = mtemplate['args']
    
    #getters
    def get_name(self):
        return self.name
    def get_message(self):
        return self.message
    def get_args(self):
        return self.args
    def get_json(self):
        return {"name" : self.name,"message" : self.message,"args" : self.args}
    
    #setters
    def set_name(self,val):
        self.name = val
    def set_message(self,val):
        self.message = val
    def set_args(self,val):
        self.args = val
class Company():

    #input
    def __init__(self,comp):
        self.id = comp["id"]
        self.company = comp["company"]
        self.city = comp["city"]
        self.timezone = comp["timezone"]

    #getters
    def get_id(self):
        return self.id
    def get_company(self):
        return self.company
    def get_city(self):
        return self.city
    def get_timezone(self):
        return self.timezone
    
    #setters
    def set_id(self,val):
        self.id = val
    def set_company(self,val):
        self.id = val
    def set_city(self,val):
        self.city = val
    def set_timezone(self,val):
        self.timezone = val

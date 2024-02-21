class Guest():

    def __init__(self,guest_dict):
        self.id = guest_dict['id']
        self.first_name = guest_dict["firstName"]
        self.last_name = guest_dict["lastName"]
        self.name = self.first_name + ' ' + self.last_name
        self.reservation = guest_dict["reservation"]
        self.room_number = self.reservation["roomNumber"]
        self.start_timestamp = self.reservation["startTimestamp"]
        self.end_timestamp = self.reservation["endTimestamp"]

        #if Guest will store sensitive personal info, initialize those attributes as private instead
    
    #getters
    def get_name(self):
        return self.first_name + ' ' + self.last_name
    def get_id(self):
        return self.id
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_reservation(self):
        return self.reservation
    def get_room_number(self):
        return self.room_number
    def get_start_timestamp(self):
        return self.start_timestamp
    def get_end_timestamp(self):
        return self.end_timestamp
    
    #setters
    def set_name(self,first,last):
        self.first_name = first
        self.last_name = last
    def set_first_name(self,val):
        self.first_name = val
    def set_last_name(self,val):
        self.last_name = val
    def set_id(self,val):
        self.id = val
    def set_reservation(self,val):
        self.reservation = val
    def set_room_number(self,val):
        self.room_number = val
    def set_start_timestamp(self,val):
        self.start_timestamp = val
    def set_end_timestamp(self,val):
        self.end_timestamp = val

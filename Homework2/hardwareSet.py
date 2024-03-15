class hardwareSet():
    def __init__(self):
        self.__Capacity = 0
        self.__Availability = 0

    def initialize_capacity(self, qty):
        self.__Capacity = qty
        self.__Availability = qty

    def get_availability(self):
        return self.__Availability
    
    def get_capacity(self):
        return self.__Capacity
    
    def check_out(self, qty):
        available_to_checkout = self.get_availability()
        if(available_to_checkout >= qty):
            self.__Availability = available_to_checkout - qty
            return 0
        else:
            self.__Availability = 0
            return -1


    def check_in(self, qty):
        available_to_checkin = self.get_capacity()
        checkin = self.get_availability()
        if(checkin + qty <= available_to_checkin):
            self.__Availability = checkin + qty
            return 0
        else:
            return -1

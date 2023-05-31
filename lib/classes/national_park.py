class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, str) and not hasattr(self, "national_park"):
            self._national_park = national_park
        else:
            raise Exception("National park cannot be change")


        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip,  Trip):
            self._trip.append(new_trip)
        return self._trip
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self._visitor.append(new_visitor)
        return self._visitor
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass
class Visitor:
    
    all = []


    def __init__(self, name):
        self.name = name

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, str) and 1 <= len(visitor) <= 15:
            self._visitor = visitor
        else:
            raise Exception("Invalid visitor")
    

        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trip.append(new_trip)
        return self._trip
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if isinstance(new_national_park, NationalPark):
            self._national_park.append(new_national_park)
        return self._national_park
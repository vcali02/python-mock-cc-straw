class Visitor:
    
    all = []


    def __init__(self, name):
        self.name = name
        #I DIDN'T DO THIS
        self._trips = []
        self._national_parks = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name) >= 1 and len(name) <= 15:
            self._name = name
        else:
            raise Exception("Invalid name")
    

        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks:
            self._national_parks.append(new_national_park)
        return self._national_parks
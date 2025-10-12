class TrapArtists:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name
        
rr = TrapArtists("Rick Ross")
print(rr.name)
rr.name = "RickyRose"
print(rr.name)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):   # Getter → controls when you READ the value
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) < 3:
            print("Name too short!")
        else:
            self._name = value

jib = Person("shem")
jib.name = "li"
print(jib.name)
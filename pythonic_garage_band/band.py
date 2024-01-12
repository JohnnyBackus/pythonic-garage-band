class Musician:
    count = 0
    instances = []

    def __init__(self, name="unknown"):
        self.instances.append(self)

    def play_solo(self):
        return f"{self.name} solo"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Musician('{self.name}')"

class Guitarist(Musician):

    def __init__(self, name="unknown"):
        self.name = name
        super().__init__(name)

    def get_instrument(self):
        return "guitar"
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):

    def __init__(self, name="unknown"):
        self.name = name
        super().__init__(name)

    def get_instrument(self):
        return "bass"
    
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):

    def __init__(self, name="unknown"):
        self.name = name
        super().__init__(name)

    def get_instrument(self):
        return "drums"
    
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Band:
    instances = []

    def __init__(self, name="unknown_name", members=None):
        self.name = name
        self.members = members or []
        self.instances.append(self)
   
    def play_solos(self):
        return [member.play_solo() for member in self.members]
    
    def to_list(self):
        return self.members

    @classmethod
    def to_list(cls):
        pass
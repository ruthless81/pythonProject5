class Person:
    def __init__(self, Heart, Brain, Leg):
        self.Brain = Brain(0, "rested")
        self.Heart = Heart(0, "feelling good")
        self.Leg = Leg(0, "walking")

    def heart_state(self,Heart):
        heart_usage = 71
        if heart_usage > 70:
            self.Heart.state = "high blood pressure"
        else :
            self.Heart.state = "felling good"

    def Brain_state(self,Brain):

        Brain_usage = 49

        if Brain_usage > 90 :
            self.Brain.state = "tired"
        else :
            self.Brain.state = "rested"

    def Leg_state(self,Leg):

        Leg_usage = 40

        if Leg_usage > 10 :
            self.Leg.state = "running"
        else :
            self.Leg.state = "walking"


class Heart:
    def __init__(self,usage,state):
        self.usage = usage
        self.state = state



class Brain:
    def __init__(self,usage,state):
        self.usage = usage
        self.state = state


class Leg:
    def __init__(self,usage,state):
        self.usage = usage
        self.state = state







person = Person(Heart,Brain,Leg)

person.heart_state(person.Heart.usage)
person.Brain_state(person.Brain.usage)
person.Leg_state(person.Leg.usage)

print("Heart condition : ",person.Heart.state)
print("brain condition ; ",person.Brain.state)
print("leg condition :",person.Leg.state)









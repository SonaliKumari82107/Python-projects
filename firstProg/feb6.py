class Ritik:
    id=20180064893
    name ="Mishra"
    def __init__(self,id,name):
        self.id
        self.name=name

    def display(self):
        print("Constructor value: ", self.id, self.name)
        # print("Field value is : ",id)

Sonali = Ritik(2018,"a")
Sonali.display()
print(getattr(Sonali,"id"))
print(getattr(Sonali,"name"))
setattr(Sonali,"name","kamina")
print(getattr(Sonali,"name"))
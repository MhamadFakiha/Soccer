class animal:
    def __init__(self) :
        self.name = 'animal'
    def sound(self):
        print(self.name +" general sound")
        
class dog(animal):
    def __init__(self):
        self.name='dog'
    def sound(self):
        super().sound()
        print(self.name+" sound")
        
diggie = dog()
diggie.sound()
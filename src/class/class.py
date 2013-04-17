class animal:
    name = "uname"
    
    def __init__(self, voice="hello"):
        self.voice=voice
    
    def __del__(self):
        pass
    
    def say(self):
        print self.voice, "---", self.name
        
t = animal();
t.say()

dog = animal("dog");
dog.say()
    
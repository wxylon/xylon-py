class animal:
    def __init__(self, voice="hello"):
        self.voice = voice
    
    def say(self, name):
        print self.voice
        
    def run(self):
        pass

class dog(animal):
    def __init__(self, voice="dog"):
        animal.__init__(self, voice)
    
    def setVoice(self, voice):
        self.voice = voice
    
    def say(self):
        print self.voice
    
    def run(self):
        print "running"
        
bobo = animal()
bobo.say("123")
bobo.run()
      
bobo = dog()
bobo.setVoice("are you bobo?")
bobo.say()
bobo.run()
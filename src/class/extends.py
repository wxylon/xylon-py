class animal:
    def __init__(self, voice="hello"):
        self.voice = voice
    
    def say(self):
        print self.voice
        
    def run(self):
        pass

class dog(animal):
    
    def setVoice(self, voice):
        self.voice = voice
    
    def run(self):
        print "running"
        
        
bobo = dog()
bobo.setVoice("are you bobo?")
bobo.say()
bobo.run()
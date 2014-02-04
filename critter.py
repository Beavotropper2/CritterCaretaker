import random

# Austen Calzadilla
# Critter class
#
# Provides Chapter 8 functionality
# Also includes more critter responses
# Feed and play responses chosen randomly
# Critter has hunger and fatigue levels which affect mood
# Feeding critter restores hunger
# Added sleep action to restore fatigue

max_level = 5

class Critter(object):
    """A virtual pet"""
    name = "Default Larry"
    mood = ""
    moods = ("happy",
             "tired",
             "sad",
             "hungry")
    
    hunger = 0
    fatigue = 0

    feedResponses = ("That tasted great!",
                     "I'm so full!",
                     "Wow, who knew you could cook so well!",
                     "Thanks for the meal!")
    playResponses = ("Good game!",
                     "That was so fun!",
                     "Whew, that was tiring!")

    def __init__(self, name):
        self.name = name
        self.mood = self.generateMood()
    
    def generateMood(self):
        gen = random.randint(0, len(self.moods) - 1)
        return self.moods[gen]

    def generateResponse(self, responses):
        gen = random.randint(0, len(responses) - 1)
        return responses[gen]

    def incrementVal(self, val):
        if val < max_level:
            return val + 1
        else:
            return max_level

    def listen(self):
        if self.fatigue > max_level - 2:
            self.mood = self.moods[1]
        elif self.hunger > max_level - 2:
            self.mood = self.moods[2]
        print("\nI'm {0} and I feel {1} now.\n".format(self.name, self.mood))

    def feed(self):
        response = self.generateResponse(self.feedResponses)
        print("\n" + response + "\n")
        self.hunger = 0
        self.fatigue = self.incrementVal(self.fatigue)
        while self.mood != "hungry":
            self.mood = generateMood()

    def play(self):
        response = self.generateResponse(self.playResponses)
        print("\n" + response + "\n")
        self.fatigue = self.incrementVal(self.fatigue)
        self.hunger = self.incrementVal(self.hunger)
        if self.mood == "sad":
            self.mood == "happy"

    def sleep(self):
        print("\nzzzzzz...\n")
        self.fatigue = 0
        if self.hunger < max_level - 1:
            self.hunger += 2
        else:
            self.hunger = 5
        

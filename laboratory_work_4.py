import random #I created a small 4x4 mini-football simulator, so random is needed here.

class Player(object):

    def __init__(self, name, shooting, passing, defence, saving):

        self.name = name #each player has its own characteristics on a ten-point scale
        self.shooting = shooting
        self.passing = passing
        self.defence = defence
        self.saving= saving  
        self.morality = 10

class Forward(Player): #Each Position class inherits the Player class

    def goal(self, other):
        if random.choices([self.name, other.name],
        weights = [self.shooting + self.morality, other.saving + other.morality]) == [self.name]:
            return True
        else:
            return False

class Midfielder(Player):

    def assist(self, other):
        if random.choices([self.name, other.name], 
        weights = [self.passing + self.morality, other.defence + other.morality]) == [self.name]:
            return True
        else:
            return False

class Defender(Player):

    def tackle(self, other):
        if random.choices([self.name, other.name], 
        weights = [self.defence + self.morality, other.passing + other.morality]) == [self.name]:
            return True
        else:
            return False

class Goalkeeper(Player):

    def save(self, other):
        if random.choices([self.name, other.name],
        weights = [self.saving, other.shooting]) == [self.name]:
            return True
        else:
            return False

class Team(Player):
    def __init__(self, name, goalkeeper, defender, midfielder, forward):
        self.name = name
        self.forward = forward #The team consists of a goalkeeper, a defender, a midfielder and a forward
        self.goalkeeper = goalkeeper
        self.defender = defender
        self.midfielder = midfielder
    

    def game(self, other): 
        #The game lasts 90 minutes, goals affect the morale of the players, 
        #which affects the quality of their play
        game_score = [0,0]
        minutes = 90
        while minutes > 0:
            if (self.forward.goal(other.goalkeeper) == True and
             self.midfielder.assist(other.defender) == True):
                print (f'{self.forward.name} scored against {other.goalkeeper.name}, assist {self.midfielder.name}')
                minutes -= 15
                game_score[0] += 1
                self.forward.morality +=10
                self.midfielder.morality +=5
                other.goalkeeper.morality -=10
                other.defender.morality -=5
            else:
                minutes -= 10
            if (self.goalkeeper.save(other.forward) == False and
            self.defender.tackle(other.defender) == False):
                print (f'{other.forward.name} scored against {self.goalkeeper.name}, assist {other.midfielder.name}')
                minutes -= 15
                game_score[1] += 1
                other.forward.morality +=10
                self.goalkeeper.morality -=10
                self.defender.morality -=5
                other.midfielder.morality -=5
            else:
                minutes -= 10
            if game_score[0] > game_score[1]:
                result = self.name
            elif game_score[0] < game_score[1]:
                result = other.name
            else:
                result = 'Draw'
            
        return f'Final score: {game_score} - {result}'


HENDERSON = Goalkeeper('HENDERSON', 5, 5, 5, 8) #Players
VARANE = Defender('VARANE', 5, 6, 8, 5)
BRUNO = Midfielder('BRUNO', 8, 9, 7, 5)
MARTIAL = Forward('MARTIAL', 9, 8, 5, 5)

NEYMAR = Forward('NEYMAR', 9, 8, 5, 5)
NAVAS = Goalkeeper('NAVAS', 5, 5, 5, 8)
RAMOS = Defender('RAMOS', 7, 7, 8, 5)
VERATTI = Midfielder('VERATTI', 6, 9, 6, 5)

MU = Team('MU', HENDERSON, VARANE, BRUNO, MARTIAL) #Team lineups
PSG = Team('PSG', NAVAS, RAMOS, VERATTI, NEYMAR)

print(MU.game(PSG))







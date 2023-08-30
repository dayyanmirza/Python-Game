"""
Let's laydown the classes we want to implement.

So what is my game going to be about. 

Title --> Paranoia

Basic Idea:
- You see great success in the business world creating a security device that protects people's computers. 
- You sell the company, but you have alot of enemies.
- You need to retreat from the US, before its too late and in order to do that you find out that you have allies in Peru find a way to get there w/ out getting killed.


Game description:

Home:
- You're going about your day, when one day a bottle is thrown at your window. The window smashes and the bottle has a note, the note says, "We know that you know".
- It's the CIA. You know it. After years of working in close conjunction with them they're afraid your recent tirades make you a weak link. They might wnat to get rid of this problem once and for all. 
- You decide its time to go, and never return. Which is simple as you don't have family that's alive anyway. 

Phonebooth:
- You leave your house and go to the phonebooth outside of the city to make sure no one's listening. You call them up using a code only they know and then they say an anagram of a country to come to.
- You write the leters down and it says Peru. 

Plane:
- You know another guy and he actually helps you gives you a fake passport and even a small plane that he will take you to peru in but he can't at the momnet and requires some compensation.
- It's not money, he has a some beef to settle with another man. 
- He stole from him. 
- It's an online transaction, though, you've done this beofre multiple times and it's for a good cause so you help him. 
- You get the money give it to him. 
- You go on the plane area but the guy is no where to be seen. 
- But luckily theres a plane there and you've had helicopter training how hard can a plane be. 
- You're on your way to peru but middle of the flight you realise your low on fuel so you do a quick emergency landing in somewhere in Ecuador. 

Ecuador:
- People try to kidnap you cause they know you have money as they recognise you from somewhere. 
- Now your in a truck and overhear the guys are going to Peru.
- You're about to arrive and you stop somewhere they open the doors and throw you out, and they start speaking in Spanish.
- One guy knows enlgish so you start talking and they are asking for alot of money cause they saw you sell your compnay in the news.
- To them you say if they take you to this spot in Peru then he knows someone that can give you the money.

Peru:
- They take you there and upon arrival they take of your cuffs, and put a gun on your back.
- Then you meet the guy and tell them he has the money get it from him. 
- They get the guy, but they didn't realise he's not only an CIA agent you know that's left CIA, so he realises you're in trouble and he tells the guys.
- He will get the money for them, he goes and gives them 500,000 us dollars.
- They leave, but little did they know thats prop money he has back from one of his cases.

- Now you've arrived safe and sound here but are unsure what the future holds, all you need is some breathing space to think about things. But still the Paranoia remains. 


Classes:
* Map 
    - next_scene
    - opening_scene 
* Engine 
    - play
* Scene
    - enter
    * Death
    * Home 
    * Phonebooth
    * Plane 
    * Ecuador
    * Peru

"""
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self): # make a generic thing here that can be inherited by all scenes. i.e. prints out the scene or location name.
        print("This scene is not yet configured.")
        print("Sublass it and implement enter.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        pass

class Death(Scene):

    quips = [
        "Your little cousin can do better than that cmon.",
        "You're not even fighting anyone, how are you losing?!",
        "Game over. You lost. Get over it. Try again."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Home(Scene):

    def enter(self):
        print(dedent("""
            You're going about your day, when one day a bottle is thrown at your window.
            The window smashes and the bottle has a note, the note says, 'We know that you know'.
            It's the CIA. You know it.
            After years of working in close conjunction with them they're afraid your recent tirades make you a weak link.
            They might wnat to get rid of this problem once and for all.

            You have to make a decision 1) leave and never come back, 2) act like nothing happened  
            """))

        action = int(input("> "))

        if action == 1:
            print(dedent("""
                You decide its time to go, and never return.
                Good choice. You need to talk to someone but your home is a liablity.
                """))
            return 'phonebooth'
        if action == 2:
            print(dedent("""
                Why would you do that? Clearly you should have done something.
                """))
            return 'death'
        

class Phonebooth(Scene):

    def enter(self):
        print(dedent("""
            You leave your house and go to the phonebooth outside of the city to make sure no one's listening.
            You call them up using a code only they know and then they say an anagram of a country to come to.\n
            The country is urep, what could the country be, 1) Reup, 2) Peru", \n 
            """))
        
        action = int(input("> "))

        if action == 1:
            print(dedent("""
                You decide to go to lookup Reup which only shows you software companies. Ok well thats odd he must work in one. 
                You go there and realise very quickly no one has any idea about helping you escape. 
                So you just decide to go back, but on your way back home your stopped and searched and taken into a van. 
                
                But they don't look like police. They caught onto you. 
                """))
            return 'death'
        elif action == 2:
            print(dedent("""
                That wasn't too hard. Now you know the location, you just need to make a call to a guy named Fred. 
                
                He has a plane and can give you a fake passport to help you not have any trouble w/ the authorities in Peru.
                """))
            return 'plane'
        else:
            print("That's not an option.\n")
            return 'home'
        

class Plane(Scene):

    def enter(self):
        print(dedent("""
            You know another guy, called Fred, and he actually will help give you a fake passport and even a small plane that he will take you to Peru in but he can't at the moment he requires a favour.
            It's not money, he has a some beef to settle with another man. 
            
            He stole from him. But luckily Fred has the guys laptop.
            It's an online transaction, though, you've done this beofre multiple times and it's for a good cause so you help him. 
            
            In order to do this you have to guess the other guys laptop password, in order to gain access to his computer. 
            
            You are only allowed 5 guesses for the password otherwise your locked out.
                     
            Password Hint: The guy your hacking is a CIA agent from LA. It's 12 characters. It needs to have a number and a special character.
            """))

        
        password = "CIAAgentLA1!"
        guess = input("> ") # 
        guesses = 1 # so there 4 guesses in the while loop as the --> guess = input("> ") line above counts as a guess too. Therefore there's 5 guesses in total.

        while guess != password and guesses < 5: # 1-5 guesses allowed in the loop plus the initial guess on the line --> guess = input("> ") therefore 5 guesses in total.
            print("BZZZED!")
            guesses += 1
            guess = input("> ")

        if guess == password:
            print(dedent("""
                You break in to the laptop and get the guys money for him. He says thanks gives you your fake details and says that you will leave in 2 days. 
                
                Until then lay low.
                """))
            return 'ecuador'
        else:
            print(dedent("""
                You get the password wrong the guy gets upset tells you to leave but on your way out he tells you to go get his mail, on your way to the mailbox he shoots you.
                """))
            return 'death'

class Ecuador(Scene):

    def enter(self):
        print(dedent("""
            You go to the plane area but the guy is no where to be seen. 
            
            But luckily theres a plane there and you've had helicopter training how hard can a plane be. 
            You pick one and from there you're on your way to peru but middle of the flight you realise your low on fuel so you do a quick emergency landing somewhere in Ecuador. 
            
            As you land people try to kidnap you cause they know you have money as they recognise you from the TV as you're big sofware company acquistion was televised worldwide. 
            Your in a truck and overhear the guys are going to Peru.
            
            You're about to arrive and you stop somewhere they open the doors and throw you out, and they start speaking in Spanish.
            One guy knows enlgish so you start talking and they are asking for alot of money cause they saw you sell your compnay in the news.
            
            You have two options: 1) negotiate, 2) run
            """))
        
        action = int(input("> "))

        if action == 1:
            print(dedent("""
                To them you say "If you take me to this spot in Peru then I know someone that can give you the money." 
                         
                So they agree.
                """))
            return 'peru'
        elif action == 2:
            print(dedent("""
                That was a veryy bad idea...do you want to lose or something? They just shoot you and leave your body there.
                """))
            return 'death'
        else:
            print("That's not an option.\n")
            return 'home'

        
class Peru(Scene):

    def enter(self):
        print(dedent("""
            They take you there and upon arrival they take of your cuffs, and put a gun on your back.
            Then you meet the guy and tell them he has the money get it from him. 
            
            
                     
            He will get the money for them, he goes and gives them 500,000 us dollars.
            They leave, but little did they know thats prop money he has back from one of his cases.

            """))
        ###########

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('home')
a_game = Engine(a_map)
a_game.play()
        
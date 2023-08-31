from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self): # make a generic thing here that can be inherited by all scenes. i.e. prints out the scene or location name.
        print("This scene is not yet configured.")
        print("Sublass it and implement enter.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map): # The constructor initialises the Engine instance. It takes a single argument scene_map.
        self.scene_map = scene_map

    def play(self):  
        current_scene = self.scene_map.opening_scene() 
        last_scene = self.scene_map.next_scene('finished')
        
        """
        The play method is responsible for the gameplay loop:
        - current_scene --> Starts by getting the initial scene using opening_scene() method of the Map instance a_map. Returns instance of the initial scene. 
        - last_ scene --> Gets the scene that signifies the end of the game. Using next_scene('finished') method of the Map instance.
        - Inside the while loop: 
            - The enter() method of the current_scene is called. This method returns the name of the next scene it should transition to based on their choices in that scene. This next_scene_name is stored in the next_scene_name variable. 
            - current_scene = self.scene_map.next_scene(next_scene_name) --> The next_scene method of the Map instance is called with the next_scene_name, obtained from the previous step.
                - This method returns the scene object associated with the provided scene name. 
                - The current_scene is then updated to this new scene object and the loop continues.


        """

        while current_scene != last_scene: # While loop runs as long as the current_scene is not equal to the last_scene. 
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene 
        current_scene.enter() # after the loop the final scene is played one more time to ensure the player sees the outcome of their choices before the game concludes.


class Death(Scene):

    quips = [
        "Your little cousin can do better than that cmon.",
        "This isn't even a fighting game, how are you losing?!",
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
            return 'phone_booth'
        if action == 2:
            print(dedent("""
                Why would you do that? Clearly you should have done something.
                """))
            return 'death'
        

class PhoneBooth(Scene):

    def enter(self):
        print(dedent("""
            You leave your house and go to the phonebooth outside of the city to make sure no one's listening.
            You call them up using a code only they know and then they say an anagram of a country to come to.\n
            The country is urep, what could the country be, 1) Reup, 2) Peru, \n 
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
            
            You are only allowed 5 guesses for the password otherwise you will be locked out.
                     
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
            Then you meet the guy, called Hank, and tell them he has the money get it from him. 
            
            The kidnappers start telling Hank your in big trouble with them and they require compensation.
                     
            Hank winks at you in a discreet way, but you don't know whether he's signalling you to do something.
                     
            You have two options: 1) turn around and headbutt the guy, 2) let Hank take the lead
            """))
        
        action = int(input("> "))

        if action == 1:
            print(dedent("""
                You turn around trying to fistbump the guy but in the process you trip up and fall to the ground. 
                
                Then Hank starts to pull out his gun but before you know it, they shoot him, and you. You're both lying there on the ground in the middle of the street.
                """))
            return 'death'
        elif action == 2:
            print(dedent("""
                Hank goes and gives them 500,000 us dollars.
                They leave, but little did they know thats prop money he has back from one of his cases when he used to work for the CIA.

                Now you've arrived safe and sound here but are unsure what the future holds, all you need is some breathing space to think about things. 
                But still the Paranoia remains. 
                """))
            return 'finished'
        else:
            print("That's not an option.\n")
            return 'home'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    # The scenes dictionary allows you to easily map scene names to their corresponding objects. Instead of having to manually instantiate each scene when needed i.e. x = Home() etc, you can retrieve the appropriate scene object from the dictionary using the scene name as the key.
    scenes = { 
        'home': Home(),  
        'phone_booth': PhoneBooth(),
        'plane': Plane(),
        'ecuador': Ecuador(),
        'death': Death(),
        'peru': Peru(),
        'finished': Finished()
    }

    """ 
    How does returning the next room work ?

    - It's done by using the next_scene method ot the Map class.
    - The scenes dictionary containes the scene name mapped to the scene object, each scene object is an instance a scene class i.e. Home etc.
    - The next_scene method takes one argument which is the scene_name of the next scene you want to transition to.
    - Map.scenes.get(scene_name) --> this line in the next_scene method uses the get method retrives a scene object depedning on the scene name. If the scene name has a corresponding scene object in the dictionary the method returns the corresponding scene object, otherwise, it returns none.
    - Then it returns the retrieved scene object as a result of the next_scene method. i.e. return val. 
    """

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene) # refers to the first scene that's inputted i.e. central_corridor, i.e. in the init constructor, returns the instance of i.e. central_corridor scene. 


# creating an instance of the Map and Engine class and invoking the play method of the engine class.
a_map = Map('home')
a_game = Engine(a_map) # passing the instance of the map class as an agrument in the Engine class instance means the Engine class has access to the Map Class. Allowing us to navigate through the different scenes.
a_game.play()
        
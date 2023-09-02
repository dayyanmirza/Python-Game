import tkinter as tk
from tkinter import *
from tkmacosx import Button # https://pypi.org/project/tkmacosx/ Fixes the issue w/ button bg color, so it actually shows the color.

from sys import exit
from random import randint

class Scene(object):

    def enter(self): # make a generic thing here that can be inherited by all scenes. i.e. prints out the scene or location name.
        exit(1) # This scene is not yet configured. Subclass it and implement enter.

# class Engine(object):

#     def __init__(self, scene_map): # The constructor initialises the Engine instance. It takes a single argument scene_map.
#         self.scene_map = scene_map

#     def play(self):  
#         current_scene = self.scene_map.opening_scene() 
#         last_scene = self.scene_map.next_scene('finished')
        
#         """
#         The play method is responsible for the gameplay loop:
#         - current_scene --> Starts by getting the initial scene using opening_scene() method of the Map instance a_map. Returns instance of the initial scene. 
#         - last_ scene --> Gets the scene that signifies the end of the game. Using next_scene('finished') method of the Map instance.
#         - Inside the while loop: 
#             - The enter() method of the current_scene is called. This method returns the name of the next scene it should transition to based on their choices in that scene. This next_scene_name is stored in the next_scene_name variable. 
#             - current_scene = self.scene_map.next_scene(next_scene_name) --> The next_scene method of the Map instance is called with the next_scene_name, obtained from the previous step.
#                 - This method returns the scene object associated with the provided scene name. 
#                 - The current_scene is then updated to this new scene object and the loop continues.


#         """

#         while current_scene != last_scene: # While loop runs as long as the current_scene is not equal to the last_scene. 
#             next_scene_name = current_scene.enter()
#             current_scene = self.scene_map.next_scene(next_scene_name)

#         # be sure to print out the last scene 
#         current_scene.enter() # after the loop the final scene is played one more time to ensure the player sees the outcome of their choices before the game concludes.

# class Death(Scene):

#     quips = [
#         "Your little cousin can do better than that cmon.",
#         "This isn't even a fighting game, how are you losing?!",
#         "Game over. You lost. Get over it. Try again."
#     ]

#     def enter(self):
#         print(Death.quips[randint(0, len(self.quips)-1)])
#         exit(1)

class Home(Scene):

    def __init__(self, window):
        self.window = window

    def enter(self):
        label = tk.Label(text="""
            You're going about your day, when one day a bottle is thrown at your window.
            The window smashes and the bottle has a note, the note says, 'We know that you know'.
            It's the CIA. You know it.
            After years of working in close conjunction with them they're afraid your recent tirades make you a weak link.
            They might wnat to get rid of this problem once and for all.

            You have to make a decision 1) leave and never come back, 2) act like nothing happened  
            """)
        label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()
        
        submit = Button(self.window, text="Submit", width=200, height=50, bg="blue", fg="red", command=self.choice) 
        submit.pack()
        
    def choice(self):
        choice_int= int(self.entry.get())
        if choice_int == 1:
            choice_one = tk.Label(text="""
                You decide its time to go, and never return.
                Good choice. You need to talk to someone but your home is a liablity.
                """)
            choice_one.pack()
        elif choice_int == "2":
            choice_two = tk.Label(text="""
                Why would you do that? Clearly you should have done something.
                """)
            choice_two.pack()
        else:
            not_option = tk.Label(text="That's not an option.")
            not_option.pack()
            

# class Map(object):

#     # The scenes dictionary allows you to easily map scene names to their corresponding objects. Instead of having to manually instantiate each scene when needed i.e. x = Home() etc, you can retrieve the appropriate scene object from the dictionary using the scene name as the key.
#     scenes = { 
#         'home': Home(),  
#         'phone_booth': PhoneBooth(),
#         'plane': Plane(),
#         'ecuador': Ecuador(),
#         'death': Death(),
#         'peru': Peru(),
#         'finished': Finished()
#     }

#     """ 
#     How does returning the next room work ?

#     - It's done by using the next_scene method ot the Map class.
#     - The scenes dictionary containes the scene name mapped to the scene object, each scene object is an instance a scene class i.e. Home etc.
#     - The next_scene method takes one argument which is the scene_name of the next scene you want to transition to.
#     - Map.scenes.get(scene_name) --> this line in the next_scene method uses the get method retrives a scene object depedning on the scene name. If the scene name has a corresponding scene object in the dictionary the method returns the corresponding scene object, otherwise, it returns none.
#     - Then it returns the retrieved scene object as a result of the next_scene method. i.e. return val. 
#     """

#     def __init__(self, start_scene):
#         self.start_scene = start_scene

#     def next_scene(self, scene_name):
#         val = Map.scenes.get(scene_name)
#         return val
    
#     def opening_scene(self):
#         return self.next_scene(self.start_scene) # refers to the first scene that's inputted i.e. central_corridor, i.e. in the init constructor, returns the instance of i.e. central_corridor scene. 


# # creating an instance of the Map and Engine class and invoking the play method of the engine class.
# a_map = Map('home')
# a_game = Engine(a_map) # passing the instance of the map class as an agrument in the Engine class instance means the Engine class has access to the Map Class. Allowing us to navigate through the different scenes.
# a_game.play()
        


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Paranoia")
    window.geometry("1000x800")
    home = Home(window)
    home.enter()
    window.mainloop()

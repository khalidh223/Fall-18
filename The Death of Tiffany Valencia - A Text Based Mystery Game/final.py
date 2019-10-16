"""
final.py

Python file containing source code for game, The Death of Tiffany Valencia
Created by Khalid Hussain and Elwood Olson

"""
intro = open("intro.txt", 'r')
intro_data = intro.read()
text = open("game_data.txt", 'r')
data = text.readlines()
"""
This set of variables keeps track of items in the players pocket and win conditions
"""
pocket = {}
box_opened = False
can_opened = False
letter_read = False
"""
This function solicits the user for input and processes it into verbs and nouns.
"""
def get_user_input():
    response = input(">>>").split(" ")
    if len(response) != 2:
        if response == ["quit"] or response == ["Quit"]:
            return "quit", None
        elif response == ["observe"] or response == ["Observe"]:
            return "observe", None
        else:
            return "",""
    else:
        verb = response[0].lower()
        noun = response[1].lower()
    return verb, noun
"""
This function translates user's verb-noun commands into in game effects, by calling
corresponding methods from defined classes. "room" is passed as a parameter in order
to keep track of the room object from the main loop.
"""
def process_user_input(room):
    global box_opened, can_opened, letter_read
    verb, noun = get_user_input()
    if verb.lower() == "pickup":
        Pocket(room.room_number).add_to_pocket(noun)
    elif verb.lower() == "examine":
        Pocket(room.room_number).examine_object(noun)
    elif verb.lower() == "go":
        room.travel(noun)
    elif verb.lower() == "observe":
        room.observe_room()
    elif verb.lower() == "quit":
        return True
    elif verb.lower() == "open":
        if noun == "box":
            if room.room_number == 2:
                if "key" in pocket:
                    print("Inside the box, there is a life insurance statement overseen by the family lawyer, Tony Venchenzo. It is in the name of 'Tiffany Valencia', and it is for the amount of $100,000.")
                    box_opened = True
                else:
                    print("You don't have a key!")
            else:
                print("That doesn't make sense right now.")
        if noun == "can":
            if room.room_number == 4:
                if "can-opener" in pocket:
                    print("Inside the can, there is a bloodied ear with a diamond earring!")
                    can_opened = True
                else:
                    print("You don't have a can-opener!")
            else:
                print("That doesn't make sense right now.")
    elif verb.lower() == "translate":
        if noun == "letter":
            if room.room_number == 5:
                if "letter" in pocket:
                    print("Dear Tiffany, I write to you only because I have your best interest at heart. I don't want to offend you, but this matter is difficult to discuss politely. Your husband, Bobby, may not be as good a man as what he makes himself out to be. For your sake and for the peace of my mind, please be careful!")
                    print("\nWith concern, Tony")
                    letter_read = True
                else:
                    print("You don't have anything to translate.")
            else:
                print("That doesn't make sense right now.")
    elif verb.lower() == "light":
        if noun == "cigarette":
            if room.room_number == 4:
                if "cigarette" in pocket:
                    print("You take the cigarette and light it on the stove. You take a long drag and feel 10 times better about the case.")
                else:
                    print("You don't have a cigarette.")
            else:
                print("That doesn't make sense right now.")
    elif verb.lower() == "cheat":
        box_opened = True
        can_opened = True
        letter_read = True
    else:
        print("I don't understand...")
"""
This function loops in order to keep receiving inputs from the user until it breaks
when all the win conditions are met or a quit command is passed.
"""
def game_loop(room):
    while True:
        game_over = process_user_input(room)
        if game_over: break
        if box_opened and can_opened and letter_read:
            print("\nYour police chief tells you that he believes you have collected enough evidence from the crime scene. You find yourself back at the police station, and you face three suspects. You must choose who to indict.")
            culprit = input("You options are Tony, Bobby, and Valentino: ")
            if culprit.lower() == "bobby":
                print("It looks like Bobby didn't have enough money to pay the mob for losing a numbers racket...too bad cashing out on his wife and her jewelery has landed him a life behind bars!")
                print("The chief says you are in for a raise. Nice work, Detective.")
            elif culprit.lower() == "tony":
                print("Tony! What were you thinking!? The family lawyer was just trying to help Tiffany out with her fracturing relationship with Bobby!")
                print("The chief says you are facing a demotion - looks like its going to be a month of desk work...")
            elif culprit.lower() == "valentino":
                print("The chief pulls Valentino out of the lineup for questioning, but it looks like his alibi for the night is air-tight. He doesn't seem to be the true culprit...")
                print("...what's worse is that he has put out a mob hit on you. Good luck, pal...")
            break
"""
This function makes keeping track of room names simpler.
"""
def room_to_room_number(room):
    if room == "Bedroom":
        return 1
    if room == "Dining Room":
        return 2
    if room == "Foyer":
        return 3
    if room == "Kitchen":
        return 4
    if room == "Living Room":
        return 5
    else:
        return False
"""
This class keeps track of data from game_data.txt and sets instance variables to the
corresponding names, descriptions, etc. of each room.
"""
class Room:
    def __init__(self):
        self.room_number = 1
        self.room_index = 0
        self.name = ""
        self.description = ""
        self.objects = []
        self.direction = {}
    """
    This method takes a room number from game_data.txt as a parameter, and creates
    and changes the Room instance variables to reflect that of the new room.
    """
    def change_room(self, room_number):
        self.room_number = room_number
        self.room_index = 5*(room_number - 1)
        self.name = data[self.room_index]
        self.description = data[self.room_index + 1]
        self.objects = data[self.room_index + 2]
        direction1, room1, direction2, room2, direction3, room3, direction4, room4 = data[self.room_index + 3].split(",")
        self.direction[direction1] = room1
        self.direction[direction2] = room2
        self.direction[direction3] = room3
        self.direction[direction4] = (room4.split("\n"))[0]
        self.Where()
        print_directions(self.direction)
    """
    This method implements change_room within the context of a "go" command.
    """
    def travel(self, direction):
        if direction in self.direction:
            room = self.direction[direction]
            if room_to_room_number(room) != False:
                room_number = room_to_room_number(room)
                self.change_room(room_number)
            else:
                print("You can't go that way!")
        else:
            print("You can't go that way!")
    """
    This method prints a list of the objects within a room.
    """
    def observe_room(self):
        things_in_room = Pocket(self.room_number).things_in_room
        print("In the room, you observe these things:")
        for key in things_in_room:
            if key != "":
                print(key)

    def clear_dictionary(self):
        return self.direction.clear()

    def Where(self):
        room_title = self.name.split(":")[1]
        print(room_title)
        print(self.description)

    def Object(self):
        print(self.objects)

    def Direction(self):
        print(self.direction)
"""
This class, similar to Room, keeps track of objects from the game_data file.
"""
class Pocket:
    def __init__(self, room_number):
        self.things_in_room = {}
        self.room_number = room_number
        self.room_index = 5*(room_number - 1)
        self.objects = data[self.room_index + 2]
        self.thing1, self.description1, self.thing2, self.description2, self.thing3, self.description3 = self.objects.split(",")
        self.things_in_room[self.thing1] = self.description1
        self.things_in_room[self.thing2] = self.description2
        self.things_in_room[self.thing3] = (self.description3.split("\n"))[0]
    """
    This method prints a description of an item that is examined with the "examine" command.
    """
    def examine_object(self, noun):
        if noun == self.thing1:
            print("You examine the", self.thing1, ".", self.description1)
        elif noun == self.thing2:
            print("You examine the", self.thing2, ".", self.description2)
        elif noun == self.thing3:
            print("You examine the", self.thing3, ".", self.description3)
        else:
            print("This item is not in this room!")
    """
    This method adds the object picked up with the "pickup" command to the pocket dictionary.
    """
    def add_to_pocket(self, noun):
        if noun == self.thing1:
            pocket[self.thing1] = self.description1
            print("You added", self.thing1, "to your pocket.")
        elif noun == self.thing2:
            pocket[self.thing2] = self.description2
            print("You added", self.thing2, "to your pocket.")
        elif noun == self.thing3:
            pocket[self.thing3] = self.description3
            print("You added", self.thing3, "to your pocket.")
        else:
            print("This item is not in the room!")
    """
    This function prints a list of directions that you can travel, along with its
    corresponding room.
    """
def print_directions(direction_dictionary):
    for direction in direction_dictionary:
        if direction_dictionary[direction] != "":
            print("If you go", direction,"==>", direction_dictionary[direction])

def main():
    print(intro_data)
    dummy = input(">>>") #Prompts user for input.
    room = Room()
    room.change_room(3)
    game_loop(room)
main()

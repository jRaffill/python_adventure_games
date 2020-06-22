import random
import sys
item = ""
dragon_hp = 0
player_hp = 0
def end_success(item):
    if item == "":
        print ("Congratulations! You completed this adventure with your life, even though you didn't get any riches. After all, life is the greatest gift of all.")
        sys.exit()
    else: 
        print ("Congratulations! You completed this adventure with your life and {}." . format (item))
        sys.exit()
def dragon_fight():
    global dragon_hp
    global player_hp
    print ("Your turn.")
    hit = random.randint (1, 3)
    if hit == 1:
        dragon_hp = dragon_hp - 1
        print ("You hit the dragon. It loses one point.")
        print ("Dragon Health: " + str (dragon_hp))
        print ("Your Health: " + str (player_hp))
    elif hit == 2:
         dragon_hp = dragon_hp - 2
         print ("You hit the dragon extra hard. It loses two points. ")
         print ("Dragon Health: " + str (dragon_hp))
         print ("Your Health: " + str (player_hp))
    else:
      print ("No luck. You miss.")
      print ("Dragon Health: " + str (dragon_hp))
      print ("Your Health: " + str (player_hp))
    if dragon_hp <= 0:
        print ("The dragon has taken too many hits. It sways, stumbles, and then falls to the ground. This is the end of the dragon's long life. Your sword is rusty and corroded from the dragon's blood, but you see piles and piles of gold that it's been hoarding for a long time. Not a bad trade. It's going to take you a while to move all this gold, but you're rich!")
        item = "a whole lot of gold"
        end_success(item)
    print ("The dragon's turn.")
    hit = random.randint (1, 5)
    if hit == 1:
        player_hp = player_hp - 1
        print ("The dragon hits you. You lose one point.")
        print ("Dragon Health: " + str (dragon_hp))
        print ("Your Health: " + str (player_hp))
    elif hit == 2:
        player_hp = player_hp - 1
        print ("The dragon hits you extra hard. You lose two points.")
        print ("Dragon Health: " + str (dragon_hp))
        print ("Your Health: " + str (player_hp))
    else:
      print ("The dragon misses.")
      print ("Dragon Health: " + str (dragon_hp))
      print ("Your health: " + str (player_hp))
    if player_hp <= 0:
        print ("You have taken too many hits. As you take your last breath, you see the dragon loom closer. Your adventure is over. Better luck next time!")
    else:
        next_move = input ("Do you want to stop or keep fighting? > ")
        if "keep" in next_move or "continue" in next_move:
          print ("Neither of you are dead (yet) so the fight continues.")
          dragon_fight()
        else:
          print ("'You cannot leave', the dragon growls. 'I will eat you.' Before you can react, you are in the dragon's mouth. Your adventure is over. Better luck next time.")
def red_door_from_hall(item):
    global dragon_hp
    global player_hp
    print ("You are in a room with a huge dragon. It glares at you angrily.")
    if item == "sword":
        next_move = input ("Do you want to fight it or return? > ")
        if "fight" in next_move:
            print ("You heft your sword, preparing to fight it in order to stay alive.")
            player_hp = 10
            dragon_hp = 20
            print ("The dragon has 20 hp and you have only 10 hp. However, you are faster and the odds are higher that you will hit it. Each round, you will try to hit the dragon. There is a 1/3 chance that it will loose 2 points, a 1/3 chance that it will loose 1 point, and a 1/3 chance that you will miss. Then the dragon will try to hit you. There is a 1/5 chance that you will lose 2 points, a 1/5 chance that you will lose 1 point, and a 3/5 chance that it will miss. Good luck!")
            dragon_fight()
        else:
            print ("'You cannot leave', the dragon growls. 'I will eat you.' Before you can react, you are in the dragon's mouth. Your adventure is over. Better luck next time.")
    elif item == "gold":
        print ("The dragon looks at your gold. It says, 'Give me your gold and you will live. Otherwise, I will eat you.'")
        next_move = input ("Do you give it the gold or keep it? > ")
        if "give" in next_move:
            end_success(item)
        else:
            print ("If you won't give up your gold, the dragon has no reason to let you live. It eats you. Your adventure is over. Better luck next time!")
    else:
        print ("With no sword and no gold, the dragon eats you. Your adventure is over. Better luck next time!")
def endless_hallway():
    print ("You step through the black door and see another hallway that seems to go on forever. Each door has a bag filled with gold in front of it.")
    next_move = input ("Do you want to go through one of the black doors (and get the treasure in front of it) or return? > ")
    if "go" in next_move:
        endless_hallway()
    else:
        print ("You realize that the hallway stretches on foreverin both directions. You can't be sure which one you went through. You will never be able to escape this endless maze. Your adventure is over. Better luck next time!")
def green_door(item):
    print ("You step through the green door. It leads to a hallway with doors on either side. The hallway seems to go on forever. Each door is black except for the door you came through, which is green. You also see a red door.")
    next_move = input ("Do you go through the red door, go through the first black door, or return through the green door? > ")
    if "red" in next_move:
        red_door_from_hall(item)
    elif "black" in next_move:
        endless_hallway()
    else:
      end_success(item)
def have_sword():
    item = "sword"
    print ("You have a sword; what do you want to do with it?")
    next_move = input ("Would you like to stop now or continue through the green door in front of you? > ")
    if "stop" in next_move:
        end_success(item)
    elif "continue" in next_move or "door" in next_move or "green" in next_move:
        green_door(item)
def have_gold():
    item = "gold"
    print ("You are now rich: this gold could keep you going for a lifetime! But you could find more riches ahead, and maybe a bigger bag to carry them.")
    next_move = input ("Do you stop now or continue through the green door in front of you? > ")
    if "stop" in next_move:
        end_success(item)
    elif "continue" in next_move or "green" in next_move or "door" in next_move:
        green_door(item)
def hide_from_guards():
    print ("You've made it this far, and you're not giving up now. The guards do a quick search of the room and don't find you. They leave. You open the chest and find a sword along with some gold. You can only carry one item with you.")
    next_move = input ("Do you want to take the sword or the gold? > ")
    if "sword" in next_move:
        print ("You grab the sword.")
        have_sword()
    elif "gold" in next_move:
        print ("You grab the gold.")
        have_gold()
    else:
        print ("You decide that you don't want a reward. Instad, you're going to escape the prison and live the rest of your life on the run. Your adventure is over. Good luck.")
def key_found():
    print ("You search in the corners of the room and find a key. Nothing can get past you! But just as you begin to unlock the chest, the door opens and guards rush in.")
    next_move = input ("Do you try to hide or stay where you are? > ")
    if "hide" in next_move:
        hide_from_guards()
    else:
        print ("It seems you have fallen out of favor with the king. He has revoked your status as knight. The guards take you to another part of the dungeon: the part where prisoners are kept. You will spend the rest of your days here. Sorry. Better luck next time.")
def find_key():
    print ("You decide to search for the key. It is not in plain sight, but you do see some corners where it could be hidden.")
    next_move = input ("Do you continue searching? y or n > ")
    if "y" in next_move:
        key_found()
    else:
        blue_room()
def break_chest():
    print ("You try to break the chest, but it is hard as stone. You feel a sharp pain in your hand and realize it's broken. You can't continue on in this state. Better luck next time.")
def red_room():
    print("You step into the red room. There stands a huge red dragon. It glares at you angrily.")
    next_move = input ("Do you go back to the previous room with your life or bravely stay? > ")
    if "go" in next_move:
        start_adventure()
    else: 
        print ("The dragon eats you. Your adventure is over. Better luck next time!")
def blue_room():
    print("You step into the blue room. You see a treasure chest but no key.")
    next_move = input ("Do you search for a key or try to break the chest open? > ")
    if "search" in next_move or "key" in next_move or "find" in next_move:
        find_key()
    elif "break" in next_move:
        break_chest()
    else:
        print ("If you can't make a simple decision, you are not ready for this quest. Better luck next time!")
def start_adventure():
    print("You are in a dungeon. You see two doors in front of you, a red door and a blue door.")
    next_move = input("Do you choose the red door or the blue door? > ")
    if "red" in next_move:
        red_room()
    elif "blue" in next_move:
        blue_room()
    else:
        print ("Sorry, it's red or blue. If you can't make this simple decision, you're not ready for this adventure. Better luck next time.")
def main(): 
    player_name = input("What is your name? It can be something random or silly if you want. Not necessarily your real name. > ")
    print("Welcome to the Dungeon Adventure Game! You are a knight named {}." . format(player_name))
    start_adventure()
main()

import time  # Imports a module to add a pause

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Grabbing objects
Gun = 0
sword = 0

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication


# T#dehe story is broken into sections, starting with "intro"
def intro():
    print("The year is 2020 New Years Eve, you are currently 4 hours from your home"
          "\nYou wake up with a killer headache and not the foggiest idea of where you. As it stands you are currently in "
          "\nyour car with no clothes on and only wearing boxers shorts with one pair of sock. To clear your mind you exit "
          "\nyour car. Moments later the tranquility  quickly fades and you hear a RRAAAUUUGGHHH sound emitting behind you."
          "\nA book-carrying amphibian swamp monster is running towards you. You will:")
    time.sleep(1)
    print("""  A. Grab a nearly log and throw it at the swamp monster
  B. Get back in your car and wait to be killed
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print("\nsigh, that was quick. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()

def option_rock():
    print("\nThe swamp monster laughed and begin "
          "running towards you again. Will you:")
    time.sleep(1)
    print("""  A. Run
  B. Throw another log
  C. Run towards a nearby abandoned church""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another log, as if the first "
              "log that was thrown did any damage. The log fell on the "
              "swamp monster's leg. You missed. \n\nYou died!")
    elif choice in answer_C:
        option_church()
    else:
        print(required)
        option_rock()

def option_church():
    print("\nYou were nervous, since the abandoned church was dark and "
          "ominous. Before you enter, you notice a rusty gun on "
          "the floor. Do you pick up a gun. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        gun = 1  # adds a sword
    else:
        gun = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Hide in closet
  B. Fight
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the closet? I think "
              "swamp monster can easily break the door, right? Not sure, but "
              "I'm going with YES, so...\n\nYou died!")
    elif choice in answer_B:
        if sword > 0:
            print("\nYou laid anxiously waiting. The rusty gun tightly held in your palm. "
                  "the swamp monster, which thought you were an easy snack, for the first time has doubt. As he walked "
                  "closer and closer, your heart beat steadily increase. As the swamp monster "
                  "with both hands stretches out the monster creep closer, you pull back the hammer "
                  "and unload all the clips at the monster. "
                  "chest. \n\nYou survived!")
        else:  # If the user didn't grab the gun
            print("\nYou should have picked up that gun. You're "
                  "defenseless. \n\nYou died!")
    elif choice in answer_C:
        print("As the swamp monster enters the abandoned church, you silently "
              "sneak out the back door. You're just several feet when the swamp monster turn around and see you "
              "running.")
        option_run()
    else:
        print(required)
        option_run()

def option_run():
    print("\nYou run as quickly as possible, but the swamp monster "
          "speed is too great. You will:")
    time.sleep(1)
    print("""  A. Hide behind boulder
  B. Trapped, fight for you life
  C. Run towards the dark cave""")
    choice = input(">>> ")
    if choice in answer_A:
        print("With a giant leap the monster was able to see you. "
              "\n\nHe killed you!")
    elif choice in answer_B:
        print("\nUsing his snake like tail he send you flying. You are no match for him. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_run()

def option_cave():
    print("\nWhile aimlessly running, you notice an antique "
          "sword shimmering in the mud. You quickly reach down and grab it, "
          "but missed. You quickly try to gather your thoughts as you hide "
          "behind a dismantle trench hole, waiting for the monster to come "
          "speeding through the corner. You notice a old book "
          "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        sword = 1
        book = 0
    print("You hear its sinister laugh, and you ready yourself for the"
          "the impending doom.")
    time.sleep(1)
    if book > 0:
        print("\nYou quickly hold out the old book, somehow "
              "hoping it will stop the orc. To your surprise it does! The orc was looking for  "
              "a book club friend. "
              "\n\nThis got weird, but you survived!")
    else:  # If the user did grab the sword
        print("\nMaybe you should have picked up the book. "
              "\n\nYou died!")

intro()

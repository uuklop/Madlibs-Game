condition = "yes"

# while loop will run until user enters anyother input aside yes or y
while (condition == 'yes' or condition == 'y'):

    # User inputs the various input for the madlib game
    adjective = input("Enter an adjective: ")
    second_adjective = input("Enter an adjective: ")
    bird_type = input("Name a bird type: ")
    room_in_house = input("Name a room in the house: ")
    pastVerb = input("Enter a verb that is in the past tense: ")
    verb = input("Enter a verb: ")
    relative_name = input("Enter a relative's name: ")
    noun = input("Enter a noun: ")
    liquid = input("Enter name of liquid: ")
    verb_ing = input("Enter a verb ending with ing: ")
    part_body = input("Enter any part of the body: ")
    plural_noun = input("Enter a plural Noun: ")
    sec_verb_ing = input("Enter a verb ending with ing: ")
    second_noun = input("Enter a noun: ")

    # The Madlib Template with string interpolation
    print(f"""\n\n
    ***************************************************************

    It was a {adjective}, cold Novemberday day. I
    woke up to the {second_adjective} smell of {bird_type} 
    roasting in the {room_in_house} downstairs. I {pastVerb} 
    down the stairs to see if I could help {verb} the dinner.
    My mun said, \"See if {relative_name} needs a fresh {noun}.\"
    So I carried a tray of glasses full of {liquid} into the {verb_ing} room.
    When I got there, I couldn't believe my {part_body}! There were 
    {plural_noun} {sec_verb_ing} on the {second_noun}!

    ***************************************************************
    """)

    print()
    replay = input("Do you want to play again (yes or no)? ") # User input determines whether the game should proceed or be terminated
    condition = replay

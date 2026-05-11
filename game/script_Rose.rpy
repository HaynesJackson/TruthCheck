# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start_Rose:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.


    me "Uhhhhh oh! I also found out about this cool organization! They work to help people like you, and I think that’s so so important. Especially nowadays, when it can be incredibly stigmatized. I know you’ve struggled with it a lot."

    f "What is it?"

    me "Right! It’s called Autism Speaks. It’s…"

    f "I…"

    me "Is something wrong?"

    "Abruptly, friend stands up and walks to a different room."

    me"Oh."

    meIt "Did I do something wrong?"


    return

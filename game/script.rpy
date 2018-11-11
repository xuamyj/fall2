# Declare characters used by this game.
define e = Character(_("Eileen"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

default numInsist = 3


# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene bg uni
    with fade

    "It's Saturday afternoon. You stumble out of your dorm into the crisp fall air."

    "Unlike you, Eileen is always on time."

    show eileen green normal
    with dissolve

    e "Hi my love! How was the pset?"

    m "Eh, it was alright."

    "The truth is that you only got 2 hours of sleep last night."

    "But if you told Eileen that, she probably would make you go to bed right away."

    m "Nevermind the pset. What about you, how's the game jam so far?"

    e "It's been really great! People seem to be enjoying it."

    m "Well, of course! You've been planning it for weeks."

    show eileen green giggle
    with dissolve

    e "Awh, thanks my love."

    e "I can't wait for you to come see it!"

    menu:

        "What do you do?"

        "Go with Eileen to her game jam!":

            jump gamejam

        "Admit that you're super sleep deprived.":

            jump giveup


label gamejam:

    m "Let's go right now!"

    scene bg lecturehall
    with fade

    "The game jam is being held in one of the newer classrooms on campus."

    "Most people are dispersed around the room in small groups, working on their laptops."

    "In the corner, there's a projector where someone is running a workshop."

    "Near the door is a table of tasty snacks: gatorade, clementines, chips, sandwich wraps."

    "There is also an entire loaf of bread."

    show eileen green smile
    with dissolve

    e "Welcome to the game jam!"

    m "Wow, Eileen, this is great! It's a really good vibe."

    e "Mmm, thanks my love!"

    m "You know, I haven't had that much time to write or even play games these days."

    m "This is actually kinda perfect..."

    m "...I'm going to make a game for your game jam!"

    show eileen green giggle
    with dissolve

    e "...!!"

    e "Really?"

    m "Yeah! I'm really excited."

    "It makes you very happy to see Eileen so happy."

    m "Oh yeah, I remember you talked about needing a theme for the game jam."

    m "Did you end up picking something?"

    show eileen green smile
    with dissolve

    e "Ah yeah, we did!"

    e "The theme is..."

    scene bg meadow
    with fade

    e "...fall!"

    scene black
    with dissolve

    "Hehe, the end."

    "{b}Good Ending{/b}."

    return



label giveup:

    m "Actually... I didn't sleep very much last night."

    show eileen green surprised
    with dissolve

    e "Oh no! You should get some sleep."

    m "But I want to come to your game jam..."

    e "I know. And I really appreciate it! But I want you to be well rested and healthy."

    m "I can be well rested and healthy tomorrow..."

    e "Wait, but don't you have meetings all day tomorrow?"

    jump insist





label insist:

    menu:

        "What do you do?"

        "Insist on going to the game jam." if numInsist > 0:

            $ numInsist -= 1

            jump pleasesleep

        "Give in and go to bed.":

            jump badending


label pleasesleep:

    m "I really, really want to go."

    e "And I really, really want you to stay healthy."

    m "You worked really hard on this game jam..."

    e "I promise, there will be more game jams my love! Please, sleep for me?"

    jump insist


label badending:

    scene black
    with dissolve

    "Upon Eileen's insistence, you go back to your dorm and take a nap."

    "She tucks you in and tells you how happy she is that you're taking care of yourself."

    "Still, deep inside you feel like you're a bit of a disappointment."

    "{b}Bad Ending{/b}."

    return


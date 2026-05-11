# The script of the game goes in this file.

define me = Character("Orange", who_color="DFA10F", what_color="FFDE90")
define meIt = Character("Orange", who_color="DFA10F", what_color="FFDE90", what_italic=True)
define f = Character("Greenish", who_color="5CC97D", what_color="BDFCD0")
# Declare characters used by this game. The color argument colorizes the
# name of the character.

#this number is to be manually changed depending on how many posts we have available.
#It should currently be the number of posts available in the game + 1.
default time = 6

define e = Character("maxwell")
define thing1 = ""
define name = ""
default phoneDown = False
default researchFlag = False
default newsIndex = 0
default post1_pos = False
default post1_neg = False
default post1_dig = False
default post2_pos = False
default post2_neg = False
default post2_dig = False
default post3_pos = False
default post3_neg = False
default post3_dig = False
default post4_pos = False
default post4_neg = False
default post4_dig = False
default post5_pos = False
default post5_neg = False
default post5_dig = False


# The game starts here. This is the Scrolling phase

label start:

    scene bglivingroom
    play music "main_theme_music.mp3"
    
    show oneutral:
        zoom 1.2
        yalign 0.7

    meIt "Sigh"
    me "It's another one of those nights."
    me "What's a good time waster? My friend should be here any minute. There isn't anything I can really do until then."
    me "Anything I do will probably just get interrupted."
    meIt "Well there's always..."

    menu:
        me "I mean..."

        "Social Media":
            jump post1
        "SOciaI MedIa":
            jump post1
        "S0ciaI Medla":
            jump post1
    

label post1: 
    scene bg_laptop

    show olaptop:
        xalign 0.2
        yalign 1.0 

    show twitter:
        zoom 1.5
        alpha 0.90
        xpos 0.5 ypos 0.0
        linear 1.0 xpos 0.5 ypos -0.0

    me "Hmm..."
    menu:
        me "Hmm..."

        "Sounds about right, keep scrolling.":
            jump post1_fine
        "Doesn't quite sound right, keep scrolling.":
            jump post1_iffy
        "Hmmmmm. Do some Digging on this.":
            jump post1_strange
        "Yeah, no. That's enough social media.":
            jump putphonedown
        
label post1_fine:
    # slight positive opinion of the first post, but not enough to do digging
    $ post1_pos = True
    $ newsIndex = newsIndex + 1
    me "Yeah, yeah."
    if newsIndex >= time:
        jump conversation
    jump post2

label post1_iffy:
    # slight negative opinion of the first post, but not enough to do digging
    $ post1_neg = True
    $ newsIndex = newsIndex + 1
    me "ehhhhhh."
    if newsIndex >= time:
        jump conversation    
    jump post2

label post1_strange:
    # fact checking the first post
    $ post1_dig = True
    $ newsIndex = newsIndex + 2
#researching takes extra time! So index ticks up by 2, not 1.
    me "Let's fact check this."
    #I need to create the fact-checking continueation part
    if newsIndex >= time:
        jump conversation
    jump post1_factcheck

label post1_factcheck:
    me "That seems… Hmm. I think I’m going to look into that a bit more."

    me "Deep fakes feels like just the tip of the iceberg. It feels weird to just… use someone else’s face to do things they wouldn’t do. Maybe I’m just overthinking it, and it is just a silly thing."

    me "Let’sssss start with a classic. Wikipedia article about deepfakes. https://en.wikipedia.org/wiki/Deepfake"

    me "Generative content using a person’s face… A whole bunch of terms I don’t really understand. Neural network, autoencoders, GANs."

    meIt "Oh."

    me "That’s… oh. Oh."

    me "96 percent? 96 percent is used for adult content? That can’t be right. What’s the source on that? https://regmedia.co.uk/2019/10/08/deepfake_report.pdf alright. That’s back in 2019. It has a footnote saying how the data was gathered."

    me "I don’t think I really… want to pursue that right now. I can table further research another time, but that is already incredibly disturbing. The implications make me sick. Politicians having plausible deniability for videos, the amount of child content, the uses for blackmail… Eugh."

    jump post2

label post2:
    show olaptop:
        xalign 0.2
        yalign 1.0  
        
    show twitter:
        zoom 1.5
        alpha 0.90
        xpos 0.5 ypos -0.0
        linear 1.0 xpos 0.5 ypos -0.7

    me "Next post."
    menu:
        "Another serrious topic. Eugh."
        "Sounds about right, keep scrolling.":
            jump post2_fine
        "Doesn't quite sound right, keep scrolling.":
            jump post2_iffy
        "Hmmmmm. Do some Digging on this.":
            jump post2_strange
        "Yeah, no. That's enough social media.":
            jump putphonedown

label post2_fine:
    # slight positive opinion of the second post, but not enough to do digging
    $ post2_pos = True
    $ newsIndex = newsIndex + 1
    me "Yeah, yeah."
    jump post3

label post2_iffy:
    # slight negative opinion of the second post, but not enough to do digging
    $ post2_neg = True
    $ newsIndex = newsIndex + 1
    me "ehhhhhh."
    jump post3

label post2_strange:
    # fact checking the second post
    $ post2_dig = True
    $ newsIndex = newsIndex + 2
#researching takes extra time! So index ticks up by 2, not 1.
    me "Let's fact check this."
    #I need to create the fact-checking continueation part
    if newsIndex >= time:
        jump conversation
    jump post2_factcheck

label post2_factcheck:
    me "This is the factchecking section for post 2"
    jump post3

label post3:
    show olaptop:
        xalign 0.2
        yalign 1.0  
        
    show twitter:
        zoom 1.5
        alpha 0.90
        xpos 0.5 ypos -0.7
        linear 1.0 xpos 0.5 ypos -1.1

    me "What's up next?"
    menu:
        "Another serrious topic. Eugh."
        "Sounds about right, keep scrolling.":
            jump post3_fine
        "Doesn't quite sound right, keep scrolling.":
            jump post3_iffy
        "Hmmmmm. Do some Digging on this.":
            jump post3_strange
        "Yeah, no. That's enough social media.":
            jump putphonedown

label post3_fine:
    # slight positive opinion of the second post, but not enough to do digging
    $ post3_pos = True
    $ newsIndex = newsIndex + 1
    me "Yeah, yeah."
    jump post4

label post3_iffy:
    # slight negative opinion of the second post, but not enough to do digging
    $ post3_neg = True
    $ newsIndex = newsIndex + 1
    me "ehhhhhh."
    jump post4

label post3_strange:
    # fact checking the second post
    $ post3_dig = True
    $ newsIndex = newsIndex + 2
#researching takes extra time! So index ticks up by 2, not 1.
    me "Let's fact check this."
    #I need to create the fact-checking continueation part
    if newsIndex >= time:
        jump conversation
    jump post3_factcheck

label post3_factcheck:
    me "This is the factchecking section for post 3"
    jump post4

label post4:
    show olaptop:
        xalign 0.2
        yalign 1.0  
        
    show twitter:
        zoom 1.5
        alpha 0.90
        xpos 0.5 ypos -1.3
        linear 1.0 xpos 0.5 ypos -2.0

    me "And another one goes, and another one goes, and another one bites the dust."
    menu:
        "Another serrious topic. Eugh."
        "Sounds about right, keep scrolling.":
            jump post4_fine
        "Doesn't quite sound right, keep scrolling.":
            jump post4_iffy
        "Hmmmmm. Do some Digging on this.":
            jump post4_strange
        "Yeah, no. That's enough social media.":
            jump putphonedown

label post4_fine:
    # slight positive opinion of the second post, but not enough to do digging
    $ post4_pos = True
    $ newsIndex = newsIndex + 1
    me "Yeah, yeah."
    jump post5

label post4_iffy:
    # slight negative opinion of the second post, but not enough to do digging
    $ post4_neg = True
    $ newsIndex = newsIndex + 1
    me "ehhhhhh."
    jump post5

label post4_strange:
    # fact checking the second post
    $ post4_dig = True
    $ newsIndex = newsIndex + 2
#researching takes extra time! So index ticks up by 2, not 1.
    me "Let's fact check this."
    #I need to create the fact-checking continueation part
    if newsIndex >= time:
        jump conversation
    jump post4_factcheck

label post4_factcheck:
    me "This is the factchecking label section"
    jump post5

label post5:
    show olaptop:
        xalign 0.2
        yalign 1.0  
        
    show twitter:
        zoom 1.5
        alpha 0.90
        xpos 0.5 ypos -2.0
        linear 1.0 xpos 0.5 ypos -3.4

    me "Hmm..."
    menu:
        "Another serrious topic. Eugh."
        "Sounds about right, keep scrolling.":
            jump post5_fine
        "Doesn't quite sound right, keep scrolling.":
            jump post5_iffy
        "Hmmmmm. Do some Digging on this.":
            jump post5_strange
        "Yeah, no. That's enough social media.":
            jump putphonedown

label post5_fine:
    # slight positive opinion of the second post, but not enough to do digging
    $ post5_pos = True
    $ newsIndex = newsIndex + 1
    me "Yeah, yeah."
#-------------------------------------------------------change this if post #6-------------------------------------------------------
    jump conversation
#-------------------------------------------------------change this if post #6-------------------------------------------------------

label post5_iffy:
    # slight negative opinion of the second post, but not enough to do digging
    $ post5_neg = True
    $ newsIndex = newsIndex + 1
    me "ehhhhhh."
    if newsIndex >= time:
        jump conversation
#-------------------------------------------------------change this if post #6-------------------------------------------------------
    jump conversation
#-------------------------------------------------------change this if post #6-------------------------------------------------------

label post5_strange:
    # fact checking the second post
    $ post5_dig = True
    $ newsIndex = newsIndex + 2
#researching takes extra time! So index ticks up by 2, not 1.
    meIt "This seems... extreme. Surely it's not that bad."

    me "I'm going to check that out a little more, I need to know how to tell it really is safe."

    me "let's look at the Missouri Poison Center, Mushroom Hunting Safety." 
    me "Mushrooms are mushrooms, doesn't matter where they are."

    meIt "Well, it says ‘NEVER pick and eat wild mushrooms unless they’ve been identified by an expert" 
    meIt "And now, I can't really tell who is an expert and who is a fabrication."

    #I need to create the fact-checking continueation part
    if newsIndex >= time:
        jump conversation
#-------------------------------------------------------change this if post #6-------------------------------------------------------
    jump post5_factcheck
#-------------------------------------------------------change this if post #6-------------------------------------------------------

label post5_factcheck:
    me "This is the factchecking label section"
    jump putphonedown

#This is transitioning into the Conversation Phase

label putphonedown:
    me "Yup yup yup. I can't deal with more of... that."
    meIt "sigh."
    $ phoneDown = True
    # put the phone down
    jump conversation

label conversation:

    scene bglivingroom
    show ohappy
    show gexcited

    f "yo yo yo! What is up my favorite funky fiend? How you doing [name]?"
    me "Hi!! Been waiting for you for too long. Come sit down! I\'m doing pretty well. You?"
    f "Yeah, same here. What's new with you?"
    if post2_dig: # taxes
        me "I'm excited to get promoted soon!" # or me "I need to take my dog to the vet soon for a flea treatment. Anyway, how's work been?"
    else:
        me "debating whether or not to take this promotion at work. I\'m not sure if it\'ll put me in the next tax bracket or not, and then I\'ll be making less money. Eugh."
        # or me "I'm excited to try some of these new home flea treatments! Anyway, how's work been?"
    f "gah, work. Don't even get me started on that."
    me "Oh?"
    f "Yea! I love love love not being able to feel safe existing as myself at work." 
    f "I came out of the closet last week, and everyone's been acting super super weird. It's like I'm some sort of animal or a predator. Why can\'t people just be Normal."
    if post4_dig: # lgbtqia+ rights
        me "Just be careful, alright? There\'s been a rise in anti-trans laws and hate crimes."
        me "As awful as it feels, it might be safer to pretend you changed your mind, at least until you can get a different job."
        f "I\'m sure you\'re just overreacting. It\'s not like they can do anything about it anyway, even if they do think I\'m delusional or something."
        me "Hate crimes being illegal doesn\'t mean people won\'t do it. Being out of the closet still isn\'t safe in a lot of places, and once something is said you can\'t take it back."
    else:
        me "I\'m sure it\'s just your anxiety talking. It\'s 2023, and this is a progressive state."
        me "Who cares about what\'s in your pants in this day and age? Just be yourself. If they don\'t like it, they can go away."
    f "yeah, I guess you\'re right. I don\'t want to think about it right now."
    me "Fair, yea. Ummm - I\'ve been craving mushrooms so so bad lately. I keep seeing those videos of people making a challenge of gathering all of their food for the winter."
    f "Oh! That reminds me, I found this foraging book online! I could totally print out the file and we could go see if we can find those mushrooms together!"
    if post5_dig: # mushrooooooooms
        me "Where\'d you find that foraging book?"
        f "Off of Mamaxon or something."
        me "Have you double checked the author?"
        f "No?"
        me "We should probably do that then. There\'s a problem with AI generated foraging books giving wrong information."
        f "Oh damn, I didn\'t know about that."
    else:
        me "Aw hell yea! I\'ve got a printer in the other room, let\'s do this."
        f "Niiiiice. I\'ll have to bring my laptop next time I visit!"
        me "Is it on cloud storage, is it free to find on the internet, or is it on your computer storage?"
        f "It\'s not exactly freeee on the internet, but I have my ways."
    meIt "Glancing at my phone, I see the deepfake ad again."
    if post1_dig: # oh god
        meIt "It\'s horrifying, what it\'s being used for. It gives me chills, and I block the ad."
    else:
        meIt "It\'s just so… easy. What would be the harm of just doing something silly, out of curiosity?" 
        meIt "It\'s not like I\'d share it, or do anything bad with it. It\'d be funny to make a politician do a hortnite dance or something."
    f "Hello?"
    me "Huh?"
    f "I just asked what your favorite mushroom was. What\'s got you distracted?"
    me "Oh I was just..."
    menu: 
        meIt "I don\'t want to say anything about the advertisement"

        "Thinking more about your workplace":
            jump workplace
        "taxes":
            jump taxes
        "My favorite mushrooms, haha. Too busy thinking about them to listen to you asking about them.":
            jump mushrooms
label workplace:
    if post4_dig:
        me "I just worry about you."
        f "I guess."
    else:
        me "You shouldn\'t let some naysayers squash you."
        f "You're right."
    f "I'll think more about it later."
    jump continue_conversation

label taxes:
    f "Gross. Anything else in that brain of yours?" # could think of can be found.
    jump continue_conversation

label mushrooms:
    me "My favorite mushrooms, haha. Too busy thinking about them to listen to you asking about them."
    menu:
        me "My favorite mushroom is..."
        "the Fly agaric mushroom":
            pass
        "the Oyster mushroom":
            pass
        "the Giant Puffball":
            pass
    f "Niceee. Those are good"
    jump continue_conversation

label continue_conversation:
    if post3_dig:
        me "Can I ask you a weird question...?"

        f "Depends on what it is."

        me "Have you heard of Autism Speaks?"

        f "Why.....?"

        me "I saw something about it today. The webpage makes it sound like a really amazing program and opportunity, to help people like you." 

        me "But a lot of the people that it’s meant to help really really hate it. So ah - I was just wondering where your opinions are on it."
    
    else:
        me "Uhhhhh oh! I also found out about this cool organization! They work to help people like you, and I think that’s so so important. Especially nowadays, when it can be incredibly stigmatized. I know you’ve struggled with it a lot."

        f "What is it?"

        me "Right! It’s called Autism Speaks. It’s…"

        show guncertain_down
        f "I…"

        me "Is something wrong?"

        "Abruptly, greenish stands up and walks to a different room."

        me "Oh."

        meIt "Did I do something wrong?"

        jump ending_logic
    jump ending_logic

label ending_logic:

    if post5_dig == False:
        jump mushroom_ending

label mushroom_ending:

    scene bg_forest
    show ohappy
    show gexcited

    me "wow there's so many mushrooms! I'm not sure which one to eat"

    f "me neither, they all look so tasty"

    me "I think this mushroom looks good, I'm going to try it"

    f "Okay I'll try this other one!"

    "hey, did you think that foraging guide was really legit? It seemed a little misleading."

    f "it probably was but how harmful could a little mushroom be?"

    me "that's true…"

    f "plus, they're so common, it wouldn’t make sense for them to be harmful at all"

    me "yeah but how can we know that what your saying, and the article for that matter, is displaying the correct information"

    f "well, you can sit there wondering. I’m going to try this thing out"

    me "fine, I guess I will too"

    "both become very sick, greenish passes out"

    me "Hey, hey, are you okay? Greenish? Greenish?"

    "The wait for an ambulance feels like years passing in the blink of an eye."

    return

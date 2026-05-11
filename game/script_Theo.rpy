# # The script of the game goes in this file.

# $ name = renpy.input("what do you prefer to be called?")

# define me = Character("[name]", who_color="DFA10F", what_color="FFDE90")
# define meIt = Character("[name]", who_color="DFA10F", what_color="FFDE90", what_italic=True)
# define f = Character("Friend", who_color="5CC97D", what_color="BDFCD0")
# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# #this number is to be manually changed depending on how many posts we have available.
# #It should currently be the number of posts available in the game + 1.
# default time = 6

# define e = Character("maxwell")
# define thing1 = ""
# define name = ""
# default phoneDown = False
# default researchFlag = False
# default newsIndex = 0
# default post1_pos = False
# default post1_neg = False
# default post1_dig = False
# default post2_pos = False
# default post2_neg = False
# default post2_dig = False
# default post3_pos = False
# default post3_neg = False
# default post3_dig = False
# default post4_pos = False
# default post4_neg = False
# default post4_dig = False
# default post5_pos = False
# default post5_neg = False
# default post5_dig = False


# # The game starts here. This is the Scrolling phase

# label start:

#     scene bg_livingroom
#     play music "main_theme_music.mp3"
    
#     show placeholder_man:
#         xalign 0.5
#         yalign 1.0
#         zoom 2.0

#     meIt "Sigh"
#     me "It's another one of those nights."
#     me "What's a good time waster? My friend should be here any minute. There isn't anything I can really do until then."
#     me "Anything I do will probably just get interrupted."
#     meIt "Well there's always..."

#     menu:
#         me "I mean..."

#         "Social Media":
#             jump post1
#         "SOciaI MedIa":
#             jump post1
#         "S0ciaI Medla":
#             jump post1
    

# label post1: 
#     scene bg_laptop

#     show placeholder_man:
#         xalign 0.2
#         yalign 1.0  
#         zoom 2.0

#     show placeholder_scroll:
#         alpha 0.69
#         xanchor 0.5 yanchor 0.0
#         xpos 0.5 ypos 0.0
#         linear 1.0 xpos 0.5 ypos -0.2

#     menu:
#         me "Hmm..."

#         "Sounds about right, keep scrolling.":
#             jump post1_fine
#         "Doesn't quite sound right, keep scrolling.":
#             jump post1_iffy
#         "Hmmmmm. Do some Digging on this.":
#             jump post1_strange
#         "Yeah, no. That's enough social media.":
#             jump putphonedown
        
# label post1_fine:
#     # slight positive opinion of the first post, but not enough to do digging
#     $ post1_pos = True
#     $ newsIndex = newsIndex + 1
#     me "Yeah, yeah."
#     if newsIndex >= time:
#         jump conversation
#     jump post2

# label post1_iffy:
#     # slight negative opinion of the first post, but not enough to do digging
#     $ post1_neg = True
#     $ newsIndex = newsIndex + 1
#     me "ehhhhhh."
#     if newsIndex >= time:
#         jump conversation    
#     jump post2

# label post1_strange:
#     # fact checking the first post
#     $ post1_dig = True
#     $ newsIndex = newsIndex + 2
# #researching takes extra time! So index ticks up by 2, not 1.
#     me "Let's fact check this."
#     #I need to create the fact-checking continueation part
#     if newsIndex >= time:
#         jump conversation
#     jump post1_factcheck

# label post1_factcheck:
#     me "Huh, apparently all these \"mushroom foraging books\" are made by AI."
#     me "I should keep that in mind for when my friend comes over."
#     jump post2

# label post2:
#     show placeholder_man:
#         xalign 0.2
#         yalign 1.0  
#         zoom 2.0
        
#     show placeholder_scroll:
#         alpha 0.75
#         xanchor 0.5 yanchor 0.0
#         xpos 0.5 ypos -0.2
#         linear 1.0 xpos 0.5 ypos -0.5
#     menu:
#         "Another serrious topic. Eugh."
#         "Sounds about right, keep scrolling.":
#             jump post2_fine
#         "Doesn't quite sound right, keep scrolling.":
#             jump post2_iffy
#         "Hmmmmm. Do some Digging on this.":
#             jump post2_strange
#         "Yeah, no. That's enough social media.":
#             jump putphonedown

# label post2_fine:
#     # slight positive opinion of the second post, but not enough to do digging
#     $ post2_pos = True
#     $ newsIndex = newsIndex + 1
#     me "Yeah, yeah."
#     jump post3

# label post2_iffy:
#     # slight negative opinion of the second post, but not enough to do digging
#     $ post2_neg = True
#     $ newsIndex = newsIndex + 1
#     me "ehhhhhh."
#     jump post3

# label post2_strange:
#     # fact checking the second post
#     $ post2_dig = True
#     $ newsIndex = newsIndex + 2
# #researching takes extra time! So index ticks up by 2, not 1.
#     me "Let's fact check this."
#     #I need to create the fact-checking continueation part
#     if newsIndex >= time:
#         jump conversation
#     jump post2_factcheck

# label post2_factcheck:
#     me ""
#     jump post3

# label post3:
#     show placeholder_man:
#         xalign 0.2
#         yalign 1.0  
#         zoom 2.0
        
#     show placeholder_scroll:
#         alpha 0.75
#         xanchor 0.5 yanchor 0.0
#         xpos 0.5 ypos -0.5
#         linear 1.0 xpos 0.5 ypos -0.8
#     menu:
#         "Another serrious topic. Eugh."
#         "Sounds about right, keep scrolling.":
#             jump post3_fine
#         "Doesn't quite sound right, keep scrolling.":
#             jump post3_iffy
#         "Hmmmmm. Do some Digging on this.":
#             jump post3_strange
#         "Yeah, no. That's enough social media.":
#             jump putphonedown

# label post3_fine:
#     # slight positive opinion of the second post, but not enough to do digging
#     $ post3_pos = True
#     $ newsIndex = newsIndex + 1
#     me "Yeah, yeah."
#     jump post4

# label post3_iffy:
#     # slight negative opinion of the second post, but not enough to do digging
#     $ post3_neg = True
#     $ newsIndex = newsIndex + 1
#     me "ehhhhhh."
#     jump post4

# label post3_strange:
#     # fact checking the second post
#     $ post3_dig = True
#     $ newsIndex = newsIndex + 2
# #researching takes extra time! So index ticks up by 2, not 1.
#     me "Let's fact check this."
#     #I need to create the fact-checking continueation part
#     if newsIndex >= time:
#         jump conversation
#     jump post3_factcheck

# label post3_factcheck:
#     me "This is the factchecking label section"
#     jump post4

# label post4:
#     show placeholder_man:
#         xalign 0.2
#         yalign 1.0  
#         zoom 2.0
        
#     show placeholder_scroll:
#         alpha 0.75
#         xanchor 0.5 yanchor 0.0
#         xpos 0.5 ypos -0.2
#         linear 1.0 xpos 0.5 ypos -0.5
#     menu:
#         "Another serrious topic. Eugh."
#         "Sounds about right, keep scrolling.":
#             jump post4_fine
#         "Doesn't quite sound right, keep scrolling.":
#             jump post4_iffy
#         "Hmmmmm. Do some Digging on this.":
#             jump post4_strange
#         "Yeah, no. That's enough social media.":
#             jump putphonedown

# label post4_fine:
#     # slight positive opinion of the second post, but not enough to do digging
#     $ post4_pos = True
#     $ newsIndex = newsIndex + 1
#     me "Yeah, yeah."
#     jump post5

# label post4_iffy:
#     # slight negative opinion of the second post, but not enough to do digging
#     $ post4_neg = True
#     $ newsIndex = newsIndex + 1
#     me "ehhhhhh."
#     jump post5

# label post4_strange:
#     # fact checking the second post
#     $ post4_dig = True
#     $ newsIndex = newsIndex + 2
# #researching takes extra time! So index ticks up by 2, not 1.
#     me "Let's fact check this."
#     #I need to create the fact-checking continueation part
#     if newsIndex >= time:
#         jump conversation
#     jump post4_factcheck

# label post4_factcheck:
#     me "This is the factchecking label section"
#     jump post5

# label post5:
#     show placeholder_man:
#         xalign 0.2
#         yalign 1.0  
#         zoom 2.0
        
#     show placeholder_scroll:
#         alpha 0.75
#         xanchor 0.5 yanchor 0.0
#         xpos 0.5 ypos -0.8
#         linear 1.0 xpos 0.5 ypos -1.0
#     menu:
#         "Another serrious topic. Eugh."
#         "Sounds about right, keep scrolling.":
#             jump post5_fine
#         "Doesn't quite sound right, keep scrolling.":
#             jump post5_iffy
#         "Hmmmmm. Do some Digging on this.":
#             jump post5_strange
#         "Yeah, no. That's enough social media.":
#             jump putphonedown

# label post5_fine:
#     # slight positive opinion of the second post, but not enough to do digging
#     $ post5_pos = True
#     $ newsIndex = newsIndex + 1
#     me "Yeah, yeah."
# #-------------------------------------------------------change this if post #6-------------------------------------------------------
#     jump conversation
# #-------------------------------------------------------change this if post #6-------------------------------------------------------

# label post5_iffy:
#     # slight negative opinion of the second post, but not enough to do digging
#     $ post5_neg = True
#     $ newsIndex = newsIndex + 1
#     me "ehhhhhh."
#     if newsIndex >= time:
#         jump conversation
# #-------------------------------------------------------change this if post #6-------------------------------------------------------
#     jump conversation
# #-------------------------------------------------------change this if post #6-------------------------------------------------------

# label post5_strange:
#     # fact checking the second post
#     $ post5_dig = True
#     $ newsIndex = newsIndex + 2
# #researching takes extra time! So index ticks up by 2, not 1.
#     me "Let's fact check this."
#     #I need to create the fact-checking continueation part
#     if newsIndex >= time:
#         jump conversation
# #-------------------------------------------------------change this if post #6-------------------------------------------------------
#     jump post5_factcheck
# #-------------------------------------------------------change this if post #6-------------------------------------------------------

# label post5_factcheck:
#     me "This is the factchecking label section"
#     jump putphonedown

# #This is transitioning into the Conversation Phase

# label putphonedown:
#     me "Yup yup yup. I can't deal with more of... that."
#     meIt "sigh."
#     $ phoneDown = True
#     # put the phone down
#     jump conversation

# label conversation:

#     show placeholder_friend_point:
#         xalign 0.75
#         yalign 0.5

#     f "yo yo yo! What is up my favorite funky fiend? How you doing [name]?"
#     me "Hi!! Been waiting for you for too long. Come sit down! I\'m doing pretty well. You?"
#     f "Yeah, same here. What's new with you?"
#     if post2_dig: # taxes
#         me "I'm excited to get promoted soon!" # or me "I need to take my dog to the vet soon for a flea treatment. Anyway, how's work been?"
#     else:
#         me "debating whether or not to take this promotion at work. I\'m not sure if it\'ll put me in the next tax bracket or not, and then I\'ll be making less money. Eugh."
#         # or me "I'm excited to try some of these new home flea treatments! Anyway, how's work been?"
#     f "gah, work. Don't even get me started on that."
#     me "Oh?"
#     f "Yea! I love love love not being able to feel safe existing as myself at work." 
#     f "I came out of the closet last week, and everyone's been acting super super weird. It's like I'm some sort of animal or a predator. Why can\'t people just be Normal."
#     if post4_dig: # lgbtqia+ rights
#         me "Just be careful, alright? There\'s been a rise in anti-trans laws and hate crimes."
#         me "As awful as it feels, it might be safer to pretend you changed your mind, at least until you can get a different job."
#         f "I\'m sure you\'re just overreacting. It\'s not like they can do anything about it anyway, even if they do think I\'m delusional or something."
#         me "Hate crimes being illegal doesn\'t mean people won\'t do it. Being out of the closet still isn\'t safe in a lot of places, and once something is said you can\'t take it back."
#     else:
#         me "I\'m sure it\'s just your anxiety talking. It\'s 2023, and this is a progressive state."
#         me "Who cares about what\'s in your pants in this day and age? Just be yourself. If they don\'t like it, they can go away."
#     f "yeah, I guess you\'re right. I don\'t want to think about it right now."
#     me "Fair, yea. Ummm - I\'ve been craving mushrooms so so bad lately. I keep seeing those videos of people making a challenge of gathering all of their food for the winter."
#     f "Oh! That reminds me, I found this foraging book online! I could totally print out the file and we could go see if we can find those mushrooms together!"
#     if post5_dig: # mushrooooooooms
#         me "Where\'d you find that foraging book?"
#         f "Off of Mamaxon or something."
#         me "Have you double checked the author?"
#         f "No?"
#         me "We should probably do that then. There\'s a problem with AI generated foraging books giving wrong information."
#         f "Oh damn, I didn\'t know about that."
#     else:
#         me "Aw hell yea! I\'ve got a printer in the other room, let\'s do this."
#         f "Niiiiice. I\'ll have to bring my laptop next time I visit!"
#         me "Is it on cloud storage, is it free to find on the internet, or is it on your computer storage?"
#         f "It\'s not exactly freeee on the internet, but I have my ways."
#     meIt "Glancing at my phone, I see the deepfake ad again."
#     if post1_dig: # oh god
#         meIt "It\'s horrifying, what it\'s being used for. It gives me chills, and I block the ad."
#     else:
#         meIt "It\'s just so… easy. What would be the harm of just doing something silly, out of curiosity?" 
#         meIt "It\'s not like I\'d share it, or do anything bad with it. It\'d be funny to make a politician do a hortnite dance or something."
#     f "Hello?"
#     me "Huh?"
#     f "I just asked what your favorite mushroom was. What\'s got you distracted?"
#     me "Oh I was just..."
#     menu: 
#         meIt "I don\'t want to say anything about the advertisement"

#         "Thinking more about your workplace":
#             jump workplace
#         "taxes":
#             jump taxes
#         "My favorite mushrooms, haha. Too busy thinking about them to listen to you asking about them.":
#             jump mushrooms
# label workplace:
#     if post4_dig:
#         me "I just worry about you."
#         f "I guess."
#     else:
#         me "You shouldn\'t let some naysayers squash you."
#         f "You're right."
#     f "I'll think more about it later."
# label taxes:
#     f "Gross. Anything else in that brain of yours?" # could think of can be found.
# label mushrooms:
#     me "My favorite mushrooms, haha. Too busy thinking about them to listen to you asking about them."
#     menu:
#         me "My favorite mushroom is..."
#         "the Fly agaric mushroom":
#             # do nothing
#         "the Oyster mushroom":
#             # again, do nothing
#         "the Giant Puffball":
#             # this boring you yet?
#     f "Niceee. Those are good"
#     if post3_dig:
#         me "Can I ask you a weird question...?"
#         f "Depends on what it is."
#         me "Have you heard of Autism Speaks?"
#         f "Why.....?"
#         me "I saw something about it today. The webpage makes it sound like a really amazing program and opportunity, to help people like you." 
#         me "But a lot of the people that it’s meant to help really really hate it. So ah - I was just wondering where your opinions are on it."

#     # $ newsIndex = newsIndex + 1
#     # # this just skips the rest of the actions

#     # if newsIndex == 0 and researchFlag == False and phoneDown == False:
#     #     $ print("funny")
#     #     me "the funny"
#     #     # wait 0.5
#     # elif newsIndex == 1 and researchFlag and phoneDown == False:
#     #     $ print("funnier")
#     #     me "much funnier"
#     # elif newsIndex == 2 and researchFlag == False and phoneDown:
#     #     $ print("funniest")
#     #     me "super funny"
#     # elif newsIndex == 3 and researchFlag and phoneDown:
#     #     $ print("funniester")
#     #     me "obscenely funny"
#     # elif newsIndex == 4 and researchFlag and phoneDown == False:
#     #     $ print("funniesterestiest")
#     #     me "AAAAAAAAAAAAAAAA"
#     # else:
#     #     me "not funny, didn't laugh"
#     #     $ print("no")

#     # if phoneDown == False and newsIndex < 5:
#     #     me "i exist!!!"
#     #     $ print("existence")
#     #     # wait 0.5
#     #     return

    
#     return

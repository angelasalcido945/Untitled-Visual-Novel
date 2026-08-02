#To-Do:
#   1. figure out how to have mouth close default when a char isn't speaking + multiple expressions
#       (a)open when roll back
#       (b)show_henry label
#       (c)make a case where if the chars dialogue is "..."  and any dialogue in () for char thoughts their mouth stays closed
#           idea 1: hide open mouth and just have it show the closed mouth corrisponding to the mood next to the dialog

#transformations
transform henry_pos:
    zoom 0.22
    xalign 0.0
    yalign 0.2

#make t transform pos here
#transform thomas_pos:

#call back functions for speaking
init python:
    def mouth_callback(event, **kwargs):
        # .get retrieves the char object and .name checks the char name
        # if char is not speaking then exit 
        if kwargs.get("who") and kwargs["who"].name != "Henry": 
            return

        #fetches global value h_mood ("normal", "upset", etc.) if not set then default = "normal"
        #value that will be used to define expressions 
        mood = globals().get("h_mood", "normal")    

        if event == "begin":    #if a char starts speaking

            # Check the mood and show the correct open mouth for that mood

            #if exp is normal show normal open mouth
            if mood == "normal":
                renpy.show("henry_mouth_normal_open", tag="henry_mouth", at_list=[henry_pos], zorder=10)

            #if exp is upset show upset open mouth
            elif mood == "upset":
                renpy.show("henry_mouth_upset_open", tag="henry_mouth", at_list=[henry_pos], zorder=10)
            
            #if exp is looking down sad then normal mouth open
            elif mood == "lookDownSad":
                renpy.show("henry_mouth_normal_open", tag="henry_mouth", at_list=[henry_pos], zorder=10)

        elif event in ("slow_done", "end"): #else char finishes speaking/stops speaking

            # Show the closed mouth depending on the mood

            # if exp normal and finsihes show normal mouth
            if mood == "normal":
                renpy.show("henry_mouth_normal", tag="henry_mouth", at_list=[henry_pos], zorder=10)
            
            # if exp upset and finishes show upset mouth
            elif mood == "upset":
                renpy.show("henry_mouth_upset", tag="henry_mouth", at_list=[henry_pos], zorder=10)
            
            # if exp is look down sad and finishes show normal mouth 
            elif mood == "lookDownSad":
                renpy.show("henry_mouth_normal", tag="henry_mouth", at_list=[henry_pos], zorder=10)


# Declare characters here 

define h = Character("Henry", callback=mouth_callback, who="h")
define t = Character("Thomas")
define mrj = Character("Mr. Jackson")
define msj = Character("Mrs. Jackson")
define mrt = Character("Mr. Thompson")
define mst = Character("Mrs. Thompson")

label show_henry:
    # Show body
    show henry_body at henry_pos

    python:
        # Show face based on mood
        if h_mood == "normal":
            renpy.show("henry_normal", at_list=[henry_pos], tag="henry_face")
            renpy.show("henry_mouth_normal", at_list=[henry_pos], tag="henry_mouth", zorder=10)  
        elif h_mood == "upset":
            renpy.show("henry_upset", at_list=[henry_pos], tag="henry_face")
            renpy.show("henry_mouth_upset", at_list=[henry_pos], tag="henry_mouth", zorder=10)
        # add more moods here
        elif h_mood == "lookDownSad":
            renpy.show("henry_look_down_sad", at_list=[henry_pos], tag="henry_face")
            renpy.show("henry_mouth_normal", at_list=[henry_pos], tag="henry_mouth", zorder=10)

    return


# The game starts here.

label start:

    # Fancy home bg for Henry
    scene dbg
    with Dissolve(1.0)

    #show Henry upset 
    $ h_mood = "upset"  # what mood char is 
    call show_henry

    #show Henry's paraents (on the right)
    mrj "Henry, you have to take this seriously!"

    msj "Henry, son. Think about this more rationally. The business will need you."

    h "Father, Mother, I don’t want that sort of life!"

    #show henry look down upset speaking
    $ h_mood = "lookDownSad"
    call show_henry

    #add a bit more dialogue here

    h "You guys wouldn’t understand… What this life has already done to me…"

    #fades to black 
    scene black with Dissolve(0.5)
    
    #walking sounds

    #door slams 

    #screen shakes
    "*Slam!!!*" with hpunch 

    #Transition to Thomas' home
    scene dbg with Dissolve(.5)

    #show Thomas upset speaking (right)
    show dThomas:
        zoom 0.65
        xalign 1.0
        yalign 0.40

    #show Thomas' parents (on the left)
    mrt "Son, what’s changed…? Why do you want to pursue this…?"

    t "Dad… this is what I want…"
    t "This can even benefit you guys too!"

    mst "Honey, we appreciate the thought, but focus on the farm…"

    t "Why can’t you guys listen to me…?"

    #fades to black
    scene black with Dissolve(0.5)

    #walking sounds + door closes 

    with Pause(0.5)
    
    #transitions to park bench bg
    scene dbg with Dissolve(.5)

    #Show Henry sigh
    show dHenry:
        zoom 0.65
        xalign 0.0
        yalign 0.40

    h "{i}Sigh{/i}"

    #show henry upset
    h "(I can't with them! I just wish they'd let me do what I want!)"

    #show h sigh
    h "(I needed to get out of there.)"

    #show h looking down w/ small smile
    h "(I haven’t been to this park since—)"

    #show h ?

    #foot steps fading in 

    "..."

    #sitting down bench noise

    #show t upset looking right with dissolve
    show dThomas with Dissolve(.5):
        zoom 0.65
        xalign 1.0
        yalign 0.40

    h "(Hm? Who…?)"

    #show t wide-eye t speaking
    t "Henry?!"

    #show wide-eye h speaking
    h "Thomas?!"

    h "(I haven’t seen him since—)"

    #show t happy speaking
    t "I haven’t seen you since we were kids!"

    #show h sweat-drop
    h "(It’s like he can read my mind.)"

    #show h base speaking
    h "How have you been, Thomas?"

    #show t freeze 
    t "Ah—"

    #show t sweat drop smile speaking
    t "Oh ya know— Just been taking care of the farm, as expected." 

    #show t normal speaking
    t "What about you, Henry?"

    #show h base speaking 
    h "I’ve been fine."

    #show h side-eye left w/ sweat drop
    #show t side-eye left w/ sweat drop

    #show t sawkward weat drop + speaking 
    t "I see."

    "..."

    scene dbg with Dissolve (.5)

    show dHenry with Dissolve(.5):
        zoom 0.65
        xalign 0.0
        yalign 0.40

    show dThomas with Dissolve(.5):
        zoom 0.65
        xalign 1.0
        yalign 0.40

    #show t clear thorugh + hand to mouth
    t "({i}clears throat{/i})"

    #show t shy smile sweat 
    t "I um– I remember I used to love playing on those swings."

    #show h sigh
    h "{i}Sigh{/i}"

    #show h normal
    h "You’d always try to swing as high as you could and jump off."
    h "It’d always lead to you either getting hurt or out right failing."

    #show t cheeks puffed out
    t "Well you’d ignore me when I’d ask to play tag, so the swings it was."

    #show h wide eyed + sweat drop 
    h "!!!"

    #show h side eye + pouting speaking mouth + ears are red 
    h "W-we were kids! Friends were and still aren’t my strong suite."

    #show t laughing 

    t "Pfft- Hahaha!"

    #show t normal

    t "Henry, it’s okay! You’re right, we were just awkward kids back then."

    #show t smile + eyebrows turned up
    t "Heh… I remember it took me a while to get you to warm up to me and actually play with me."
    t "It didn’t seem like you liked me very much at the beginning."

    #show h blank meme face 
    h "You were a loud kid."

    #show h normal + hint of blush 
    h "I thought you were going to be annoying at first. But you became tolerable the more you stuck around. You were quite persistent."

    #show t one eyebrow turned up + smirk + hint of blush
    t "“Were?” So I wasn’t annoying?"

    #show h tensed up shoulders + bluuuuush
    h "Y-you know what I mean!"

    #show h sigh
    h "{i}Sigh{/i}"

    #show h looking down + crooked smile
    h "Look. You weren’t annoying…"

    pause 0.5

    h "You were— nice."

    #show laughing t 
    t "Hahaha! Why’s your smile al’ crooked!"

    #show h brows furrowed 
    h "I’m not really used to it— is all…"
    h "Is it strange?"

    #show hm? t 
    t "Hmmm."

    #Scene 1 - smile close up scene!!!

    scene dScene with Dissolve (.5)

    "..."

    #T's responce + Henry's reaction
    scene dScene

    t "Your smile’s fine."

    scene dbg with Dissolve(.5) 

    #show h flushed 
    show dHenry with Dissolve(.5):
        zoom 0.65
        xalign 0.0
        yalign 0.40

    #show t smile
    show dThomas with Dissolve(.5):
        zoom 0.65
        xalign 1.0
        yalign 0.40

    "..."

    #show h clears throat shyly 
    h "{i}clears throat{/i}"
    #show h normal + blush + sweat drop
    h "T-Thanks, Thomas."
    h "(This guy is gonna kill me…)"

    #show t smile + speak
    t "Anytime!"

    #show t !
    t "!"

    #show t curious 
    t "By the way, Henry?"

    #show h ?
    h "Hm?"

    #show t curious
    t "I’ve been wonderin’."
    t "Dontcha have a busy schedule? Cause of your family?"
    t "I recently saw promos around the city when we visited to restock the markets."
    t "I hope I haven’t been keepin’ you."

    #show h !
    h "Oh! U-um, you really don’t have to concern yourself about that, Thomas…"

    #show h side eye + sweat drop 
    h "I’m um—"

    #show h look fw + sweat drop 
    h "I’m… I’m not planning to take part in any of that stuff with my family…"
    h "I haven’t in a while."

    #show t freeze
    t "Oh! I see…"

    #show t shy
    t "Well if you’re not, then can I ask…"
    t "Why?"

    #show h side eye + sweat
    h "I just hate having to act all prissy and care about reputation and business talk. I merely just don’t have a care for it. I’d prefer a simple life away from my family and this city…"

    #show h looking down sad
    h "You must think it’s stupid, Thomas."
    h "I know I could probably do whatever I’d like if I just went along with what my Father has to say…"

    #show t ! + broows furrowed upset*mad
    t "Of course not!"
    t "If that life and career ain’t something you want, then I don’t think you should force yourself!"

    #show h shocked
    h "Oh."
    #show h normal
    h "Well… u-um thank you, Thomas."

    #show t smile
    t "Of course!"
    t "You should always follow what your heart says."

    #show h bluuuush
    h "(My heart…?)"
    h "Again, thank you Thomas."
    h "Your family and the farm must really appreciate that heart of yours…"

    #show t ah- freeze + sweat drop
    t "Hahaha— Y-ya I bet you’re right…"

    #show t ! + oh!
    t "!!!"

    #Scene 2 - flower scene!!!

    scene dScene with Dissolve(.5)

    t "Here. To cheer you up. Just picked them as I was passing through the park."

    scene dScene

    h "..."
    h "Thank you..."

    scene dScene

    pause 0.5

    scene dbg with Dissolve(.5)

    #show h normal + sweat drop
    show dHenry with Dissolve(.5):
        zoom 0.65
        xalign 0.0
        yalign 0.40

    #show t smile
    show dThomas with Dissolve(.5):
        zoom 0.65
        xalign 1.0
        yalign 0.40

    #show t !
    t "Hey!"
    #show t smile
    t "Hey! How about you visit the farm once in a while to get out of the city?!"

    #show t hands up 
    t "I-If ya want of course! Just a suggestion since you mentioned wanting out of the city!"

    #show h side eye + sweat drop
    h "(Follow your heart huh…)"

    scene dScene with Dissolve(.5)

    h "Okay."

    scene dScene

    scene black with Dissolve(.5)

    "Henry's determined to follow his heart."

    #END of Prelude + Act I

    #start of Act II

    

    # This ends the game.

    return

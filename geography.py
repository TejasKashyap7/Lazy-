def geography():
    geograph=" "
    k=0
    while True:
            # Hilly
        print('''
            Do you like Hilly areas ?
            “The mountains whisper for me to wander; my soul hikes to the call.” 
            — Angie Weiland-Crosby

            Do you like claiming those big mountains, or you just like the facinating view from the top
            ''')

        while True :
            user_hilly=input('Answer in y/n : ')
            if user_hilly=="y" :
                geograph="hilly"
                k=1
                break
            elif user_hilly=="n":
                break
            else:
                print("Invalid anwser try again")
                continue
        if k==1:
            break
            # Coastal
        print('''
                Do you like Coastal areas ?

                Are you a thalassophile ? 
                OR
                A person who loves and is magnetically attracted to the ocean and the sea.
                Many people say they enjoy spending time at the beach, especially during summertime.''' )

        while True:
            user_coastal=input('Answer in y/n : ')
            if user_coastal=='y' :
                geograph='coastal'
                k=1
                break
            elif user_coastal == 'n':
                break
            else:
                print('Try again ')
                continue
            # plain
        if k==1:
            break
        print('''
            Do you like plains ?
            Are you a guy who love to see the beauty of plains where life is simple,
            you get to see those big farming lands or simply don't want much hustle ''')
        while True:
            user_plain=input('Answer in y/n : ')
            if user_plain=='y'  : 
                geograph='plain'
                break
            elif user_plain == 'n':
                break
            else:
                print('Try again ')
                continue
        break
    return(geograph)
#print(geography())
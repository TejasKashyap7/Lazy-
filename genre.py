def genre():
    k=0
    gnora="+"
    while True:
        # Heritage
        print('''
        Do you like Heritage of INDIA ?

        Despite the technological advancement, India as a nation has been deeply attached to its root of the old ancient tradition.

        or you want to explore artefacts, monuments, a group of buildings and sites, museums that have a diversity of values including symbolic,
        historic,artistic, aesthetic, ethnological or anthropological, scientific and social significance

        If you have a intrest in our culture heritage , or you just want to explore Indian Heritage
        ''')


        while True:
            user_heritage=input('Answer in y/n : ')
            if user_heritage=='y' :
                k=1
                gnora="Heritage"
                break
            elif user_heritage =='n':
                break
            else:
                print('Try again ')
                continue
        if k==1:
            break

        # Spiritual 
        print('''
        Do you like Spiritual places ?

                    अमृतत्वस्य तु नाशास्ति वित्तेन ।
                                        - Brihdaranyakopanishad 2.4.2

                    Immortality cannot be achieved by wealth.


        DO you want to connect to a higher power beyond your understanding or just simply want to that positive boost 
        you get after you visit a temple 
        ''')


        while True:
            user_spiritual=input('Answer in y/n : ')
            if user_spiritual=='y'  :
                k=1
                gnora="Spiritual"
                break
            elif user_spiritual == 'n':
                break
            else:
                print('Try again ')
                continue
        if k==1:
            break

        # chill
        print('''
        Are you just going for fun for adventures which lie in your journey


        ''')

        while True:
            user_chill=input('Answer in y/n : ')
            if user_chill=='y' :
                k=1
                gnora="chill"
                break
            elif  user_chill == 'n':
                break
            else:
                print('Try again ')
                continue
        break
    return (gnora)

'''
print(genre())'''
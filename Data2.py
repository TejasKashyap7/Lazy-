"""             DATA            """


from random import choice



def North_India( genre,geography):
    
    sptual_hilly=['Ladakh','Spiti','Dharamshala','Rishikesh','Gangotri','Vrindavan','Pushkar','Amarnath','Jamu','Haridwar','Kedarnath','Chitrakoot','Shrinagr','AnantNnag','Yamunotri','Badrinath','Tirupathi Nath','Mcleodganj']
    sptual_plain = ['Ayodhya', 'Varanasi', 'Haridwar', 'Amritsar', 'Ajmer', 'Prayagraj', 'Kuruksheatra', 'Mathura',
                    'Devgarh', 'Pawapuri', 'Vaishali', 'Kashi Vishwanath', 'Sarnath', 'Sulatanpur', 'Anantnag',
                    'Bateshwar']
    Heritage_plain = ['Agra Fort', 'Taj Mahal', 'Fatehpur Sikri', 'Keoladeo National Park', 'Humayun Tomb',
                      'Qutub Minar']
    Heritage_hilly = ['Dharamshala', 'Bhimtal', 'Rishikesh']
    chill_plain = ['New Delhi', 'Agra', 'Haridwar', 'Amritsar', 'Chandigarh', 'Varanasi', 'Mathura', 'Lucknow',
                   'Jaipur', 'Udaipur', 'Jaisalmer']
    chill_hilly = ['Auli', 'Shimla', 'Mussorie', 'Spiti', 'Parvati Valley', 'Dalhousie', 'Kullu and manali']

    if genre=='Spiritual':
        
             
        if geography=='hilly':
            
            while True:
                choic=(choice(sptual_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break


                
        elif geography=='plain':
           
            
            while True:
                choic=(choice(sptual_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break  
                    
        elif geography=='coastal':
            
            print('None')
        
    elif genre=="Heritage":
        
            
        if geography=='plain':
            
               
            while True:
                choic=(choice(Heritage_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break


        elif geography=='hilly':
            
            
            while True:
                choic=(choice(Heritage_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
                                
        elif geography=='coastal':
            
            print('none')

    elif genre=='chill':
        if geography=='plain':
            
            while True:
                choic=(choice(chill_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

                
        elif geography=='hilly':
            while True:
                choic=(choice(chill_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

                
        elif geography=='coastal':
            print('none')

def East_India( genre,geography):
    
    
    
    heritage_plain=['Jal Mandir','Vaishali','Konkark','Nalanda Mahavihara','Sundarbans National Park','Gandhi Ghat']
    spiritual_plane=['Pawapuri','Vaishali','Bodh Gaya','Gaya','Baidyanathdham','nalanda']
    spiritual_coastal=['Puri','Bhubaneswar','Mayapur (west bengal)','Konark','Siliguri']

    heritage_hilly=['Khangchendzonga National Park','Manas Wildlife Sanctuary','Kalimpong','Kohima','Mokokchung','Kurseong']
    heritage_coastal=['Sagar island']
    chill_plain=['Majuli','Dooars','Nameri National Park','Sibsagar','Bhubaneshwar','Gopalpur','Ranchi']
    chill_hilly=['Itanagar']
    chill_coastal=['Varkala Beach','puri beach','Marina beach','Juhu beach','Digha','Majorda Beach']

    spiritual_hilly=['rajgir']
    if genre=='Spiritual':
        if geography=='hilly':
            
            
            while True:
                choic=(choice(spiritual_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='plain':
            
            
            while True:
                choic=(choice(spiritual_plane))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
        elif geography=='coastal':
            while True:
                choic=(choice(spiritual_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
    elif genre=="Heritage":
        if geography=="plain":
            while True:
                choic=(choice(heritage_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='hilly':
            
            while True:
                choic=(choice(heritage_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='coastal':
            while True:
                choic=(choice(heritage_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

    elif genre=='chill':
        
            
            
        if geography=='plain':
            while True:
                choic=(choice(chill_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
        elif geography=='hilly':
            
            while True:
                choic=(choice(chill_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

                
        elif geography=='coastal':
            
            while True:
                choic=(choice(chill_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
def North_East( genre,geography):
    
    
    spiritual_hilly=['Guwahati ( Kamakhya Temple)','Akash Ganga','Tripura','Umananda','Tawang Monestri']
    heritage_hilly=['Majuli','Yumthang','Aizawl','Kaziranga','Kohima','Gangtok','Tawang','Dimapur','Roing']
    heritage_plain=['Malinithan Temple','Itanagar']
    chill_hilly=['Sikkim','Gorichen Peak','Goechala','Umiam lake','Gangtok','Pelling','Yuksom']
    chilly_plain=['Loktak Lake','Siang River Rafting','Mawlynnong Village','Namdapha National Park']

    if genre=='Spiritual':
        
        if geography=='hilly':
            
            while True:
                choic=(choice(spiritual_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography == 'plain':
            
            print('none')
            
        elif geography == 'coastal':
            
            print('None')
            
    elif genre=="Heritage":
        
        if geography=='hilly':
            
            while True:
                choic=(choice(heritage_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='plain':
            
            while True:
                choic=(choice(heritage_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='coastal':
            
            print('none')
            
    elif genre=='chill':
        
        if geography=='hilly':
            
            while True:
                choic=(choice(chill_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='plain':
            
            
            while True:
                choic=(choice(chilly_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
        elif geography=='coastal':
            
            
            print(None)

def South_India( genre,geography):
    
    spiritual_plain=['Madurai','Tiruvannamalai','Kanchipuram','Coimbatore']
    spiritual_coastal=['Rameswaram','Gokarna','Kollam','Puducherry']
    heritage_plain=['Hampi','Mahabalipuram','Darasuram','Pattadakal','Bijapur','Madurai','Kanchipuram','Thanjavur','Chindambaram']
    heritage_hilly=['Nilgiri','Kavaledurga Fort']
    heritage_coastal=['Kozhikode','Thalassery','Pondicherry','Kasargod']
    spiritual_hilly=['Tirupati']
    chill_hilly=['Coorg','Kodaikanal','Ooty and Coonoor','Wayanad','Gokrana','Munnar','Thekkady']
    chill_plain=['Hampi','Madurai','Kanchipuram','Pondicherry','Warangal']
    chill_coastal=['Chennai','Gokarna','Varkala','Mahabalipuram','Alleppey','Kumarakom','Kochi','Kanyakumari']
        
        
    if genre=='Spiritual':
        
        
        if geography=='hilly':
            
            while True:
                choic=(choice(spiritual_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography == 'plain':
            
            while True:
                choic=(choice(spiritual_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography == 'coastal':
            
            while True:
                choic=(choice(spiritual_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

    elif genre=="Heritage":
        
            
        if geography=='plain':
            
                
            while True:
                choic=(choice(heritage_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='hilly':
            
            while True:
                choic=(choice(heritage_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='coastal':
            
            while True:
                choic=(choice(heritage_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

    elif genre=='chill':
        
        if geography=='hilly':
            
            while True:
                choic=(choice(chill_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
        elif geography=='plain':
            
            while True:
                choic=(choice(chill_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='coastal':
            
            while True:
                choic=(choice(chill_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

def West_India( genre,geography):
    spiritual_hilly=['Igatpuri','Kolhapur','Nashik']
    spiritual_plain=['Dwarka','Nanded','Shirdi Baba','Pushkar','Ghandi Nagar']
    spiritual_coastal=['Akshardham','Somnath']
    heritage_plain=['Ajanta Caves','Champaner-Pavagadh']
    heritage_hilly=['Ellora','Kailasa Temple','Chittorgarh Fort']
    heritage_coastal=['Elephanta Caves','Chhatrapati Shivaji Maharaj Terminus','Velha Goa']
    chill_coastal=['Goa','Kutch','Daman and Diu','Mumbai','Tarkarli','Alibag','Murud']
    chill_plain=['Gir','Jodhpur','Matheran','Ranthambore','Bharatpur']
    chill_hilly=['Mahabaleshwar','Panchgani','Khandala','Lonavla','Saputara','Mount Abu']
    if genre=='Spiritual':
        
        if geography=='hilly':
            
            while True:
                choic=(choice(spiritual_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='plain':
            
                
            while True:
                choic=(choice(spiritual_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='coastal':
            
                
            while True:
                choic=(choice(spiritual_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break


    elif genre == 'Heritage':
        
        if geography == 'plain':
            
            while True:
                choic=(choice(heritage_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography == 'hilly':
            
            while True:
                choic=(choice(heritage_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break
        elif geography == 'coastal':
            
            
            while True:
                choic=(choice(heritage_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break


    elif genre=='chill':
        
        if geography=='coastal':
            
            while True:
                choic=(choice(chill_coastal))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='plain':
           
      
            
            while True:
                choic=(choice(chill_plain))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break

        elif geography=='hilly':
            
            while True:
                choic=(choice(chill_hilly))
                print(choic)
                a=input("If you want another suggestion press 'Enter' otherwise press any other key :")
                if a=="":
                    continue
                else:
                    return choic
                    break




'''
East_India(8, 'chill','hilly')
East_India(8, 'chill','plain')
East_India(8, 'chill','coastal')'''
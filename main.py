import Data2 
import region_finder
import genre
import geography
import wiki
from os import system
import email1234
 

# Inputs

user_name=input('Enter your name :')

user_state=input('Tell us which state you live in : ')

user_holidays=int(input('Enter the number of holidays you want to spend :'))


user_emaill=email1234.check_mail()
email1234.mail(email=user_emaill)

# we have variable 'user_preffered_location'

print('''
Everyone is diffrent , So are you
Some like conquer those big hills which penetrate sky and the satisfying view from the top which can't be described in words
but some like the breeze coming from the sea calling them for adventures or just chill at a quite beach and see huge and calming sea
Some may like just the simplicity of plains and embrace it's beauty

Below survey will help us to know a bit about you :
 ''')




# finding user genre
user_genre=genre.genre()

# finding user geography  prefrences
user_geography_prefrences=geography.geography()

# Magic
#user_preffered_location(user_genre,user_geography_prefrences)


if user_holidays > 5:
    upl=int(input('''
    which region of India will you like to visit :

    1.North_India           4.South_India

    2.East_India            5.West_India

    3.North_East
    '''))
    if upl == 1:
        user_preffered_location='North_India'
        hi=Data2.North_India(user_genre,user_geography_prefrences)
    elif upl== 2:
        user_preffered_location='East_India'
        hi=Data2.East_India(user_genre,user_geography_prefrences)
    elif upl==3:
        user_preffered_location='North_East'
        hi=Data2.North_East(user_genre,user_geography_prefrences)
    elif upl==4:
        user_preffered_location='South_India'
        hi=Data2.South_India(user_genre,user_geography_prefrences)
    elif upl==5:
        user_preffered_location='West_India'
        hi=Data2.West_India(user_genre,user_geography_prefrences)

else:
    user_preffered_location=region_finder.region_finder(user_state)
    
    if user_preffered_location=='North_India':
        hi=Data2.North_India(user_genre,user_geography_prefrences)
    elif user_preffered_location=='East_India':
        hi=Data2.East_India(user_genre,user_geography_prefrences)
    elif user_preffered_location=='North_East':
        hi=Data2.North_East(user_genre,user_geography_prefrences)
    elif user_preffered_location=='South_India':
        hi=Data2.South_India(user_genre,user_geography_prefrences)
    elif user_preffered_location=='West_India':
        hi=Data2.West_India(user_genre,user_geography_prefrences)


system("cls")
try:
    wiki.website(hi)
except KeyboardInterrupt:
    print("You press ctrl c")

except:
    print("not able to fetch data from server ")
    print("to slove this try to check internet")
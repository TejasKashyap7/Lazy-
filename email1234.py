import smtplib

string_to_send_email="""Greetings Lazy Yatri!

Exploring a solution for your ITCHY FEETS?  

Finding famous place to rendezvous with your beloved?
 
NO WORRIES, you've come to the right place and we're really happy to have you onboard. Stay connected for further information :)

Thank you."""
 
def mail(email):
    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.starttls()
    gmail.login("LazyYatri1234@gmail.com","xdsiqxqgonpiccxi")
    
    gmail.sendmail("LazyYatri1234@gmail.com",str(email),str(string_to_send_email))
    gmail.quit()

mail("yamansharma2004@gmail.com")

def check_mail():
    list_=["gmail","com","in","edu"]
    while True:
        user_mail=input("Enter your email : ")
        a=user_mail[:]
        a=a.replace("@",".")
        a=a.split(".")
        try:
            a=a[-2]
        except:
            print("Invalid email")
            continue
        if a in list_:
            return user_mail
            break
        else:
            print("Invalid email")
            continue


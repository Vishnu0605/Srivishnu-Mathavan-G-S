import random

ALP=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['1','2','3','4','5','6','7','8','9']
sym=['!','#','&','*','?']

Choices=(ALP+alp+num+sym)
       
length=int(input("\nEnter the length of the password :"))
    
Generate="".join(random.sample(Choices,length))

print("Password :",Generate)

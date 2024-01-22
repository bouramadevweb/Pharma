"""Exemple"""

# value= int(input("Tapez un nombre entre 1 et 10"))

# if(value >0) and(value<=10):
#     print("vous avez tapez :",value)
# else:
#     print("vous avez tapez une valeur incorrecte !")
try :
    value = int(input(" Tapez un nom entre 1 et 10 "))
except(ValueError ,KeyboardInterrupt):
    print(" vous devez tapez un nombre entre 1 et 10 ")
else:
    if(value >0) and(value<= 10):
        print(" vous avez tapez : ",value)
    else:
        print("vous avez tapez une valeur incorrecte !")
finally :
    print(" vous avez tapez" ,value)

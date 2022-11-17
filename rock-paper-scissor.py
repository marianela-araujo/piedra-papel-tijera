import random

f = open('puntaje.txt','a', encoding="utf-8")
while True:         #for i in range (1,4):(el while reemplaza al for)
    for i in range (1,4):
        user_action=input("seleccione (piedra-papel-tijera)")
        possible_actions=["piedra", "papel", "tijera"] 
        computer_action=random.choice(possible_actions)
    #print(computer_action)
        print("\ntu elegiste", user_action, ", la computadora eligio,",computer_action,"\n")
        if user_action == computer_action :
            print("empate", user_action, "ambos ganaron!")
            f.write("empate,ambos ganaron . \n")
        elif user_action == "piedra" and computer_action == "papel":
            print("gano la computadora . \n")
            f.write("gano la computadora . \n")
        elif user_action == "papel" and computer_action == "piedra":
            print("gano el usuario . \n")
            f.write("gano el usuario .\n")
        elif user_action == "tijera" and computer_action == "papel":
            print("gano el usuario . \n")
            f.write("gano el usuario . \n")
        elif user_action == "piedra" and computer_action == "tijera":
            print("gano el usuario . \n")
            f.write("gano el usuario . \n")      
        else :
            print("error seleccione bien !") 
    play_again= input("desea jugar nuevamente? (s/n) : ")
    if play_again. lower () == "n" :
        break



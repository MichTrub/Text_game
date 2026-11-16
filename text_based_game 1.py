import random
def randomise_location(): #randomises the place of locations
    location = ["start","","","","shop","","","","","shop","","","","","shop","","","","","shop","","","","shop","boss"]
    #placed1 = False
    #print(location)
    #while not placed1:
     #   place = random.randint(1,24)
      #  if location[place] =="":
       #     location[place] = "quest1"
        #    #print(place)
         #   placed1 = True
    #placed2 = False
    #print(location)
    #while not placed2:
     #   place = random.randint(1,24)
      #  if location[place] =="":
       #     location[place] = "quest2"
        #    #print(place)
         #   placed2 = True
    #placed3 = False
    #print(location)
    #while not placed3:
     #   place = random.randint(1,24)
      #  if location[place] =="":
       #     location[place] = "quest3"
        #    #print(place)
         #   placed3 = True
    #print(location)
    for i in range(7):
        placed= False
        #print(location)
        while not placed:
            place = random.randint(1,24)
            if location[place] == "":
                location[place] = "event"
                placed = True
                #print(place)
    for i in range (len(location)):
        if location[i] == "":
            location[i] = "fight"
    #print(location)
    return location
def input_checker_type(type,valid_list,type_range_of_numbers_or_list,first,second):         # input type checker
    inp = input()
    if type  == "str":
        try:
            inp = str(inp) 
        except:
            print("Not valid input")
            return input_checker_type(type,valid_list,type_range_of_numbers_or_list,first,second)
        else:
            return input_checker_range(inp,valid_list,type_range_of_numbers_or_list,first,second,type)
    elif type == "int":
        try:
            inp = int(inp)
        except:
            print("Not valid input")
            return input_checker_type(type,valid_list,type_range_of_numbers_or_list,first,second)
        else:
            return input_checker_range(inp,valid_list,type_range_of_numbers_or_list,first,second,type)

def input_checker_range(inp,valid_list,type_range_of_numbers_or_list,first,second,type):
    if type_range_of_numbers_or_list == "range":
        if inp >= first and inp <= second:
            return inp
        print("Not valid input") 
        return input_checker_type(type,valid_list,type_range_of_numbers_or_list,first,second)
    if type_range_of_numbers_or_list == "list":
        if inp in valid_list:
            return inp 
        else:
            print("Not valid input")
            return input_checker_type(type,valid_list,type_range_of_numbers_or_list,first,second)



                    #finish the input_checker first
def menu():
    print("Please choose the charachter")
    for i in range(0,len(Characters)):
        print(str(i+1)+". "+Characters[i][0] +" Max Health ["+str(Characters[i][2])+"] Max Stamina ["+str(Characters[i][4])+"]")
    inp = input_checker_type("int",EmptyList,"range",1,2)
    return Characters[inp-1]

def tavern(locations,input_locations_list):
    print("Choose the location where you are going")
    for i in range (len(locations)):
        print(i+1 ,". "+ locations[i][0][0])
    inp = input_checker_type("int",input_locations_list,"list",0,len(locations)-1)
    return locations[inp-1]

def inventory(bag,charachter,gold,exp):
    Empty_list = []
    command_list= ["e","f","i"]
    while True:
        print("Your charachter")
        print("LEVEL [",exp[0],"] exp [",exp[1],"/",(2**(exp[0]-1))*100,"]")
        print("HP [",charachter[1],"/",charachter[2],"]   ST [",charachter[3],"/",charachter[4],"] GOLD [",gold,"]")
        for clothe in bag[0]:
            if clothe[0] == "arms":
                print("[ arms ] - [",clothe[1],"] - Damage - [",clothe[2],"] - cost - [",clothe[3],"]")
            else: 
                print("[",clothe[0],"] - [",clothe[1],"] - Resistance - [",clothe[2],"] - cost - [",clothe[3],"]")
        print("Your bag")
        if len(bag[1]) == 0:
                print("You have nothing")
        else:
            for clothe in bag[1]:
                if clothe[0] == "arms":
                    print("[ arms ] - [",clothe[1],"] - Damage - [",clothe[2],"] - cost - [",clothe[3],"]")
                else: 
                    print("[",clothe[0],"] - [",clothe[1],"] - Resistance - [",clothe[2],"] - cost - [",clothe[3],"]")
        print ("What do you wabt to do?")
        print("Use the clothe.................[e]")
        print("leave the inventory............[i]")                                        
        answer = input_checker_type("str",command_list,"list",0,0)
        if answer == "i":
            print("-------------------------------------------------------------------")
            return bag,charachter
        if answer == "e":
            print("-------------------------------------------------------------------")
            if len(bag[1]) == 0:
                print("You have nothing")
            else:
                for i in range(len(bag[1])):
                    if bag[1][i][0] == "poition":
                        print(i+1,". [",bag[1][i][1],"] HEALTH + [",bag[1][i][2],"]")
                    if bag[1][i][0] == "arms":
                        print(i+1,". [",bag[1][i][1],"] damage [",bag[1][i][2],"]")
                    if bag[1][i][0] == "head":
                        print(i+1,". [",bag[1][i][1],"] resistance [",bag[1][i][2],"]")
                    if bag[1][i][0] == "body":
                        print(i+1,". [",bag[1][i][1],"] resistance [",bag[1][i][2],"]")
                    if bag[1][i][0] == "legs":
                        print(i+1,". [",bag[1][i][1],"] resistance [",bag[1][i][2],"]")
                print("Which one do you want to use?")
                chose = input_checker_type("int",Empty_list,"range",1,len(bag[1]))
                print("-------------------------------------------------------------------")
                chose -= 1
                if bag[1][chose][0] == "poition":
                    charachter[1] += bag[1][chose][2]
                    if charachter[1] > charachter[2]:
                        charachter[1] = charachter[2]
                        print("Your HP is max")
                    deleted= bag[1].pop(chose)

                elif bag[1][chose][0] == "head":
                    if bag[0][0][1] =="":
                        bag[0][0] =bag[1][chose]
                        deleted = bag[1].pop(chose)
                    else:
                        save = bag[0][0]
                        bag[0][0]= bag[1][chose] 
                        bag[1][chose]= save
                elif bag[1][chose][0] == "body":
                    if bag[0][1][1] =="":
                        bag[0][1] =bag[1][chose]
                        deleted = bag[1].pop(chose)
                    else:
                        save = bag[0][1]
                        bag[0][1]= bag[1][chose] 
                        bag[1][chose]= save

                elif bag[1][chose][0] == "legs":
                    if bag[0][2][1] =="":
                        bag[0][0] =bag[1][chose]
                        deleted = bag[1].pop(chose)
                    else:
                        save = bag[0][0]
                        bag[0][2]= bag[1][chose] 
                        bag[1][chose]= save
                elif bag[1][chose][0] == "arms":
                    if bag[0][3][1] =="":
                        bag[0][3] =bag[1][chose]
                        deleted = bag[1].pop(chose)
                    else:
                        save = bag[0][3]
                        bag[0][3]= bag[1][chose] 
                        bag[1][chose]= save                                      #finish inventory use 


def shop(shop_chances,bag,gold,exp):
    choice_list = ["i","a","d"]
    Trade_list = []
    for i in range (9 + exp[0]):
        choice = random.randint(0,len(shop_chances)-1)
        Trade_list.append(shop_chances[choice])
    while True:
        print("GOLD [",gold,"]")
        for i in range(0,len(Trade_list)):
            print(i+1,". ",Trade_list[i][1],"type [",Trade_list[i][0],"]  stats [",Trade_list[i][2],"] cost[",Trade_list[i][3],"]")
        print("Leave the shop..........................i")
        print("buy.....................................a") 
        print("sell....................................d")
        player_choice = input_checker_type("str",choice_list,"list",0,0)
        if player_choice == "i": 
            return bag,gold
        if player_choice == "a":
            print("Input the number of what you want to buy")
            player_buy = input_checker_type("int",choice_list,"range",1,len(Trade_list))
            if gold >= Trade_list[player_buy-1][3]:
                gold -= Trade_list[player_buy-1][3]
                bag[1].append(Trade_list[player_buy-1])
                Trade_list.pop(player_buy-1)

            else:
                print("You do not have enough gold")
        if player_choice =="d":
            number = 1
            for clothe in bag[1]:
                
                if clothe[0] == "arms":
                    print(number,". [ arms ] - [",clothe[1],"] - Damage - [",clothe[2],"] - cost - [",clothe[3],"]")
                else: 
                    print(number,". [",clothe[0],"] - [",clothe[1],"] - Resistance - [",clothe[2],"] - cost - [",clothe[3],"]")
                number+=1
            if len(bag[1])!= 0:
                print("Which one do you want to sell")
                player_sell = input_checker_type("int",choice_list,"range",1,len(bag[1]))
                player_sell -=1
                print("You got ",bag[1][player_sell][3]," gold")
                gold += bag[1][player_sell][3]
                bag[1].pop(player_sell)
            else:
                print("You have nothing")



def fight(charachter,locations,bag,The_player_location,gold,exp,GAME_OVER,effects):
    
    effect_main = [[]]
    armor = bag[0][0][2] + bag[0][1][2] + bag[0][2][2]
    choice_list1 = ["w","i","s","r"]
    choice_list2 = ["a","s","d"]
    enemy_list = ["a","d"]
    monster = random.randint(0,len(locations)+1)
    enemy =locations[0][1][monster]
    max_hp = enemy[1]
    print("You see the ",locations[0][1][monster][0],"[",enemy[1],"/",max_hp,"]. It sees you as well , you start fighting.")
    while True:
        effect = effect_main                               
        if len(effect) != 1:
            for i in range (1,len(effect)):
                print("You are getting [",effect[i][1],"] from ",effect[i][0])
                charachter[1] -=effect[i][1]                                                                                                         #the posion effect does not ends
                effect[i][2]-=1
                if effect[i][2] <= 0:
                    print("The [",effect[i][0],"] has passed.")
                    effect_main.pop(i)
        print("attack....................w")
        print("regenerate stamina........s")
        print("inventory.................i")
        print("run away..................r")
        player_choice = input_checker_type("str",choice_list1,"list",0,0)
        if player_choice == "i":
            bag,charachter = inventory(bag,charachter,gold,exp)
        if player_choice == "r":
            print("You suck my battle ship")
            The_player_location -= 1  
            lefted = True
            return GAME_OVER,charachter,The_player_location,gold,exp,lefted
        if player_choice == "w":
            if charachter[3] >= 10:
                print("You attack the",enemy[0],"[",enemy[1]-bag[0][3][2],"/",max_hp,"] for ",bag[0][3][2],"damage") 
            
                enemy[1] -= int(bag[0][3][2])              #problem here
                charachter[3] -= 10
                if enemy[1] <= 0 :
                    print("you have defeated the ",enemy[0],". You get [", enemy[3],"] exp and [",enemy[4],"]")
                    gold += enemy[4]
                    exp[1] += enemy[3]
                    exp = exp_checker(exp)
                    lefted = False
                    return GAME_OVER,charachter,The_player_location,gold,exp,lefted
            else:
                print("You do not have enough energy, you missed")
        if player_choice == "s":
            charachter[3] += 20
            if charachter[4] <= charachter[3]:
                charachter[3] = charachter[4]
                print("You have full stamina")
            else:
                print("You have regenerated 20 stamina")
        print(enemy[0]," is going to attack you , Where are you going?")
        print("stay....................s")
        print("move left...............a")
        print("move right..............d")
        player_choice = input_checker_type("str",choice_list2,"list",0,0)
        if player_choice == "s":

            chance = random.randint(1,100)
            if chance > armor:
                if len(enemy) == 6:
                        for name in effects:
                            if enemy[5] == name[0] and name not in effect:
                                effect.append(name)
                damage = enemy[2]/2
                damage = int(damage)
                print(enemy[0],"heats you for [",damage,"] damage.")
                charachter[1] -= damage
                GAME_OVER = death_checker(charachter)
                if GAME_OVER:
                    lefted = False
                    return GAME_OVER,charachter,The_player_location,gold,exp,lefted
            else:
                print("The ",enemy[0],"[",enemy[1],"/",max_hp,"] heats you but your armor defends you from damage")
        else:
            bot_choice = random.choice(enemy_list)       
            if bot_choice == player_choice:
                chance = random.randint(1,100)
                if chance > armor:
                    if len(enemy) == 6:
                        for name in effects:
                            if enemy[5] == name[0] and name not in effect:
                                effect.append(name)
                    print("The ",enemy[0],"heats you")
                    print("You gain [",enemy[2],"] damage") 
                    charachter[1] -= enemy[2]
                    GAME_OVER = death_checker(charachter)
                    if GAME_OVER:
                        lefted = False
                        return GAME_OVER,charachter,The_player_location,gold,exp,lefted
                else:
                    print("The ",enemy[0],"[",enemy[1],"/",max_hp,"] heats you but your armor defends you from damage")
            else: 
                print("The ",enemy[0],"missed")
        print("HP [", charachter[1],"/",charachter[2],"] ST [",charachter[3],"/",charachter[4],"]")        


def boss_fight(charachter,locations,bag,The_player_location,gold,exp,GAME_OVER,effects):
    effect= []
    effect_main = [[]]
    armor = bag[0][0][2] + bag[0][1][2] + bag[0][2][2]
    choice_list1 = ["w","i","s","r"]
    choice_list2 = ["a","s","d"]
    enemy_list = ["a","d"]
    enemy = locations[0][3]
    max_hp = enemy[1]
    print(enemy[6]," that is the ",enemy[0],"[",enemy[1],"/",max_hp,"]")
    while True:
        effect = effect_main                               
        if len(effect) != 1:
            for i in range (1,len(effect)):
                print("You are getting [",effect[i][1],"] from ",effect[i][0])
                charachter[1] -=effect[i][1]                                                                                                         #the posion effect does not ends
                effect[i][2]-=1
                if effect[i][2] <= 0:
                    print("The [",effect[i][0],"] has passed.")
                    effect_main.pop(i)

            
            
        print("attack....................w")
        print("regenerate stamina........s")
        print("inventory.................i")
        print("run away..................r")
        player_choice = input_checker_type("str",choice_list1,"list",0,0)
        if player_choice == "r":
            print("There is no way back")
        if player_choice == "i":
            bag,charachter = inventory(bag,charachter,gold,exp)
            

        if player_choice == "w":
            if charachter[3] >= 10:
                print("You attack the",enemy[0],"[",enemy[1]-bag[0][3][2],"/",max_hp,"] for ",bag[0][3][2],"damage") 
            
                enemy[1] -= int(bag[0][3][2])              #problem here
                charachter[3] -= 10
                if enemy[1] <= 0 :
                    print("you have defeated the ",enemy[0],"[",enemy[1],"/",max_hp,"]. You get [", enemy[3],"] exp and [",enemy[4],"]")
                    gold += enemy[4]
                    exp[1] += enemy[3]
                    exp = exp_checker(exp)
                    lefted = False
                    return GAME_OVER,charachter,The_player_location,gold,exp,lefted
            else:
                print("You do not have enough energy, you missed")
        if player_choice == "s":
            charachter[3] += 20
            if charachter[4] <= charachter[3]:
                charachter[3] = charachter[4]
                print("You have full stamina")
            else:
                print("You have regenerated 20 stamina")

        print(enemy[0],"[",enemy[1],"/",max_hp,"] is going to attack you , Where are you going?")
        print("stay....................s")
        print("move left...............a")
        print("move right..............d")
        player_choice = input_checker_type("str",choice_list2,"list",0,0)
        if player_choice == "s":
            chance = random.randint(1,100)
            if chance > armor:
                if len(enemy) == 6:
                        for name in effects:
                            if enemy[5] == name[0]:
                                effect.append(name)

                damage = enemy[2]/2
                damage = int(damage)
                print(enemy[0],"[",enemy[1],"/",max_hp,"] hits you for [",damage,"] damage.")
                charachter[1] -= damage
                GAME_OVER = death_checker(charachter)
                if GAME_OVER:
                    return GAME_OVER,charachter,The_player_location,gold,exp,lefted
            else:
                print("The ",enemy[0]," heats you but your armor defends you from damage")
        else:
            bot_choice = random.choice(enemy_list)       
            if bot_choice == player_choice:
                chance = random.randint(1,100)
                if chance > armor:
                    if len(enemy) == 6:
                        for name in effects:
                            if enemy[5] == name[0] and name not in effect:
                                effect.append(name)
                    print("The ",enemy[0],"[",enemy[1],"/",max_hp,"] hits you")
                    print("You gain [",enemy[2],"] damage") 
                    charachter[1] -= enemy[2]
                    GAME_OVER = death_checker(charachter)
                    if GAME_OVER:
                        return GAME_OVER,charachter,The_player_location,gold,exp,lefted
                else:
                    print("The ",enemy[0],"[",enemy[1],"/",max_hp,"] hits you but your armor defends you from damage")
            else: 
                print("The ",enemy[0],"[",enemy[1],"/",max_hp,"] missed")
        print("HP [", charachter[1],"/",charachter[2],"] ST [",charachter[3],"/",charachter[4],"]")        

        
                                                                                                        #finish fight 
def exp_checker(exp):
    while True:
        if exp[1] > (2**(exp[0]-1))*100:
            print("You have got new level")
            print("Now there is more clothes in the shop")
            exp[0] += 1
            exp[1] -= (2**(exp[0]-1))*100
            if exp[1] < (2**(exp[0]-1))*100:
                return exp
        return exp


def death_checker(charachter):
    if charachter[1] <= 0:
        print("YOU DIED")
        print("!!!YOU SUCK MY BATTLESHIP!!!")
        return True
    else:
        return False

         
def location_print(location,The_player_location):
    if The_player_location == 0:
        print(">>[",location[The_player_location],"]<< [",location[The_player_location+1],"]")
    elif The_player_location == 24:
        print("[",location[The_player_location-1],"] >>[",location[The_player_location],"]<<") 
    elif The_player_location > 0 :
        print("[",location[The_player_location-1],"] >>[",location[The_player_location],"]<< [",location[The_player_location+1],"]")

            

The_boss_drop = []
The_enemy_drop = []
effects = [["poison",5,3],["fier",10,5]]
The_player_location = 0 
gold = 100 
shop_chances = [["head","leather halmet",15,33],["body","leather body armor",15,50],["legs","leather leg armor",15,40],["arms","iron sword",5,75],["head","wood halmet",10,5],["body","wood body armor",10,20],["legs","wood leg armor",10,10],["arms","wood sword",3,30],["poition","Weak health poition",25,25],["poition","Strong health poition",50,50]]
EmptyList=[]
input_locations_list =[1]
Characters = [["Warior",100,150,75,100],["Asasin",75,100,100,150]]                        #name, hp , max hp , stamina , max stamina
locations = [[["DEAD CITY"],[["Slime",3,2,25,10],["Skeleton",6,5,50,20],["Toxic Skeleton",10,10,100,100,"poison"]],["sword","help","help to enemy"],["Giant skeleton in toxix slime",20,20,200,300,"poison","You are walking through the destroyed hall , you sew the movement and IT is going out from the entrance,"]]]          #name of monster , health , damage , exp , gold
exp = [1,0]
place = 0
location = randomise_location()
charachter = menu()
bag = [[["head","",0,0],["body","",0,0],["legs","",0,0],["arms","",1,0]],[["poition","Weak health poition",25,25]]]
GAME_OVER = False
location_lor = tavern(locations,input_locations_list)
print("You left the teven. There is no way back")
while not GAME_OVER:
    input_list = ["w","s","i"]
    location_print(location,The_player_location)
    print("Move foward.............................(w)")
    print("Move back...............................(s)")
    print("Open the inventory .....................(i)")
    Player_choice = input_checker_type("str",input_list,"list",0,0)
    if Player_choice == "s":
        The_player_location -= 1
        location_print(location,The_player_location)
    if Player_choice == "w":
        The_player_location += 1
        location_print(location,The_player_location)
    if Player_choice == "i":
        bag,charachter = inventory(bag,charachter,gold,exp)
        location_print(location,The_player_location)
    if The_player_location <0:
        print("You left the location")
        print("You died on the way back")
        GAME_OVER = True
    if location[The_player_location] == "fight":
        GAME_OVER,charachter,The_player_location,gold,exp,lefted = fight(charachter,locations,bag,The_player_location,gold,exp,GAME_OVER,effects)
        if not lefted:
            location[The_player_location] = "empty"
            location_print(location,The_player_location)
    elif location[The_player_location] =="shop":
        bag,gold = shop(shop_chances,bag,gold,exp)
        location_print(location,The_player_location)
    elif location[The_player_location] == "boss":
        GAME_OVER,charachter,The_player_location,gold,exp,lefted = boss_fight(charachter,locations,bag,The_player_location,gold,exp,GAME_OVER,effects)

        print("I have done only one location so")
        print("Thak you for playing in my game")
        print("you won")
        GAME_OVER = True
    else:
        print("Here is nothing what you can do ,move foward")
print("You died in the ",locations[0][0][0]," on the level [",The_player_location,"]")





    
    
    
    
    
    



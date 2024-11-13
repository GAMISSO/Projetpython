pizza_list=[]
NamePizza=input("Vueillez entrer le nom d'un pizza: ").replace("\n","")
pizza_list.append(NamePizza)
cpt=1
while True:
    choix=input("Voulez vous ajouter[O/N]:\n")
    if choix.upper()=='O':
        NamePizza=input("Vueillez entrer le nom d'un pizza: ")
        if NamePizza==' ':
            break
        if NamePizza not in pizza_list:
            pizza_list.append(NamePizza)
            cpt+=1
        if NamePizza in pizza_list:
            print("il se trouve déja")
    else:
        break
print(f"le nombre total de pizza est de :{cpt}")
print("-"*50,f"les {cpt}pizza",50*"-")
cpt2=1
for pizza in pizza_list:
    if pizza not in pizza_list:
        print("la liste est vide")
for i in pizza_list:
    print(f"{cpt2}:{i}")
    cpt2+=1

for x in range(len(pizza_list)):
    if x==0:
        print(f"le premier pizza est : {pizza_list[x]}")
    if x==-1:
        print(f"le dernier pizza est : {pizza_list[x]}")
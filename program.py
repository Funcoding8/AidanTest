Prolan_list = ["Java","Swift","Python","JavaScript","C++"]#/programming languages
New_Prolan =input("what program would you like to add?")
def rank_Prolan(Prolan_list,New_Prolan):
    for i in range(len(Prolan_list)):
        rank = input("Do you like A)" + New_Prolan+ " more or B)" + Prolan_list[i] + "more? A/B")

        if rank == "A":

            Prolan_list.insert(i, New_Prolan) 
            return Prolan_list

        elif rank =="B":
            Continue

    Prolan_list.append(New_Prolan)

    return Prolan_list

print("Your new ranking of engines is", rank_Prolan (New_Prolan, Prolan_list))


Friends = int(input("how many friends do you have? "))
Chocolates = int(input("how many chocolates do you have? "))

pieces_per_friend = Chocolates/Friends
Remainder = Chocolates % Friends

print(" You should give each frined", pieces_per_friend, "chocolate")

print("You will have ", Remainder, "chocolates left ")
quit()

import random
import time

x = input("> ")

scavenge_list = ["Trash can", "Public Toilet", 'Park', 'Library', "Mall", "Vending Machine"]

money = '0', '1', '2', '3', '5', '10'

wallet = 0

fishtype = ['Cod', 'Salmon', 'Tuna', 'Sardines']

invfish = {"Cod": [], "Salmon": [], "Tuna": [], "Sardines": []}

fishtime = [10, 20, 30, 40, 50, 60]

shop1 = ["Wooden rod", "Normal metal rod", 'Uncommon rod']
shop2 = ['Rare rod', 'Epic rod', "Legendary rod"]

wooden_rod = 25
Normal_metal_rod = 75
Uncommon_rod = 100
rare_rod = 150
epic_rod = 200
legendary_rod = 250

rod_id = 0

def fishtmr(t):
    while t:
        mins, secs = divmod(t, 60)
        if len(str(secs)) < 2:
            timer = f"{mins:2d}:0{secs}"
        else:
            timer = f"{mins:2d}:{secs:2d}"
        print(timer)
        time.sleep(1)
        t -= 1


while True:
    if x == "!fish":
        if rod_id == 0:
            print("You don't have a fishing rod, sorry.")
        if rod_id > 0:
            print("Ah! you have a fishing rod! Ready to fish?")
            answer = input("Y/N > ")
            if answer == "Y" or "y":
                print("How long do you want to fish for?")
                print(fishtime)
                answer = input("> ")
                answer = int(answer)
                if answer in fishtime:
                    if answer == fishtime[0]:
                        print(f"Ok, you will fish for {answer} minutes.")
                        fishtmr(answer)
                        fishtypeselect = random.choice(fishtype)
                        fishamnt = random.randint(0, 21)
                        print(f"You have caught {fishamnt} {fishtypeselect}!")
                        invfish[fishtypeselect].append(fishamnt)


                else:
                    print("Sorry, you can only fish for the times allocated")

    if x == "!invfish":
        print(invfish)

    if x == "!wallet":
        print(wallet)

    if x == "!shop":
        print("Here's the shop! To swap pages, type in next.")
        print(shop1)
        x = input("> ")
        if x == shop1[0] or shop1[1] or shop1[2]:
            print("Ok, let's see here...")

            if x == shop1[0]:
                if wooden_rod > wallet:
                    print("You don't have enough money, sorry")
                else:
                    print(f"Would you like to buy the wooden rod for {wooden_rod}?")
                    answer = input("Y/N > ")
                    if answer == "Y" or "y":
                        rod_id += 1
                        wallet = wallet - wooden_rod
                        print("You have successfully bought a wooden rod!")
                        print("You can now go fishing")
                    elif answer == "N" or "n":
                        print("ok, it's  your choice")

            if x == shop1[1]:
                if Normal_metal_rod > wallet:
                    print("You don't have enough money, sorry")
                else:
                    if rod_id < 1:
                        print("You need to buy the following before this one.")
                    else:
                        print(f"Would you like to buy the Normal metal rod for {Normal_metal_rod}?")
                        answer = input("Y/N > ")
                        if answer == "Y" or "y":
                            rod_id += 1
                            wallet = wallet - Normal_metal_rod
                            print("You have successfully bought a Normal metal rod")
                        elif answer == "N" or "n":
                            print("ok, it's  your choice")

            if x == shop1[2]:
                if Uncommon_rod > wallet:
                    print("You don't have enough money, sorry")
                else:
                    if rod_id < 2:
                        print("You need to buy the following before this one.")
                    else:
                        print(f"Would you like to buy the Uncommon rod for {Uncommon_rod}?")
                        answer = input("Y/N > ")
                        if answer == "Y" or "y":
                            rod_id += 1
                            wallet = wallet - Uncommon_rod
                            print("You have successfully bought a Uncommon rod")
                        elif answer == "N" or "n":
                            print("ok, it's  your choice")

            if x == "Next":
                print("Here's the shop, type in 'back' to go back and 'next' to go to the next one")
                print(shop2)
                inner_shop = input("> ")

                if inner_shop in shop2:
                    if inner_shop == shop2[0]:
                        if shop2[0] > wallet:
                            print("Sorry, you don't have enough money yet")
                        else:
                            print(f"Would you like to by the rare rod for {rare_rod}?")
                            answer = input("> ")
                            if answer == "Y" or "y":
                                wallet = wallet - rare_rod
                                print("You have now obtained the rare rod!")
                            elif answer == "N" or "n":
                                print("It's your choice")

    if x == "!scavenge":
        print("Where would you like to scavenge?")
        scavenge_list_end = random.sample(scavenge_list, 3)
        print(scavenge_list_end)
        x = input("> ")

        if x == scavenge_list_end[0] or scavenge_list_end[1] or scavenge_list_end[2]:
            print("Ok, let's see here...")
            money_end = random.choice(money)

            money_end = int(money_end)

            if money_end == 0:
                print(f"Aww, what a shame. You got {money_end}$ today.")

            else:
                print(f'Congratulations! You got {money_end}$ from scavenging!')
                wallet += money_end
                print(f"You now have in your wallet, {wallet}$! ")

        else:
            print("Sorry, you didn't choose the selected places given. Please try again.")

    x = input("> ")

import random
import time

x = input("> ")

scavenge_list = ["Trash can", "Public Toilet", 'Park', 'Library', "Mall", "Vending Machine"]

money = '0', '1', '2', '3', '5', '10'

wallet = 1000

fishtype = ['Cod', 'Salmon', 'Tuna', 'Sardines']

invfish = {"Cod": [], "Salmon": [], "Tuna": [], "Sardines": []}

fishtime = [10, 20, 30, 40, 50, 60]

shop1 = ["Wooden rod", "Normal metal rod", 'Uncommon rod']
shop2 = ['Rare rod', 'Epic rod', "Legendary rod"]

shop_access = ["1", "2"]

Wooden_rod = 25
Normal_metal_rod = 75
Uncommon_rod = 100
Rare_rod = 150
Epic_rod = 200
Legendary_rod = 250

rod_id = 1


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
                timefishing = input("> ")
                timefishing = int(timefishing)
                if timefishing in fishtime:
                    print(f"Ok, you will fish for {timefishing} minutes.")
                    fishlmt = 11 + timefishing

                    if rod_id == 1:
                        fishlmt *= 1
                    else:
                        fishlmt *= rod_id

                    fishtmr(timefishing)
                    fishtypeselect = random.choice(fishtype)
                    fishamnt = random.randint(0, fishlmt)
                    print(f"You have caught {fishamnt} {fishtypeselect}!")
                    invfish[fishtypeselect].append(fishamnt)
                else:
                    print("Sorry, you can only fish for the times allocated")

    if x == "!invfish":
        print(invfish)

    if x == "!wallet":
        print(wallet)

    if x == "!shop":
        print("Here's the shop! To swap pages, type in the page number.")
        print(shop1)
        x = input(">> ")

        if x in shop1 or shop_access:
            print("Ok, let's see here...")
            item_request_price = eval(x.replace(" ", "_"))

        elif x in shop_access:
            page_swap = eval(x.replace(x, f"shop{x}"))
            print(page_swap)
            x = input(">>> ")

            if x == shop1[0]:
                if item_request_price > wallet:
                    print("You don't have enough money, sorry.")
                else:
                    if rod_id < 0:
                        print("You need to buy the following before this one.")
                    elif rod_id >= 1:
                        print("You already have this rod.")
                    else:
                        print(f"Would you like to buy the {x} for {item_request_price}?")
                        answer = input("Y/N > ")
                        if answer == "Y" or "y":
                            rod_id += 1
                            wallet = wallet - item_request_price
                            print(f"You have successfully bought a {x}!")
                            print("You can go fish now!")
                        elif answer == "N" or "n":
                            print("ok, it's  your choice...")

            if x == shop1[1]:
                if item_request_price > wallet:
                    print("You don't have enough money, sorry.")
                else:
                    if rod_id < 1:
                        print("You need to buy the following before this one.")
                    elif rod_id >= 2:
                        print("You already have this rod.")
                    else:
                        print(f"Would you like to buy the {x} for {item_request_price}?")
                        answer = input("Y/N > ")
                        if answer == "Y" or "y":
                            rod_id += 1
                            wallet = wallet - item_request_price
                            print(f"You have successfully bought a {x}!")
                        elif answer == "N" or "n":
                            print("ok, it's  your choice...")

            if x == shop1[2]:
                if item_request_price > wallet:
                    print("You don't have enough money, sorry.")
                else:
                    if rod_id < 2:
                        print("You need to buy the following before this one.")
                    elif rod_id >= 3:
                        print("You already have this rod.")
                    else:
                        print(f"Would you like to buy the {x} for {item_request_price}?")
                        answer = input("Y/N > ")
                        if answer == "Y" or "y":
                            rod_id += 1
                            wallet = wallet - item_request_price
                            print(f"You have successfully bought a {x}!")
                        elif answer == "N" or "n":
                            print("ok, it's  your choice...")

########################################################################################################################

############################################################################################################

    if x == "!scavenge":
        print("Where would you like to scavenge?")
        scavenge_list_end = random.sample(scavenge_list, 3)
        print(scavenge_list_end)
        x = input("> ")

        if x in scavenge_list_end:
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

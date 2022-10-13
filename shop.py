# De eerste groentenwinkel

asperges = 69

gevraagd_aantal = int(input("Hoeveel asperges wenst u? "))

if gevraagd_aantal > asperges:
    print(f"Ik heb maar {asperges} in voorraad.")
else:
    asperges = asperges - gevraagd_aantal
    print("🥬" * gevraagd_aantal)
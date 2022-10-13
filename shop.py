# De eerste groentenwinkel
voorraad = { "asperges" : 69, "pompoenen" : 23}

while voorraad["asperges"] > 0 or voorraad["pompoenen"] > 0:
    # we vragen wat de klant wenst
    gevraagde_groente = input("Welke groente wenst u? ")

    # we vragen de hoeveelheid
    gevraagd_aantal = int(input(f"Hoeveel wenst u van {gevraagde_groente}? "))

    # we controleren de gevraagde hoeveelheid en geven indien in voorraad
    if gevraagd_aantal > voorraad[gevraagde_groente]:
        print(f"Ik heb maar {voorraad[gevraagde_groente]} in voorraad.")
    else:
        voorraad[gevraagde_groente] = voorraad[gevraagde_groente] - gevraagd_aantal
        if gevraagde_groente == "asperges":
            print("🥬" * gevraagd_aantal)
        elif gevraagde_groente == "pompoenen":
            print("🎃" * gevraagd_aantal)


print("Uitverkocht")
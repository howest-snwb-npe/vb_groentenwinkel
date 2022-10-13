# De eerste groentenwinkel
def main():
    voorraad = { "asperges" : 69, "pompoenen" : 23}

    while voorraad["asperges"] > 0 or voorraad["pompoenen"] > 0:
        # geef lijstje van voorraad
        for groente in voorraad:
            print(f"{groente:12} aantal: {voorraad[groente]}")

        # we vragen wat de klant wenst
        while True:
            gevraagde_groente = input("Welke groente wenst u? ")
            if gevraagde_groente in voorraad.keys():
                break
        
        while True:
            # we vragen de hoeveelheid
            gevraagd_aantal = vraag_natuurlijk_getal(f"Hoeveel wenst u van {gevraagde_groente}? ")

            # we controleren de gevraagde hoeveelheid en geven indien in voorraad
            if gevraagd_aantal > voorraad[gevraagde_groente]:
                print(f"Ik heb maar {voorraad[gevraagde_groente]} in voorraad. Geef 0 in om uw bestelling te stoppen.")
            elif gevraagd_aantal == 0:
                break
            else:
                voorraad[gevraagde_groente] = voorraad[gevraagde_groente] - gevraagd_aantal
                if gevraagde_groente == "asperges":
                    print("🥬" * gevraagd_aantal)
                elif gevraagde_groente == "pompoenen":
                    print("🎃" * gevraagd_aantal)
                break

    print("Uitverkocht")

def vraag_natuurlijk_getal(boodschap):
    while True:
        try:
            getal = int(input(boodschap))
        except ValueError:
            pass
        else:
            if getal >= 0:
                return getal

main()
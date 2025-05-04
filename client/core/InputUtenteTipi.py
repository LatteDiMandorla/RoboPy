from core.CalcoloTipi import calcola_tipi

def chiedi_risposte():
    domande = [
        "1. Estroverso, entusiasta",
        "2. Critico, polemico",
        "3. Affidabile, auto-disciplinato",
        "4. Ansioso, facilmente turbabile",
        "5. Aperto a nuove esperienze, complesso",
        "6. Riservato, tranquillo",
        "7. Simpatico, caloroso",
        "8. Disorganizzato, negligente",
        "9. Calmo, emotivamente stabile",
        "10. Convenzionale, poco creativo"
    ]

    risposte = []
    print("Rispondi con un numero da 1 (fortemente in disaccordo) a 7 (fortemente d'accordo):\n")
    for domanda in domande:
        while True:
            try:
                risposta = int(input(f"{domanda}: "))
                if 1 <= risposta <= 7:
                    risposte.append(risposta)
                    break
                else:
                    print("Inserisci un numero tra 1 e 7.")
            except ValueError:
                print("Per favore inserisci un numero valido.")
    return risposte

def mostra_risultati(risposte):
    punteggi = calcola_tipi(risposte)
    print("\nRisultati TIPI (punteggi da 2 a 14):")
    for tratto, punteggio in punteggi.items():
        print(f"{tratto}: {punteggio}")

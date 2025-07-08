from core.CalcoloTipi import calcola_tipi

def mostra_risultati(risposte):
    punteggi = calcola_tipi(risposte)
    print("\nRisultati TIPI (punteggi da 2 a 14):")
    for tratto, punteggio in punteggi.items():
        print(f"{tratto}: {punteggio}")

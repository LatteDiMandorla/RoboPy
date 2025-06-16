import json

def calcola_tipi(risposte):
    tipi = {
        "Estroversione": risposte[0] + (8 - risposte[5]),
        "Amicalità":     risposte[6] + (8 - risposte[1]),
        "Coscienziosità":risposte[2] + (8 - risposte[7]),
        "Stabilità":     risposte[8] + (8 - risposte[3]),
        "Apertura":      risposte[4] + (8 - risposte[9])
    }
    return tipi

def ConvertDictionaryToJson(risposte):
    return json.dumps(calcola_tipi(risposte), ensure_ascii=False)

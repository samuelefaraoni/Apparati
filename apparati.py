Apparato = {}

STATI_AMMESSI = ("OK", "ATTENZIONE", "OFFLINE")

APPARATI = {
    "NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
    "COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
    "SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}


def aggiungi_apparato(codice: str, nome: str, bus: str, stato: str) -> bool:
    stato_normalizzato = stato

    APPARATI[codice] = {"nome": nome, "bus": bus, "stato": stato_normalizzato}
    return True


def aggiorna_stato(codice: str, stato: str) -> bool:
    stato_normalizzato = stato
    
    APPARATI[codice]["stato"] = stato_normalizzato
    return True
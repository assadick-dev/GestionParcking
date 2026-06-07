"""
Scénario de simulation du système de gestion de parking.

Charge un jeu de clients depuis `donnees.json`, les fait entrer dans le
parking, délivre leurs tickets, gère les super abonnés puis simule
quelques sorties et demandes de services additionnels.
"""

import json

from parking import Parking
from client import Client
from voiture import Voiture
from acces import Acces
from borneTicket import BorneTicket
from teleporteur import Teleporteur
from interface import Interface


def charger_clients(chemin):
    """
    Construit la liste des clients (et de leurs voitures) à partir du fichier JSON.

    Args:
        chemin (str): Chemin du fichier JSON contenant le jeu de données.

    Returns:
        list[Client]: Les clients chargés, chacun déjà associé à sa voiture.
    """
    with open(chemin, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    clients = []
    for entree in donnees:
        infosClient = entree["client"]
        infosVoiture = entree["voiture"]

        client = Client(
            infosClient["nom"],
            infosClient["adresse"],
            infosClient["moyen_paiement"],
            infosClient["superabonne"],
        )
        voiture = Voiture(
            infosVoiture["hauteur"],
            infosVoiture["longueur"],
            infosVoiture["immatriculation"],
        )
        client.nouvellevoiture(voiture)
        clients.append(client)

    return clients


def main():
    parking = Parking(nbplaceParNiveau=5, nbPlaces=10)
    acces = Acces()
    borneTicket = BorneTicket()
    teleporteur = Teleporteur()
    interface = Interface()

    clients = charger_clients("donnees.json")
    tickets = {}

    print("=== Entrées dans le parking ===")
    acces.actionneauPanneau(parking)
    for client in clients:
        voiture = acces.actionnerCamera(client)
        if voiture is None:
            continue

        idplace = client.EntrerParking(parking)
        teleporteur.teleporterVoiture(voiture, parking.getPlace(idplace))

        # Les clients déjà super abonnés se voient garantir leur place.
        if idplace is not None and client.isSuperAbonne():
            parking.proposerAbonnement(client, idplace, choix=1)
        else:
            interface.proposerAbonnement(parking, client, idplace)

        ticket = borneTicket.delivrerTicket(client, idplace)
        if ticket is not None:
            tickets[voiture.getImmatriculation()] = ticket
            borneTicket.afficherTicket(ticket)

    print("\n=== État du parking après les entrées ===")
    acces.actionneauPanneau(parking)
    parking.afficheParkingGarantie()

    print("\n=== Demandes de services additionnels ===")
    if len(clients) >= 2:
        clients[0].demanderEntretien("2026-06-01", "2026-06-08", 45.0)
        clients[1].demanderMaintenance("2026-06-01", "2026-06-10", 120.0)
        clients[0].demanderLivraison("2026-06-12", "10h00", clients[0].adresse)

    print("\n=== Sorties du parking ===")
    for client in clients[:3]:
        immatriculation = client.voiture.getImmatriculation()
        ticket = tickets.get(immatriculation)
        if ticket is None:
            continue
        client.sortirParking(parking, ticket)
        print(f"{client.nom} ({immatriculation}) a quitté le parking : place {ticket['place']} libérée.")

    print("\n=== État du parking après les sorties ===")
    acces.actionneauPanneau(parking)
    parking.affichePlaceDisponnible()


if __name__ == "__main__":
    main()

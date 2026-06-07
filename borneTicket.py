class BorneTicket:
    """
    Borne délivrant un ticket de stationnement à chaque client qui entre dans le parking.

    Attributes:
        nbreTicket (int): Compteur du nombre total de tickets délivrés
            (variable de classe partagée par toutes les instances).
    """

    nbreTicket = 0

    def delivrerTicket(self, client, idplace):
        """
        Délivre un ticket à un client pour la place qui vient de lui être attribuée.
        Chaque délivrance incrémente le compteur partagé `nbreTicket`, qui sert
        ainsi de numéro de ticket.

        Args:
            client (Client): Le client à qui le ticket est délivré.
            idplace (str|None): L'identifiant de la place attribuée au client.

        Returns:
            dict|None: Le ticket délivré, ou None si aucune place n'a été attribuée.
        """
        if idplace is None:
            return None

        BorneTicket.nbreTicket += 1
        return {
            "numeroTicket": BorneTicket.nbreTicket,
            "nom": client.nom,
            "adresse": client.adresse,
            "immatriculation": client.voiture.getImmatriculation(),
            "place": idplace,
            "modePaiement": client.mp,
        }

    def afficherTicket(self, ticket):
        """
        Affiche un ticket de manière lisible.

        Args:
            ticket (dict|None): Le ticket à afficher.
        """
        if ticket is None:
            print("Aucun ticket à afficher.")
            return

        print("#------------------------------------------------#")
        print("|  Numéro ticket    :", ticket["numeroTicket"])
        print("|  Nom client       :", ticket["nom"])
        print("|  Adresse client   :", ticket["adresse"])
        print("|  Immatriculation  :", ticket["immatriculation"])
        print("|  Place attribuée  :", ticket["place"])
        print("|  Mode de paiement :", ticket["modePaiement"])
        print("#------------------------------------------------#")

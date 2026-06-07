from maintenance import Maintenance
from entretien import Entretien


class Client:
    """
    Un client du parking, pouvant être abonné ou super abonné et demander
    des services additionnels pour sa voiture.

    Attributes:
        nom (str): Nom du client.
        adresse (str): Adresse du client.
        mp (str): Mode de paiement du client.
        estAbonne (bool): Indique si le client est abonné.
        estSuperAbonne (bool): Indique si le client est un super abonné.
        voiture (Voiture|None): Voiture associée au client.
    """

    def __init__(self, nom, adresse, modeP, estSuperAbonne=False):
        self.nom = nom
        self.adresse = adresse
        self.mp = modeP
        self.estAbonne = False
        self.estSuperAbonne = estSuperAbonne
        self.voiture = None

    def nouvellevoiture(self, voiture):
        """
        Associe une nouvelle voiture au client.

        Args:
            voiture (Voiture): L'objet Voiture à associer au client.
        """
        self.voiture = voiture

    def isAbonne(self):
        return self.estAbonne

    def isSuperAbonne(self):
        return self.estSuperAbonne

    def setAbonne(self, abonnement):
        """
        Args:
            abonnement (bool): État d'abonnement à définir.
        """
        self.estAbonne = abonnement

    def setSuperAbonne(self, abonnement):
        """
        Args:
            abonnement (bool): État de super abonnement à définir.
        """
        self.estSuperAbonne = abonnement

    def Desabonner(self):
        """
        Désabonne le client (abonnement et super abonnement).
        """
        self.estAbonne = False
        self.estSuperAbonne = False

    def demanderMaintenance(self, dateDemande, dateService, apport):
        """
        Crée et effectue une demande de maintenance pour la voiture du client.

        Returns:
            dict: Le résumé de la maintenance effectuée.
        """
        maintenance = Maintenance(dateDemande, dateService, apport)
        resume = maintenance.effectuerMaintenance()
        print(f"{self.nom} a demandé une maintenance pour le {resume['dateService']}.")
        return resume

    def demanderEntretien(self, dateDemande, dateService, apport):
        """
        Crée et effectue une demande d'entretien pour la voiture du client.

        Returns:
            dict: Le résumé de l'entretien effectué.
        """
        entretien = Entretien(dateDemande, dateService, apport)
        resume = entretien.effectuerEntretien()
        print(f"{self.nom} a demandé un entretien pour le {resume['dateService']}.")
        return resume

    def demanderLivraison(self, dateLivraison, heure, adresseLiv):
        """
        Demande la livraison de la voiture du client à une adresse donnée.

        Args:
            dateLivraison (str): Date de livraison souhaitée.
            heure (str): Heure de livraison souhaitée.
            adresseLiv (str): Adresse de livraison souhaitée.

        Returns:
            dict: Les informations de la demande de livraison.
        """
        demande = {
            "client": self.nom,
            "immatriculation": self.voiture.getImmatriculation() if self.voiture else None,
            "dateLivraison": dateLivraison,
            "heure": heure,
            "adresseLivraison": adresseLiv,
        }
        print(
            f"{self.nom} a demandé la livraison de sa voiture le {dateLivraison} "
            f"à {heure} à l'adresse : {adresseLiv}."
        )
        return demande

    def sortirParking(self, parking, ticket):
        """
        Fait sortir le client (et sa voiture) du parking grâce à son ticket.

        Args:
            parking (Parking): Le parking dans lequel le client était garé.
            ticket (dict): Le ticket délivré à l'entrée.
        """
        if ticket is None:
            return
        parking.libererPlace(ticket["place"])
        if self.voiture is not None:
            self.voiture.setEstDansParking(False)

    def EntrerParking(self, parking):
        """
        Fait entrer le client (et sa voiture) dans le parking.

        Args:
            parking (Parking): Le parking dans lequel se garer.

        Returns:
            str|None: L'identifiant de la place attribuée, ou None si aucune place n'a pu être attribuée.
        """
        return parking.seGarer(self)

    def affiche(self):
        """
        Affiche les informations du client.
        """
        statut = "super abonné" if self.isSuperAbonne() else ("abonné" if self.isAbonne() else "non abonné")
        voiture = self.voiture.getImmatriculation() if self.voiture else "aucune voiture"
        print(f"{self.nom} ({self.adresse}) - {statut} - voiture : {voiture} - paiement : {self.mp}")

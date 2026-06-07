from place import Place


class Parking:
    """
    Gère les places de stationnement, les abonnés et les super abonnés d'un parking.

    Attributes:
        nbplaceParNiveau (int): Nombre de places par niveau.
        nbPlaces (int): Nombre total de places dans le parking.
        nbrePlacesLibre (int): Compteur de places actuellement libres.
        listePlace (dict): Places du parking, indexées par identifiant (ex. "A0").
        listeAbonnes (dict): Abonnés du parking, indexés par identifiant de place.
        parkingGarantie (list): Super abonnés en attente d'une place lorsque le parking est complet.
    """

    def __init__(self, nbplaceParNiveau, nbPlaces):
        self.nbplaceParNiveau = nbplaceParNiveau
        self.nbPlaces = nbPlaces
        self.nbrePlacesLibre = nbPlaces
        self.listePlace = dict()
        self.listeAbonnes = dict()
        self.parkingGarantie = list()
        self.initialiserPlacesDansParking()

    def creerPlace(self, place):
        """
        Ajoute une place au parking.

        Args:
            place (Place): La place à ajouter.
        """
        self.listePlace[place.identifiant()] = place

    def affiche(self):
        """
        Affiche l'état de chaque place du parking.
        """
        for idplace, place in self.listePlace.items():
            print(idplace, "-", place)

    def initialiserPlacesDansParking(self):
        """
        Crée toutes les places du parking, réparties par niveaux (A, B, C, ...)
        de `nbplaceParNiveau` places chacun, avec des dimensions variées.
        """
        for i in range(self.nbPlaces):
            niveau = chr(ord("A") + i // self.nbplaceParNiveau)
            numero = i % self.nbplaceParNiveau
            longueur = 3 + (i % 3)
            hauteur = 2 + (i % 2)
            self.creerPlace(Place(numero, niveau, longueur, hauteur))

    def proposerAbonnement(self, client, idplace, choix):
        """
        Applique le choix d'abonnement d'un client pour la place qu'il vient d'occuper.
        Cette méthode est volontairement non interactive : le menu de sélection
        est géré par la couche `interface`, afin que la logique métier reste testable.

        Args:
            client (Client): Le client qui se gare.
            idplace (str): Identifiant de la place qu'il occupe.
            choix (int): 1 = devenir super abonné, 2 = devenir abonné, autre = ne rien faire.
        """
        if choix == 1:
            client.setSuperAbonne(True)
            self.listeAbonnes[idplace] = client
            self.listePlace[idplace].setEstPourSuperAbonne(True)
            print(f"{client.nom} est désormais super abonné de la place {idplace}.")
        elif choix == 2:
            client.setAbonne(True)
            self.listeAbonnes[idplace] = client
            print(f"{client.nom} est désormais abonné du parking.")

    def seGarer(self, client):
        """
        Cherche une place libre compatible avec la voiture du client et l'y gare.
        Si le parking est complet, un super abonné est placé en liste d'attente
        prioritaire (`parkingGarantie`).

        Args:
            client (Client): Le client cherchant à se garer.

        Returns:
            str|None: L'identifiant de la place attribuée, ou None si aucune place
            n'a pu être attribuée.
        """
        voiture = client.voiture
        if voiture is None:
            print(f"{client.nom} ne peut pas entrer : aucune voiture détectée.")
            return None

        for idplace, place in self.listePlace.items():
            reserveePourAutrui = place.estPourSuperAbonne() and self.listeAbonnes.get(idplace) is not client
            if (not reserveePourAutrui
                    and place.estDisponible()
                    and voiture.getLongueur() <= place.longueur
                    and voiture.getHauteur() <= place.hauteur):
                place.setEstDisponible(False)
                self.nbrePlacesLibre -= 1
                voiture.setEstDansParking(True)
                voiture.addPlacementVoiture(place)
                print(f"Voiture {voiture.getImmatriculation()} garée à la place {idplace}.")
                return idplace

        print(f"Désolé, aucune place compatible n'est disponible pour la voiture {voiture.getImmatriculation()}.")
        if client.isSuperAbonne() and client not in self.parkingGarantie:
            self.parkingGarantie.append(client)
            print(f"{client.nom} (super abonné) est placé en liste d'attente prioritaire.")
        return None

    def affichePlaceDisponnible(self):
        """
        Affiche les identifiants des places actuellement disponibles.
        """
        disponibles = [idplace for idplace, place in self.listePlace.items() if place.estDisponible()]
        print(f"Places disponibles ({len(disponibles)}/{self.nbPlaces}) :", disponibles)
        return disponibles

    def libererPlace(self, idplace):
        """
        Libère une place de parking en fonction de son identifiant.

        Args:
            idplace (str): Identifiant de la place à libérer.
        """
        place = self.listePlace.get(idplace)
        if place is None or place.estDisponible():
            return
        place.setEstDisponible(True)
        self.nbrePlacesLibre += 1
        print(f"Place {idplace} libérée.")

    def getPlace(self, idplace):
        """
        Args:
            idplace (str|None): Identifiant de la place recherchée.

        Returns:
            Place|None: La place correspondante, ou None si elle n'existe pas.
        """
        if idplace is None:
            return None
        return self.listePlace.get(idplace)

    def afficheParkingGarantie(self):
        """
        Affiche les super abonnés actuellement en attente d'une place garantie.
        """
        if not self.parkingGarantie:
            print("Aucun super abonné en attente d'une place.")
            return
        print("Super abonnés en attente d'une place garantie :")
        for client in self.parkingGarantie:
            print(f" - {client.nom} ({client.voiture.getImmatriculation()})")

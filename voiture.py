class Voiture:
    """
    Une voiture pouvant entrer, stationner et sortir d'un parking.

    Attributes:
        hauteur (float): Hauteur de la voiture en mètres.
        longueur (float): Longueur de la voiture en mètres.
        immatriculation (str): Plaque d'immatriculation de la voiture.
        estDansParking (bool): Indique si la voiture est actuellement garée.
        placement (Place|None): Place actuellement occupée par la voiture, le cas échéant.
    """

    def __init__(self, hauteur, longueur, immatriculation):
        self.hauteur = hauteur
        self.longueur = longueur
        self.immatriculation = immatriculation
        self.estDansParking = False
        self.placement = None

    def addPlacementVoiture(self, placement):
        """
        Mémorise la place sur laquelle la voiture vient de se garer.

        Args:
            placement (Place): La place occupée par la voiture.
        """
        self.placement = placement

    def getPlacement(self):
        """
        Returns:
            Place|None: La place actuellement occupée par la voiture, ou None.
        """
        return self.placement

    def setEstDansParking(self, etat):
        """
        Définit si la voiture se trouve dans le parking.

        Args:
            etat (bool): True si la voiture est dans le parking, False sinon.
        """
        self.estDansParking = etat
        if not etat:
            self.placement = None

    def getEstDansParking(self):
        """
        Returns:
            bool: True si la voiture est dans le parking, False sinon.
        """
        return self.estDansParking

    def getHauteur(self):
        return self.hauteur

    def getLongueur(self):
        return self.longueur

    def getImmatriculation(self):
        return self.immatriculation

    def __repr__(self):
        return f"Voiture {self.immatriculation} ({self.longueur}m x {self.hauteur}m)"

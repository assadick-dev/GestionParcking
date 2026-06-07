class Place:
    """
    Une place de parking individuelle.

    Attributes:
        numero (int): Numéro unique de la place.
        niveau (str): Niveau du parking où se situe la place.
        longueur (float): Longueur de la place en mètres.
        hauteur (float): Hauteur de la place en mètres.
        disponible (bool): Indique si la place est actuellement disponible.
        pourSuperAbonne (bool): Indique si la place est réservée pour les super abonnés.
    """

    def __init__(self, numero, niveau, longueur, hauteur):
        self.numero = numero
        self.niveau = niveau
        self.longueur = longueur
        self.hauteur = hauteur
        self.disponible = True
        self.pourSuperAbonne = False

    def estDisponible(self):
        """
        Returns:
            bool: True si la place est disponible, False sinon.
        """
        return self.disponible

    def setEstDisponible(self, disponible):
        """
        Définit l'état de disponibilité de la place.

        Args:
            disponible (bool): Nouvel état de disponibilité de la place.
        """
        self.disponible = disponible

    def estPourSuperAbonne(self):
        """
        Returns:
            bool: True si la place est réservée pour les super abonnés, False sinon.
        """
        return self.pourSuperAbonne

    def setEstPourSuperAbonne(self, pourSuperAbonne):
        """
        Définit si la place est réservée pour les super abonnés.

        Args:
            pourSuperAbonne (bool): Nouvel état de réservation pour super abonnés.
        """
        self.pourSuperAbonne = pourSuperAbonne

    def identifiant(self):
        """
        Returns:
            str: Identifiant unique de la place, basé sur son niveau et son numéro.
        """
        return f"{self.niveau}{self.numero}"

    def __repr__(self):
        etat = "libre" if self.estDisponible() else "occupée"
        return f"Place {self.identifiant()} ({self.longueur}m x {self.hauteur}m, {etat})"

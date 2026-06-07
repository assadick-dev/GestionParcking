class Camera:
    """
    Capture les caractéristiques d'une voiture qui se présente à l'entrée du parking.
    """

    def capturerLongueur(self, voiture):
        """
        Returns:
            float: La longueur capturée de la voiture.
        """
        return voiture.getLongueur()

    def capturerHauteur(self, voiture):
        """
        Returns:
            float: La hauteur capturée de la voiture.
        """
        return voiture.getHauteur()

    def capturerImmatriculation(self, voiture):
        """
        Returns:
            str: L'immatriculation capturée de la voiture.
        """
        return voiture.getImmatriculation()

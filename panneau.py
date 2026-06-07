class PanneauAffichage:
    """
    Panneau lumineux affichant le nombre de places disponibles dans le parking.
    """

    def afficherNbrePlaceDisponible(self, parking):
        """
        Affiche et retourne le nombre de places actuellement disponibles dans le parking.

        Args:
            parking (Parking): Le parking à afficher.

        Returns:
            int: Le nombre de places disponibles.
        """
        nbreDisponible = parking.nbrePlacesLibre
        print(f"Panneau : {nbreDisponible} place(s) disponible(s) sur {parking.nbPlaces}.")
        return nbreDisponible

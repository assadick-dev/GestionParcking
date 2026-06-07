class Teleporteur:
    """
    Achemine (symboliquement) une voiture vers la place qui lui a été attribuée.
    """

    def teleporterVoiture(self, voiture, place):
        """
        Déplace la voiture vers la place indiquée et mémorise ce placement.

        Args:
            voiture (Voiture): La voiture à déplacer.
            place (Place|None): La place de destination.
        """
        if place is None:
            print(f"Aucune place disponible pour la voiture {voiture.getImmatriculation()}.")
            return

        voiture.addPlacementVoiture(place)
        print(
            f"Voiture {voiture.getImmatriculation()} téléportée à la place {place.identifiant()}."
        )

    def teleporterVoitureSuperAbonne(self, voiture):
        """
        Reconduit la voiture d'un super abonné vers sa place habituelle.

        Args:
            voiture (Voiture): La voiture du super abonné à reconduire.
        """
        place = voiture.getPlacement()
        if place is None:
            print(f"La voiture {voiture.getImmatriculation()} n'a pas encore de place habituelle.")
            return
        print(
            f"Voiture {voiture.getImmatriculation()} (super abonné) reconduite "
            f"à sa place habituelle {place.identifiant()}."
        )

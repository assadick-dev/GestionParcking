from camera import Camera
from panneau import PanneauAffichage


class Acces:
    """
    Point d'accès au parking : orchestre la caméra (détection d'une voiture
    à l'entrée) et le panneau d'affichage (places disponibles).
    """

    def __init__(self):
        self.camera = Camera()
        self.panneau = PanneauAffichage()

    def actionnerCamera(self, client):
        """
        Active la caméra pour détecter la voiture d'un client qui se présente
        à l'entrée du parking.

        Args:
            client (Client): Le client dont la voiture doit être détectée.

        Returns:
            Voiture|None: La voiture détectée, ou None si le client n'a pas de voiture.
        """
        voiture = client.voiture
        if voiture is None:
            print(f"Caméra : aucune voiture détectée pour {client.nom}.")
            return None

        longueur = self.camera.capturerLongueur(voiture)
        hauteur = self.camera.capturerHauteur(voiture)
        immatriculation = self.camera.capturerImmatriculation(voiture)
        print(f"Caméra : voiture {immatriculation} détectée ({longueur}m x {hauteur}m).")
        return voiture

    def actionneauPanneau(self, parking):
        """
        Active le panneau de signalisation pour afficher le nombre de places
        disponibles dans le parking.

        Args:
            parking (Parking): Le parking concerné.

        Returns:
            int: Le nombre de places disponibles affiché.
        """
        return self.panneau.afficherNbrePlaceDisponible(parking)

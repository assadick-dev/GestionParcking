from service import Service


class Entretien(Service):
    """
    Service d'entretien d'une voiture (nettoyage, contrôle technique, etc.).
    """

    def __init__(self, dateDemande, dateService, apport):
        super().__init__(dateDemande, dateService, apport)

    def effectuerEntretien(self):
        """
        Réalise l'entretien et retourne son résumé.

        Returns:
            dict: Les informations de l'entretien effectué.
        """
        return self.resume()

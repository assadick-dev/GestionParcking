from service import Service


class Maintenance(Service):
    """
    Service de maintenance d'une voiture (révision, réparation, etc.).
    """

    def __init__(self, dateDemande, dateService, apport):
        super().__init__(dateDemande, dateService, apport)

    def effectuerMaintenance(self):
        """
        Réalise la maintenance et retourne son résumé.

        Returns:
            dict: Les informations de la maintenance effectuée.
        """
        return self.resume()

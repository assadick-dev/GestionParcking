class Service:
    """
    Représente un service demandé et fourni dans le cadre de la gestion d'un client.

    Attributes:
        dateDemande (str): Date à laquelle la demande de service a été effectuée.
        dateService (str): Date prévue ou réelle de la prestation du service.
        apport (float): Coût ou bénéfice apporté par le service.
    """

    def __init__(self, dateDemande, dateService, apport):
        self.dateDemande = dateDemande
        self.dateService = dateService
        self.apport = apport

    def resume(self):
        """
        Retourne un résumé du service sous forme de dictionnaire.

        Returns:
            dict: Les informations du service (dates et apport).
        """
        return {
            "dateDemande": self.dateDemande,
            "dateService": self.dateService,
            "apport": self.apport,
        }

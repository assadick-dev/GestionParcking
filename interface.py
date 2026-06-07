class Interface:
    """
    Couche d'interaction utilisateur (menus en console).

    Elle est volontairement séparée de la logique métier (`Parking`, `Client`, ...)
    afin que celle-ci reste testable sans simuler des entrées clavier (`input`).
    """

    def proposerAbonnement(self, parking, client, idplace):
        """
        Propose à un client qui vient de se garer de devenir abonné ou super abonné,
        puis applique son choix via `parking.proposerAbonnement`.

        Args:
            parking (Parking): Le parking concerné.
            client (Client): Le client qui vient de se garer.
            idplace (str|None): Identifiant de la place qu'il occupe.
        """
        if idplace is None or client.isAbonne() or client.isSuperAbonne():
            return

        print(f"\n--- Bienvenue {client.nom}, propriétaire de {client.voiture.getImmatriculation()} ---")
        print("1. Devenir super abonné (place garantie)")
        print("2. Devenir abonné")
        print("3. Ne pas s'abonner")

        try:
            choix = int(input("Votre choix : "))
        except (ValueError, EOFError):
            choix = 3

        parking.proposerAbonnement(client, idplace, choix)

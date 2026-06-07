import unittest

from parking import Parking
from client import Client
from voiture import Voiture
from camera import Camera
from acces import Acces
from borneTicket import BorneTicket


class TestParkingSystem(unittest.TestCase):
    """
    Tests unitaires du système de gestion de parking.
    """

    def setUp(self):
        self.parking = Parking(nbplaceParNiveau=5, nbPlaces=10)
        self.camera = Camera()
        self.acces = Acces()
        self.borneTicket = BorneTicket()

        self.client1 = Client('Assadick', '31100, Toulouse', 'CB')
        self.voiture1 = Voiture(2, 3, "EF-441-TX")
        self.client1.nouvellevoiture(self.voiture1)

    def test_ajout_client_et_voiture(self):
        self.assertEqual(self.client1.voiture, self.voiture1)
        self.assertEqual(self.client1.nom, 'Assadick')

    def test_capture_camera(self):
        self.assertEqual(self.camera.capturerLongueur(self.voiture1), 3)
        self.assertEqual(self.camera.capturerHauteur(self.voiture1), 2)
        self.assertEqual(self.camera.capturerImmatriculation(self.voiture1), "EF-441-TX")

    def test_entree_parking(self):
        voiture_detectee = self.acces.actionnerCamera(self.client1)
        self.assertIsNotNone(voiture_detectee, "La voiture n'a pas été détectée à l'accès.")

        idplace = self.client1.EntrerParking(self.parking)
        self.assertIsNotNone(idplace, "Aucune place n'a été attribuée.")
        self.assertTrue(self.voiture1.getEstDansParking())
        self.assertIs(self.voiture1.getPlacement(), self.parking.getPlace(idplace))

    def test_generation_ticket(self):
        idplace = self.client1.EntrerParking(self.parking)
        ticket = self.borneTicket.delivrerTicket(self.client1, idplace)

        self.assertIsNotNone(ticket, "Le ticket n'a pas été généré.")
        self.assertEqual(ticket['place'], idplace)
        self.assertEqual(ticket['immatriculation'], "EF-441-TX")

    def test_pas_de_ticket_sans_place(self):
        self.assertIsNone(self.borneTicket.delivrerTicket(self.client1, None))

    def test_sortie_parking(self):
        idplace = self.client1.EntrerParking(self.parking)
        ticket = self.borneTicket.delivrerTicket(self.client1, idplace)

        self.client1.sortirParking(self.parking, ticket)

        self.assertFalse(self.voiture1.getEstDansParking(), "La voiture n'est pas sortie du parking.")
        self.assertTrue(self.parking.getPlace(idplace).estDisponible(), "La place n'a pas été libérée.")

    def test_places_disponibles(self):
        disponibles = self.parking.affichePlaceDisponnible()
        self.assertEqual(len(disponibles), self.parking.nbrePlacesLibre)
        self.assertGreater(self.parking.nbrePlacesLibre, 0, "Aucune place disponible dans le parking.")

    def test_abonnement_super_abonne(self):
        idplace = self.client1.EntrerParking(self.parking)

        self.parking.proposerAbonnement(self.client1, idplace, choix=1)

        self.assertTrue(self.client1.isSuperAbonne())
        self.assertTrue(self.parking.getPlace(idplace).estPourSuperAbonne())
        self.assertIs(self.parking.listeAbonnes[idplace], self.client1)

    def test_voiture_trop_grande_rejoint_parking_garantie(self):
        # Construit un parking dont aucune place ne peut accueillir la voiture du client.
        petit_parking = Parking(nbplaceParNiveau=2, nbPlaces=2)
        for place in petit_parking.listePlace.values():
            place.longueur = 1
            place.hauteur = 1

        self.client1.setSuperAbonne(True)
        idplace = self.client1.EntrerParking(petit_parking)

        self.assertIsNone(idplace)
        self.assertIn(self.client1, petit_parking.parkingGarantie)


if __name__ == '__main__':
    unittest.main()

# Projet Python — Gestion de Parking

Système de gestion d'un parking automatisé : entrée/sortie des véhicules,
attribution des places, abonnements, services additionnels (entretien,
maintenance, livraison) et suivi des super-abonnés.

Ce dépôt regroupe en une seule version (branche `main`) ce qui était
auparavant éclaté entre les branches `partie0` (squelette de classes) et
`partie1` (premier jet de logique métier). Le code a été restructuré,
nettoyé des incohérences/typos accumulées au fil des itérations, et complété.

## Objectifs du projet

1. **Modéliser le domaine** : Parking, Place, Voiture, Client, Service
   (Maintenance / Entretien), Ticket.
2. **Gérer le cycle de vie d'un stationnement** :
   - un client se présente avec sa voiture → la caméra capture ses
     caractéristiques (longueur, hauteur, immatriculation) ;
   - le système cherche une place libre compatible et gare la voiture ;
   - une borne délivre un ticket ;
   - à la sortie, le ticket permet de libérer la place.
3. **Gérer les abonnements** : un client peut devenir abonné ou
   super-abonné ; les super-abonnés disposent d'une place garantie même
   lorsque le parking est complet (liste « parking garanti »).
4. **Gérer les services additionnels** liés à un client : demande de
   maintenance, d'entretien ou de livraison de véhicule.
5. **Simuler un scénario complet** à partir d'un jeu de données
   (`donnees.json`) rejouant l'arrivée de plusieurs clients, et vérifier
   le comportement via une suite de tests unitaires.

## Architecture

| Fichier | Rôle |
|---|---|
| `place.py` | Une place de parking (numéro, niveau, dimensions, disponibilité). |
| `voiture.py` | Une voiture (dimensions, immatriculation, état de stationnement). |
| `client.py` | Un client du parking (identité, voiture, abonnement, services demandés). |
| `service.py` | Classe de base d'un service rendu à un client (date, apport). |
| `maintenance.py`, `entretien.py` | Services spécialisés héritant de `Service`. |
| `camera.py` | Capture des caractéristiques d'une voiture détectée. |
| `panneau.py` | Panneau d'affichage du nombre de places disponibles. |
| `acces.py` | Point d'accès qui orchestre caméra + panneau lors d'une entrée. |
| `borneTicket.py` | Délivrance et affichage des tickets de stationnement. |
| `teleporteur.py` | Acheminement (symbolique) d'une voiture vers sa place. |
| `parking.py` | Cœur du système : places, abonnés, attribution/libération de places. |
| `interface.py` | Couche d'interaction (menus en console), séparée de la logique métier pour rester testable. |
| `main.py` | Scénario de simulation rejouant `donnees.json`. |
| `classeTest.py` | Suite de tests unitaires (`unittest`) du système. |

La logique métier (`parking.py`, `client.py`, …) ne fait aucun appel à
`input()` : les interactions utilisateur sont concentrées dans
`interface.py`, ce qui permet de tester le cœur du système sans
simulation d'entrées clavier.

## Utilisation

```bash
# Lancer la simulation
python3 main.py

# Lancer les tests unitaires
python3 -m unittest classeTest.py -v
```

## Auteur

Abdelrahim Annadif Assadick — Master MI, Université Toulouse 2.

"""
main.py - Menu principal du quiz
TÂCHE 1

À faire :
- Afficher un menu en boucle (while) : 1) Jouer  2) Classement  3) Quitter
- Réagir au choix avec match/case (ou if/elif/else)
- Gérer un choix invalide
- Lors d'une partie : demander le nom, appeler jouer(), calculer le score,
  afficher le résultat et enregistrer le score dans le classement.

Compétences : while, conditions, input
"""
from questions import get_questions
from jeu import jouer
from score import calculer_score, get_mention
from classement import ajouter_score, afficher_top3
from affichage import afficher_titre, afficher_resultat


def afficher_menu():
    # TODO : afficher les 3 options du menu
    pass


def lancer_partie():
    # TODO :
    # 1. demander le nom du joueur
    # 2. questions = get_questions()
    # 3. bonnes = jouer(questions)
    # 4. pourcentage = calculer_score(bonnes, len(questions))
    # 5. mention = get_mention(pourcentage)
    # 6. afficher_resultat(nom, pourcentage, mention)
    # 7. ajouter_score(nom, pourcentage)
    pass


def main():
    afficher_titre("QUIZ PYTHON")
    # TODO : boucle while avec le menu et match/case
    pass


if __name__ == "__main__":
    main()

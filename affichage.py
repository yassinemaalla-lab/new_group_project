"""
affichage.py - Rendu dans le terminal
TÂCHE 6

À faire :
- afficher_titre(texte) : titre encadré, par exemple
    |--------------|
    |  QUIZ PYTHON |
    |--------------|
  (inspirez-vous de draw_rectangle du jour 7-8)
- afficher_question(numero, question) : affiche le numéro, l'énoncé et les choix
  (question est un dictionnaire, voir le contrat dans questions.py)
- afficher_resultat(nom, pourcentage, mention) : affiche le résultat final

Compétences : boucles, chaînes de caractères, formatage
"""


def afficher_titre(texte):
    largeur = len(texte) + 2          # +2 pour un espace de chaque côté
    print("|" + "-" * largeur + "|")
    print("| " + texte + " |")
    print("|" + "-" * largeur + "|")
if __name__ == "__main__":
  afficher_titre("QUIZ PYTHON")

def afficher_question(numero, question):
    # TODO
    pass


def afficher_resultat(nom, pourcentage, mention):
    # TODO
    pass

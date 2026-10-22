"""
questions.py - Banque de questions
TÂCHE 2

CONTRAT (ne pas changer sans prévenir le groupe) :
une question est un dictionnaire avec ces 4 clés :
    "question"  : str
    "choix"     : liste de str (ex: ["A) ...", "B) ...", "C) ..."])
    "reponse"   : str, la lettre de la bonne réponse ("A", "B" ou "C")
    "categorie" : str (ex: "variables", "boucles", "listes", "git")

À faire :
- Ajouter au moins 10 questions dans QUESTIONS
- Compléter get_questions() et filtrer_par_categorie()

Compétences : listes, dictionnaires, fonctions, return
"""

QUESTIONS = [
    {
        "question": "Quelle fonction affiche du texte dans le terminal ?",
        "choix": ["A) show()", "B) print()", "C) echo()"],
        "reponse": "B",
        "categorie": "variables",
    },
    {
        "question": "Quelle commande Git envoie vos commits sur GitHub ?",
        "choix": ["A) git pull", "B) git clone", "C) git push"],
        "reponse": "C",
        "categorie": "git",
    },
    # TODO : ajouter au moins 8 autres questions
]


def get_questions():
    # TODO : retourner la liste des questions
    pass


def filtrer_par_categorie(categorie):
    # TODO : retourner uniquement les questions de la catégorie donnée
    pass

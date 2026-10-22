# Quiz en terminal

Projet de groupe Python + Git.

## Lancer le quiz
```bash
python3 main.py
```

## Répartition des tâches

| Tâche | Fichier | Responsable |
|---|---|---|
| 1 | `main.py` | |
| 2 | `questions.py` | |
| 3 | `jeu.py` | |
| 4 | `score.py` | |
| 5 | `classement.py` | |
| 6 | `affichage.py` | |
| 7 (bonus) | `utils.py` | |

Écrivez votre nom dans la colonne « Responsable » (via votre branche) **avant** de commencer.

## Workflow Git

```bash
git clone <url-du-depot>
cd quiz
git switch -c tache-<nom-du-fichier>
# ... vous codez dans VOTRE fichier uniquement ...
git add <votre-fichier>
git commit -m "Message explicite"
git push origin tache-<nom-du-fichier>
```
Puis ouvrir une Pull Request vers `master`.

Avant de reprendre le travail : `git pull origin master`.

## Règles
- Un fichier = une personne (pas de modification des fichiers des autres sans prévenir).
- Ne pas changer les noms des fonctions ni le format des questions (contrat dans `questions.py`).
- Pas de push direct sur `master`.
- Commentez votre code.

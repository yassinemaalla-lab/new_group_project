# Quiz en terminal

Projet de groupe Python + Git. Chacun code une partie du quiz dans **son propre fichier**.

---

## 1. Lancer le quiz complet

Dans le terminal, depuis le dossier du projet :

```bash
python3 main.py
```

> Le quiz ne fonctionnera entièrement qu'une fois toutes les tâches terminées et fusionnées.
> En attendant, testez **votre fichier seul** (voir ci-dessous).

---

## 2. Tester SON fichier seul (débutants)

Un fichier qui contient seulement des fonctions **n'affiche rien** quand on le lance : Python enregistre les fonctions, mais personne ne les appelle. Il faut ajouter un petit bloc de test **tout en bas** du fichier.

### Exemple pour `affichage.py`

```python
def afficher_titre(texte):
    largeur = len(texte) + 2
    print("|" + "-" * largeur + "|")
    print("| " + texte + " |")
    print("|" + "-" * largeur + "|")


if __name__ == "__main__":
    afficher_titre("QUIZ PYTHON")
```

Puis lancez votre fichier :

```bash
python3 affichage.py
```

Résultat attendu :

```
|-------------|
| QUIZ PYTHON |
|-------------|
```

### Les 4 règles à retenir

1. **Enregistrez** le fichier (`Ctrl+S` dans VS Code) avant de le lancer.
2. Le bloc `if __name__ == "__main__":` est **collé à la marge gauche**, après toutes les fonctions.
3. À l'intérieur, vous **appelez vos fonctions** avec des valeurs de test.
4. Ce bloc est ignoré quand un autre fichier importe le vôtre : vous pouvez le laisser.

### Tester une fonction qui retourne une valeur

Une fonction avec `return` ne **montre** rien : il faut afficher le résultat avec `print`.

```python
def calculer_score(bonnes, total):
    return bonnes / total * 100


if __name__ == "__main__":
    print(calculer_score(3, 4))    # attendu : 75.0
    print(calculer_score(0, 10))   # attendu : 0.0
```

Testez plusieurs cas, y compris les cas limites (liste vide, 0, réponse invalide...).

---

## 3. Erreurs fréquentes

| Message ou symptôme | Cause probable | Solution |
|---|---|---|
| Rien ne s'affiche | Aucun appel de fonction | Ajoutez le bloc `if __name__ == "__main__":` |
| `IndentationError: unexpected indent` | Lignes d'un même bloc mal alignées | 4 espaces partout dans le bloc (`Shift+Tab` dans VS Code) |
| `IndentationError: expected an indented block` | Rien d'indenté après `def`, `if`, `for`... | Indentez la ligne suivante ou mettez `pass` |
| `SyntaxError` | Parenthèse, guillemet ou `:` oublié | Regardez la ligne indiquée et celle d'avant |
| `NameError: name 'x' is not defined` | Variable ou fonction pas définie, ou faute de frappe | Vérifiez l'orthographe et l'ordre |
| `TypeError: can't multiply sequence by non-int` | Vous multipliez une chaîne par une chaîne | Utilisez `len(...)` ou un nombre |
| `ModuleNotFoundError` | Vous n'êtes pas dans le bon dossier | `cd ~/projet_python_git` puis relancez |
| `python3: can't open file` | Mauvais dossier ou mauvais nom | `ls` pour voir les fichiers présents |

**Astuce :** lisez toujours la **dernière ligne** du message d'erreur (le type d'erreur) et le **numéro de ligne** indiqué au-dessus.

### Déboguer avec `print`

Si le résultat n'est pas celui attendu, affichez les variables à chaque étape :

```python
print("DEBUG bonnes =", bonnes, "total =", total)
```

Supprimez ces `print` avant de faire votre commit.

---

## 4. Répartition des tâches

| Tâche | Fichier | Responsable |
|---|---|---|
| 1 | `main.py` | |
| 2 | `questions.py` | |
| 3 | `jeu.py` | |
| 4 | `score.py` | |
| 5 | `classement.py` | |
| 6 | `affichage.py` | |
| 7 (bonus) | `utils.py` | |


### Doublons autorisés

Si plusieurs personnes veulent la même tâche, chacune crée **son propre fichier** avec son prénom :

```
questions.py            <- version officielle
questions_yassine.py    <- version de lucas
questions_sara.py       <- version de Sara
```

Chaque version respecte le même « contrat » (mêmes noms de fonctions, même format de données). Le groupe choisit ensuite la meilleure version, ou combine les idées. Un fichier créé par quelqu'un n'est jamais modifié par un autre.

---

## 5. Le contrat entre les fichiers

Ne changez pas ces noms sans prévenir le groupe.

- Une question est un dictionnaire :
  `{"question": "...", "choix": ["A) ...", "B) ..."], "reponse": "B", "categorie": "git"}`
- `jouer(questions)` reçoit une liste de questions et retourne le nombre de bonnes réponses (entier).
- `calculer_score(bonnes, total)` retourne un pourcentage entre 0 et 100.
- Un score de classement est un dictionnaire : `{"nom": "eric", "score": 80}`.

---

## 6. Workflow Git (pas à pas)

### Première fois

```bash
git clone https://github.com/yassinemaalla-lab/new_group_project.git
cd new_group_project
```

### Pour chaque tâche

```bash
git switch -c tache-<fichier>       # exemple : tache-questions
# ... vous codez dans VOTRE fichier ...
python3 <votre-fichier>.py          # testez !
git status                          # vérifiez ce qui a changé
git add <votre-fichier>.py
git commit -m "Message explicite"   # exemple : "Ajout de afficher_titre"
git push origin tache-<fichier>
```

Puis sur GitHub : bouton **Compare & pull request**, base `main`, et demandez à un camarade de relire.

### Récupérer le travail des autres

```bash
git switch main
git pull origin main
```

### En cas de problème

| Erreur | Solution |
|---|---|
| `fatal: not a git repository` | Vous n'êtes pas dans le dossier du projet : `cd` dedans |
| `Permission denied` / `403` au push | Vous n'êtes pas encore collaborateur : acceptez l'invitation reçue par mail |
| `rejected ... fetch first` | Faites `git pull origin main` puis réessayez |
| `nothing to commit` | Vous avez oublié d'enregistrer ou de faire `git add` |

---

## 7. Règles du groupe

- Pas de push direct sur `main` : passez par une Pull Request.
- Commentez votre code (au moins une phrase par fonction).
- Pas de mot de passe ni d'information privée : le dépôt est public.
- Demandez de l'aide dès que vous bloquez.

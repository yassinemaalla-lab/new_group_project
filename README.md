# Quiz en terminal

Projet de groupe **Python + Git**. Chacun code une petite partie du quiz, on assemble le tout à la fin.
Ce guide est écrit pour des **débutants** : suivez les étapes dans l'ordre, une par une.

## Sommaire

1. [Ce qu'on construit](#1-ce-quon-construit)
2. [Avant de commencer](#2-avant-de-commencer)
3. [Pas à pas : de zéro à ma première contribution](#3-pas-à-pas--de-zéro-à-ma-première-contribution)
4. [Où coder ? Les 7 tâches en détail](#4-où-coder--les-7-tâches-en-détail)
5. [Tester son code](#5-tester-son-code)
6. [Erreurs fréquentes](#6-erreurs-fréquentes)
7. [Petit lexique Git](#7-petit-lexique-git)
8. [Le contrat entre les fichiers](#8-le-contrat-entre-les-fichiers)
9. [Règles du groupe](#9-règles-du-groupe)
10. [Check-list avant d'envoyer son travail](#10-check-list-avant-denvoyer-son-travail)

---

## 1. Ce qu'on construit

Un quiz qui se joue dans le terminal. Voilà ce que le joueur verra à la fin :

```
|-------------|
| QUIZ PYTHON |
|-------------|

1) Jouer
2) Voir le classement
3) Quitter
Votre choix : 1
Votre nom : Sara

Question 1 : Quelle commande Git envoie vos commits sur GitHub ?
  A) git pull
  B) git clone
  C) git push
Votre réponse (A, B ou C) : C

...

Bravo Sara ! Score : 75.0% - Mention : Très bon
```

Le programme est découpé en **7 fichiers**. Chaque fichier correspond à une **tâche**. Chaque personne choisit une tâche et ne code que dans le fichier correspondant.

| Fichier | Son rôle en une phrase |
|---|---|
| `main.py` | Le menu principal, qui relie tout |
| `questions.py` | Les questions du quiz |
| `jeu.py` | Le déroulement d'une partie |
| `score.py` | Le calcul du score et de la mention |
| `classement.py` | La liste des meilleurs scores |
| `affichage.py` | Tout ce qui s'affiche joliment à l'écran |
| `utils.py` | Bonus (facultatif) |

---

## 2. Avant de commencer

Vérifiez que tout est installé. Ouvrez un terminal et tapez ces commandes **une par une** :

```bash
python3 --version
git --version
```

Chacune doit afficher un numéro de version (par exemple `Python 3.12.3`). Si vous voyez `command not found`, demandez de l'aide au groupe.

Il vous faut aussi :

- un compte **GitHub** ;
- l'**invitation** à rejoindre le dépôt (vous la recevez par mail, il faut cliquer sur « Accept invitation ») ;
- **VS Code** pour écrire le code.

> **Important** : dans ce guide, les blocs gris avec `git ...` ou `python3 ...` sont à taper **dans le terminal**. Ne collez jamais le résultat affiché par le terminal, seulement les commandes.

---

## 3. Pas à pas : de zéro à ma première contribution

### Étape 1 : Récupérer le projet (une seule fois)

Dans le terminal :

```bash
git clone https://github.com/yassinemaalla-lab/new_group_project.git
cd new_group_project
ls
```

Le `ls` doit afficher : `README.md  affichage.py  classement.py  jeu.py  main.py  questions.py  score.py  utils.py`.

### Étape 2 : Ouvrir le projet dans VS Code

Dans le terminal, toujours dans le dossier `new_group_project` :

```bash
code .
```

Sinon, dans VS Code : **File > Open Folder** et choisissez le dossier `new_group_project`.
Vous voyez alors la liste des fichiers à gauche. C'est dans ces fichiers que vous allez coder.

### Étape 3 : Choisir sa tâche

Regardez le tableau de la [section 4](#4-où-coder--les-7-tâches-en-détail) et choisissez la tâche qui vous plaît. Plusieurs personnes peuvent travailler sur la même, c'est autorisé.

Si vous voulez éviter d'écraser le fichier d'un camarade, créez **votre propre fichier** avec votre prénom, par exemple `score_sara.py`.

### Étape 4 : Créer sa branche

Une **branche** est une copie de travail à vous, qui ne gêne personne. Dans le terminal :

```bash
git switch -c tache-score
```

Remplacez `score` par le nom de votre fichier. Pour vérifier que vous êtes bien sur votre branche :

```bash
git branch
```

Votre branche doit avoir une étoile `*` devant son nom.

### Étape 5 : Coder

1. Dans VS Code, cliquez sur **votre fichier** dans la liste de gauche.
2. Lisez le grand commentaire en haut du fichier (entre les `"""`) : ce sont les consignes.
3. Cherchez les lignes qui contiennent `# TODO` : c'est **là que vous devez écrire du code**.
4. **Supprimez le mot `pass`** et écrivez votre code à la place, avec la même indentation (4 espaces).

Exemple, avant :

```python
def calculer_score(bonnes, total):
    # TODO
    pass
```

Après :

```python
def calculer_score(bonnes, total):
    return bonnes / total * 100
```

> **Comprendre `pass`** : c'est un mot qui veut dire « ne rien faire ». Il sert à garder une fonction vide sans erreur. Dès que votre fonction contient du vrai code, supprimez-le.

> **Indentation** : tout ce qui est dans une fonction, une boucle ou un `if` doit être décalé de **4 espaces** vers la droite, toutes les lignes du même bloc avec exactement le même décalage. Dans VS Code : `Tab` pour décaler, `Shift+Tab` pour revenir en arrière.

### Étape 6 : Tester

Voir la [section 5](#5-tester-son-code). **Ne passez pas à l'étape suivante tant que votre fichier ne marche pas.**

### Étape 7 : Enregistrer et envoyer son travail

Enregistrez le fichier dans VS Code (`Ctrl+S`), puis dans le terminal :

```bash
git status
```

Vous devez voir votre fichier en rouge (modifié). Ensuite :

```bash
git add score.py
git commit -m "Ajout de calculer_score et get_mention"
git push -u origin HEAD
```

- Remplacez `score.py` par **votre** fichier.
- Remplacez le message entre guillemets par une phrase qui explique ce que vous avez fait.
- `git push -u origin HEAD` envoie **la branche sur laquelle vous êtes**, sans avoir à écrire son nom.

### Étape 8 : Ouvrir une Pull Request

Une **Pull Request** est une demande pour ajouter votre travail au projet principal (`main`).

1. Allez sur `https://github.com/yassinemaalla-lab/new_group_project`.
2. Juste après votre push, un **bandeau jaune** apparaît en haut de la page avec le bouton **Compare & pull request**. Cliquez dessus.
   S'il n'apparaît pas : onglet **Pull requests**, puis **New pull request**, et choisissez votre branche.
3. Vérifiez que `base` est bien `main`. C'est l'endroit où votre travail doit **arriver** (votre branche est celle d'où il **vient**).
4. Écrivez un titre qui dit ce que vous ajoutez, par exemple « Ajout de score.py ».
5. Cliquez sur **Create pull request**.
6. Sur la même page, cliquez sur **Merge pull request**, puis **Confirm merge**. Votre travail est maintenant dans `main`.

### Étape 9 : Récupérer le travail des autres

Quand des PR ont été fusionnées, mettez votre copie à jour :

```bash
git switch main
git pull origin main
```

Pour commencer une nouvelle tâche, repartez de l'étape 4.

---

## 4. Où coder ? Les 7 tâches en détail

Choisissez la tâche que vous voulez, n'importe laquelle.

| Tâche | Fichier | Difficulté |
|---|---|---|
| 1 | `main.py` | moyenne |
| 2 | `questions.py` | facile |
| 3 | `jeu.py` | moyenne |
| 4 | `score.py` | facile |
| 5 | `classement.py` | difficile |
| 6 | `affichage.py` | facile |
| 7 (bonus) | `utils.py` | difficile |

Pour chaque tâche : **où coder**, **ce qu'il faut obtenir**, **un indice** et **un test à coller** en bas de votre fichier. Pour revoir les notions, relisez les PDF du cours (Jour 2 boucles, Jour 3 conditions, Jour 4 fonctions, Jour 6 listes, Jour 7-8 algo).

### Tâche 1 : `main.py` (le menu)

**Où coder** : dans les 3 fonctions `afficher_menu()`, `lancer_partie()` et `main()`. Regardez les `# TODO`.

**Ce qu'il faut obtenir** :
- `afficher_menu()` affiche les 3 choix (Jouer / Classement / Quitter).
- `main()` répète le menu **en boucle** jusqu'à ce que le joueur choisisse Quitter.
- Un choix invalide affiche un message d'erreur et redemande.
- `lancer_partie()` enchaîne : demander le nom, jouer, calculer le score, afficher le résultat, enregistrer le score. Les étapes sont écrites dans les `# TODO`.

**Indice** : `while True:` pour la boucle, `choix = input("Votre choix : ")`, puis `if / elif / else` (ou `match / case`) pour réagir, et `break` pour sortir de la boucle.

**Tester** :

```bash
python3 main.py
```

Le menu doit s'afficher. Tapez `3` : le programme doit s'arrêter. Tapez `9` : il doit dire que le choix est invalide et redemander. Les options « Jouer » et « Classement » ne marcheront entièrement que quand les autres tâches seront finies : c'est normal.

### Tâche 2 : `questions.py` (les questions)

**Où coder** : dans la liste `QUESTIONS` (ajoutez des questions) et dans les fonctions `get_questions()` et `filtrer_par_categorie()`.

**Ce qu'il faut obtenir** :
- Au moins **10 questions** dans `QUESTIONS`, toutes au même format (voir l'exemple dans le fichier).
- `get_questions()` retourne la liste complète.
- `filtrer_par_categorie("git")` retourne seulement les questions dont la catégorie est `"git"`.

**Indice** : pour filtrer, créez une liste vide `resultat = []`, parcourez `QUESTIONS` avec `for`, et faites `resultat.append(question)` si `question["categorie"] == categorie`. N'oubliez pas le `return resultat`.

**Tester** (à coller tout en bas du fichier, sans indentation) :

```python
if __name__ == "__main__":
    print("Nombre de questions :", len(get_questions()))   # attendu : 10 ou plus
    print(filtrer_par_categorie("git"))                     # attendu : les questions sur git
```

### Tâche 3 : `jeu.py` (une partie)

**Où coder** : dans `demander_reponse(nb_choix)` et `jouer(questions)`.

**Ce qu'il faut obtenir** :
- `demander_reponse(3)` demande une lettre (A, B ou C). Si le joueur tape autre chose, elle **redemande**. Elle retourne la lettre en **majuscule** (« b » devient « B »).
- `jouer(questions)` parcourt toutes les questions, les affiche (avec `afficher_question`), récupère la réponse, la compare à `question["reponse"]`, et **retourne le nombre de bonnes réponses** (un entier).

**Indice** : dans `jouer`, créez `bonnes = 0` avant la boucle, et faites `bonnes = bonnes + 1` quand la réponse est juste. Pour `demander_reponse`, utilisez `while True:` avec un `return` quand la réponse est valide.

**Tester** :

```python
if __name__ == "__main__":
    questions_test = [
        {"question": "2 + 2 ?", "choix": ["A) 3", "B) 4", "C) 5"], "reponse": "B", "categorie": "test"},
        {"question": "3 x 3 ?", "choix": ["A) 6", "B) 9", "C) 12"], "reponse": "B", "categorie": "test"},
    ]
    print("Bonnes réponses :", jouer(questions_test))
```

Lancez `python3 jeu.py` et répondez aux questions. Avec « b » puis « b », le résultat doit être `2`.

> **Attention** : tant que la personne qui fait `affichage.py` n'a pas fini `afficher_question`, la question ne s'affiche pas. Pour tester, ajoutez **temporairement** dans `jouer` une ligne `print(question["question"])`, et **supprimez-la** avant de faire votre commit.

### Tâche 4 : `score.py` (le score)

**Où coder** : dans `calculer_score(bonnes, total)` et `get_mention(pourcentage)`.

**Ce qu'il faut obtenir** :
- `calculer_score(3, 4)` retourne `75.0`. Si `total` vaut 0, retournez `0` (on ne peut pas diviser par zéro).
- `get_mention(pourcentage)` retourne : `"Très bon"` si 75 ou plus, `"Bon"` si 50 ou plus, `"Moyen"` si 25 ou plus, `"À revoir"` sinon.

**Indice** : `if / elif / else` avec `return` dans chaque branche. Voir le job 09 du jour 4.

**Tester** :

```python
if __name__ == "__main__":
    print(calculer_score(3, 4))    # attendu : 75.0
    print(calculer_score(0, 10))   # attendu : 0.0
    print(calculer_score(5, 0))    # attendu : 0
    print(get_mention(80))         # attendu : Très bon
    print(get_mention(60))         # attendu : Bon
    print(get_mention(30))         # attendu : Moyen
    print(get_mention(10))         # attendu : À revoir
```

### Tâche 5 : `classement.py` (les meilleurs scores)

**Où coder** : dans `ajouter_score`, `trier_classement` et `afficher_top3`.

**Ce qu'il faut obtenir** :
- `ajouter_score("Sara", 75)` ajoute `{"nom": "Sara", "score": 75}` à la liste `CLASSEMENT`.
- `trier_classement()` retourne la liste **triée du meilleur au moins bon**. Interdit d'utiliser `sort()` ou `sorted()` : écrivez votre propre tri.
- `afficher_top3()` affiche les 3 meilleurs (attention s'il y en a moins de 3).

**Indice** : c'est un tri « à bulles ». Comparez deux éléments voisins, échangez-les s'ils sont dans le mauvais ordre, et recommencez jusqu'à ce que plus rien ne bouge. Reprenez le job 08 du jour 7-8 (`my_sort`), mais en comparant `liste[i]["score"]` au lieu de nombres, et dans l'ordre décroissant. Pour échanger deux éléments : `liste[i], liste[i + 1] = liste[i + 1], liste[i]`.

**Tester** :

```python
if __name__ == "__main__":
    ajouter_score("Sara", 60)
    ajouter_score("Yassine", 90)
    ajouter_score("Léo", 75)
    ajouter_score("Inès", 40)
    print(trier_classement())   # attendu : Yassine (90), Léo (75), Sara (60), Inès (40)
    afficher_top3()             # attendu : les 3 premiers
```

### Tâche 6 : `affichage.py` (l'affichage)

**Où coder** : dans `afficher_titre`, `afficher_question` et `afficher_resultat`.

**Ce qu'il faut obtenir** :
- `afficher_titre("QUIZ PYTHON")` affiche un cadre :

```
|-------------|
| QUIZ PYTHON |
|-------------|
```

- `afficher_question(1, question)` affiche :

```
Question 1 : Quelle commande Git envoie vos commits sur GitHub ?
  A) git pull
  B) git clone
  C) git push
```

- `afficher_resultat("Sara", 75.0, "Très bon")` affiche par exemple :

```
Bravo Sara ! Score : 75.0% - Mention : Très bon
```

**Indice** : pour le cadre, calculez `largeur = len(texte) + 2` puis `"-" * largeur`. Pour les choix, parcourez `question["choix"]` avec une boucle `for`.

**Tester** :

```python
if __name__ == "__main__":
    afficher_titre("QUIZ PYTHON")
    exemple = {
        "question": "Quelle commande Git envoie vos commits sur GitHub ?",
        "choix": ["A) git pull", "B) git clone", "C) git push"],
        "reponse": "C",
        "categorie": "git",
    }
    afficher_question(1, exemple)
    afficher_resultat("Sara", 75.0, "Très bon")
```

### Tâche 7 (bonus) : `utils.py`

**Où coder** : dans `melanger(liste)` et `cesar(texte, decalage)`.

- `melanger` mélange une liste **sans** `random.shuffle` (vous pouvez utiliser `random.randint`).
- `cesar("abc", 3)` retourne `"def"` : chaque lettre est décalée dans l'alphabet (`z` revient sur `a`). Voir le job 04 du jour 7-8.

**Tester** :

```python
if __name__ == "__main__":
    print(cesar("abc", 3))      # attendu : def
    print(cesar("xyz", 3))      # attendu : abc
    print(melanger([1, 2, 3, 4, 5]))
```

---

## 5. Tester son code

Un fichier qui contient **seulement des fonctions n'affiche rien** quand on le lance : Python enregistre les fonctions, mais personne ne les appelle. Il faut donc un petit **bloc de test** tout en bas du fichier.

```python
def dire_bonjour(prenom):
    return "Bonjour " + prenom


if __name__ == "__main__":
    print(dire_bonjour("Sara"))
```

Lancez ensuite votre fichier :

```bash
python3 nom_du_fichier.py
```

Les 5 règles à retenir :

1. **Enregistrez** le fichier avant de le lancer (`Ctrl+S`).
2. Le bloc `if __name__ == "__main__":` est **collé à la marge gauche**, après toutes les fonctions.
3. Les lignes à l'intérieur sont **décalées de 4 espaces**.
4. Une fonction avec `return` n'affiche rien toute seule : entourez l'appel d'un `print(...)`.
5. Ce bloc est ignoré quand un autre fichier importe le vôtre : vous pouvez le laisser.

**Testez plusieurs cas**, y compris les cas particuliers : zéro, liste vide, réponse invalide, etc.

**Déboguer avec `print`** : si le résultat n'est pas celui attendu, affichez les variables à chaque étape.

```python
print("DEBUG bonnes =", bonnes, "total =", total)
```

Supprimez ces `print` de débogage avant de faire votre commit.

---

## 6. Erreurs fréquentes

**Astuce** : lisez toujours la **dernière ligne** du message d'erreur (le type d'erreur) et le **numéro de ligne** indiqué juste au-dessus.

### Erreurs Python

| Message ou symptôme | Cause probable | Solution |
|---|---|---|
| Rien ne s'affiche | Aucune fonction n'est appelée | Ajoutez le bloc `if __name__ == "__main__":` |
| `IndentationError: unexpected indent` | Lignes d'un même bloc mal alignées | Même décalage (4 espaces) pour tout le bloc |
| `IndentationError: expected an indented block` | Rien d'indenté après `def`, `if`, `for`... | Indentez la ligne suivante, ou mettez `pass` |
| `SyntaxError` | Parenthèse, guillemet ou `:` oublié | Regardez la ligne indiquée **et celle d'avant** |
| `NameError: name 'x' is not defined` | Variable ou fonction inconnue, ou faute de frappe | Vérifiez l'orthographe et l'ordre |
| `TypeError: can't multiply sequence by non-int` | Vous multipliez une chaîne par une chaîne | Utilisez un nombre ou `len(...)` |
| `TypeError: can only concatenate str` | Vous additionnez du texte et un nombre | Utilisez `str(nombre)` |
| `KeyError: 'nom'` | Clé de dictionnaire inexistante | Vérifiez l'orthographe de la clé |
| `IndexError: list index out of range` | Indice trop grand pour la liste | Vérifiez la taille de la liste |
| `ZeroDivisionError` | Division par zéro | Testez si le diviseur vaut 0 |
| `ImportError` / `ModuleNotFoundError` | Mauvais dossier ou mauvais nom | `cd` dans le projet, `ls` pour voir les fichiers |
| `python3: can't open file` | Mauvais dossier ou mauvais nom | `ls` pour voir les fichiers présents |
| Une fonction retourne `None` | Il reste `pass`, ou le `return` est oublié | Supprimez `pass` et ajoutez `return` |

### Erreurs Git

| Message | Solution |
|---|---|
| `fatal: not a git repository` | Vous n'êtes pas dans le dossier du projet : `cd new_group_project` |
| `nothing to commit` | Vous avez oublié d'enregistrer, ou de faire `git add` |
| `error: src refspec ... does not match any` | Mauvais nom de branche : `git branch` pour voir le bon |
| `Permission denied` ou `403` au push | Vous n'êtes pas encore collaborateur : acceptez l'invitation reçue par mail |
| `rejected ... fetch first` | Faites `git pull origin main`, puis réessayez |
| `command not found` après avoir collé du texte | Vous avez collé un résultat au lieu d'une commande : ignorez, rien n'a été cassé |

---

## 7. Petit lexique Git

| Mot | Explication simple |
|---|---|
| **Dépôt** (repository) | Le dossier du projet, suivi par Git et hébergé sur GitHub |
| **Clone** | Télécharger une copie du dépôt sur son ordinateur |
| **Branche** | Une version parallèle du projet, pour travailler sans gêner les autres |
| **`main`** | La branche principale, celle qui contient la version « officielle » |
| **Commit** | Une sauvegarde de vos modifications, avec un message qui les décrit |
| **Push** | Envoyer vos commits vers GitHub |
| **Pull** | Récupérer les nouveautés depuis GitHub |
| **Pull Request** (PR) | Une demande pour fusionner votre branche dans `main` |
| **Merge** | La fusion de votre branche dans `main` |
| **Conflit** | Deux personnes ont modifié la même ligne : Git demande de choisir |

Les 5 commandes à connaître :

```bash
git status                          # voir ce qui a changé
git add mon_fichier.py              # préparer un fichier à sauvegarder
git commit -m "Mon message"         # sauvegarder
git push -u origin HEAD             # envoyer sa branche sur GitHub
git pull origin main                # récupérer le travail des autres
```

---

## 8. Le contrat entre les fichiers

Comme les fichiers travaillent ensemble, **ne changez pas** ces noms et ces formats sans prévenir le groupe.

- Une **question** est un dictionnaire :
  `{"question": "...", "choix": ["A) ...", "B) ..."], "reponse": "B", "categorie": "git"}`
- `jouer(questions)` reçoit une liste de questions et retourne le **nombre de bonnes réponses** (un entier).
- `calculer_score(bonnes, total)` retourne un **pourcentage entre 0 et 100**.
- `get_mention(pourcentage)` retourne un **texte** (`"Très bon"`, `"Bon"`, `"Moyen"` ou `"À revoir"`).
- Un **score du classement** est un dictionnaire : `{"nom": "Sara", "score": 80}`.

Si chaque personne respecte ces règles, les fichiers fonctionneront ensemble sans modification.

---

## 9. Règles du groupe

- Pas de push direct sur `main` : passez par une Pull Request.
- Commentez votre code (au moins une phrase par fonction).
- Pas de mot de passe ni d'information privée : le dépôt est public.
- Demandez de l'aide dès que vous bloquez.

---

## 10. Check-list avant d'envoyer son travail

Avant de faire `git push`, cochez dans votre tête :

- [ ] Je suis bien sur **ma branche** (`git branch`).
- [ ] J'ai **supprimé les `pass`** là où j'ai écrit du code.
- [ ] Mon fichier **se lance sans erreur** (`python3 mon_fichier.py`).
- [ ] J'ai **testé plusieurs cas** avec mon bloc `if __name__ == "__main__":`.
- [ ] J'ai **supprimé les `print` de débogage**.
- [ ] J'ai écrit **un commentaire** pour chaque fonction.
- [ ] Je n'ai **pas changé les noms** des fonctions du contrat.
- [ ] Mon message de commit est **clair**.

Bon courage à tous !

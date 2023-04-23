# TP - SQL et algèbre relationnelle

## Prérequis

* téléchargez le fichier [`pokedex.sqlite`](https://seafile.emse.fr/f/8f8da5d7d52c46e88b71/).
* installez [_DB Browser for SQLite_](https://sqlitebrowser.org/) (avec interface graphique), [SQLite](https://sqlite.com/) (avec interface en ligne de commande) ou n'importe quel outil pouvant ouvrir une base de données SQLite.
* ouvrez le fichier téléchargé avec l'outil choisi.

## Prise en main

Dans cette partie, vous allez découvrir le schéma de la base de données et reproduire les exemples du cours (à retrouver [ici](https://www.vcharpenay.link/courses/sql-algebra.html)).

1.1. L'exemple de base de données du cours est une simplification du Pokédex (qui contient 173 tables). Vous allez écrire une requête `SELECT` qui permet de construire la table `pokemon_fr`, équivalent à la table `Pokémon` du cours.
- Commencez par inspecter le contenu de la table `pokemon_species_names`, par exemple avec un requête `SELECT * FROM pokemon_species_names`. _DB Browser for SQLite_ affiche les contenu des tables dans l'onglet « Parcourir les données ».
- Écrivez une requête sur la table `pokemon_species_names` pour ne garder que les noms français, via l'attribut `local_language_id` (choisissez le bon identifiant). Comment pouvez-vous vous assurer que l'identifiant de la langue correspond bien au français ? Pour répondre, inspectez les schéma de la table et trouvez la contrainte de clé étrangère s'appliquant à `local_language_id`. Dans _DB Browser for SQLite_, le schéma d'une table est visible dans l'onglet « Structure de la base de données » (panneau principal). Dans l'interface en ligne de commande d'SQLite, utilisez la commande `.schema pokemon_species_names`. Quelle est la table référencée dans cette contrainte ? À partir de cette second table, suivez de nouveau la référence de clé étrangère vers la table contenant le label `Français`, associé à son identifiant de langue.
- Inspectez ensuite le contenu de la table `pokemon`, qui contient les taille et poids des Pokémons. En suivant le même processus d'exploration par clés étrangères, trouvez comment relier un Pokémon (avec sa taille et son poids) à un nom d'espèce en français.
- Écrivez la requête `SELECT` pour reconstruire la table `pokemon_fr(species_id, name, height, weight)`, qui donne le rang (l'identifiant) de l'espèce de Pokémon, son nom en français, sa taille et son poids.


1.2. Vous allez maintenant construire la table `pokemon_types_fr` équivalent à `PokémonType` dans le cours. Les types de Pokémons sont donnés dans la table `pokemon_types` et leur noms dans plusieurs langues dans la table  `type_names`. Procédez de la même manière que dans la question précédente pour trouver le lien entre ces tables puis écrivez la requête `SELECT` pour construire `pokemon_types_fr(species_id, type_name)`, qui donne le rang de l'espèce et le ou les types pour cette espèce (plante, feu, eau, ...). Les types doivent être donnés en français.

1.3. SQL permet de créer des _vues_, c'est-à-dire des tables « virtuelles » définies comme le résultat d'une requête `SELECT` plutôt que comme un ensemble de tuples matérialisés en mémoire. Définissez les tables `pokemon_fr` et `pokemon_types_fr` comme des vues (avec la commande [`CREATE VIEW`](https://sqlite.com/lang_createview.html)).

1.4. À partir des vues créées dans la question précédente, écrivez une requête pour lister les Pokémons de type feu (Q1, dans le cours). Ajoutez ensuite la contrainte que le poids des Pokémons doit être inférieur à 100kg (Q2, dans le cours). Ne listez que les [Pokémons de la première génération](https://bulbapedia.bulbagarden.net/wiki/Category:Generation_I_Pok%C3%A9mon), allant du rang #1 à #151.

## Normalisation

Les vues, comme celles que vous avez créées dans la partie précédente, permettent généralement de simplifier l'écriture de requêtes. Mais pour ce faire, ces vues sont souvent dénormalisées. Vous allez donc étudier les dépendances fonctionnelles qui s'appliquent aux vues.

2.1. Dans le cours, plusieurs dépendances fonctionnelles ont été données sur la table `Pokémon`.
- Reprenez le cours et faites la liste de toutes les dépendances atomiques élémentaires sur cette table.
- La vue `pokemon_fr` a-t-elle les dépendances fonctionnelles équivalentes ? Pour le prouver (ou l'infirmer), écrivez une requête pour chaque dépendance X → A qui teste l'existence de possible violations : utilisez une agrégation (avec [`GROUP BY`](https://sqlite.com/lang_select.html#resultset)) qui compte le nombre de valeurs distinctes de A pour un même sous-ensemble de valeurs de X et sélectionnez les résultats dont le compte est strictement supérieur à 1 (avec [`HAVING`](https://sqlite.com/lang_select.html#resultset)). Le résultat devrait être vide si la contrainte est satisfaite.


2.2. Créez la vue `pokemon_fr_bis(id, species_id, name)` qui associe à chaque `pokemon.id` l'identifiant de son espèce et son nom en français.
- Quelles sont les dépendances fonctionnelles s'appliquant sur cette vue, selon vous ? Il y a au moins deux dépendances fonctionnelles atomiques élémentaires. Pour chaque dépendance fonctionnelle, prouvez par une requête qu'elle n'est pas violée dans la table.
- La vue que vous avez créée est-elle en forme normale ? Si oui, laquelle (1NF, 2NF, 3NF, BCNF) et pourquoi ?


2.3 Créez la vue `location_areas_en(id, location_id, name)` qui associe à chaque lieu de l'univers Pokémon son nom anglais (les lieux ne sont pas documentés en français). La requête pour le faire est la suivante :
```sql
create view location_areas_en(id, location_id, name) as
select l.id, la.id, case when lap.name is null then ln.name else (ln.name || ' - ' || lap.name) end
from locations l, location_names ln, location_areas la, location_area_prose lap
where l.id = ln.location_id and
      l.id = la.location_id and
      la.id = lap.location_area_id and
	  ln.local_language_id = 9 and
	  (lap.local_language_id = 9 or lap.local_language_id is null);
```
- Expliquez en langage naturel quelle est la différence entre `id` et `location_id` (d'après les données du Pokédex) et comment l'attribut `name` est construit.
- Comme pour la question précédente, faites la liste des dépendances fonctionnelles s'appliquant sur cette vue, avec une requête pour le prouver. La vue est-elle en forme normale ? Si oui, laquelle et pourquoi ?


## Réécriture de requête

Dans cette partie, vous allez comparer différentes réécritures de requêtes en termes de temps d'exécution. Les optimisations faites par SQLite sont documentées [ici](https://www.sqlite.org/optoverview.html). Vous pouvez vous aider de la commande [`EXPLAIN QUERY PLAN`](https://www.sqlite.org/lang_explain.html) pour afficher la requête après optimisation par SQLite.

3.1. Écrivez une requête donnant l'étalement géographique des Pokémons sur leur territoire. La requête doit retourner le nom du Pokémon, la région dans laquelle il vit et un pourcentage indiquant l'étalement du Pokémon dans la région, à savoir le rapport entre le nombre de lieux sur lesquels on trouve le Pokémon sur le nombre total de lieux dans la région. La principale table à utiliser pour cette requête est `encounters`. Lorsqu'un lieu a plusieurs sous-espaces, ne comptez le Pokémon qu'une seule fois. Notez le temps d'exécution de la requête.

3.2. Proposez une écriture alternative de cette requête basée sur une jointure _implicite_. Pour cela, écrivez les jointures intermédiaires comme des sous-requêtes avec renommage de telle sorte que les attributs à joindre porte le même nom (cf exemple ci-dessous). Puis, dans la requête principale, enlevez la condition de jointure. Que constatez-vous en terme de temps d'exécution entre la jointure explicite et la jointure implicite ? Pourquoi ?

```sql
select *
from (select primaryKey1 as sameAttribut, someAttribut from table1) as t1,
     (select foreignKey2 as sameAttribut, someOtherAttribut from table2) as t2
-- condition implicite : where t1.sameAttribut = t2.sameAttribut

```

3.3. Écrivez une requête associant une liste d'attaques aux Pokémons sur lesquels ces attaques n'ont pas d'effet. Par exemple, les attaques de type électrique n'ont pas d'effet sur les Pokémons de type terre. Restreignez votre requête aux Pokémons de première génération (rang #1 à #151).

3.4. Proposez au moins trois écritures alternatives de cette requête, de façon à obtenir des temps temps d'exécution distincts. Proposez une procédure pour classer ces réécritures de la plus rapide à la moins rapide, sans avoir à les exécuter.

3.5. Exécutez la commande [`ANALYZE`](https://www.sqlite.org/lang_analyze.html). Inspectez ensuite la table `sqlite_stat1`. Que contient cette table ? Donnez en exemple comment son contenu a pu être utilisé dans l'une des deux requêtes précédentes (étalement géographique et attaques sans effet).

## Indexage

Dans cette partie, vous allez mesurer l'impact des index sur le temps d'exécution des requêtes. La commande [`EXPLAIN QUERY PLAN`](https://www.sqlite.org/lang_explain.html) vous sera aussi utile.

4.1. Faites une copie du Pokédex et enlevez toutes les contraintes de clé primaire et de clé étrangère dans le schéma copié. Refaites la requête Q1. Que constatez-vous ? Pourquoi ?

4.2. Faites de même avec la requête écrite dans la questions 3.1 (sur l'étalement géographique des Pokémons). Testez avec jointure explicite et avec jointure implicite. Constatez-vous une différence ? Pourquoi ?

4.3. Écrivez une requête qui liste les Pokémons dont l'évolution commence par les mêmes lettres (1, 2 et 3 lettres). Utilisez l'opérateur [`LIKE`](https://sqlite.com/lang_expr.html#the_like_glob_regexp_match_and_extract_operators) et la fonction [`substr`](https://www.sqlite.org/lang_corefunc.html#substr) dans votre filtre de sélection. Notez son temps d'exécution.

4.4. Retirez l'index `ix_pokemon_species_names_name` avec [`DROP INDEX`](https://www.sqlite.org/lang_dropindex.html) et reproduisez la . Constatez-vous une différence en termes  de temps d'exécution ? Pourquoi ?



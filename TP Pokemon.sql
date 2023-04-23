--Prise en main

--1.1)

-- a)
select * from pokemon_species_names 

-- b)
select DISTINCT PS.name from pokemon_species_names as PS 
join language_names as LN on PS.local_language_id=LN.local_language_id
where PS.local_language_id=( select local_language_id from language_names where local_language_id=5)

????

-- c)
Select PS.name, weight, height from pokemon as P
join pokemon_species_names as PS on pokemon_species_id = id
join language_names as LN on PS.local_language_id=LN.local_language_id
where PS.local_language_id=( select local_language_id from language_names where local_language_id=5)

-- d)
create table pokemon_fr(
	species_id INT NOT NULL UNIQUE,
	name varchar(80) NOT NULL,
	weight INT,
	height INT)
	
Insert into pokemon_fr	
	Select DISTINCT pokemon_species_id, PS.name, weight, height from pokemon as P
	join pokemon_species_names as PS on pokemon_species_id = id
	join language_names as LN on PS.local_language_id=LN.local_language_id
	where PS.local_language_id=( select local_language_id from language_names where local_language_id=5)

-- 1.2

Create table pokemon_types_fr(
		species_id INT NOT NULL,
		type_name varchar(80))

drop table pokemon_types_fr
		
Insert into pokemon_types_fr
	Select DISTINCT pokemon_id, TN.name from pokemon_types as PT
	join type_names as TN on TN.type_id=PT.type_id
	join language_names as LN on LN.local_language_id=TN.local_language_id
	where TN.local_language_id=( select local_language_id from language_names where local_language_id=5)

select * from pokemon_types_fr

-- 1.3

-- Vue de pokemon_fr
Create view Vue_pokemon_fr as
	Select DISTINCT pokemon_species_id, PS.name, weight, height from pokemon as P
	join pokemon_species_names as PS on pokemon_species_id = id
	join language_names as LN on PS.local_language_id=LN.local_language_id
	where PS.local_language_id=( select local_language_id from language_names where local_language_id=5)
	
select * from Vue_pokemon_fr
	
-- Vue de pokemon_types_fr
Create view Vue_pokemon_types_fr as
	Select DISTINCT pokemon_id, TN.name from pokemon_types as PT
	join type_names as TN on TN.type_id=PT.type_id
	join language_names as LN on LN.local_language_id=TN.local_language_id
	where TN.local_language_id=( select local_language_id from language_names where local_language_id=5)

	select * from Vue_pokemon_types_fr
	
-- 1.4

-- On liste les pokemons de type feu

Select VP.name from Vue_pokemon_fr as VP
join Vue_pokemon_types_fr as VPT on pokemon_species_id=pokemon_id
where VPT.name='Feu'

--On ajoute la contrainte sur le poids

Select VP.name from Vue_pokemon_fr as VP
join Vue_pokemon_types_fr as VPT on pokemon_species_id=pokemon_id
where VPT.name='Feu' AND weight < 100

--Enfin, on ne garde que les pokemons de 1ere génération

Select pokemon_id, VP.name from Vue_pokemon_fr as VP
join Vue_pokemon_types_fr as VPT on pokemon_species_id=pokemon_id
where VPT.name='Feu' AND weight < 100 
AND (pokemon_id > 0 AND pokemon_id <152)

-- Réécriture de requête

--3.1)

SELECT pbis.name, r.identifier, COUNT(DISTINCT e.location_area_id) * 100.0 / COUNT(l.id) as pourcentage
FROM encounters AS e
JOIN pokemon_fr_bis AS pbis ON e.pokemon_id = pbis.id -- jointure pour obtenir le nom des pokemons
JOIN locations AS l ON l.id = e.location_area_id
JOIN regions AS r ON r.id = l.region_id -- jointure pour obtenir le nom de la région
GROUP BY pbis.name, r.identifier;
	
-- En moyenne sur 10 exécutions, la requête s'effectue en 236ms.
	
--3.2)

SELECT pbis.name, r.identifier, COUNT(DISTINCT e.location_area_id) * 100.0 / COUNT(l.id) as pourcentage
FROM encounters AS e
CROSS JOIN pokemon_fr_bis AS pbis ON e.pokemon_id = pbis.id -- jointure pour obtenir le nom des pokemons
CROSS JOIN locations AS l ON l.id = e.location_area_id
CROSS JOIN regions AS r ON r.id = l.region_id -- jointure pour obtenir le nom de la région
GROUP BY pbis.name, r.identifier;
	
-- En moyenne sur 10 exécutions, la requête s'effectue en 278ms

--3.3)

SELECT m.identifier as move_identifier, 
	   p.identifier as pokemon_identifier
From type_efficacy te
join moves m
join pokemon_types pt 
join pokemon p 
	on target_type_id = pt.type_id AND
	te.damage_type_id = m.target_id AND
	p.id = pt.pokemon_id
Where damage_factor = 0 
AND p.id < 152

--3.4)

--1ere variante (avec CROSS JOIN)
SELECT m.identifier as move_identifier, 
	   p.identifier as pokemon_identifier
From type_efficacy te
cross join moves m
cross join pokemon_types pt 
cross join pokemon p 
	on target_type_id = pt.type_id AND
	te.damage_type_id = m.target_id AND
	p.id = pt.pokemon_id
Where damage_factor = 0 
AND p.id < 152

--2eme variante (avec JOIN explicite)
SELECT m.identifier as move_identifier, 
	   p.identifier as pokemon_identifier
From type_efficacy te
join moves m on te.damage_type_id = m.target_id
join pokemon_types pt on target_type_id = pt.type_id
join pokemon p on p.id = pt.pokemon_id
Where damage_factor = 0 
AND p.id < 152

--3e alternative (sous-requête au lieu des jointures)
SELECT 
  (SELECT identifier FROM moves WHERE target_id = te.damage_type_id) AS move_identifier,
  (SELECT identifier FROM pokemon WHERE id = pt.pokemon_id) AS pokemon_identifier
FROM type_efficacy AS te, pokemon_types AS pt
WHERE te.target_type_id = pt.type_id
AND te.damage_factor = 0
AND pt.pokemon_id < 152

----- DONNER AUSSI LA PROCEDURE

--3.5)

--On analyse l'ensemble de la table de données:
	ANALYZE type_efficacy

-- On inspecte ensuite la table 'sqlite_stat1':
	SELECT * FROM sqlite_stat1
	
-- On remarque que plusieurs valeurs sont stockées dans la colonne 'stat'. 
-- Le 1er entier correspond au nombre d'enregistrements de l'index corrspondant (ou nombre totale de pages utilisées par l'index)
-- Le 2eme entier désigne le nombre moyen de lignes ayant la même valeur, vis à vis de la 1ere colonne.
-- ...
-- Le K-ième entier désigne le nombre de lignes ayant la même valeur sur les K-1 colonnes précédentes.

-- Avoir accès au nombre de lignes partageant une même valeur peut être utile dans l'optimisation des requêtes
-- car si peu de lignes partagent cette même valeur, on peut utiliser l'index pour accéder directement aux lignes
-- correspondantes plutôt que de parcourir la table entière.

-- Ainsi pour la requête sur les attaques sans effet par exemple, étant donné qu'il existe peu de combinaisons de types pour
-- lesquelles les attaques sont sans effet d'un type sur l'autre, il est plus rapide d'accéder aux valeurs de ces
-- types par index que par un parcours de la table entière. 

-- De même pour la requête sur l'étalement géographique,
-- .
-- . 
-- .


-- Indexage

-- 4.1)

-- En enlevant les contraintes de clé primaire et de clé étrangère des tables, on ne peut plus garantir l'intégrité 
-- des tables de données: cela peut entrainer l'apparition de doublons ou des valeurs incorrectes.

-- 4.2)

-- Idem Q4.1

-- 4.3)

-- On réalise une auto-jointre sur la table 'pokemon_species' car elle contient l'attribut 'evolves_from_species_id',
-- qui permet de faire un lien entre les pokemons et leurs évolutions.

-- Les autres jointures sont similaires à celles utilisées à la question Q1.1 et permettent d'avoir les noms français des pokemons.

SELECT DISTINCT PS.name, ps2.identifier as evolution
	FROM pokemon_species ps1
	JOIN pokemon_species ps2 ON ps1.id=ps2.evolves_from_species_id
	JOIN pokemon_species_names PS on pokemon_species_id = ps1.id
	JOIN language_names LN on PS.local_language_id=LN.local_language_id
	WHERE PS.local_language_id = (SELECT local_language_id FROM language_names WHERE local_language_id=5)
	AND substr(evolution, 1, 3) LIKE substr(PS.name, 1, 3)

-- Sur un total de 10 requêtes, l'exécution se fait en 8ms en moyenne.

-- 4.4)

DROP INDEX ix_pokemon_species_names_name

SELECT DISTINCT PS.name, ps2.identifier as evolution
	FROM pokemon_species ps1
	JOIN pokemon_species ps2 ON ps1.id=ps2.evolves_from_species_id
	JOIN pokemon_species_names PS on pokemon_species_id = ps1.id
	JOIN language_names LN on PS.local_language_id=LN.local_language_id
	WHERE PS.local_language_id=( SELECT local_language_id FROM language_names WHERE local_language_id=5)
	AND substr(evolution, 1, 3) LIKE substr(PS.name, 1, 3)

-- Le temps d'exécution reste similaire même sans index (environ 9ms).
-- Cela semble peu étonnant: en enlevant l'index, le parcours se fait sur la table entière 'pokemon_species_names' pour l'attribut 'name'. 
-- On pourrait s'attendre à un temps de réponse plus long, mais étant donné que dans ce cas précis une grande majorité des pokemons
-- possède une évolution, la recherche par index différe peu d'une recherche sur la table entière (d'où un temps d'éxecution similaire.
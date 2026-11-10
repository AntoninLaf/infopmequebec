# Journal éditorial

## 2026-11-08 — lancement
- Site créé (générateur `build.py`, GitHub Pages, domaine infopmequebec.com).
- Publié : /emplois-ete-canada-2027-date-limite/ — source : canada.ca (guide du demandeur EEC, modifié le 2026-10-27; page critères).
  - Note : la page « qui peut présenter une demande » affichait encore les dates 2025 ; les critères (6-16 semaines, 30-40 h) y sont repris, les dates 2027 viennent du guide du demandeur.
- Publié : /festivals-evenements-touristiques-2027-aide-financiere/ — sources : communiqué Québec.ca du 2026-11-04 + page du programme.
- Pages : à propos, politique éditoriale, corrections.
- Corrections : via GitHub Issues (compte GitHub requis = filtre anti-robots). Antonin ne veut être avisé que des signalements qui méritent enquête.
- Éditeur affiché : Acteur Social (Montréal), confirmé tacitement par Antonin.

## 2026-11-08 (soir) — préparation trafic
- IndexNow ajouté : clé dans `site.yml` (`indexnow_key`), fichier de clé généré par `build.py` à la racine de `docs/`. Étape 8b ajoutée à la routine de CLAUDE.md.
- Stratégie de trafic sur 12 mois ajoutée à CLAUDE.md (fondation, pages de référence par programme, moteurs IA, Discover, autorité, monétisation plus tard).
- Bing Webmaster Tools : site ajouté par Antonin (import depuis Search Console), 2026-11-08.
- IndexNow testé avec WebFetch sur les 2 articles et /calendrier/ : requêtes acceptées (réponse vide, aucune erreur). Une réponse vide sans erreur = succès.

## 2026-11-09
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (EEC 2027 et festivals vérifiés le 2026-11-08; dates limites 2 et 3 décembre inchangées).
- Publié : /paupme-tarifs-douaniers-pret-150000-admissibilite/ — sources : quebec.ca (page du programme, mise à jour 2026-10-19; communiqué du 2026-08-28) + cadre normatif 2026-2028 (version 2026-08-27, PDF diffusé par la MRC des Chenaux).
  - Note : la page quebec.ca dit « prêt ou garanties de prêt » et « garantie ou cautionnement de l'entreprise »; le cadre normatif précise « aucune garantie ni caution personnelle ». Ancien seuil minimal de CA non publié : non mentionné.
- Publié : /iria-dec-intelligence-artificielle-pme-quebec/ — sources : page IRIA de DEC (modifiée 2026-10-13) + communiqué DEC du 2026-07-15.
  - Correction de nos notes : financement fédéral total maintenant 700 M$ (pas 38,2 M$) et mise en œuvre par DEC jusqu'au 31 mars 2031 (pas 2029). Aucun maximum par projet publié.
- Écarté : DÉPART — guide de mai 2026 vérifié (contribution non remboursable 15 000 $ à 150 000 $ selon le communiqué de mars 2025, projets terminés au plus tard le 31 décembre 2028), mais l'état actuel de la période de dépôt n'est confirmé par aucune source officielle consultée. À revérifier sur investquebec.com.
- Écarté : appel de projets Primo-adoptants (date limite 4 novembre 2026, passée).
- IndexNow : ÉCHEC pour les 2 nouvelles URL et /calendrier/ (WebFetch refusé : PROVENANCE_REQUIRED, permission non accordée pendant l'exécution planifiée). À relancer à la prochaine exécution.
- Veille : les pages de liste quebec.ca/nouvelles et DEC/nouvelles n'ont pas pu être lues directement (même refus); veille faite par recherche web puis lecture des pages officielles trouvées.

## 2026-11-10
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (dates limites EEC 3 déc. et festivals 2 déc. vérifiées le 2026-11-08; PAUPME et IRIA vérifiés le 2026-11-09).
- Publié : /programme-depart-subvention-pme-regions-125000/ — sources : cadre normatif 2026-2027 du programme (MEIE, version 2026-05-27, décret 784-2026) + guide de présentation DÉPART d'IQ (mai 2026) + communiqué de réouverture (18 mars 2025).
  - Notes : maximum 125 000 $ par demande dans le cadre 2026-2027 (le communiqué de 2025 disait 150 000 $ : écart signalé dans l'article). Demandes en continu, autorisation au plus tard le 31 mars 2027 (pas de champ `deadline` : ce n'est pas une date limite de dépôt). Le cadre n'utilise pas l'acronyme DÉPART (le nom complet et le fichier CN_DEPART concordent avec le guide). Page investquebec.com du programme non lisible (PROVENANCE_REQUIRED).
- Publié : /fin-prets-pardonnables-entreprises-quebec/ — sources : communiqués du 9 novembre 2026 du cabinet du ministre du Développement économique, de l'Innovation et de l'Énergie et du cabinet du premier ministre (diffusés par CNW; aucune version quebec.ca trouvée).
  - Notes : aucun programme nommé, aucune règle de transition. Retiré faute de vérification mot à mot : la mention d'une baisse d'impôts des PME (2e communiqué). À suivre : modalités de la révision des outils d'aide (ESSOR, etc.).
- Contexte : nouveau gouvernement (premier ministre Paul St-Pierre Plamondon; ministre de l'Économie Stéphane Paquet). Les communiqués de quebec.ca des anciens cabinets sont archivés au 21 octobre 2026 : revérifier les programmes avant de s'y fier.
- Écarté : Productivité-Compétences (CPMT) — appel « Formation en IA » fermé le 1er juin 2026; appel « Formation aux gestionnaires » (8 avril 2026, 10 M$, promoteurs collectifs) sans date limite confirmée; page CPMT non lisible (PROVENANCE_REQUIRED).
- IndexNow : ÉCHEC encore (PROVENANCE_REQUIRED sur api.indexnow.org et bing.com, toutes URL). Deuxième exécution de suite : l'autorisation de WebFetch vers api.indexnow.org doit être accordée par Antonin dans les réglages de la tâche planifiée. À signaler dans le rapport mensuel du 1er décembre. URL en attente : /paupme-tarifs-douaniers-pret-150000-admissibilite/, /iria-dec-intelligence-artificielle-pme-quebec/, /calendrier/, /programme-depart-subvention-pme-regions-125000/, /fin-prets-pardonnables-entreprises-quebec/.

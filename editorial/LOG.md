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

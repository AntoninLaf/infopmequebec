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

## 2026-11-11
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (EEC 3 déc. et festivals 2 déc. vérifiés le 2026-11-08; aucun changement repéré dans la veille pour PAUPME, IRIA, DÉPART, prêts pardonnables).
- Publié : /budget-federal-2026-pme-megadeduction-productivite/ — source : document du budget fédéral 2026 (budget.canada.ca, PDF, déposé le 5 novembre 2026; p. 32, 77, 97, 120-123, 125, 197-198, 423, 430, 434-439).
  - Notes : écart dans le budget sur le taux effectif marginal (13 % p. 32/120 contre 15,4 % p. 77) : chiffre non repris. Aucune section fiscale détaillée sur la Mégadéduction (règles de mise en service absentes) : mentionné comme à préciser par le projet de loi. Taux d'imposition des petites entreprises : rien trouvé dans les pages lues (p. 455-491 non lues). Retiré : mention que DEC offre l'IRRT au Québec (DEC non nommé dans le budget).
- Écarté : Programme Innovation Bois (appel volets 1A, 2, 3 fermé le 18 sept. 2026; volet 1B à l'hiver 2027 — à surveiller). FORET (MEIE/IQ, prêt max 5 M$, scieries de bois d'œuvre résineux jugées stratégiques, CA ≥ 5 M$, jusqu'au 31 mars 2027) : très ciblé, annoncé en juillet; possible article court plus tard.
- IndexNow : ÉCHEC (3e exécution; PROVENANCE_REQUIRED via l'agent web-fetch). URL en attente : les 5 précédentes + /budget-federal-2026-pme-megadeduction-productivite/. À signaler à Antonin dans le rapport du 1er décembre.
- IndexNow (avec Antonin, 2026-11-11) : remplacé par un workflow GitHub Actions (.github/workflows/indexnow.yml) déclenché à chaque push sur main touchant content/. Étape 8b de CLAUDE.md mise à jour. Arriéré envoyé : lancement manuel du workflow (toutes les URL du sitemap), exécution 43058194316 réussie.

## 2026-11-12
- Signalements (GitHub Issues) : aucun.
- Mises à jour : /fin-prets-pardonnables-entreprises-quebec/ — le communiqué du 9 nov. 2026 est maintenant publié sur quebec.ca : source CNW du cabinet du ministre remplacée par la version quebec.ca (contenu identique : 88 prêts, plus de 2 G$, 1,1 G$ ou 57 %; toujours aucun programme nommé ni règle de transition). Lien interne vers l'IRRT ajouté. `updated`/`verified` 2026-11-12.
- EEC 2027 (3 déc.) et festivals (2 déc.) : aucun changement repéré dans la veille; revérification complète à faire vers le 25 novembre.
- Publié : /irrt-dec-reponse-tarifaire-pme-quebec-liquidites-2-millions/ — source : page IRRT de DEC (canada.ca, modifiée 2026-10-19), lue deux fois (FAQ sur la même page).
  - Notes : demandes en continu, pas de champ `deadline` (31 mars 2028 = fin du soutien de liquidité; 31 mars 2029 = fin des projets). Total de 3,45 G$ cité par DEC = toutes les ADR du Canada : non repris. Hausse de 1,5 G$ du budget fédéral mentionnée avec lien vers l'article du budget.
- Écarté : appel de projets d'innovation collaboratifs dans les secteurs stratégiques (MEIE) — date limite 1er avril 2026 passée, dépôt par les RSRI.
- IndexNow : par le workflow GitHub Actions après le push.

## 2026-11-13
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (EEC 3 déc. et festivals 2 déc. : revérification complète prévue vers le 25 novembre; rien de nouveau repéré dans la veille pour PAUPME, IRIA, DÉPART, IRRT, prêts pardonnables).
- Publié : /essor-diagnostic-numerique-plan-numerique-subvention-pme/ — sources : cadre normatif ESSOR 2025-2027 (MEIE, version 2.0 du 2 juillet 2026, décret 1026-2026, p. 3, 9-17) + guides de présentation IQ des sous-volets 1B et 1C (mars 2026).
  - Vérification : cadre normatif relu une 2e fois, 13 énoncés confirmés mot à mot (montants 20 000 $ / 50 000 $ pour la durée du programme, taux 50 %, cumul 80 % / 50 %, PME ≤ 250 employés et CA ≥ 2,5 M$, échéance 31 mars 2027, 24 mois après le plan 1B, début ≤ 3 mois, durée ≤ 12 mois, apport privé 20 %, versements).
  - Notes : la règle franchises/chaînes de plus de 5 établissements (25 000 $, 30 %) vise 1A et 1C, pas 1B. Les guides ne donnent ni taux ni montant (renvoient à la lettre d'offre) : chiffres tirés du cadre normatif seulement. Pas de champ `deadline` (31 mars 2027 = autorisation, pas dépôt). Page HTML ESSOR d'IQ non lue.
- Écarté : soutien de 4,5 M$ à Les Produits du Québec (communiqué du 7 juillet 2026, aide à un organisme, rien à demander pour les PME).
- Veille : flux de nouvelles DEC et EDSC (api.io.canada.ca) non lisibles (PROVENANCE_REQUIRED); veille faite par recherche web.

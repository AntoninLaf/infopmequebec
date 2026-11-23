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

## 2026-11-13 (soir) — identité visuelle
- À la demande d'Antonin : drapeau du Québec (SVG en ligne) dans l'en-tête et nouvelle icône du site aux couleurs du Québec (fleur de lys blanche sur bleu #003da5). Fichiers dans `static/` (favicon.svg, favicon.ico, favicon-48.png, apple-touch-icon.png), copiés par `build.py`. Le reste du design (marine et or, Georgia) est inchangé.
- Drapeau remplacé par l'image fournie par Antonin (plus fidèle), réduite à 180×120 (3 Ko); ajouté aussi dans le pied de page.

## 2026-11-16
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (EEC 3 déc. et festivals 2 déc. : revérification complète prévue vers le 25 novembre; rien de nouveau repéré dans la veille pour PAUPME, IRIA, DÉPART, IRRT, ESSOR 1B/1C, prêts pardonnables).
- Publié : /essor-volet-2-projets-investissement-pme-pret-garantie/ — source : cadre normatif ESSOR 2025-2027 (MEIE, version 2.0 du 2 juillet 2026, décret 1026-2026, p. 8-9, 18-25, 29).
  - Vérification : relecture indépendante du texte intégral de la section 4; 16 énoncés confirmés mot à mot. Corrigés avant publication : exceptions du secteur primaire (serre, exploitation forestière, conditionnement > 10 M$), exception hébergement (rattaché à un projet touristique), ajout de l'exclusion bois d'œuvre résineux (< 10 M$), ajout de la règle des 24 mois avant approbation, fonds de roulement d'opération exclu.
  - Notes : le cadre mentionne encore le prêt pardonnable (formes d'aide) alors que le gouvernement en a annoncé la fin le 9 nov. : signalé dans l'analyse. Aucun seuil de taille ou de CA pour le volet 2. Mode de dépôt (IQ) non précisé faute de guide lu. Volets 4 et 5 non lus mot à mot.
- Veille : rien de nouveau et vérifiable (recherches Québec.ca, DEC, CPMT). Productivité-Compétences : communiqué du 14 juillet 2026 (51 projets IA, 10 M$) déjà ancien; appels « Formation aux gestionnaires » et « Économie verte et transformation numérique » sans date confirmée (page CPMT non lisible). Le Devoir (article sur le faible recours aux programmes d'aide tarifaire d'août) et infobref (énoncé économique d'automne) non lisibles : pistes à confirmer à une source officielle.
- Accès web : plusieurs pages refusées (PROVENANCE_REQUIRED) quand l'URL n'apparaît pas d'abord dans un résultat de recherche; astuce : faire d'abord une recherche web qui fait ressortir l'URL officielle, puis la lire.

## 2026-11-17
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (EEC 3 déc. et festivals 2 déc. : revérification complète prévue vers le 25 novembre; rien de nouveau repéré pour PAUPME, IRIA, DÉPART, IRRT, ESSOR, prêts pardonnables).
- Publié (page pilier) : /subventions-pme-quebec/ — guide des programmes ouverts (dates limites, programmes à faire autoriser avant le 31 mars 2027, programmes en continu, aide au choix). Tous les faits repris des 10 articles existants (vérifiés aux sources entre le 8 et le 16 novembre), aucun fait nouveau. Lien ajouté dans le pied de page (build.py). À mettre à jour chaque mois et à chaque nouvel article de la catégorie.
- Veille : rien de nouveau et vérifiable (recherches Québec.ca et DEC : seulement des annonces d'aide à des entreprises nommées). Mise à jour économique du Québec 2026 : aucune date trouvée (en 2025, elle avait eu lieu le 18 novembre) : à surveiller.
- IndexNow : workflow du 16 nov. réussi; celui de ce push à vérifier à la prochaine exécution.

## 2026-11-18
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (EEC 3 déc. et festivals 2 déc. : revérification complète prévue vers le 25 novembre; rien de nouveau repéré pour PAUPME, IRIA, DÉPART, IRRT, ESSOR, prêts pardonnables).
- Publié : /psce-subvention-exportation-pme-quebec-60000/ — sources : cadre normatif PSCE 2025-2028 (MEIE, novembre 2025, p. 4-28 lues mot à mot) + décret 1416-2025 du 26 nov. 2025 (Gazette officielle, 17 déc. 2025) + page Volet 2 d'IQ (mise à jour le 1er oct. 2026) + page Volet 1 d'IQ (mise à jour le 1er déc. 2025).
  - Vérification : relecture indépendante, 16 énoncés confirmés (taux 50/40/25 %, 25 000 $ à 60 000 $ par projet par année, représentant 45 000 $, cumul 65 %, apport privé 35 % en espèces, CA 1 M$-50 M$, plafonds 10 000 $/25 000 $/52 semaines, 18 mois, calendrier de dépôt).
  - Notes : Volet 2 fermé (dernière période 17 sept.-1er oct. 2026); printemps 2027 (Canada et Europe) « à confirmer » : surveiller la page Volet 2 d'IQ et mettre l'article à jour (champ `deadline`) dès que les dates sont publiées. Écarts mineurs entre le cadre et la page IQ (60 000 $ par projet vs par entreprise; apport privé sur dépenses admissibles vs coût total) : version du cadre retenue. Annexe 3 du cadre (p. 36) et pages 29-36 non lues mot à mot. Page Volet 3 d'IQ et page de préqualification (illisible) non lues.
- Page pilier /subventions-pme-quebec/ mise à jour : nouvelle section « Programmes à périodes de dépôt » (PSCE) et conseil exportation.
- Veille : mise à jour économique du Québec 2026 toujours sans date officielle trouvée; rien d'autre de nouveau et vérifiable (Québec.ca, DEC).
- IndexNow : workflow du 17 nov. réussi (exécution 44086100145).

## 2026-11-19
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire (EEC 3 déc. et festivals 2 déc. : revérification complète prévue vers le 25 novembre; rien de nouveau repéré pour PAUPME, IRIA, DÉPART, IRRT, ESSOR, PSCE, prêts pardonnables).
- Publié : /productivite-competences-formation-gestionnaires-pme/ (catégorie emploi) — sources : guide de l'appel de projets « Formation aux gestionnaires pour soutenir la performance des PME » (CPMT/MESS, 2026, PDF p. 2-8) + page CPMT « Appels de projets en cours » (mise à jour 2026-10-23, appel affiché en cours, « à l'épuisement des fonds disponibles ») + communiqués quebec.ca du 8 avril 2026 (enveloppe 10 M$ sur deux ans) et du 2 février 2026 (programme 55 M$, FDRCMO).
  - Vérification : relecture indépendante du guide, 17 énoncés confirmés. Corrigés avant publication : « séances d'information » retiré de la liste des exclusions (le guide les cite aussi comme élément admissible, p. 3), qualificatifs ajoutés (franchiseurs, comités paritaires, organismes autochtones), courriel présenté comme option (« peut être faite par courriel »), départage seulement entre projets équivalents.
  - Notes : les communiqués sont dans les archives des anciens cabinets (gouvernement changé le 21 oct. 2026) : statut de l'appel confirmé seulement par la page CPMT du 23 oct. Maximums horaires de l'annexe (25 $/h salaires, 150 $/h formateurs) mentionnés sans chiffres (tableau extrait à plat). Aucune donnée sur les fonds restants.
- Page pilier /subventions-pme-quebec/ mise à jour (ligne Productivité-Compétences et conseil « former vos gestionnaires »).
- Écarté : CanExport PME (fermé; « toutes les demandes reçues pour la période 2026-2027 ont été traitées », aucune date de réouverture). Appels CPMT Lanaudière (16 oct.) et Montérégie (28 oct.) fermés. Autres appels CPMT (Sceau rouge, Emplois durables, Côte-Nord) : visent des promoteurs de formation, peu pertinents pour les PME.
- Veille : mise à jour économique du Québec 2026 toujours sans date officielle trouvée; rien d'autre de nouveau et vérifiable (Québec.ca, DEC).
- IndexNow : workflow du 18 nov. réussi (exécution 44307919227); celui de ce push (44528026191) lancé.

## 2026-11-20
- Signalements (GitHub Issues) : aucun.
- Mises à jour : aucune nécessaire. PAUPME revérifié à la page Québec.ca (mise à jour du 19 oct. 2026, inchangée : 150 000 $, 0 % 12 mois puis 3,86 %, jusqu'au 31 mars 2028). EEC 3 déc. et festivals 2 déc. : revérification complète prévue vers le 25 novembre.
- Publié : /papde-subvention-projets-collectifs-developpement-economique/ — sources : cadre normatif PAPDE 2026-2029 (MEIE, approuvé par le CT le 9 juin 2026, dernière mise à jour novembre 2026, p. 3-29 lues mot à mot) + pages Québec.ca des volets 2 (31 juill. 2026) et 1 (27 juill. 2026).
  - Vérification : relecture indépendante, 13 énoncés confirmés (1 M$/projet/année et 3 M$ sur trois ans, taux 60/70 % et 60/40/70 %, cumul 80/50/100 %, mise de fonds 20 %/50 %, 3 mois/3 ans/36 mois, traitement en continu, déclaration PAEE >100 employés et subvention ≥ 100 000 $, non-cumul avec le FDE). Retirés avant publication : « fonctionnement courant » (non confirmé pour le volet 2) et la mention des dépenses entre le dépôt et l'autorisation.
  - Notes : les pages Québec.ca disent « avant le 31 mars 2029 », le cadre dit « autorisées au plus tard » : précisé dans l'article. Pas de champ `deadline`. Ambiguïté du cadre sur les entreprises à but lucratif (« dont les activités sont similaires ») : article limité à la condition sûre (projet au bénéfice de plusieurs entreprises).
- Page pilier /subventions-pme-quebec/ mise à jour (ligne PAPDE et conseil « projet commun »).
- Écarté : appel CPMT « Économie verte et transformation numérique » : le PDF trouvé date de janvier 2022 (programme Ambition-Compétences), pas l'appel 2026 : à revoir si un guide 2026 est trouvé. ESSOR volet 3 : PDF du cadre refusé (PROVENANCE_REQUIRED) cette fois. Mise à jour économique du Québec : les résultats « 25 novembre » datent de 2025; aucune date 2026 officielle trouvée.
- IndexNow : workflow du 19 nov. réussi (exécution 44528026191).

## 2026-11-23
- Signalements (GitHub Issues) : aucun.
- Mises à jour (vérification seulement, `verified` 2026-11-23, contenu inchangé) :
  - /emplois-ete-canada-2027-date-limite/ — guide du demandeur EDSC (page datée 2026-10-27) : période du 27 oct. au 3 déc. 2026 à 23 h 59 (heure du Pacifique), statut « Ouvert », aucune prolongation; ≤ 50 employés à temps plein; 50 % / 100 %; emplois du 19 avril au 28 août 2027.
  - /festivals-evenements-touristiques-2027-aide-financiere/ — page du programme et communiqué du 4 nov. : 2 déc. 2026 à 15 h 59 (volets 1 et 2), aucune prolongation; événements du 1er mai au 31 oct. 2027; OBL admissibles, cumul 50 %, coûts admissibles ≥ 90 000 $; ententes triennales/biennales sans nouvelle demande. Prochaine période (événements du 1er nov. 2027 au 30 avril 2028) : « un mois au cours du printemps 2027 », dates non publiées.
- Publié : aucun article (rien de nouveau et vérifiable).
- Veille : appels de projets en innovation (Québec.ca) : Primo-adoptants — dernière date de dépôt 4 nov. 2026 passée (75 000 $, 60 %); culture scientifique et innovation sociale terminés; secteurs stratégiques fermé (1er avril 2026). Relève et transfert d'entreprises (communiqué du 18 juin 2026, 500 M$ IQ/FCEQ/Réseau accès PME) : ancien et sans modalités de demande, écarté. Mise à jour économique du Québec 2026 : toujours aucune date officielle trouvée. Projet de loi fédéral sur la Mégadéduction : rien trouvé. DEC : seulement des annonces d'aide à des entreprises nommées.
- Accès web : les pages canada.ca et quebec.ca refusées (PROVENANCE_REQUIRED) en lecture directe ont été lues après une recherche web qui faisait ressortir l'URL.
- IndexNow : workflow du 20 nov. réussi (exécution 44739657835).

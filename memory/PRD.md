# PRD — ALLO BRISE DE GLACE

## Problème initial (résumé)
Site web multi-pages de génération de leads pour une société de réparation /
remplacement de pare-brise et vitrages automobiles. 10 pages publiques exactes
(8 pages régionales SEO / Google Ads + Contactez-nous + Mentions légales/CGU),
100 % français, mobile-first, conversion principale = appel téléphonique,
WhatsApp uniquement sur les 5 pages régionales françaises, numéro de téléphone
propre à chaque région, aucun lien régional dans le header ni le footer,
formulaire de contact avec sauvegarde en base avant e-mail, SMTP local (Exim),
aucun avis/statistique/certification inventé.

## Choix d'architecture (validés avec l'utilisateur)
- Frontend : HTML5 + CSS3 + JavaScript vanilla, site statique généré
  (`frontend/build.py` + `site_data.py` + `templates.py` → `frontend/dist/`).
- Backend : FastAPI — `/api/contact` (validation FR, honeypot, rate limiting,
  stockage lead, envoi e-mail), `/api/config` (IDs de suivi publics),
  `/api/health`.
- Données : MongoDB (preview Emergent) derrière une couche isolée
  (`backend/database.py`) ; migration MariaDB documentée (README §5.7, schéma
  SQL fourni).
- E-mail : SMTP local via variables d'environnement ; lead conservé même en
  cas d'échec (email_status = failed).
- Suivi Google Ads/Analytics : variables d'environnement vides par défaut,
  chargement gtag uniquement après consentement cookies.

## Personas
- Automobiliste avec impact/fissure/vitre brisée, sur mobile, cherche un
  numéro à appeler immédiatement (trafic Google Ads local).
- Visiteur préférant une demande écrite (formulaire / devis).
- Moteurs de recherche : pages régionales indépendantes, contenu unique.

## Exigences cœur (statiques)
1. 10 pages : 8 régionales + /contactez-nous/ + /mentions-legales-cgu/ (+ /
   passerelle légère et une 404 système).
2. Numéros régionaux exacts ; WhatsApp (+33756861576) uniquement sur
   ile-de-france, nord-ouest, nord-est, sud-ouest, sud-est.
3. Français uniquement, partout (UI, formulaires, messages, SEO, OG).
4. SEO unique par page (title, description, H1, canonical, OG, FAQ, contenu).
5. Aucun lien régional dans header/footer ; pas de section « Nos régions ».
6. Mobile-first, CTA collant bas d'écran ; en-tête minimal (Accueil,
   Contactez-nous, téléphone).
7. Formulaire : 10 champs + consentement RGPD + honeypot ; validation
   client ET serveur en français ; lead stocké avant tentative d'e-mail.
8. Aucune affirmation invérifiable (pas d'avis, notes, prix, garanties,
   délais promis).

## Réalisé (juillet 2026)
- Générateur de site statique + 12 pages générées (10 + accueil + 404).
- Design « industriel automobile » : marine profond, ambre #E65100, Chivo /
  IBM Plex Sans, hero cinétique (révélation ligne à ligne), marquee éditorial,
  parallaxe hero, sections numérotées, révélations au scroll, Lenis (CDN).
- 8 pages régionales avec contenu SEO + FAQ uniques, schémas
  AutomotiveBusiness + FAQPage, images Open Graph brandées générées (PIL).
- API contact complète (validation FR, honeypot, rate limit 5/10 min,
  MongoDB, SMTP avec statut sent/failed), headers de sécurité.
- Bandeau cookies (opt-in, localStorage), suivi événementiel préparé.
- sitemap.xml (11 URLs), robots.txt, favicon SVG, 404 avec vrai statut 404.
- README de déploiement complet (Ubuntu, Nginx, systemd, Certbot, Exim,
  migration MariaDB, suivi Google, dépannage).
- Header mobile repensé (juillet 2026) : logo à gauche, bouton téléphone
  circulaire 44 px + menu hamburger à droite ; panneau navy (Accueil,
  Contactez-nous, Mentions légales / CGU — aucun lien régional) ; fermeture
  par lien, clic extérieur, Escape ; aria-expanded/aria-label ; breakpoint
  768 px ; desktop inchangé. Correction du débordement 320 px (min-width
  des colonnes du hero).
- Système de CTA hero raffiné (juillet 2026) : bouton d'appel à deux lignes
  (icône + « Appelez-nous » + numéro en plus grand), hauteurs 60-62 px
  desktop (groupe horizontal) et 58-62 px empilés pleine largeur sur mobile
  (écarts 12 px) ; sticky CTA compact distinct (56 px) ; bandeau cookies
  décalé au-dessus du sticky CTA avec safe-area iPhone.

## Vérifications effectuées
- 12 routes en 200 + 404 réel ; titres/meta/canonical/lang fr uniques.
- Numéros affichés + URI tel: conformes sur les 8 régions ; WhatsApp
  présent (×3) sur les 5 pages FR, absent des autres pages.
- Formulaire : validation FR côté client et serveur, envoi réussi
  (lead en base), honeypot silencieux, e-mail en échec propre (pas d'Exim
  local dans le preview) avec lead conservé.
- Captures desktop + mobile (sticky CTA, hero, formulaire, Genève sans
  WhatsApp).

## Backlog priorisé
- P0 : configuration des vrais IDs Google Ads/Analytics + test de conversion
  de bout en bout ; test d'envoi e-mail réel sur le serveur Exim de prod.
- P1 : migration MariaDB sur le serveur Ubuntu (adaptateur `database.py`,
  schéma SQL prêt dans le README) ; mise en place Nginx + Certbot.
- P1 : compléter les [À compléter] des mentions légales (directeur de la
  publication, hébergeur).
- P2 : variantes d'images hero par région (photos locales), test A/B des
  libellés de CTA, compression WebP locale des photos (aujourd'hui servies
  par le CDN Unsplash).

## Prochaines tâches
1. Renseigner MAIL_FROM/MAIL_TO définitifs et tester Exim en production.
2. Ajouter les identifiants Google Ads/Analytics quand disponibles.
3. Exécuter la migration MariaDB et pointer Nginx vers dist/.

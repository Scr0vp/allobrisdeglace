# ALLO BRIS DE GLACE — Documentation technique

Site vitrine multi-pages (génération de leads) pour la réparation et le
remplacement de pare-brise et vitrages automobiles. 100 % en français.

- Frontend : HTML5 + CSS3 + JavaScript vanilla (aucun framework)
- Backend : FastAPI (Python) — formulaire de contact, configuration publique
- Production : Ubuntu + Nginx (reverse proxy) + systemd

---

## 0. Récupérer le projet (GitHub)

```bash
git clone <URL_DU_DEPOT> allobrisdeglace
cd allobrisdeglace
cp .env.example backend/.env   # renseigner les valeurs (aucun secret dans le dépôt)
```

Le site statique complet est déjà généré dans `frontend/dist/` (inclus dans le
dépôt). Pour le régénérer après modification du contenu :
`cd /var/www/allobrisdeglace.com && .venv/bin/python frontend/build.py`.

Fichiers de déploiement fournis dans `deploy/` :
- `deploy/nginx/allobrisdeglace.conf` — configuration Nginx de production
- `deploy/systemd/allobrisdeglace.service` — service systemd du backend
- `deploy/mariadb/001_create_leads.sql` — migration MariaDB (table `leads`)

Le frontend de production est généré par `frontend/build.py` et servi depuis
`frontend/dist/`.

---

## 1. Structure du projet

```
/app
├── backend/
│   ├── server.py          # API FastAPI (/api/contact, /api/config, /api/health)
│   ├── database.py        # Accès aux leads MariaDB
│   ├── mailer.py          # Envoi d'e-mails via /usr/sbin/sendmail (Exim)
│   └── .env               # Configuration (jamais commitée)
├── frontend/
│   ├── site_data.py       # Contenu éditorial FR des 8 régions (numéros, SEO, FAQ)
│   ├── templates.py       # Fragments HTML partagés (header, footer, CTA mobile…)
│   ├── build.py           # Générateur du site statique (+ sitemap + images OG)
│   └── dist/              # Site généré (à servir en production)
│       ├── index.html                     # page passerelle (accueil léger)
│       ├── ile-de-france/index.html       # 8 pages régionales SEO
│       ├── nord-ouest/index.html          # …
│       ├── contactez-nous/index.html      # formulaire de contact
│       ├── mentions-legales-cgu/index.html
│       ├── 404.html
│       ├── robots.txt
│       ├── sitemap.xml
│       ├── favicon.svg
│       └── assets/ (css, js, img)
├── .env.example           # modèle de configuration
└── README.md
```

Les 10 pages publiques : `/ile-de-france/`, `/nord-ouest/`, `/nord-est/`,
`/sud-ouest/`, `/sud-est/`, `/geneve/`, `/montreal/`, `/belgique/`,
`/contactez-nous/`, `/mentions-legales-cgu/` (+ `/` passerelle et une 404).

## 2. Régénérer le site après modification du contenu

Tout le contenu régional (numéros de téléphone, titres, méta-descriptions,
textes SEO, FAQ) se trouve dans `frontend/site_data.py`.

```bash
cd /var/www/allobrisdeglace.com
.venv/bin/python frontend/build.py        # régénère dist/ + sitemap.xml + images Open Graph
```

En production, Nginx sert directement `frontend/dist/`.

## 3. Variables d'environnement

Voir `.env.example`. Principales clés (`backend/.env`) :

| Clé | Rôle |
| --- | --- |
| `MAIL_FROM` | Expéditeur des notifications (ex. `site@allobrisdeglace.com`) |
| `MAIL_TO` | Destinataire des demandes de contact |
| `GOOGLE_ADS_CONVERSION_ID` / `GOOGLE_ADS_CONVERSION_LABEL` | Suivi des conversions (vides = désactivé) |
| `GOOGLE_ANALYTICS_ID` | Mesure d'audience (vide = désactivé) |

Le frontend récupère les identifiants de suivi via `GET /api/config` et ne
charge gtag.js **qu'après consentement** (bandeau cookies) et seulement si
les identifiants sont renseignés.

## 4. Formulaire de contact — flux complet

```
Navigateur → POST /api/contact → validation serveur (messages FR)
  → anti-spam (honeypot « entreprise » + limite : 5 req / 10 min / IP)
  → sauvegarde du lead (couche données)
  → envoi e-mail via `/usr/sbin/sendmail` (Exim)
       succès : email_status = "sent"   + email_sent_at
       échec  : email_status = "failed" (lead CONSERVÉ, erreur journalisée)
  → réponse visiteur : message français dans tous les cas où le lead est stocké
```

Champs stockés : created_at, nom, prenom, telephone, email, region,
type_vehicule, immatriculation, service, message, consentement_rgpd,
page_source, ip_address, user_agent, email_status, email_sent_at.

### Tester le formulaire

```bash
curl -X POST https://VOTRE-DOMAINE/api/contact \
  -H "Content-Type: application/json" \
  -d '{"nom":"Martin","prenom":"Claire","telephone":"06 12 34 56 78",
       "email":"claire@example.fr","region":"Île-de-France",
       "type_vehicule":"Peugeot 208","service":"Remplacement de pare-brise",
       "message":"Impact au centre du pare-brise.","consentement_rgpd":true,
       "page_source":"https://allobrisdeglace.com/ile-de-france/"}'
```

## 5. Déploiement production (Ubuntu + Nginx + Exim + MariaDB)

### 5.1 Prérequis serveur

```bash
sudo apt update
sudo apt install -y python3 python3-venv nginx exim4 mariadb-server
```

### 5.2 Application (backend FastAPI)

```bash
sudo mkdir -p /var/www/allobrisdeglace
sudo chown $USER /var/www/allobrisdeglace
cd /var/www/allobrisdeglace
# copier backend/ et frontend/ du projet
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
cp .env.example backend/.env   # puis renseigner les valeurs
cd /var/www/allobrisdeglace.com && .venv/bin/python frontend/build.py # générer dist/
```

### 5.3 Service systemd (backend)

`/etc/systemd/system/allobrisdeglace.service` :

```ini
[Unit]
Description=API Allo Bris de Glace
After=network.target mariadb.service

[Service]
WorkingDirectory=/var/www/allobrisdeglace/backend
ExecStart=/var/www/allobrisdeglace/.venv/bin/uvicorn server:app --host 127.0.0.1 --port 8001
Restart=always
RestartSec=3
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now allobrisdeglace
```

Le port 8001 reste interne (127.0.0.1) : seul Nginx est exposé.

### 5.4 Nginx / TinyCP

Le serveur actuel utilise TinyCP + Nginx.

Le domaine est servi depuis :

```text
/var/www/allobrisdeglace.com
```

Le certificat TLS actuellement utilisé est :

```text
/opt/tinycp/domains/allobrisdeglace.com/ssl/ssl-BriseSSL.crt
/opt/tinycp/domains/allobrisdeglace.com/ssl/ssl-BriseSSL.key
```

Les règles spécifiques du site sont chargées depuis :

```text
/var/www/allobrisdeglace.com/.nginx.conf
```

Elles assurent notamment le reverse proxy `/api/`, le service des assets,
les URLs régionales, `robots.txt`, `sitemap.xml`, la protection des fichiers
sensibles et la page 404.

Après toute modification :

```bash
nginx -t
systemctl reload nginx
```

Le frontend réellement servi en production se trouve dans :

```text
/var/www/allobrisdeglace.com/frontend/dist
```

### 5.5 SSL — TinyCP / BriseSSL

La gestion du certificat TLS est assurée par TinyCP.


### 5.6 Exim — e-mails locaux

Exim4 fournit le transport local.

Le backend utilise directement :

```text
/usr/sbin/sendmail
```

Les adresses sont définies par `MAIL_FROM` et `MAIL_TO` dans `backend/.env`.

Vérifier le routage :

```bash
exim -bt serviceclient@allobrisdeglace.com
```

Consulter les logs :

```bash
tail -f /var/log/exim4/mainlog
```

Test :

```bash
echo "Test Allo Bris de Glace" | mail -s "Test Exim" serviceclient@allobrisdeglace.com
```

### 5.7 MariaDB

La base de production est MariaDB.

La connexion utilise :

```text
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=allobrisdeglace
DB_USER=...
DB_PASSWORD=...
```

Le schéma SQL se trouve dans :

```text
deploy/mariadb/001_create_leads.sql
```

L'accès aux leads est centralisé dans `backend/database.py` avec `aiomysql`.

Après une modification de configuration :

```bash
systemctl restart allobrisdeglace.service
```

## 6. Suivi Google Ads / Analytics

1. Renseigner `GOOGLE_ADS_CONVERSION_ID`, `GOOGLE_ADS_CONVERSION_LABEL`,
   `GOOGLE_ANALYTICS_ID` dans `backend/.env` puis redémarrer le service.
2. Le bandeau de consentement bloque tout chargement de gtag.js avant accord.
3. Événements envoyés : `click_to_call` (liens tel:), `whatsapp_click`
   (5 pages françaises uniquement), `quote_click` (boutons « Demander un
   devis »), `conversion` Google Ads à l'envoi réussi du formulaire.

## 7. SEO

- `robots.txt` et `sitemap.xml` servis à la racine (11 URLs).
- Chaque page régionale : `<title>`, méta-description, H1, URL canonique,
  Open Graph (titre, description, image brandée générée), `lang="fr"`.
- Données structurées : `AutomotiveBusiness` + `FAQPage` (contenu FAQ
  strictement identique à celui affiché).
- La 404 renvoie un vrai statut HTTP 404 avec `noindex`.

## 8. Sécurité

- Validation serveur + côté client (messages en français).
- Requêtes préparées / ORM uniquement (aucune concaténation SQL).
- Anti-spam : honeypot + limitation de débit par IP.
- Aucun secret dans le frontend ; SMTP/DB côté serveur uniquement.
- En-têtes de sécurité (nosniff, frame, referrer) sur pages et API.
- Aucune trace d'erreur technique exposée au visiteur.

## 9. Dépannage

| Symptôme | Piste |
| --- | --- |
| Formulaire : « Une erreur est survenue… » | Vérifier la base : logs `journalctl -u allobrisdeglace` |
| Lead présent mais `email_status=failed` | Vérifier Exim : `/var/log/exim4/mainlog`, `MAIL_FROM`/`MAIL_TO` |
| 502 sur /api/ | Service backend arrêté : `sudo systemctl status allobrisdeglace` |
| CSS/JS non mis à jour | Cache navigateur : le HTML est en `no-cache`, les assets en cache long — vider le cache |
| Suivi absent | Normal si consentement refusé ou IDs vides |

# ALLO BRISE DE GLACE — Documentation technique

Site vitrine multi-pages (génération de leads) pour la réparation et le
remplacement de pare-brise et vitrages automobiles. 100 % en français.

- Frontend : HTML5 + CSS3 + JavaScript vanilla (aucun framework)
- Backend : FastAPI (Python) — formulaire de contact, configuration publique
- Base de données (preview) : MongoDB via une couche d'accès isolée
- Base de données (production) : MariaDB — voir « Migration MariaDB »
- E-mail : SMTP local (Exim) — 127.0.0.1:25, sans service externe
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
`cd frontend && python3 build.py`.

Fichiers de déploiement fournis dans `deploy/` :
- `deploy/nginx/allobrisdeglace.conf` — configuration Nginx de production
- `deploy/systemd/allobrisdeglace.service` — service systemd du backend
- `deploy/mariadb/001_create_leads.sql` — migration MariaDB (table `leads`)

Note : `frontend/src/`, `craco.config.js`, `tailwind.config.js` sont des
reliques du gabarit initial de l'environnement de développement et ne sont
PAS utilisés par le site (frontend = HTML/CSS/JS vanilla généré dans `dist/`).

---

## 1. Structure du projet

```
/app
├── backend/
│   ├── server.py          # API FastAPI (/api/contact, /api/config, /api/health)
│   ├── database.py        # COUCHE DONNÉES ISOLÉE (MongoDB en preview)
│   ├── mailer.py          # Envoi d'e-mails via SMTP local (Exim)
│   └── .env               # Configuration (jamais commitée)
├── frontend/
│   ├── site_data.py       # Contenu éditorial FR des 8 régions (numéros, SEO, FAQ)
│   ├── templates.py       # Fragments HTML partagés (header, footer, CTA mobile…)
│   ├── build.py           # Générateur du site statique (+ sitemap + images OG)
│   ├── server_static.py   # Serveur statique du PREVIEW (port 3000)
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
cd /app/frontend
python3 build.py        # régénère dist/ + sitemap.xml + images Open Graph
```

En preview Emergent, le serveur statique sert immédiatement les nouveaux
fichiers (aucun redémarrage nécessaire). `dist/assets/` (CSS/JS) est servi
tel quel et n'est pas régénéré par build.py.

## 3. Variables d'environnement

Voir `.env.example`. Principales clés (`backend/.env`) :

| Clé | Rôle |
| --- | --- |
| `MONGO_URL`, `DB_NAME` | Base du preview (fournies par l'environnement) |
| `SMTP_HOST` / `SMTP_PORT` / `SMTP_SECURE` | `127.0.0.1` / `25` / `false` (Exim local) |
| `SMTP_USER` / `SMTP_PASSWORD` | Vides pour Exim local sans auth |
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
  → envoi e-mail via SMTP local
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
sudo apt install -y python3 python3-venv nginx exim4 mariadb-server certbot python3-certbot-nginx
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
cd frontend && python3 build.py # générer dist/
```

### 5.3 Service systemd (backend)

`/etc/systemd/system/allobrisdeglace.service` :

```ini
[Unit]
Description=API Allo Brise de Glace
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

### 5.4 Nginx — configuration de référence

`/etc/nginx/sites-available/allobrisdeglace` :

```nginx
# HTTP → HTTPS
server {
    listen 80;
    listen [::]:80;
    server_name allobrisdeglace.com www.allobrisdeglace.com;
    return 301 https://allobrisdeglace.com$request_uri;
}

# www → domaine canonique
server {
    listen 443 ssl;
    http2 on;
    server_name www.allobrisdeglace.com;
    ssl_certificate     /etc/letsencrypt/live/allobrisdeglace.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/allobrisdeglace.com/privkey.pem;
    return 301 https://allobrisdeglace.com$request_uri;
}

server {
    listen 443 ssl;
    http2 on;
    server_name allobrisdeglace.com;

    ssl_certificate     /etc/letsencrypt/live/allobrisdeglace.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/allobrisdeglace.com/privkey.pem;

    root /var/www/allobrisdeglace/frontend/dist;
    index index.html;

    gzip on;
    gzip_types text/css application/javascript image/svg+xml application/json;

    add_header X-Content-Type-Options nosniff always;
    add_header X-Frame-Options SAMEORIGIN always;
    add_header Referrer-Policy strict-origin-when-cross-origin always;

    # API : reverse proxy, JAMAIS de cache (formulaire)
    location /api/ {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        add_header Cache-Control "no-store" always;
    }

    # Assets statiques : cache long
    location /assets/ {
        expires 30d;
        add_header Cache-Control "public, max-age=2592000, immutable";
        try_files $uri =404;
    }

    location = /favicon.svg { expires 30d; }
    location = /robots.txt { try_files $uri =404; }
    location = /sitemap.xml { try_files $uri =404; }

    # Pages HTML : pas de cache, URLs propres avec slash final
    location / {
        try_files $uri $uri/index.html =404;
        add_header Cache-Control "no-cache" always;
    }

    error_page 404 /404.html;
}
```

```bash
sudo ln -s /etc/nginx/sites-available/allobrisdeglace /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

### 5.5 SSL — Let's Encrypt / Certbot

```bash
sudo certbot --nginx -d allobrisdeglace.com -d www.allobrisdeglace.com
sudo certbot renew --dry-run
```

Les chemins de certificats ci-dessus sont les chemins standards créés par
Certbot ; adaptez-les si votre configuration diffère.

### 5.6 Exim — vérification du SMTP local

```bash
sudo dpkg-reconfigure exim4-config   # type : « internet site » (distribution directe)
echo "Test allobrisdeglace" | mail -s "Test Exim" serviceclient@allobrisdeglace.com
sudo tail -f /var/log/exim4/mainlog
```

L'application envoie sur `127.0.0.1:25` sans authentification
(`SMTP_SECURE=false`). Vérifiez qu'Exim accepte le relais depuis localhost
(comportement par défaut) et que `MAIL_FROM` utilise une adresse du domaine
configuré dans Exim (SPF/DKIM gérés au niveau DNS si nécessaire).

### 5.7 Migration MariaDB (remplacement de MongoDB)

Schéma SQL de la table des leads :

```sql
CREATE DATABASE IF NOT EXISTS allobrisdeglace CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'allobrisdeglace'@'localhost' IDENTIFIED BY 'MOT_DE_PASSE_FORT';
GRANT ALL PRIVILEGES ON allobrisdeglace.* TO 'allobrisdeglace'@'localhost';
FLUSH PRIVILEGES;

USE allobrisdeglace;
CREATE TABLE IF NOT EXISTS leads (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  nom VARCHAR(120) NOT NULL,
  prenom VARCHAR(120) NOT NULL,
  telephone VARCHAR(32) NOT NULL,
  email VARCHAR(190) NOT NULL,
  region VARCHAR(60) NOT NULL,
  type_vehicule VARCHAR(120) NOT NULL,
  immatriculation VARCHAR(20) DEFAULT NULL,
  service VARCHAR(80) NOT NULL,
  message TEXT NOT NULL,
  consentement_rgpd TINYINT(1) NOT NULL DEFAULT 0,
  page_source VARCHAR(500) DEFAULT NULL,
  ip_address VARCHAR(45) DEFAULT NULL,
  user_agent VARCHAR(300) DEFAULT NULL,
  email_status ENUM('pending','sent','failed') NOT NULL DEFAULT 'pending',
  email_sent_at DATETIME(6) DEFAULT NULL,
  INDEX idx_leads_created_at (created_at),
  INDEX idx_leads_email_status (email_status),
  INDEX idx_leads_region (region)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

La couche données est isolée dans `backend/database.py` : remplacez le corps
de `LeadStore.insert()` et `LeadStore.set_email_status()` par des requêtes
préparées MariaDB (paquet `aiomysql` ou `mysql-connector-python`). Aucune
autre partie du code ne change. Méthode :

```bash
.venv/bin/pip install aiomysql
# backend/.env : DB_HOST=127.0.0.1 DB_PORT=3306 MARIADB_NAME=allobrisdeglace ...
sudo systemctl restart allobrisdeglace
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

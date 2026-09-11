# -*- coding: utf-8 -*-
"""Fragments HTML partagés — ALLO BRISE DE GLACE.

En-tête, pied de page, barre d'appel mobile, bannière cookies, icônes.
Aucun lien vers les pages régionales dans l'en-tête ou le pied de page.
"""

LOGO_SVG = (
    '<svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
    '<rect width="64" height="64" rx="14" fill="#0B1528"/>'
    '<path d="M14 44 L22 18 H42 L50 44 Z" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linejoin="round"/>'
    '<path d="M32 22 L28.5 30.5 L34 30.5 L30 40" fill="none" stroke="#E65100" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    "</svg>"
)

ICON_PHONE = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
    '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
    "19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 "
    'a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 '
    '2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
)

ICON_WHATSAPP = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
    '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21 '
    'l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5 '
    'a8.48 8.48 0 0 1 8 8v.5z"/></svg>'
)

ICON_CHECK = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
    '<polyline points="20 6 9 17 4 12"/></svg>'
)

SERVICE_ICONS = {
    "shield": (
        '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
    ),
    "drop": (
        '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>'
    ),
    "glass": (
        '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        '<path d="M4 18 L7 5 H17 L20 18 Z"/><path d="M4 18 H20"/></svg>'
    ),
    "door": (
        '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        '<rect x="5" y="3" width="14" height="18" rx="2"/><line x1="14.5" y1="11" x2="14.5" y2="13"/></svg>'
    ),
    "rear": (
        '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
        '<path d="M4 16 L8 6 H16 L20 16 Z"/><path d="M9.5 10.5h5"/><path d="M9 13h6"/></svg>'
    ),
}


def head(title, desc, canonical, og_image, jsonld="", og_locale="fr_FR",
         page_key="", body_class=""):
    """Bloc <head> complet + ouverture du <body> (langue française)."""
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:locale" content="{og_locale}">
<meta property="og:site_name" content="Allo Brise de Glace">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chivo:wght@500;700;900&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
{jsonld}
</head>
<body data-page="{page_key}" class="{body_class}">
<a class="skip-link" href="#contenu">Aller au contenu</a>
"""


def header(phone_display, phone_tel):
    return f"""<header class="site-header" data-testid="site-header">
  <div class="header-inner">
    <a class="brand" href="/" data-testid="brand-link" aria-label="Allo Brise de Glace — Accueil">
      {LOGO_SVG}
      <span class="brand-name">Allo <strong>Brise de Glace</strong></span>
    </a>
    <nav class="main-nav" aria-label="Navigation principale">
      <a href="/" data-testid="nav-accueil">Accueil</a>
      <a href="/contactez-nous/" data-testid="nav-contact">Contactez-nous</a>
    </nav>
    <a class="header-phone" href="tel:{phone_tel}" data-testid="header-phone-cta" data-track="call" aria-label="Appeler le {phone_display}">
      {ICON_PHONE}<span class="header-phone-number">{phone_display}</span>
    </a>
    <button type="button" class="menu-toggle" data-testid="mobile-menu-toggle" aria-expanded="false" aria-controls="mobile-menu" aria-label="Ouvrir le menu">
      <span class="bar"></span>
      <span class="bar"></span>
    </button>
  </div>
  <nav id="mobile-menu" class="mobile-menu" aria-label="Navigation mobile" data-testid="mobile-menu" hidden>
    <a href="/" data-testid="mobile-nav-accueil">Accueil</a>
    <a href="/contactez-nous/" data-testid="mobile-nav-contact">Contactez-nous</a>
    <a href="/mentions-legales-cgu/" data-testid="mobile-nav-legal">Mentions légales / CGU</a>
  </nav>
</header>
"""


def footer():
    return """<footer class="site-footer" data-testid="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      """ + LOGO_SVG + """
      <div>
        <p class="footer-brand-name">Allo <strong>Brise de Glace</strong></p>
        <p class="footer-baseline">Réparation et remplacement de pare-brise et vitrages automobiles.</p>
      </div>
    </div>
    <nav class="footer-nav" aria-label="Liens de pied de page">
      <a href="/contactez-nous/" data-testid="footer-contact-link">Contactez-nous</a>
      <a href="/mentions-legales-cgu/" data-testid="footer-legal-link">Mentions légales / CGU</a>
    </nav>
  </div>
  <div class="footer-legal">
    <p>© 2026 Allo Brise de Glace — Neutra Group. Tous droits réservés.</p>
  </div>
</footer>
"""


def sticky_cta(kind, phone_display, phone_tel, wa_url=None):
    """Barre d'action fixe mobile. kind = 'both' (Appeler + WhatsApp), 'call' ou None."""
    if kind == "both":
        return f"""<div class="sticky-cta" data-testid="sticky-cta-bar">
  <a class="sticky-btn sticky-btn-call" href="tel:{phone_tel}" data-testid="sticky-call-cta" data-track="call">{ICON_PHONE}<span>Appeler</span></a>
  <a class="sticky-btn sticky-btn-wa" href="{wa_url}" target="_blank" rel="noopener" data-testid="sticky-whatsapp-cta" data-track="whatsapp">{ICON_WHATSAPP}<span>WhatsApp</span></a>
</div>
"""
    if kind == "call":
        return f"""<div class="sticky-cta" data-testid="sticky-cta-bar">
  <a class="sticky-btn sticky-btn-call sticky-btn-full" href="tel:{phone_tel}" data-testid="sticky-call-cta" data-track="call">{ICON_PHONE}<span>Appeler le {phone_display}</span></a>
</div>
"""
    return ""


def cookie_banner():
    return """<div class="cookie-banner" data-testid="cookie-banner" role="dialog" aria-live="polite" aria-label="Consentement aux cookies" hidden>
  <p class="cookie-text">Nous utilisons des cookies de mesure d'audience et de suivi publicitaire, uniquement avec votre accord. Vous pouvez accepter ou refuser : le site reste pleinement utilisable dans les deux cas.</p>
  <div class="cookie-actions">
    <button type="button" class="btn btn-primary btn-sm" data-testid="cookie-accept" data-consent="accept">Accepter les cookies</button>
    <button type="button" class="btn btn-ghost-dark btn-sm" data-testid="cookie-refuse" data-consent="refuse">Refuser</button>
  </div>
  <a class="cookie-more" href="/mentions-legales-cgu/">En savoir plus</a>
</div>
"""


def scripts(extra=""):
    out = (
        '<script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js" defer></script>\n'
        '<script src="/assets/js/main.js" defer></script>\n'
    )
    if extra:
        out += f'<script src="{extra}" defer></script>\n'
    return out + "</body>\n</html>\n"

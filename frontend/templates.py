# -*- coding: utf-8 -*-
"""Fragments HTML partagés — ALLO BRIS DE GLACE.

En-tête, pied de page, barre d'appel mobile, bannière cookies, icônes.
Le pied de page expose les 8 zones régionales pour renforcer le maillage interne.
"""

LOGO_SVG = (
    '<svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
    '<rect width="64" height="64" rx="14" fill="#003B73"/>'
    '<path d="M14 44 L22 18 H42 L50 44 Z" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linejoin="round"/>'
    '<path d="M32 22 L28.5 30.5 L34 30.5 L30 40" fill="none" stroke="#E30613" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    "</svg>"
)

ICON_PHONE = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
    '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
    "19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 "
    'a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 1 '
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
    regional_css = """
<style>
@media (min-width: 900px) {
  body[data-page]:not([data-page="accueil"]):not([data-page="contact"]) .hero-ctas a[data-testid="hero-quote-cta"] { display: none; }
}
.sticky-cta .sticky-btn-call { flex: 1.3; }
.sticky-cta .sticky-btn-wa { flex: .7; }
@media (max-width: 899px) {
  body[data-page]:not([data-page="accueil"]):not([data-page="contact"]) .hero-ctas a[data-testid="hero-quote-cta"] { display: none; }
}
.footer-regions { margin-top: 24px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,.12); }\n.footer-legal { padding-top: 16px; }
.footer-regions-title { margin: 0 0 10px; font-weight: 700; }
.footer-regions-links { display: flex; flex-wrap: wrap; gap: 8px 16px; }
.footer-regions-links a { color: inherit; text-decoration: none; }
.footer-regions-links a:hover { text-decoration: underline; }
</style>
"""
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
<meta property="og:site_name" content="Allo Bris de Glace">
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
{regional_css}
{jsonld}
</head>
<body data-page="{page_key}" class="{body_class}">
<a class="skip-link" href="#contenu">Aller au contenu</a>
"""


def header(phone_display, phone_tel):
    return f"""<header class="site-header" data-testid="site-header">
  <div class="header-inner">
    <a class="brand" href="/" data-testid="brand-link" aria-label="Allo Bris de Glace — Accueil">
      {LOGO_SVG}
      <span class="brand-name">Allo <strong>Bris de Glace</strong></span>
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
    regions = [
        ("ile-de-france", "Île-de-France"),
        ("nord-ouest", "Nord-Ouest"),
        ("nord-est", "Nord-Est"),
        ("sud-ouest", "Sud-Ouest"),
        ("sud-est", "Sud-Est"),
        ("geneve", "Genève"),
        ("montreal", "Montréal"),
        ("belgique", "Belgique"),
    ]
    region_links = "".join(
        f'<a href="/{slug}/">{name}</a>' for slug, name in regions
    )
    return """<footer class="site-footer" data-testid="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      """ + LOGO_SVG + """
      <div>
        <p class="footer-brand-name">Allo <strong>Bris de Glace</strong></p>
        <p class="footer-baseline">Réparation et remplacement de pare-brise et vitrages automobiles.</p>
      </div>
    </div>
    <nav class="footer-nav" aria-label="Liens de pied de page">
      <a href="/contactez-nous/" data-testid="footer-contact-link">Contactez-nous</a>
      <a href="/mentions-legales-cgu/" data-testid="footer-legal-link">Mentions légales / CGU</a>
    </nav>
  </div>
  <div class="footer-inner footer-regions">
    <p class="footer-regions-title">Nos zones d’intervention</p>
    <nav class="footer-regions-links" aria-label="Zones d’intervention">""" + region_links + """</nav>
  </div>
  <div class="footer-inner footer-legal">
    <p>© 2026 Allo Bris de Glace — Neutra Group. Tous droits réservés.</p>
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
    out += '''<script>
(function () {
  var waText = "Bonjour, j'ai un impact sur mon pare-brise, voici une photo";
  document.querySelectorAll('a[href*="wa.me/"]').forEach(function (link) {
    try {
      var url = new URL(link.href, window.location.origin);
      if (!url.searchParams.get('text')) url.searchParams.set('text', waText);
      link.href = url.toString();
    } catch (e) {}
  });

  var page = document.body && document.body.getAttribute('data-page');
  var copy = {
    'ile-de-france': {services: 'Interventions adaptées au rythme francilien', servicesSub: 'En zone urbaine dense comme en grande couronne, nous vous orientons vers la solution de vitrage adaptée à votre véhicule.', why: 'Un accompagnement pensé pour vos trajets quotidiens', steps: 'Un parcours simple, même quand le bris de glace tombe au mauvais moment', stepsSub: 'Décrivez les dégâts, recevez une orientation claire et convenez du prochain créneau avec notre équipe.'},
    'nord-ouest': {services: 'Vitrage automobile pour les routes du Nord-Ouest', servicesSub: 'De l’impact sur autoroute au vitrage brisé après une intempérie, les prestations sont adaptées au type de dommage.', why: 'Une prise en charge claire dans le Nord-Ouest', steps: 'De votre premier appel à la restitution du véhicule', stepsSub: 'Quelques informations sur le véhicule et les dégâts suffisent pour préparer la suite.'},
    'nord-est': {services: 'Pare-brise et vitrages face aux conditions du Nord-Est', servicesSub: 'Les variations de température et les longs trajets peuvent fragiliser un impact : nous vous aidons à choisir la bonne solution.', why: 'Des conseils adaptés aux besoins du Nord-Est', steps: 'Trois repères pour avancer sans perdre de temps', stepsSub: 'Identification du vitrage, estimation de la solution et organisation de l’intervention.'},
    'sud-ouest': {services: 'Réparation et remplacement dans le Sud-Ouest', servicesSub: 'Autoroute, routes départementales ou stationnement : chaque dommage de vitrage est évalué selon sa nature et son emplacement.', why: 'Un service pratique pour vos déplacements', steps: 'Une organisation claire avant l’intervention', stepsSub: 'Nous recueillons les informations utiles avant de convenir avec vous de la suite.'},
    'sud-est': {services: 'Vitrage automobile dans le Sud-Est', servicesSub: 'Impact, fissure ou vitre brisée : la prise en charge est orientée selon le vitrage concerné et les équipements du véhicule.', why: 'L’essentiel pour reprendre la route sereinement', steps: 'Un accompagnement en trois temps', stepsSub: 'Contact, analyse de la demande puis organisation du rendez-vous selon votre situation.'},
    'geneve': {services: 'Pare-brise et vitrage autour de Genève', servicesSub: 'Pour les trajets transfrontaliers et les déplacements quotidiens, nous vous indiquons la solution adaptée au vitrage concerné.', why: 'Une communication simple autour de Genève', steps: 'Comment organiser votre demande', stepsSub: 'Décrivez le dommage et votre véhicule : nous vous indiquons les prochaines étapes.'},
    'montreal': {services: 'Réparation et remplacement de vitrage à Montréal', servicesSub: 'Les vitrages automobiles endommagés sont orientés vers la solution adaptée au véhicule et au type de dommage.', why: 'Un accompagnement adapté à votre véhicule', steps: 'Du signalement du dommage au rendez-vous', stepsSub: 'Un premier échange permet de préciser le besoin avant l’organisation de l’intervention.'},
    'belgique': {services: 'Vitrage automobile en Belgique', servicesSub: 'Pare-brise, vitres latérales et lunette arrière : nous vous aidons à identifier la prestation correspondant au dommage.', why: 'Une prise en charge lisible en Belgique', steps: 'Une démarche en trois étapes', stepsSub: 'Votre demande, l’orientation adaptée et la confirmation des modalités d’intervention.'}
  };

  if (page && page !== 'accueil' && page !== 'contact') {
    var c = copy[page];
    if (c) {
      var s = document.querySelector('[data-testid="services-section"]');
      var w = document.querySelector('[data-testid="why-section"]');
      var p = document.querySelector('[data-testid="process-section"]');
      if (s) { var st = s.querySelector('.section-title'); var ss = s.querySelector('.section-sub'); if (st) st.textContent = c.services; if (ss) ss.textContent = c.servicesSub; }
      if (w) { var wt = w.querySelector('.section-title'); if (wt) wt.textContent = c.why; }
      if (p) { var pt = p.querySelector('.section-title'); var ps = p.querySelector('.section-head'); if (pt) pt.textContent = c.steps; if (ps && c.stepsSub) { var old = ps.querySelector('.section-sub'); if (old) old.textContent = c.stepsSub; else { var sub = document.createElement('p'); sub.className = 'section-sub'; sub.textContent = c.stepsSub; ps.appendChild(sub); } } }
    }

    var seo = document.querySelector('[data-testid="seo-section"]');
    if (seo && !document.querySelector('[data-testid="regional-modalities"]')) {
      var section = document.createElement('section');
      section.className = 'section section--seo regional-modalities-section';
      section.setAttribute('data-testid', 'regional-modalities');
      section.innerHTML = '<div class="section-head reveal"><p class="chapter"><span class="chapter-num">05B</span><span class="chapter-label">Prise de rendez-vous</span></p><h2 class="section-title">Délai et modalités d’intervention</h2></div><div class="prose reveal"><p>Le délai et la modalité d’intervention sont confirmés lors de la prise de rendez-vous selon votre zone, le type de vitrage, le véhicule et la disponibilité.</p><p>Lors de votre appel, nous vous indiquons le créneau proposé et les informations utiles avant l’intervention.</p></div>';
      seo.parentNode.insertBefore(section, seo.nextSibling);
    }
  }
})();
</script>\n'''
    return out + "</body>\n</html>\n"

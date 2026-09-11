# -*- coding: utf-8 -*-
"""Générateur du site statique ALLO BRISE DE GLACE.

Usage : python3 build.py
Produit les pages HTML dans dist/ (10 pages + accueil + 404), le sitemap.xml
et les images Open Graph brandées (dist/assets/img/og-*.png).
"""
import html
import json
import os

from PIL import Image, ImageDraw, ImageFont

import site_data as data
import templates as tpl

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
IMG_DIR = os.path.join(DIST, "assets", "img")
LASTMOD = "2026-07-01"

NAVY = (0, 59, 115)
NAVY_2 = (10, 77, 140)
AMBER = (227, 6, 19)
WHITE = (255, 255, 255)
MUTED = (190, 215, 240)

FONT_BOLD = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"
FONT_REG = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"


def esc(text):
    return html.escape(text, quote=True)


# ---------------------------------------------------------------- images OG
def _fit_font(draw, text, start_size, max_width):
    size = start_size
    while size > 28:
        font = ImageFont.truetype(FONT_BOLD, size)
        if draw.textlength(text, font=font) <= max_width:
            return font
        size -= 4
    return ImageFont.truetype(FONT_BOLD, 28)


def make_og(filename, big_line, sub_line, phone=""):
    img = Image.new("RGB", (1200, 630), NAVY)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 1200, 14], fill=AMBER)
    draw.rectangle([0, 616, 1200, 630], fill=AMBER)
    # marque
    draw.rounded_rectangle([64, 56, 136, 128], radius=16, fill=NAVY_2, outline=(26, 90, 158), width=2)
    draw.polygon([(80, 112), (88, 72), (112, 72), (120, 112)], outline=WHITE, width=4)
    brand_font = ImageFont.truetype(FONT_BOLD, 34)
    draw.text((160, 78), "ALLO BRISE DE GLACE", font=brand_font, fill=WHITE)
    # grand titre
    big_font = _fit_font(draw, big_line, 92, 1050)
    draw.text((64, 250), big_line, font=big_font, fill=WHITE)
    sub_font = _fit_font(draw, sub_line, 44, 1050)
    draw.text((64, 380), sub_line, font=sub_font, fill=MUTED)
    if phone:
        phone_font = ImageFont.truetype(FONT_BOLD, 40)
        width = int(draw.textlength(phone, font=phone_font)) + 72
        draw.rounded_rectangle([64, 480, 64 + width, 556], radius=38, fill=AMBER)
        draw.text((100, 498), phone, font=phone_font, fill=WHITE)
    img.save(os.path.join(IMG_DIR, filename), "PNG", optimize=True)


# ------------------------------------------------------------------ sections
def hero_lines(lines):
    out = []
    for i, line in enumerate(lines):
        out.append(
            f'<span class="line"><span class="line-inner" '
            f'style="--d:{0.1 + i * 0.12:.2f}s">{line}</span></span>'
        )
    return "".join(out)


def trust_list():
    items = "".join(
        f'<li>{tpl.ICON_CHECK}<span>{esc(item)}</span></li>' for item in data.TRUST_ITEMS
    )
    return f'<ul class="trust-list reveal-now" style="--d:.55s">{items}</ul>'


def marquee():
    seq = "".join(
        f'<span class="marquee-item">{esc(item)}</span><span class="marquee-dot" aria-hidden="true"></span>'
        for item in data.MARQUEE_ITEMS
    )
    return (
        '<div class="marquee" aria-hidden="true"><div class="marquee-track">'
        + seq + seq +
        "</div></div>"
    )


def services_section(number="01"):
    cards = []
    for i, svc in enumerate(data.SERVICES):
        icon = tpl.SERVICE_ICONS.get(svc["icon"], tpl.SERVICE_ICONS["shield"])
        cards.append(
            f'<article class="card reveal" style="--d:{i * 0.08:.2f}s" data-testid="service-card-{svc["slug"]}">'
            f'<div class="card-icon">{icon}</div>'
            f"<h3>{esc(svc['title'])}</h3>"
            f"<p>{esc(svc['desc'])}</p>"
            "</article>"
        )
    return f"""<section class="section" data-testid="services-section">
  <div class="section-head reveal">
    <p class="chapter"><span class="chapter-num">{number}</span><span class="chapter-label">Nos prestations</span></p>
    <h2 class="section-title">Réparation &amp; remplacement de vitrage automobile</h2>
    <p class="section-sub">Chaque intervention suit une méthode professionnelle, du diagnostic jusqu'à la restitution du véhicule.</p>
  </div>
  <div class="cards-grid">{''.join(cards)}</div>
</section>
"""


def benefits_section(number="02"):
    items = []
    for i, b in enumerate(data.BENEFITS):
        items.append(
            f'<li class="benefit reveal" style="--d:{i * 0.08:.2f}s">'
            f'<span class="benefit-index">{i + 1:02d}</span>'
            f"<div><h3>{esc(b['title'])}</h3><p>{esc(b['desc'])}</p></div></li>"
        )
    return f"""<section class="section section--alt" data-testid="why-section">
  <div class="section-head reveal">
    <p class="chapter"><span class="chapter-num">{number}</span><span class="chapter-label">Pourquoi nous choisir</span></p>
    <h2 class="section-title">Un service pensé pour la confiance</h2>
  </div>
  <ul class="benefits-grid">{''.join(items)}</ul>
</section>
"""


def steps_section(number="03"):
    steps = []
    for i, s in enumerate(data.STEPS):
        steps.append(
            f'<li class="step reveal" style="--d:{i * 0.1:.2f}s" data-testid="step-{s["num"]}">'
            f'<span class="step-num">{s["num"]}</span>'
            f"<h3>{esc(s['title'])}</h3><p>{esc(s['desc'])}</p></li>"
        )
    return f"""<section class="section" data-testid="process-section">
  <div class="section-head reveal">
    <p class="chapter"><span class="chapter-num">{number}</span><span class="chapter-label">Comment ça marche</span></p>
    <h2 class="section-title">Trois étapes, rien de plus</h2>
  </div>
  <ol class="steps-grid">{''.join(steps)}</ol>
</section>
"""


def final_cta(phone_display, phone_tel, whatsapp):
    wa = ""
    if whatsapp:
        wa = (
            f'<a class="btn btn-whatsapp btn-lg" href="{data.WHATSAPP_URL}" target="_blank" rel="noopener" '
            f'data-testid="final-cta-whatsapp" data-track="whatsapp">{tpl.ICON_WHATSAPP}<span>Nous contacter sur WhatsApp</span></a>'
        )
    return f"""<section class="final-cta reveal" data-testid="final-cta">
  <h2>Besoin d'une réparation ou d'un remplacement de vitrage automobile&nbsp;?</h2>
  <p>Appelez-nous directement ou envoyez votre demande en quelques minutes.</p>
  <div class="final-cta-actions">
    <a class="btn btn-primary btn-lg" href="tel:{phone_tel}" data-testid="final-cta-call" data-track="call">{tpl.ICON_PHONE}<span>Appelez-nous — {esc(phone_display)}</span></a>
    <a class="btn btn-outline-light btn-lg" href="/contactez-nous/" data-testid="final-cta-quote" data-track="quote"><span>Demander un devis</span></a>
    {wa}
  </div>
</section>
"""


def faq_section(faq, number="05"):
    items = []
    for i, (q, a) in enumerate(faq):
        items.append(
            f'<details class="faq-item reveal" style="--d:{i * 0.06:.2f}s" data-testid="faq-item-{i + 1}">'
            f"<summary><span>{esc(q)}</span>"
            '<svg class="icon faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'
            f"</summary><div class=\"faq-answer\"><p>{esc(a)}</p></div></details>"
        )
    return f"""<section class="section section--alt" data-testid="faq-section">
  <div class="section-head reveal">
    <p class="chapter"><span class="chapter-num">{number}</span><span class="chapter-label">Questions fréquentes</span></p>
    <h2 class="section-title">Vos questions sur le bris de glace</h2>
  </div>
  <div class="faq-list">{''.join(items)}</div>
</section>
"""


def jsonld_scripts(*objects):
    return "".join(
        '<script type="application/ld+json">'
        + json.dumps(obj, ensure_ascii=False)
        + "</script>"
        for obj in objects
    )


# ---------------------------------------------------------------- régions
def render_region(r):
    slug = r["slug"]
    canonical = f"{data.BASE_URL}/{slug}/"
    og_image = f"{data.BASE_URL}/assets/img/og-{slug}.png"
    title = esc(r["meta_title"])
    desc = esc(r["meta_desc"])

    business = {
        "@context": "https://schema.org",
        "@type": "AutomotiveBusiness",
        "name": f"Allo Brise de Glace — {r['name']}",
        "url": canonical,
        "telephone": r["phone_tel"],
        "image": og_image,
        "description": r["meta_desc"],
        "areaServed": {"@type": "Place", "name": r["area"]},
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in r["faq"]
        ],
    }
    jsonld = jsonld_scripts(business, faq_ld)

    wa_hero = ""
    if r["whatsapp"]:
        wa_hero = (
            f'<a class="btn btn-whatsapp btn-lg" href="{data.WHATSAPP_URL}" target="_blank" rel="noopener" '
            f'data-testid="hero-whatsapp-cta" data-track="whatsapp">{tpl.ICON_WHATSAPP}<span>Nous contacter sur WhatsApp</span></a>'
        )

    seo_paras = "".join(f"<p>{esc(p)}</p>" for p in r["seo_paras"])
    hero_img = data.img_url(r["hero_img"], 1600)
    hero_alt = data.IMG_ALTS.get(r["hero_img"], "Intervention sur un vitrage automobile")

    body = f"""<main id="contenu">
<section class="hero" data-testid="hero-section">
  <span class="hero-watermark" aria-hidden="true">Bris de glace</span>
  <div class="hero-inner">
    <div class="hero-copy">
      <p class="eyebrow reveal-now" style="--d:.05s">Pare-brise · Vitrage automobile · {esc(r['name'])}</p>
      <h1 class="hero-title" data-testid="hero-title" aria-label="{esc(r['h1_aria'])}">{hero_lines(r['h1_lines'])}</h1>
      <p class="hero-sub reveal-now" style="--d:.42s">{esc(r['hero_sub'])}</p>
      <div class="hero-ctas reveal-now" style="--d:.52s">
        <a class="btn btn-primary btn-hero-call" href="tel:{r['phone_tel']}" data-testid="hero-call-cta" data-track="call" aria-label="Appeler le {esc(r['phone_display'])}">{tpl.ICON_PHONE}<strong class="cta-number">{esc(r['phone_display'])}</strong></a>
        <a class="btn btn-outline-light btn-lg" href="/contactez-nous/" data-testid="hero-quote-cta" data-track="quote"><span>Demander un devis</span></a>
        {wa_hero}
      </div>
      {trust_list()}
    </div>
    <figure class="hero-media reveal-now" style="--d:.3s" data-parallax>
      <img src="{hero_img}" alt="{esc(hero_alt)}" width="1600" height="1067" fetchpriority="high" decoding="async">
      <figcaption class="hero-badge">{tpl.ICON_CHECK}<span>Réparation &amp; remplacement de vitrage automobile</span></figcaption>
    </figure>
  </div>
</section>
{marquee()}
{services_section("01")}
{benefits_section("02")}
{steps_section("03")}
<section class="section section--seo" data-testid="seo-section">
  <div class="section-head reveal">
    <p class="chapter"><span class="chapter-num">04</span><span class="chapter-label">Votre secteur</span></p>
    <h2 class="section-title">{esc(r['seo_heading'])}</h2>
  </div>
  <div class="prose reveal">
    {seo_paras}
    <p class="coverage"><strong>Zone desservie&nbsp;:</strong> {esc(r['cities'])}.</p>
  </div>
</section>
{faq_section(r['faq'], "05")}
{final_cta(r['phone_display'], r['phone_tel'], r['whatsapp'])}
</main>
"""
    sticky_kind = "both" if r["whatsapp"] else "call"
    page = (
        tpl.head(title, desc, canonical, og_image, jsonld=jsonld,
                 og_locale=r["og_locale"], page_key=slug, body_class="has-sticky")
        + tpl.header(r["phone_display"], r["phone_tel"])
        + body
        + tpl.footer()
        + tpl.sticky_cta(sticky_kind, r["phone_display"], r["phone_tel"], data.WHATSAPP_URL)
        + tpl.cookie_banner()
        + tpl.scripts()
    )
    path = os.path.join(DIST, slug, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(page)
    return f"/{slug}/"


# ------------------------------------------------------------------ accueil
def render_home():
    canonical = f"{data.BASE_URL}/"
    og_image = f"{data.BASE_URL}/assets/img/og-accueil.png"
    title = esc("Allo Brise de Glace — Pare-brise & vitrage automobile")
    desc = esc("Allo Brise de Glace : réparation et remplacement de pare-brise, vitres latérales et lunettes arrière. Interlocuteur unique, conseils adaptés, devis clair.")
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Allo Brise de Glace",
        "url": canonical,
        "logo": f"{data.BASE_URL}/favicon.svg",
    }
    lines = ["Réparation &amp; ", "remplacement ", "de vitrage automobile"]
    hero_img = data.img_url(data.IMG_TECH, 1600)
    body = f"""<main id="contenu">
<section class="hero hero--home" data-testid="hero-section">
  <span class="hero-watermark" aria-hidden="true">Bris de glace</span>
  <div class="hero-inner">
    <div class="hero-copy">
      <p class="eyebrow reveal-now" style="--d:.05s">Spécialiste du vitrage automobile</p>
      <h1 class="hero-title" data-testid="hero-title" aria-label="Réparation et remplacement de vitrage automobile">{hero_lines(lines)}</h1>
      <p class="hero-sub reveal-now" style="--d:.42s">Allo Brise de Glace vous accompagne pour la réparation et le remplacement de pare-brise, vitres latérales et lunettes arrière. Un interlocuteur unique, des conseils adaptés et un devis clair avant toute intervention.</p>
      <div class="hero-ctas reveal-now" style="--d:.52s">
        <a class="btn btn-primary btn-lg" href="/contactez-nous/" data-testid="hero-contact-cta" data-track="quote"><span>Contactez-nous</span></a>
        <a class="btn btn-outline-light btn-hero-call" href="tel:{data.MAIN_PHONE_TEL}" data-testid="hero-call-cta" data-track="call" aria-label="Appeler le {esc(data.MAIN_PHONE_DISPLAY)}">{tpl.ICON_PHONE}<strong class="cta-number">{esc(data.MAIN_PHONE_DISPLAY)}</strong></a>
      </div>
      {trust_list()}
    </div>
    <figure class="hero-media reveal-now" style="--d:.3s" data-parallax>
      <img src="{hero_img}" alt="{esc(data.IMG_ALTS[data.IMG_TECH])}" width="1600" height="1067" fetchpriority="high" decoding="async">
      <figcaption class="hero-badge">{tpl.ICON_CHECK}<span>Pare-brise · vitres latérales · lunettes arrière</span></figcaption>
    </figure>
  </div>
</section>
{marquee()}
{services_section("01")}
{steps_section("02")}
{benefits_section("03")}
{final_cta(data.MAIN_PHONE_DISPLAY, data.MAIN_PHONE_TEL, False)}
</main>
"""
    page = (
        tpl.head(title, desc, canonical, og_image, jsonld=jsonld_scripts(org),
                 page_key="accueil", body_class="has-sticky")
        + tpl.header(data.MAIN_PHONE_DISPLAY, data.MAIN_PHONE_TEL)
        + body
        + tpl.footer()
        + tpl.sticky_cta("call", data.MAIN_PHONE_DISPLAY, data.MAIN_PHONE_TEL)
        + tpl.cookie_banner()
        + tpl.scripts()
    )
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as handle:
        handle.write(page)
    return "/"


# ------------------------------------------------------------------ contact
def _field(field_id, label, input_html, required=True):
    mark = ' <span class="required" aria-hidden="true">*</span>' if required else ' <span class="optional">(facultatif)</span>'
    return f"""<div class="field">
  <label for="f-{field_id}">{label}{mark}</label>
  {input_html}
  <span class="field-error" data-error-for="{field_id}" role="alert" data-testid="error-{field_id}"></span>
</div>"""


def render_contact():
    canonical = f"{data.BASE_URL}/contactez-nous/"
    og_image = f"{data.BASE_URL}/assets/img/og-contact.png"
    title = esc("Contactez-nous — Allo Brise de Glace")
    desc = esc("Contactez Allo Brise de Glace pour la réparation ou le remplacement de votre pare-brise ou vitrage automobile. Formulaire de demande et réponse dans les meilleurs délais.")

    region_opts = '<option value="" disabled selected>Sélectionnez votre région</option>' + "".join(
        f"<option value=\"{esc(o)}\">{esc(o)}</option>" for o in data.REGION_OPTIONS
    )
    service_opts = '<option value="" disabled selected>Sélectionnez un service</option>' + "".join(
        f"<option value=\"{esc(o)}\">{esc(o)}</option>" for o in data.SERVICE_OPTIONS
    )

    form = f"""<form id="contact-form" class="contact-form" data-testid="contact-form" novalidate>
  {_field("nom", "Nom", '<input type="text" id="f-nom" name="nom" autocomplete="family-name" required data-testid="field-nom">')}
  {_field("prenom", "Prénom", '<input type="text" id="f-prenom" name="prenom" autocomplete="given-name" required data-testid="field-prenom">')}
  {_field("telephone", "Téléphone", '<input type="tel" id="f-telephone" name="telephone" autocomplete="tel" inputmode="tel" placeholder="Ex. : 06 12 34 56 78" required data-testid="field-telephone">')}
  {_field("email", "E-mail", '<input type="email" id="f-email" name="email" autocomplete="email" placeholder="vous@exemple.fr" required data-testid="field-email">')}
  {_field("region", "Région", f'<select id="f-region" name="region" required data-testid="field-region">{region_opts}</select>')}
  {_field("type_vehicule", "Type de véhicule", '<input type="text" id="f-type-vehicule" name="type_vehicule" placeholder="Ex. : Peugeot 208, Renault Clio…" required data-testid="field-type-vehicule">')}
  {_field("immatriculation", "Immatriculation", '<input type="text" id="f-immatriculation" name="immatriculation" placeholder="Ex. : AB-123-CD" data-testid="field-immatriculation">', required=False)}
  {_field("service", "Service demandé", f'<select id="f-service" name="service" required data-testid="field-service">{service_opts}</select>')}
  {_field("message", "Message", '<textarea id="f-message" name="message" rows="5" placeholder="Décrivez les dégâts : type de vitrage, position de l’impact, circonstances…" required data-testid="field-message"></textarea>')}
  <div class="hp-field" aria-hidden="true"><label for="f-entreprise">Entreprise</label><input type="text" id="f-entreprise" name="entreprise" tabindex="-1" autocomplete="off"></div>
  <input type="hidden" name="page_source" value="">
  <div class="field field--consent">
    <label class="checkbox" for="f-consentement">
      <input type="checkbox" id="f-consentement" name="consentement_rgpd" required data-testid="field-consentement">
      <span>J'accepte que les informations saisies soient utilisées afin de traiter ma demande de contact conformément à la politique de confidentialité.</span>
    </label>
    <span class="field-error" data-error-for="consentement_rgpd" role="alert" data-testid="error-consentement"></span>
  </div>
  <p class="form-status" role="status" aria-live="polite" data-testid="form-status"></p>
  <button type="submit" class="btn btn-primary btn-lg form-submit" data-testid="form-submit-button"><span>Envoyer ma demande</span></button>
</form>
<div class="form-success" data-testid="form-success-message" hidden>
  <div class="form-success-icon">{tpl.ICON_CHECK}</div>
  <h2>Demande envoyée</h2>
  <p>Votre demande a bien été envoyée. Nous vous recontacterons dans les meilleurs délais.</p>
</div>"""

    body = f"""<main id="contenu">
<section class="page-hero" data-testid="contact-hero">
  <p class="eyebrow reveal-now" style="--d:.05s">Demande de contact &amp; devis</p>
  <h1 class="page-title" data-testid="contact-title"><span class="line"><span class="line-inner" style="--d:.1s">Contactez-nous</span></span></h1>
  <p class="page-sub reveal-now" style="--d:.3s">Un impact, une fissure, un vitrage à remplacer&nbsp;? Décrivez votre besoin&nbsp;: nous vous recontacterons dans les meilleurs délais. Pour une réponse immédiate, appelez-nous.</p>
</section>
<section class="section section--contact">
  <div class="contact-layout">
    <aside class="contact-aside reveal" data-testid="contact-aside">
      <div class="contact-card">
        <h2>Par téléphone</h2>
        <p>La voie la plus directe pour décrire votre besoin.</p>
        <a class="btn btn-primary btn-lg" href="tel:{data.MAIN_PHONE_TEL}" data-testid="contact-call-cta" data-track="call">{tpl.ICON_PHONE}<strong>{esc(data.MAIN_PHONE_DISPLAY)}</strong></a>
      </div>
      <div class="contact-card">
        <h2>Siège</h2>
        <p>Neutra Group<br>200, rue de la Croix Nivert<br>75015 Paris</p>
      </div>
      <div class="contact-card">
        <h2>Votre demande</h2>
        <p>Vos informations servent uniquement à traiter votre demande de contact, conformément à notre politique de confidentialité.</p>
      </div>
    </aside>
    <div class="contact-form-wrap reveal" style="--d:.15s">{form}</div>
  </div>
</section>
</main>
"""
    page = (
        tpl.head(title, desc, canonical, og_image, page_key="contact", body_class="has-sticky")
        + tpl.header(data.MAIN_PHONE_DISPLAY, data.MAIN_PHONE_TEL)
        + body
        + tpl.footer()
        + tpl.sticky_cta("call", data.MAIN_PHONE_DISPLAY, data.MAIN_PHONE_TEL)
        + tpl.cookie_banner()
        + tpl.scripts("/assets/js/contact.js")
    )
    path = os.path.join(DIST, "contactez-nous", "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(page)
    return "/contactez-nous/"


# ------------------------------------------------------------ mentions légales
def render_legal():
    canonical = f"{data.BASE_URL}/mentions-legales-cgu/"
    og_image = f"{data.BASE_URL}/assets/img/og-default.png"
    title = esc("Mentions légales / CGU — Allo Brise de Glace")
    desc = esc("Mentions légales et conditions générales d'utilisation du site allobrisdeglace.com, édité par Neutra Group.")
    body = f"""<main id="contenu">
<section class="page-hero" data-testid="legal-hero">
  <p class="eyebrow reveal-now" style="--d:.05s">Informations légales</p>
  <h1 class="page-title" data-testid="legal-title"><span class="line"><span class="line-inner" style="--d:.1s">Mentions légales / CGU</span></span></h1>
</section>
<section class="section">
  <div class="prose prose--legal" data-testid="legal-content">
    <h2>Mentions légales</h2>
    <p>Le site allobrisdeglace.com est édité par la société <strong>Neutra Group</strong>.</p>
    <ul>
      <li>SIREN&nbsp;: 101 724 83</li>
      <li>Siège social&nbsp;: 200, rue de la Croix Nivert, 75015 Paris</li>
      <li>Capital social&nbsp;: 25&nbsp;000&nbsp;€</li>
      <li>Directeur de la publication&nbsp;: [À compléter]</li>
      <li>Hébergeur du site&nbsp;: [À compléter]</li>
    </ul>
    <h2>Informations sur l'entreprise</h2>
    <p>Allo Brise de Glace est une enseigne de Neutra Group spécialisée dans la réparation et le remplacement de pare-brise et de vitrages automobiles. Pour toute question, utilisez la page <a href="/contactez-nous/">Contactez-nous</a>.</p>
    <h2>Conditions générales d'utilisation</h2>
    <p>L'accès au site allobrisdeglace.com implique l'acceptation des présentes conditions. Le site a pour objet de présenter les services de réparation et de remplacement de vitrages automobiles et de permettre aux visiteurs de transmettre une demande de contact. Les informations présentées sont fournies à titre indicatif et peuvent évoluer.</p>
    <h2>Responsabilité</h2>
    <p>Neutra Group s'efforce d'assurer l'exactitude des informations diffusées sur le site, sans pouvoir en garantir l'exhaustivité. L'éditeur ne saurait être tenu responsable d'un dommage résultant de l'utilisation du site ou d'une difficulté technique d'accès. Les demandes transmises via le formulaire font l'objet d'un traitement dans les meilleurs délais, sans engagement sur un délai précis de réponse.</p>
    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble des contenus du site (textes, éléments graphiques, identité visuelle) est la propriété de Neutra Group ou fait l'objet d'une autorisation d'utilisation. Toute reproduction ou réutilisation, totale ou partielle, sans autorisation écrite préalable est interdite.</p>
    <h2>Données personnelles</h2>
    <p>Les informations transmises via le formulaire de contact (identité, coordonnées, informations relatives au véhicule) sont utilisées exclusivement pour traiter votre demande. Conformément au Règlement général sur la protection des données (RGPD) et à la loi Informatique et Libertés, vous disposez de droits d'accès, de rectification, d'opposition et de suppression des données vous concernant. Pour les exercer, contactez-nous via la page <a href="/contactez-nous/">Contactez-nous</a>. Les données ne sont ni cédées ni vendues à des tiers.</p>
    <h2>Cookies</h2>
    <p>Le site peut utiliser des cookies de mesure d'audience et de suivi publicitaire (Google Analytics, Google Ads) uniquement après votre consentement, recueilli via le bandeau affiché lors de votre première visite. Vous pouvez accepter ou refuser ces cookies&nbsp;: le refus n'affecte pas l'utilisation du site. Aucun cookie de suivi n'est déposé sans votre accord.</p>
    <h2>Contact</h2>
    <p>Pour toute question concernant le site ou vos données personnelles, utilisez la page <a href="/contactez-nous/">Contactez-nous</a> ou appelez le <a href="tel:{data.MAIN_PHONE_TEL}">{esc(data.MAIN_PHONE_DISPLAY)}</a>.</p>
  </div>
</section>
</main>
"""
    page = (
        tpl.head(title, desc, canonical, og_image, page_key="mentions-legales")
        + tpl.header(data.MAIN_PHONE_DISPLAY, data.MAIN_PHONE_TEL)
        + body
        + tpl.footer()
        + tpl.cookie_banner()
        + tpl.scripts()
    )
    path = os.path.join(DIST, "mentions-legales-cgu", "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(page)
    return "/mentions-legales-cgu/"


# -------------------------------------------------------------------- 404
def render_404():
    canonical = f"{data.BASE_URL}/404"
    og_image = f"{data.BASE_URL}/assets/img/og-default.png"
    page = (
        tpl.head("Page introuvable — Allo Brise de Glace",
                 "La page que vous recherchez n'existe pas ou a été déplacée.",
                 canonical, og_image, page_key="404")
        .replace('<meta name="robots" content="index, follow">',
                 '<meta name="robots" content="noindex, follow">')
        + tpl.header(data.MAIN_PHONE_DISPLAY, data.MAIN_PHONE_TEL)
        + """<main id="contenu">
<section class="page-hero page-hero--404" data-testid="notfound-section">
  <p class="notfound-code" aria-hidden="true">404</p>
  <h1 class="page-title" data-testid="notfound-title"><span class="line"><span class="line-inner" style="--d:.1s">Page introuvable</span></span></h1>
  <p class="page-sub reveal-now" style="--d:.3s">La page que vous recherchez n'existe pas ou a été déplacée.</p>
  <div class="hero-ctas reveal-now" style="--d:.4s">
    <a class="btn btn-primary btn-lg" href="/" data-testid="notfound-home-cta"><span>Retour à l'accueil</span></a>
  </div>
</section>
</main>
"""
        + tpl.footer()
        + tpl.scripts()
    )
    with open(os.path.join(DIST, "404.html"), "w", encoding="utf-8") as handle:
        handle.write(page)


# ------------------------------------------------------------------ sitemap
def render_sitemap(urls):
    entries = "".join(
        f"  <url><loc>{data.BASE_URL}{u}</loc><lastmod>{LASTMOD}</lastmod></url>\n"
        for u in urls
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + entries
        + "</urlset>\n"
    )
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as handle:
        handle.write(xml)


# ---------------------------------------------------------------------- main
def main():
    os.makedirs(IMG_DIR, exist_ok=True)

    urls = [render_home()]
    for r in data.REGIONS:
        urls.append(render_region(r))
    urls.append(render_contact())
    urls.append(render_legal())
    render_404()

    for r in data.REGIONS:
        make_og(
            f"og-{r['slug']}.png",
            r["name"],
            "Pare-brise & vitrage automobile",
            r["phone_display"],
        )
    make_og("og-accueil.png", "Pare-brise & vitrage", "Réparation et remplacement de vitrage automobile", data.MAIN_PHONE_DISPLAY)
    make_og("og-contact.png", "Contactez-nous", "Réparation et remplacement de vitrage automobile", data.MAIN_PHONE_DISPLAY)
    make_og("og-default.png", "Allo Brise de Glace", "Réparation et remplacement de vitrage automobile", "")

    render_sitemap(urls)
    print("Pages générées :")
    for u in urls:
        print(" -", u)
    print(" - /404.html")
    print("Sitemap et images Open Graph générés.")


if __name__ == "__main__":
    main()

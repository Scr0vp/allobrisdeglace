# -*- coding: utf-8 -*-
"""Contenu éditorial du site ALLO BRISE DE GLACE.

Toutes les chaînes visibles sont en français. Chaque page régionale possède
un titre, une méta-description, un H1, un contenu SEO et une FAQ uniques.
Aucune statistique, avis, certification ou affirmation invérifiable.
"""

SITE_NAME = "Allo Brise de Glace"
BASE_URL = "https://allobrisdeglace.com"
WHATSAPP_URL = "https://wa.me/33756861576"

# Numéro de la ligne Île-de-France, utilisé comme ligne principale sur les
# pages non régionales (accueil, contact, mentions légales).
MAIN_PHONE_DISPLAY = "01 89 70 35 61"
MAIN_PHONE_TEL = "+330189703561"

IMG_TECH = "photo-1651084296894-105edab05b26"      # pose de joint sur pare-brise
IMG_REPAIR = "photo-1708805282706-f44730b7e527"    # intervention sur pare-brise
IMG_INTERIOR = "photo-1771491237218-cbd4a707497e"  # préparation du vitrage
IMG_SIDE = "photo-1602970890693-e576d76a900f"      # vitrage latéral / portière
IMG_ADAS = "photo-1608259243654-70c070e0f6ed"      # contrôle technique atelier

IMG_ALTS = {
    IMG_TECH: "Technicien appliquant un joint d'étanchéité sur un pare-brise",
    IMG_REPAIR: "Intervention de réparation sur un pare-brise automobile",
    IMG_INTERIOR: "Préparation minutieuse d'un vitrage automobile en atelier",
    IMG_SIDE: "Vitre latérale et portière d'un véhicule",
    IMG_ADAS: "Technicien contrôlant un vitrage automobile en atelier",
}


def img_url(photo_id, width=1600):
    return (
        "https://images.unsplash.com/"
        + photo_id
        + "?auto=format&fit=crop&w="
        + str(width)
        + "&q=70"
    )


SERVICES = [
    {
        "slug": "remplacement-pare-brise",
        "title": "Remplacement de pare-brise",
        "desc": "Dépose du vitrage endommagé et pose d'un pare-brise neuf, avec un collage professionnel et un contrôle complet avant la restitution de votre véhicule.",
        "icon": "shield",
    },
    {
        "slug": "reparation-impact",
        "title": "Réparation d'impact",
        "desc": "Injection d'une résine spécifique dans l'impact pour stopper son évolution et retrouver une surface homogène, sans remplacer le pare-brise lorsque la réparation est possible.",
        "icon": "drop",
    },
    {
        "slug": "remplacement-vitrage",
        "title": "Remplacement de vitrage automobile",
        "desc": "Prise en charge de l'ensemble des vitrages : vitres latérales, lunette arrière, déflecteurs ou éléments fixes, avec des vitrages adaptés à votre véhicule.",
        "icon": "glass",
    },
    {
        "slug": "vitre-laterale",
        "title": "Remplacement de vitre latérale",
        "desc": "Remplacement de la vitre de portière, nettoyage des débris de verre dans l'habitacle et vérification du mécanisme de lève-vitre.",
        "icon": "door",
    },
    {
        "slug": "lunette-arriere",
        "title": "Remplacement de lunette arrière",
        "desc": "Pose d'une lunette arrière neuve avec reconnexion du dégivrage et des équipements intégrés lorsqu'ils sont présents.",
        "icon": "rear",
    },
]

TRUST_ITEMS = [
    "Service professionnel",
    "Accompagnement personnalisé",
    "Devis clair avant intervention",
    "Solutions adaptées à votre véhicule",
]

BENEFITS = [
    {
        "title": "Service professionnel",
        "desc": "Des vitrages conformes et une pose soignée, dans le respect des règles de sécurité.",
    },
    {
        "title": "Prise en charge simple",
        "desc": "Un seul interlocuteur, de votre premier appel jusqu'à l'intervention.",
    },
    {
        "title": "Conseils adaptés",
        "desc": "Réparation ou remplacement : nous vous orientons vers la solution la plus pertinente pour votre situation.",
    },
    {
        "title": "Communication claire",
        "desc": "Un devis transparent et des réponses directes à vos questions, sans jargon inutile.",
    },
    {
        "title": "Véhicules modernes",
        "desc": "Prise en compte des équipements embarqués : capteurs de pluie, caméras, pare-brise chauffants ou athermiques.",
    },
]

STEPS = [
    {
        "num": "01",
        "title": "Appelez-nous",
        "desc": "Un interlocuteur vous répond et prend en compte votre demande.",
    },
    {
        "num": "02",
        "title": "Décrivez votre besoin",
        "desc": "Type de vitrage, véhicule, circonstances : quelques précisions suffisent pour évaluer la situation.",
    },
    {
        "num": "03",
        "title": "Nous vous accompagnons",
        "desc": "Vous recevez un devis clair et nous organisons ensemble la suite.",
    },
]

MARQUEE_ITEMS = [
    "Remplacement de pare-brise",
    "Réparation d'impact",
    "Vitre latérale",
    "Lunette arrière",
    "Vitrage automobile",
    "Devis clair",
]

REGIONS = [
    {
        "slug": "ile-de-france",
        "name": "Île-de-France",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "en Île-de-France"],
        "h1_aria": "Pare-brise et vitrage automobile en Île-de-France",
        "meta_title": "Pare-Brise & Vitrage Automobile Île-de-France | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles en Île-de-France. Appelez le 01 89 70 35 61 : interlocuteur unique, devis clair.",
        "og_locale": "fr_FR",
        "phone_display": "01 89 70 35 61",
        "phone_tel": "+330189703561",
        "whatsapp": True,
        "hero_img": IMG_TECH,
        "hero_sub": "Un impact, une fissure ou une vitre brisée ? Nous vous accompagnons pour la réparation ou le remplacement de votre vitrage automobile, partout en Île-de-France, avec un interlocuteur unique et un devis clair.",
        "seo_heading": "Pare-brise et vitrage automobile en Île-de-France",
        "seo_paras": [
            "Boulevard périphérique, A1, A4, A6 ou A86 : les axes franciliens comptent parmi les plus fréquentés d'Europe, et les projections de gravillons y sont quotidiennes. Un simple impact peut rapidement se transformer en fissure. Allo Brise de Glace vous accompagne pour la réparation ou le remplacement de votre pare-brise en Île-de-France, que vous soyez à Paris, dans les Hauts-de-Seine, la Seine-Saint-Denis, le Val-de-Marne, les Yvelines, l'Essonne, le Val-d'Oise ou la Seine-et-Marne.",
            "Au-delà du pare-brise, nous prenons en charge l'ensemble du vitrage automobile : vitre latérale brisée, lunette arrière endommagée, déflecteur ou élément fixe. Après une effraction en stationnement ou un choc, nous vous aidons à sécuriser votre véhicule et à organiser le remplacement du vitrage concerné.",
            "Notre démarche est simple : vous appelez, vous décrivez votre besoin, nous vous accompagnons. Vous obtenez un devis clair avant toute intervention et des conseils adaptés à votre véhicule, qu'il s'agisse d'une citadine récente, d'un utilitaire ou d'un modèle équipé de caméras et de capteurs d'aide à la conduite.",
        ],
        "cities": "Paris, Boulogne-Billancourt, Saint-Denis, Créteil, Nanterre, Versailles, Argenteuil, Montreuil et l'ensemble des départements franciliens",
        "area": "Île-de-France",
        "faq": [
            (
                "Quand faut-il remplacer un pare-brise plutôt que le réparer ?",
                "Le remplacement est nécessaire lorsque l'impact se situe dans le champ de vision du conducteur, lorsque la fissure est longue ou lorsque le verre est endommagé en profondeur. Un petit impact hors champ de vision peut souvent être réparé par injection de résine. Décrivez-nous les dégâts : nous vous orientons vers la bonne solution.",
            ),
            (
                "Peut-on réparer un impact sur un pare-brise ?",
                "Oui, dans de nombreux cas. Un impact de type œil-de-bœuf ou étoile, de taille limitée et situé hors du champ de vision, peut être réparé par injection de résine. Plus l'intervention est rapide, moins l'impact risque de s'étendre en fissure, notamment avec les variations de température.",
            ),
            (
                "Quel est le prix d'un remplacement de pare-brise en Île-de-France ?",
                "Le tarif dépend du véhicule, du modèle de pare-brise et de ses équipements : capteurs de pluie, caméra, affichage tête haute, verre chauffant ou athermique. Appelez-nous avec votre immatriculation : nous vous communiquons un devis clair avant toute intervention.",
            ),
            (
                "Combien de temps prend une intervention ?",
                "Une réparation d'impact prend généralement moins d'une heure. Un remplacement de pare-brise demande davantage de temps, notamment en raison du temps de séchage de la colle et du recalibrage éventuel des caméras. Nous vous indiquons une estimation précise lors de votre appel.",
            ),
            (
                "Quels vitrages automobiles peuvent être remplacés ?",
                "Nous prenons en charge le pare-brise, les vitres latérales avant et arrière, la lunette arrière ainsi que les déflecteurs et vitrages fixes. Selon le modèle du véhicule, les toits vitrés et éléments spécifiques sont étudiés au cas par cas.",
            ),
        ],
    },
    {
        "slug": "nord-ouest",
        "name": "Nord-Ouest",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "dans le Nord-Ouest"],
        "h1_aria": "Pare-brise et vitrage automobile dans le Nord-Ouest",
        "meta_title": "Pare-Brise & Vitrage Automobile Nord-Ouest | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles dans le Nord-Ouest. Appelez le 02 55 99 45 92 : conseils adaptés, devis clair.",
        "og_locale": "fr_FR",
        "phone_display": "02 55 99 45 92",
        "phone_tel": "+330255994592",
        "whatsapp": True,
        "hero_img": IMG_REPAIR,
        "hero_sub": "Impact, fissure ou vitre brisée dans le Nord-Ouest ? Un interlocuteur unique vous accompagne pour la réparation ou le remplacement de votre vitrage automobile, avec un devis clair avant toute intervention.",
        "seo_heading": "Pare-brise et vitrage automobile dans le Nord-Ouest",
        "seo_paras": [
            "De la Normandie à la Bretagne et aux Pays de la Loire, les automobilistes du Nord-Ouest parcourent chaque jour l'A13, l'A28, l'A84 ou les routes nationales. Gravillons, intempéries et écarts de température fragilisent les vitrages. Allo Brise de Glace répond à vos besoins de réparation et de remplacement de pare-brise dans tout le quart nord-ouest de la France, de Rouen à Nantes en passant par Caen et Rennes.",
            "Impact sur l'autoroute, vitre latérale brisée, lunette arrière fendue : nous vous aidons à identifier la solution adaptée à votre véhicule. Lorsqu'une réparation d'impact est possible, elle évite le remplacement complet du pare-brise. Lorsque le remplacement est nécessaire, nous organisons la suite avec vous, simplement.",
            "Un appel suffit pour démarrer : vous nous décrivez la situation, nous vous donnons un avis clair et un devis transparent. Notre objectif : vous remettre en route dans les meilleures conditions, avec un vitrage conforme et une prise en charge professionnelle.",
        ],
        "cities": "Rouen, Caen, Rennes, Nantes, Le Mans, Brest, Angers, Tours, Laval, Le Havre et leurs agglomérations",
        "area": "Nord-Ouest de la France",
        "faq": [
            (
                "Un impact peut-il être réparé ou faut-il remplacer le pare-brise ?",
                "Tout dépend de la taille, de la profondeur et de la position de l'impact. Un éclat limité, hors du champ de vision, se répare généralement par injection de résine. Une fissure longue, un impact dans le champ de vision ou un verre atteint en profondeur imposent le remplacement. Nous vous donnons un avis clair dès la description des dégâts.",
            ),
            (
                "Combien coûte un remplacement de pare-brise dans le Nord-Ouest ?",
                "Le prix varie selon le véhicule et les équipements intégrés au vitrage : capteurs, caméra d'aide à la conduite, verre athermique ou chauffant. Contactez-nous avec votre immatriculation pour recevoir un devis transparent avant toute décision.",
            ),
            (
                "Combien de temps faut-il prévoir pour une réparation d'impact ?",
                "Une réparation d'impact par injection de résine prend généralement moins d'une heure. C'est une solution rapide qui évite le remplacement complet lorsque l'impact est réparable. Nous vous confirmons la faisabilité avant l'intervention.",
            ),
            (
                "Intervenez-vous aussi pour les vitres latérales et la lunette arrière ?",
                "Oui. Nous prenons en charge les vitres latérales avant et arrière, la lunette arrière, les déflecteurs et les vitrages fixes. Le nettoyage des débris de verre dans l'habitacle fait partie de la prise en charge.",
            ),
            (
                "Puis-je continuer à rouler avec une fissure sur le pare-brise ?",
                "Une fissure fragilise la structure du vitrage et peut s'étendre brutalement, en particulier avec les variations de température. Elle peut également entraîner une contre-visite au contrôle technique si elle se situe dans le champ de vision. Faites évaluer la situation rapidement.",
            ),
        ],
    },
    {
        "slug": "nord-est",
        "name": "Nord-Est",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "dans le Nord-Est"],
        "h1_aria": "Pare-brise et vitrage automobile dans le Nord-Est",
        "meta_title": "Pare-Brise & Vitrage Automobile Nord-Est | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles dans le Nord-Est. Appelez le 03 74 47 64 78 : prise en charge simple, devis clair.",
        "og_locale": "fr_FR",
        "phone_display": "03 74 47 64 78",
        "phone_tel": "+330374476478",
        "whatsapp": True,
        "hero_img": IMG_INTERIOR,
        "hero_sub": "Sur les axes du Nord-Est, un impact arrive vite. Nous vous accompagnons pour la réparation ou le remplacement de votre pare-brise et de vos vitrages, avec des conseils adaptés et un devis clair.",
        "seo_heading": "Pare-brise et vitrage automobile dans le Nord-Est",
        "seo_paras": [
            "L'A4, l'A26, l'A31 ou l'A36 structurent les déplacements du Nord-Est, entre Lille, Reims, Metz, Strasbourg et Dijon. Le trafic poids lourds, les gravillons et les hivers rigoureux mettent les vitrages à rude épreuve. Allo Brise de Glace vous accompagne pour la réparation d'impact et le remplacement de pare-brise dans l'ensemble du quart nord-est de la France.",
            "Le froid est l'ennemi d'un pare-brise déjà marqué : les écarts de température entre un habitacle chauffé et un extérieur gelé transforment rapidement un impact en fissure. Mieux vaut faire évaluer les dégâts sans attendre. Nous prenons également en charge les vitres latérales, lunettes arrière et vitrages fixes.",
            "Vous appelez, vous décrivez votre besoin, nous vous accompagnons : un interlocuteur unique, un avis honnête sur la solution adaptée et un devis clair avant toute intervention. Cette simplicité est au cœur de notre service, pour les particuliers comme pour les professionnels.",
        ],
        "cities": "Lille, Strasbourg, Metz, Nancy, Reims, Dijon, Amiens, Roubaix, Mulhouse, Besançon et leurs agglomérations",
        "area": "Nord-Est de la France",
        "faq": [
            (
                "Le froid peut-il aggraver un impact sur le pare-brise ?",
                "Oui. Les écarts de température entre l'habitacle chauffé et l'extérieur, fréquents dans le Nord-Est en hiver, font travailler le verre et peuvent transformer un simple impact en fissure. Faites évaluer l'impact rapidement : une réparation à temps évite souvent le remplacement.",
            ),
            (
                "Quand le remplacement du pare-brise est-il nécessaire ?",
                "Le remplacement s'impose lorsque l'impact se trouve dans le champ de vision du conducteur, lorsque la fissure est longue ou proche du bord du vitrage, ou lorsque le verre feuilleté est atteint en profondeur. Nous vous expliquons clairement la situation avant toute décision.",
            ),
            (
                "Quel est le prix d'une réparation d'impact ?",
                "Le tarif dépend de la nature de l'impact et de sa position. La réparation est dans tous les cas plus économique qu'un remplacement complet. Appelez-nous : après quelques questions, nous vous communiquons un devis clair.",
            ),
            (
                "Combien de temps dure un remplacement de pare-brise ?",
                "Il faut compter le temps de dépose, de pose et de séchage de la colle, auquel s'ajoute le recalibrage des caméras lorsque le véhicule en est équipé. Nous vous donnons une estimation précise en fonction de votre véhicule lors de votre appel.",
            ),
            (
                "Quels vitrages remplacez-vous dans le Nord-Est ?",
                "Pare-brise, vitres latérales avant et arrière, lunette arrière, déflecteurs et vitrages fixes. Pour les vitrages spécifiques comme les toits panoramiques, nous étudions votre demande au cas par cas.",
            ),
        ],
    },
    {
        "slug": "sud-ouest",
        "name": "Sud-Ouest",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "dans le Sud-Ouest"],
        "h1_aria": "Pare-brise et vitrage automobile dans le Sud-Ouest",
        "meta_title": "Pare-Brise & Vitrage Automobile Sud-Ouest | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles dans le Sud-Ouest. Appelez le 05 54 54 83 81 : interlocuteur unique, devis clair.",
        "og_locale": "fr_FR",
        "phone_display": "05 54 54 83 81",
        "phone_tel": "+330554548381",
        "whatsapp": True,
        "hero_img": IMG_SIDE,
        "hero_sub": "Entre Bordeaux, Toulouse et l'ensemble du Sud-Ouest, nous vous accompagnons pour la réparation ou le remplacement de votre pare-brise et de vos vitrages automobiles, avec un devis clair et une prise en charge simple.",
        "seo_heading": "Pare-brise et vitrage automobile dans le Sud-Ouest",
        "seo_paras": [
            "L'A62, l'A63, l'A64 ou l'A89 traversent le Sud-Ouest sur de longues distances, entre Bordeaux, Toulouse, Pau et Bayonne. Les projections de gravillons y sont fréquentes, et la chaleur estivale accentue l'évolution des fissures : un impact sans gravité au printemps peut devenir une fissure en plein été. Allo Brise de Glace vous accompagne pour la réparation et le remplacement de pare-brise dans tout le Sud-Ouest.",
            "Vitre latérale brisée, lunette arrière endommagée ou pare-brise fissuré : nous vous aidons à choisir entre réparation et remplacement, en toute transparence. Les véhicules récents équipés de capteurs ou de caméras derrière le pare-brise sont pris en compte dans notre évaluation.",
            "Notre fonctionnement tient en trois étapes : vous appelez, vous décrivez votre besoin, nous vous accompagnons. Vous recevez un devis clair avant toute intervention et vous échangez avec un interlocuteur unique jusqu'à la résolution de votre demande.",
        ],
        "cities": "Bordeaux, Toulouse, Pau, Bayonne, La Rochelle, Limoges, Poitiers, Montauban, Agen, Biarritz et leurs agglomérations",
        "area": "Sud-Ouest de la France",
        "faq": [
            (
                "La chaleur peut-elle faire évoluer une fissure ?",
                "Oui. La chaleur fait se dilater le verre, et l'air conditionné créé un écart de température important entre l'intérieur et l'extérieur du véhicule. Dans le Sud-Ouest en été, un impact non traité peut s'étendre rapidement. Mieux vaut le faire réparer dès qu'il est constaté.",
            ),
            (
                "Quand faut-il remplacer un pare-brise ?",
                "Lorsque l'impact se situe dans le champ de vision, lorsque la fissure est longue ou atteint le bord du vitrage, ou lorsque le verre est endommagé en profondeur. Dans les autres cas, une réparation par injection de résine est souvent possible. Nous vous orientons vers la solution la plus pertinente.",
            ),
            (
                "Quel est le prix d'un remplacement de pare-brise dans le Sud-Ouest ?",
                "Le tarif dépend du modèle de véhicule et des équipements du vitrage : capteurs de pluie, caméra, affichage tête haute ou verre athermique modifient le prix. Contactez-nous avec votre immatriculation pour obtenir un devis clair.",
            ),
            (
                "Peut-on réparer un impact sans changer le pare-brise ?",
                "Oui, lorsque l'impact est de taille limitée, peu profond et situé hors du champ de vision du conducteur. La réparation par injection de résine prend généralement moins d'une heure et stoppe l'évolution des dégâts.",
            ),
            (
                "Quels vitrages automobiles prenez-vous en charge ?",
                "Le pare-brise, les vitres latérales avant et arrière, la lunette arrière, les déflecteurs et les vitrages fixes. Pour les éléments spécifiques comme les toits vitrés, nous étudions la demande au cas par cas selon le véhicule.",
            ),
        ],
    },
    {
        "slug": "sud-est",
        "name": "Sud-Est",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "dans le Sud-Est"],
        "h1_aria": "Pare-brise et vitrage automobile dans le Sud-Est",
        "meta_title": "Pare-Brise & Vitrage Automobile Sud-Est | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles dans le Sud-Est. Appelez le 04 65 84 82 76 : conseils adaptés, devis clair.",
        "og_locale": "fr_FR",
        "phone_display": "04 65 84 82 76",
        "phone_tel": "+330465848276",
        "whatsapp": True,
        "hero_img": IMG_ADAS,
        "hero_sub": "De Lyon à Marseille et Nice, nous vous accompagnons pour la réparation ou le remplacement de votre pare-brise et de vos vitrages automobiles, avec un interlocuteur unique et un devis clair.",
        "seo_heading": "Pare-brise et vitrage automobile dans le Sud-Est",
        "seo_paras": [
            "L'A7, l'A8, l'A43 ou l'A50 concentrent un trafic intense, notamment sur l'autoroute du Soleil en saison. Projections de gravillons, chaleur et longs trajets font du pare-brise un élément particulièrement exposé dans le Sud-Est. Allo Brise de Glace vous accompagne pour la réparation d'impact et le remplacement de vitrage automobile, de Lyon à Marseille, Nice, Toulon, Grenoble ou Montpellier.",
            "Les véhicules récents intègrent souvent caméras et capteurs derrière le pare-brise : freinage d'urgence, maintien de voie, régulateur adaptatif. Lors d'un remplacement, ces équipements sont pris en compte dans l'évaluation et le devis. Signalez-les nous simplement lors de votre appel.",
            "Notre promesse est la clarté : un interlocuteur unique, un avis honnête entre réparation et remplacement, et un devis transparent avant toute intervention. Vous appelez, vous décrivez votre besoin, nous vous accompagnons jusqu'à la solution.",
        ],
        "cities": "Lyon, Marseille, Nice, Toulon, Grenoble, Montpellier, Avignon, Aix-en-Provence, Cannes, Annecy et leurs agglomérations",
        "area": "Sud-Est de la France",
        "faq": [
            (
                "Mon véhicule a une caméra derrière le pare-brise, est-ce pris en compte ?",
                "Oui. Après un remplacement, les caméras et capteurs d'aide à la conduite nécessitent une attention particulière, avec un recalibrage selon le véhicule. Signalez-nous les équipements de votre voiture lors de l'appel : nous en tenons compte dans le devis et l'organisation de l'intervention.",
            ),
            (
                "Quand faut-il remplacer un pare-brise plutôt que réparer ?",
                "Le remplacement est nécessaire lorsque l'impact se trouve dans le champ de vision, lorsque la fissure est longue ou atteint le bord du vitrage, ou lorsque le verre est touché en profondeur. Un petit impact hors champ de vision peut généralement être réparé.",
            ),
            (
                "Quel est le prix d'un remplacement de pare-brise dans le Sud-Est ?",
                "Le prix dépend du véhicule et des équipements intégrés au vitrage : capteurs de pluie, caméra, verre athermique ou chauffant. Appelez-nous avec votre immatriculation : nous vous communiquons un devis clair avant toute intervention.",
            ),
            (
                "La chaleur estivale aggrave-t-elle les impacts ?",
                "Oui. La dilatation du verre sous forte chaleur, combinée à l'air conditionné dans l'habitacle, favorise l'extension des fissures. Dans le Sud-Est en été, faites évaluer un impact sans attendre : la réparation reste possible tant que la fissure ne s'est pas développée.",
            ),
            (
                "Quels vitrages automobiles peuvent être remplacés ?",
                "Pare-brise, vitres latérales avant et arrière, lunette arrière, déflecteurs et vitrages fixes. Les toits vitrés et éléments spécifiques sont étudiés au cas par cas selon le modèle du véhicule.",
            ),
        ],
    },
    {
        "slug": "geneve",
        "name": "Genève",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "à Genève"],
        "h1_aria": "Pare-brise et vitrage automobile à Genève",
        "meta_title": "Pare-Brise & Vitrage Automobile Genève | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles à Genève. Appelez le 22 506 8688 : prise en charge professionnelle, devis clair.",
        "og_locale": "fr_CH",
        "phone_display": "22 506 8688",
        "phone_tel": "+41225068688",
        "whatsapp": False,
        "hero_img": IMG_TECH,
        "hero_sub": "À Genève et dans le bassin lémanique, nous vous accompagnons pour la réparation ou le remplacement de votre pare-brise et de vos vitrages automobiles, avec un interlocuteur unique et un devis clair.",
        "seo_heading": "Pare-brise et vitrage automobile à Genève",
        "seo_paras": [
            "Entre les axes autoroutiers du bassin lémanique, le trafic transfrontalier et les hivers marqués, les vitrages automobiles sont mis à l'épreuve à Genève. Projections de gravillons, sel de déneigement et écarts de température fragilisent les pare-brise tout au long de l'année. Allo Brise de Glace vous accompagne pour la réparation ou le remplacement de votre pare-brise à Genève, de Carouge à Vernier, de Lancy à Nyon.",
            "Impact, fissure, vitre latérale brisée ou lunette arrière endommagée : nous vous aidons à identifier la solution adaptée à votre véhicule. Lorsque la réparation par injection de résine est possible, elle évite le remplacement complet du vitrage. Sinon, nous organisons le remplacement avec vous, en toute transparence.",
            "Vous appelez, vous décrivez votre besoin, nous vous accompagnons. Un interlocuteur unique suit votre demande, vous recevez un devis clair avant toute intervention et des conseils adaptés à votre véhicule, y compris pour les modèles équipés de caméras et de capteurs d'aide à la conduite.",
        ],
        "cities": "Genève, Carouge, Lancy, Vernier, Nyon, ainsi qu'Annemasse et le bassin lémanique",
        "area": "Genève et le bassin lémanique",
        "faq": [
            (
                "Quand faut-il remplacer un pare-brise ?",
                "Le remplacement s'impose lorsque l'impact se situe dans le champ de vision du conducteur, lorsque la fissure est longue ou proche du bord du vitrage, ou lorsque le verre feuilleté est atteint en profondeur. Dans les autres cas, une réparation est souvent possible. Nous vous donnons un avis clair dès la description des dégâts.",
            ),
            (
                "Peut-on réparer un impact avant qu'il ne s'étende ?",
                "Oui, et c'est recommandé. À Genève, les écarts de température hivernaux accélèrent l'évolution d'un impact en fissure. Tant que l'impact reste de taille limitée et hors du champ de vision, une réparation par injection de résine permet d'éviter le remplacement.",
            ),
            (
                "Quel est le prix d'un remplacement de pare-brise à Genève ?",
                "Le tarif dépend du véhicule et des équipements du vitrage : capteurs de pluie, caméra d'aide à la conduite, verre chauffant ou athermique. Appelez-nous avec les informations de votre véhicule : nous vous communiquons un devis clair.",
            ),
            (
                "Combien de temps prend une intervention ?",
                "Une réparation d'impact prend généralement moins d'une heure. Un remplacement de pare-brise demande davantage de temps en raison du séchage de la colle et du recalibrage éventuel des caméras. Nous vous indiquons une estimation précise lors de votre appel.",
            ),
            (
                "Quels vitrages automobiles peuvent être remplacés ?",
                "Nous prenons en charge le pare-brise, les vitres latérales avant et arrière, la lunette arrière ainsi que les déflecteurs et vitrages fixes. Les vitrages spécifiques sont étudiés au cas par cas selon le véhicule.",
            ),
        ],
    },
    {
        "slug": "montreal",
        "name": "Montréal",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "à Montréal"],
        "h1_aria": "Pare-brise et vitrage automobile à Montréal",
        "meta_title": "Pare-Brise & Vitrage Automobile Montréal | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles à Montréal. Appelez le 514 312 9410 : interlocuteur unique, devis clair.",
        "og_locale": "fr_CA",
        "phone_display": "514 312 9410",
        "phone_tel": "+15143129410",
        "whatsapp": False,
        "hero_img": IMG_REPAIR,
        "hero_sub": "À Montréal, entre le gravillon d'hiver et les écarts de température, les pare-brise sont mis à rude épreuve. Nous vous accompagnons pour la réparation ou le remplacement de votre vitrage automobile, avec un devis clair.",
        "seo_heading": "Pare-brise et vitrage automobile à Montréal",
        "seo_paras": [
            "À Montréal, l'hiver est la première cause des dommages aux pare-brise : les abrasifs et gravillons répandus sur les chaussées provoquent des impacts, et les écarts extrêmes de température entre l'habitacle chauffé et le froid extérieur les transforment en fissures. Allo Brise de Glace vous accompagne pour la réparation ou le remplacement de votre pare-brise à Montréal, à Laval, à Longueuil comme sur la Rive-Nord et la Rive-Sud.",
            "Vitre latérale brisée, lunette arrière endommagée ou pare-brise fissuré : nous vous aidons à choisir la bonne solution. La réparation par injection de résine, lorsqu'elle est possible, évite le remplacement complet du vitrage et prend généralement moins d'une heure.",
            "Notre démarche est simple : vous appelez, vous décrivez votre besoin, nous vous accompagnons. Vous échangez avec un interlocuteur unique, vous recevez un devis clair avant toute intervention et des conseils adaptés aux réalités de la route québécoise.",
        ],
        "cities": "Montréal, Laval, Longueuil, Brossard, la Rive-Nord et la Rive-Sud",
        "area": "Montréal et sa région métropolitaine",
        "faq": [
            (
                "Pourquoi les impacts de pare-brise sont-ils si fréquents à Montréal ?",
                "Les abrasifs et gravillons répandus sur les routes pendant l'hiver québécois sont projetés par les véhicules qui précèdent. Combinés aux écarts de température importants, ces impacts évoluent facilement en fissures. Faire réparer un impact dès son apparition évite souvent un remplacement complet.",
            ),
            (
                "Le froid peut-il transformer un impact en fissure ?",
                "Oui. Le choc thermique entre un pare-brise gelé et un habitacle chauffé fait travailler le verre. Un impact stable peut alors s'étendre soudainement, parfois sur toute la largeur du vitrage. En hiver, ne tardez pas à faire évaluer un impact.",
            ),
            (
                "Quel est le prix d'un remplacement de pare-brise à Montréal ?",
                "Le tarif dépend du véhicule et des équipements intégrés au vitrage : caméra, capteurs, verre chauffant ou acoustique. Appelez-nous avec les informations de votre véhicule : nous vous communiquons un devis clair avant toute intervention.",
            ),
            (
                "Quand faut-il remplacer plutôt que réparer ?",
                "Le remplacement est nécessaire lorsque l'impact se trouve dans le champ de vision du conducteur, lorsque la fissure est longue ou atteint le bord du vitrage, ou lorsque le verre est endommagé en profondeur. Nous vous orientons vers la solution la plus pertinente dès votre appel.",
            ),
            (
                "Quels vitrages pouvez-vous remplacer ?",
                "Le pare-brise, les vitres latérales avant et arrière, la lunette arrière — y compris avec reconnexion du dégivrage — ainsi que les déflecteurs et vitrages fixes. Les éléments spécifiques sont étudiés au cas par cas selon le véhicule.",
            ),
        ],
    },
    {
        "slug": "belgique",
        "name": "Belgique",
        "h1_lines": ["Pare-brise &amp; vitrage ", "automobile ", "en Belgique"],
        "h1_aria": "Pare-brise et vitrage automobile en Belgique",
        "meta_title": "Pare-Brise & Vitrage Automobile Belgique | Allo Brise de Glace",
        "meta_desc": "Réparation et remplacement de pare-brise et vitrages automobiles en Belgique. Appelez le 02 844 45 87 : prise en charge simple, devis clair.",
        "og_locale": "fr_BE",
        "phone_display": "02 844 45 87",
        "phone_tel": "+3228444587",
        "whatsapp": False,
        "hero_img": IMG_SIDE,
        "hero_sub": "De Bruxelles à Liège, Namur ou Charleroi, nous vous accompagnons pour la réparation ou le remplacement de votre pare-brise et de vos vitrages automobiles, avec un interlocuteur unique et un devis clair.",
        "seo_heading": "Pare-brise et vitrage automobile en Belgique",
        "seo_paras": [
            "L'E19, l'E40, l'E42 ou le ring de Bruxelles concentrent chaque jour un trafic dense, et les projections de gravillons y sont fréquentes. Un impact sur le pare-brise arrive vite, et une fissure plus vite encore. Allo Brise de Glace vous accompagne pour la réparation et le remplacement de pare-brise en Belgique, de Bruxelles à Liège, Namur, Charleroi ou Mons.",
            "Au-delà du pare-brise, nous prenons en charge l'ensemble du vitrage automobile : vitre latérale, lunette arrière, déflecteur ou élément fixe. Nous vous aidons à choisir entre réparation et remplacement selon la taille, la position et la profondeur des dégâts.",
            "Notre fonctionnement est volontairement simple : vous appelez, vous décrivez votre besoin, nous vous accompagnons. Un interlocuteur unique suit votre dossier et vous recevez un devis clair avant toute intervention, pour les véhicules récents comme pour les modèles plus anciens.",
        ],
        "cities": "Bruxelles, Liège, Namur, Charleroi, Mons, le Brabant wallon et leurs agglomérations",
        "area": "Belgique",
        "faq": [
            (
                "Quand faut-il remplacer un pare-brise ?",
                "Le remplacement est nécessaire lorsque l'impact se situe dans le champ de vision du conducteur, lorsque la fissure est longue ou proche du bord du vitrage, ou lorsque le verre est atteint en profondeur. Un petit impact hors champ de vision peut souvent être réparé. Décrivez-nous les dégâts : nous vous orientons clairement.",
            ),
            (
                "Peut-on réparer un impact sur un pare-brise ?",
                "Oui, lorsque l'impact est de taille limitée, peu profond et hors du champ de vision. La réparation par injection de résine prend généralement moins d'une heure et stoppe l'évolution des dégâts. Plus vous intervenez tôt, plus la réparation a de chances d'être possible.",
            ),
            (
                "Quel est le prix d'un remplacement de pare-brise en Belgique ?",
                "Le tarif dépend du modèle de véhicule et des équipements du vitrage : capteurs de pluie, caméra, verre athermique ou chauffant. Contactez-nous avec votre immatriculation pour recevoir un devis clair avant toute décision.",
            ),
            (
                "Combien de temps prend une intervention ?",
                "Une réparation d'impact prend généralement moins d'une heure. Un remplacement demande davantage de temps, notamment pour le séchage de la colle et le recalibrage éventuel des caméras. Nous vous donnons une estimation précise lors de votre appel.",
            ),
            (
                "Quels vitrages automobiles peuvent être remplacés ?",
                "Pare-brise, vitres latérales avant et arrière, lunette arrière, déflecteurs et vitrages fixes. Pour les toits vitrés et les éléments spécifiques, nous étudions votre demande au cas par cas selon le véhicule.",
            ),
        ],
    },
]

SERVICE_OPTIONS = [
    "Remplacement de pare-brise",
    "Réparation d'impact",
    "Remplacement de vitre latérale",
    "Remplacement de lunette arrière",
    "Autre",
]

REGION_OPTIONS = [r["name"] for r in REGIONS] + ["Autre"]

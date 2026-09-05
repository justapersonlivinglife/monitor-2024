# -*- coding: utf-8 -*-
"""
Configuration des sites à surveiller.

Deux modes possibles par site :

  "new_items"    -> on notifie quand un NOUVEL identifiant (lien) apparaît
                     dans la liste (utile si le site n'affiche que les
                     logements dispo, et les retire une fois pris).

  "availability" -> la liste contient TOUJOURS les mêmes résidences, mais
                     chacune a un indicateur (ex: une icône) qui change
                     selon sa disponibilité. On notifie quand une résidence
                     passe de "non disponible" à "disponible".

Champs communs :
  - url              : URL de la page à scraper
  - mode             : "new_items" (défaut) ou "availability"
  - item_selector    : sélecteur CSS du conteneur répété pour CHAQUE résidence/annonce
  - link_selector     : sélecteur CSS (relatif à item_selector) du lien <a>
                        -> son href sert d'identifiant unique
  - name_selector     : sélecteur CSS (relatif à item_selector) du texte affiché
                        (laisse "" pour prendre le texte du lien)

Champs spécifiques au mode "availability" :
  - availability_selector : sélecteur CSS (relatif à item_selector) de l'élément
                             qui porte l'info de disponibilité (ex: une <img>)
  - unavailable_keyword   : texte qui, présent dans l'attribut "src" (ou le texte)
                             de availability_selector, signifie "PAS disponible"

Astuce pour trouver ces sélecteurs : F12 sur la page > clic sur une annonce
avec l'outil "inspecter" > repère la classe CSS qui se répète pour chaque annonce.
"""

NTFY_TOPIC = "https://ntfy.sh/logement-alerte-x7k2p9"  # <-- remplace par TON topic

SITES = [
    {
        "name": "Studefi",
        "url": "https://www.studefi.fr/main.php",
        "mode": "availability",
        "item_selector": "div.list-res-elem",
        "link_selector": "div.list-res-link a",
        "name_selector": "div.list-res-link a",
        "availability_selector": "img.dispoRes",
        "unavailable_keyword": "non_disponible",
    },
    {
        "name": "Fac Habitat",
        "url": "https://logement.smerra.fr/ville/paris/?budget_min=250&budget_max=490&language=fr",
        "mode": "availability",
        "availability_type": "text",
        "item_selector": "div.card-logement",
        "link_selector": "a",
        "name_selector": "h3",
        "availability_selector": "p.text-3xs.rounded-3xs.inline-flex",
        "positive_values": ["Dispo à venir", "Dispo immédiate"],
        "price_selector": "p.text-sm.text-black span.font-semibold",
    },
    # Logifac utilise le même moteur de recherche que Fac Habitat
    # (même domaine logement.smerra.fr). Si besoin un jour, il suffit de
    # dupliquer le bloc ci-dessus avec l'URL de recherche Logifac correspondante.
]

# Intervalle conseillé entre deux vérifications (en minutes).
# Reste raisonnable (15-30 min) pour ne pas surcharger les sites.
CHECK_INTERVAL_MINUTES = 20

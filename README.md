# Détecteur d'offres de logement → ntfy

## Installation

```bash
cd logement-alertes
python3 -m venv venv
source venv/bin/activate   # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

1. Ouvre `config.py`
2. Remplace `NTFY_TOPIC` par ton propre topic ntfy (choisi lors de l'étape 1 du guide)
3. Pour chaque site, remplace `item_selector` (et éventuellement `link_selector` /
   `title_selector`) par les vrais sélecteurs CSS trouvés via l'inspecteur du navigateur (F12)

## Tester manuellement

```bash
python scraper.py
```

- Le premier run enregistre l'état actuel sans envoyer de notif (normal, sinon tu
  recevrais une notif pour CHAQUE annonce déjà existante).
- Relance le script après avoir modifié un fichier dans `data/` (supprime une entrée
  pour simuler une "nouvelle" annonce) pour vérifier que la notif part bien.

## Automatiser

### Option A — cron (Linux/Mac)

```bash
crontab -e
```

Ajoute une ligne (vérifie toutes les 20 min) :
```
*/20 * * * * cd /chemin/vers/logement-alertes && /chemin/vers/venv/bin/python scraper.py >> log.txt 2>&1
```

### Option B — Planificateur de tâches (Windows)

Crée une tâche qui exécute :
```
C:\chemin\vers\venv\Scripts\python.exe C:\chemin\vers\logement-alertes\scraper.py
```
toutes les 20 minutes.

### Option C — sur un serveur/Raspberry Pi qui tourne 24/7

Utilise un service `systemd` + `systemd timer`, ou simplement `python scraper.py --loop`
dans un `screen`/`tmux`, ou via un gestionnaire de process comme `pm2` ou `supervisor`.

## Notes importantes

- **Respecte les sites** : un intervalle de 15-20 min est largement suffisant pour ce
  genre d'usage, pas besoin de checker toutes les minutes.
- **Sites en JavaScript** : si `fetch_listings` ne trouve rien alors que les annonces sont
  bien visibles dans le navigateur, c'est probablement que le contenu est chargé en JS
  après coup. Dans ce cas il faut remplacer `requests` par un outil qui exécute le JS
  (Playwright, par exemple) — dis-le-moi si tu es dans ce cas, je peux adapter le script.
- **API cachée** : avant de scraper le HTML, regarde dans l'onglet Réseau (F12) si une
  requête vers une API JSON se déclenche quand la liste se charge — si oui, c'est
  souvent bien plus simple et stable de taper directement dessus plutôt que de parser du HTML.

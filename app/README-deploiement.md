# Tracker REMAEDE : mise en ligne et entretien

Application web mobile pour les clientes de l'accompagnement REMAEDE (Émilie Charles).
Un seul dossier, aucune base de données, aucun serveur à administrer : les données de chaque cliente restent sur son téléphone.

## Contenu du dossier

- `index.html` : l'application complète.
- `manifest.webmanifest` : permet l'installation sur l'écran d'accueil (nom, couleurs, icône).
- `sw.js` : fait fonctionner l'application hors ligne après une première ouverture.
- `icons/` : icône de l'application (SVG, PNG 192 et 512, icône Apple 180).
- `README-deploiement.md` : ce guide.

## Mise en ligne en 5 minutes

Il faut un hébergement de fichiers statiques en HTTPS. Le HTTPS est obligatoire pour l'installation sur le téléphone et le mode hors ligne.

Option la plus simple, gratuite : Netlify Drop.
1. Aller sur https://app.netlify.com/drop
2. Glisser le dossier `app` entier dans la zone.
3. Netlify donne une adresse du type `nom-aleatoire.netlify.app`. L'application est en ligne.
4. Dans Site settings puis Domain management, ajouter un sous-domaine d'Émilie, par exemple `tracker.remaede.fr`, et créer chez son registrar l'enregistrement CNAME indiqué par Netlify.

Alternatives équivalentes : Cloudflare Pages, Vercel, ou n'importe quel hébergement web classique (OVH, o2switch) en déposant les fichiers par FTP dans un sous-dossier.

## Intégration dans Notion

Dans l'espace Notion de chaque cliente, taper `/embed`, coller l'adresse de l'application. Le tracker s'affiche dans la page.
Attention : les données saisies dans l'embed Notion et celles saisies dans l'application ouverte directement sur le téléphone sont deux jeux de données distincts (deux navigateurs différents). Conseiller aux clientes un seul usage, de préférence l'application installée sur le téléphone. La sauvegarde par fichier permet de transférer les données de l'un à l'autre.

## Ce qu'il faut dire aux clientes

- Ouvrir l'adresse sur le téléphone, puis suivre la carte « Installer sur mon téléphone » dans Réglages.
  Sur iPhone : bouton Partager de Safari, puis « Sur l'écran d'accueil ».
  Sur Android : menu du navigateur, puis « Installer l'application ».
- Les données restent sur le téléphone. En cas de changement de téléphone ou de nettoyage du navigateur, elles sont perdues : faire de temps en temps « Télécharger le fichier » dans Réglages, Sauvegarde.
- Le bouton « Envoyer à Émilie » (onglet Semaine, repas) ouvre la feuille de partage du téléphone pour envoyer le journal alimentaire par message.

## Mettre le logo officiel

L'application affiche un logo typographique reconstitué d'après la charte (REMAEDE avec AE en vert foncé, signature « Emilie »).
Pour utiliser le fichier officiel :
1. Déposer `logo.svg` (ou `logo.png`, fond transparent) à côté de `index.html`.
2. Dans `index.html`, chercher `const LOGO_SRC=''` et mettre `const LOGO_SRC='logo.svg'`.
3. Remettre en ligne le dossier.

## Modifier les habitudes, les options ou les textes

Tout est dans `index.html`, dans la partie `<script>` :
- `HABITS` : la liste des habitudes. `socle:true` pour le socle imposé, `m:1/2/3` pour le mois de déblocage d'une option, `f:'d'` quotidien, `f:'w',n:2` deux fois par semaine, `f:'mo',n:1` une fois par mois.
- `JALONS` : les étapes à cocher une fois (bilan, questionnaire, etc.).
- `RESSENTI` : les quatre curseurs et leurs libellés.
- `REPAS` : les champs du journal de repas.
Après modification, remettre le dossier en ligne. Les clientes reçoivent la nouvelle version à l'ouverture suivante (le service worker met à jour le cache).

Si le fichier source `remaede-tracker.html` du dossier parent est modifié (version artefact Claude), lancer `python3 build.py` pour régénérer `app/index.html`.

## Données et RGPD

Aucune donnée ne quitte le téléphone de la cliente : pas de compte, pas de serveur, pas de cookie tiers. Les polices sont chargées depuis Google Fonts (une requête vers Google au premier chargement, puis mises en cache). Pour supprimer même cela, télécharger les polices League Spartan, Lato et Alex Brush et les servir depuis le dossier.

#!/usr/bin/env python3
"""Génère app/index.html (application finale, page complète) à partir de remaede-tracker.html (source, format artefact)."""
import pathlib, re, datetime
root=pathlib.Path(__file__).parent
src=(root/'remaede-tracker.html').read_text(encoding='utf-8')
version=datetime.date.today().strftime('%Y.%m.%d')
head=f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Tracker de progression longévité de la méthode REMAEDE : habitudes, énergie, sommeil, stress, état d'esprit et repas, jour après jour.">
<meta name="theme-color" content="#008038" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121f1a" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="REMAEDE">
<meta name="robots" content="noindex">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
'''
tail=f'''
<script>
if('serviceWorker' in navigator && (location.protocol==='https:' || location.hostname==='localhost')){{
  window.addEventListener('load',()=>{{navigator.serviceWorker.register('sw.js').catch(()=>{{}});}});
}}
</script>
</body>
</html>
'''
# le fragment commence par <title> et les <link> de polices, puis <style> ; tout ce qui précède <div id="app"> va dans <head>
i=src.index('<div id="app"')
page=head+src[:i].strip()+'\n</head>\n<body>\n'+src[i:].rstrip()+tail
out=root/'app'/'index.html'
out.write_text(page,encoding='utf-8')
# version du service worker
sw=(root/'app'/'sw.js').read_text(encoding='utf-8')
sw=re.sub(r"const VERSION='[^']*'",f"const VERSION='{version}'",sw)
(root/'app'/'sw.js').write_text(sw,encoding='utf-8')
print('app/index.html généré, version',version)

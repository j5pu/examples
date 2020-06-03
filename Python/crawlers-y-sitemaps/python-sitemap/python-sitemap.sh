#!/bin/bash
python3.6 main.py --domain https://icorating.com/ico --output icobench.xml --verbose

#python3.6 main.py --domain https://www.icobench.com --output icobench.xml --verbose
#python3.6 main.py --domain https://blog.lesite.us --output lesite.xml --verbose

# RUSO no funciona el de icorating.com y este no funciona icobench si no tiene www
# Probaar RUSO
# Que cuando le viene la respuesta saque la url para ver si es de telegram... y
# tener en cuenta las que tienen el domino coom icoratinng.
# las que tienen una como pagina coo la de tgramio hacer bucle y hacer la respuesta con:
# puedo hacer con el  xidel

503 server unavailable es que me han baneado.
poner retraaso y cambiar IP
llamar desde el ruso al scrapy??? y que tenga que esperar y ahi si que hago la clase generica

o dentro de la clase llamo al sitemap ruso

xidel http://icorating.com -e '//a/@href' |
grep -v "http" |
sort -u |
xargs -L1 -I {}  xidel http://icorating.com/{} -e '//a/@href' |
grep -v "http" | sort -u

xidel http://icorating.com -e '//a/@href' |
grep -v "http" |
sort -u |
xargs -L1 -I {}  xidel http://icorating.com/{} -e '//a/@href' |
grep -v "http" | sort -u

xidel http://example.org --follow //a --extract //title
--follow-include=host
xidel http://icorating.com --follow //a --follow-include=host --extract '//a/@href'
xidel http://icorating.com --follow '//a/@href' --follow-include=host --extract '//a/@href'
import re

exts = ['htm', 'php']
allowed_regex = '\.((?!htm)(?!php)\w+)$'
print(allowed_regex)
def set_exts(self, exts):
    self.exts = exts


def allow_regex(regex=None):
    if regex is not None:
        allowed_regex = regex
    else:
        allowed_regex = ''
        for ext in ['htm', 'php']:
            allowed_regex += '(!{})'.format(ext)
        allowed_regex = '\.({}\w+)$'.format(allowed_regex)
    return allowed_regex

regex = re.compile(allow_regex())
print(regex)
url = 'https://foundico.com/ico/centcoin.php'
if re.search(regex, url):
    print('True: re.search={}, url={}'.format(re.search(regex, url), url))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url), url))

url_1 = 'https://foundico.com/rating/'
regex = re.compile(allow_regex())
print(regex)
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))

regex = re.compile(allow_regex('h'))
print(regex)
"""
Si desde algun sitio if(\) .(algun sitio) encuentra=!htm OR !php 
"""
allowed_regex = '\.((!htm)(!php)\w+)$'

url_1 = '!ph'
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))

regex = re.compile(allow_regex('.h'))
print(regex)
"""
Si desde algun sitio if(\) .(algun sitio) encuentra=!htm OR !php 
"""
allowed_regex = '\.((!htm)(!php)\w+)$'

url_1 = '!ph'
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))

regex = re.compile(allow_regex('\.h'))
print(regex)
"""
Si desde algun sitio if(\) .(algun sitio) encuentra=!htm OR !php 
"""

url_1 = '!ph'
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))

regex = re.compile(allow_regex('\!ph'))
print(regex)
"""
Si desde algun sitio if(\) .(algun sitio) encuentra=!htm OR !php 
"""

url_1 = '!ph'
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))


regex = re.compile(allow_regex('\.!ph'))
print(regex)
"""
Si desde algun sitio if(\) .(algun sitio) encuentra=!htm OR !php 
"""

url_1 = '!ph'
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))


regex = re.compile(allow_regex('.!ph'))
print(regex)
"""
Si desde algun sitio if(\) .(algun sitio) encuentra=!htm OR !php 
"""

url_1 = 'h!ph'
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))

regex = re.compile(allow_regex('\.!ph'))
print(regex)
"""
Si desde algun sitio if(\) .(algun sitio) encuentra=!htm OR !php 
"""

url_1 = 'h!ph'
if re.search(regex, url_1):
    print('True: re.search={}, url={}'.format(re.search(regex, url_1), url_1))
else:
    print('False: re.search={}, url={}'.format(re.search(regex, url_1), url_1))

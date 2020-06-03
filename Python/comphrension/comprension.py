from pprint import pprint
import inspect
prefijo = 'Hola'
sufijo = 'jilipollas'
sin_prefijo = 'Adios'

cadena = '{} {}'.format(prefijo, sufijo) if prefijo else '{} {}'.format(sin_prefijo, sufijo)
print(cadena)

lista = ['{} {}'.format(prefijo, sufijo)] if prefijo else '{} {}'.format(sin_prefijo, sufijo)
print(lista)

diccionario = {prefijo: sufijo} if prefijo else {sin_prefijo: sufijo}
print(diccionario)

no_conjunto = (prefijo) if prefijo else (sin_prefijo)
print(no_conjunto)

conjunto = (prefijo, sufijo) if prefijo else (sin_prefijo, sufijo)
print(conjunto)

diccionario = {'var_1': 1, 'var_2': 2}
pprint(diccionario)
msg = 'ERROR'
msg = '{}: '.format(msg) if msg else str()

extra_info = msg + ", ".join("{}={}".format(*item) for item in diccionario.items())
pprint(extra_info)


caller_locals = lambda : inspect.currentframe().f_back.f_locals
# levels = {name: logging_levels[ini['common']['level']]
#           if name in ini['common']['to'] else logging_levels[ini['default'][name]] for name in ini['default']}


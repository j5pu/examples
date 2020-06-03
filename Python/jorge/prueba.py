
# enfermedades = {'Sprains & Strains', 'Fracture', 'Deep Venous Thrombosis', 'Varicose Veins', 'Internal Infection'}
# sintomas = {'Pain', 'Bruising', 'Swelling', 'Redness', 'Deformity', 'Purple Veins'}

sprain = 'Sprains & Strains'
fracture = 'Fracture'
thrombosis = 'Deep Venous Thrombosis'
varicose = 'Varicose Veins'
infection = 'Internal Infection'

pain = 'Pain'
bruising = 'Bruising'
swelling = 'Swelling'
redness = 'Redness'
deformity = 'Deformity'
purple = 'Purple Veins'

# class Diagnose:
#     def __init__(self):
#         self.
enfermedades = {sprain, fracture, thrombosis, varicose, infection}
sintomas = {pain, bruising, swelling, redness, deformity, purple}

enfermedad_y_sintomas = { enfermedad: { sintoma: None for sintoma in sintomas} for enfermedad in enfermedades }


def populate_tabla_enfermedad_sintomas(enfermedad, **kwargs):
    for key, value in kwargs:
        enfermedad_y_sintomas[enfermedad[key]] = value

populate_tabla_enfermedad_sintomas(sprain, pain = True, bruising = True, swelling = True, redness = True)
populate_tabla_enfermedad_sintomas(fracture, pain = True, deformity = True, bruising = True, swelling = True, redness = True)
populate_tabla_enfermedad_sintomas(thrombosis, deformity = True, redness = True)
populate_tabla_enfermedad_sintomas(varicose, purple = True, pain = False, bruising = False, swelling = False, redness = False, deformity = False)
populate_tabla_enfermedad_sintomas(infection, pain = True, swelling = True, redness = True)


def get_enfermedad(*args):
    enfermedad_paciente = None
    for enfermedad in enfermedades:
        for sintoma in sintomas:
            if enfermedad_y_sintomas[enfermedad][sintoma] and sintoma in args:
                enfermedad_paciente = enfermedad
            else:
                enfermedad_paciente = None
                break
        if enfermedad_paciente is not None:
            print(f'You probably suffer of : {enfermedad_paciente}, based on your symptoms {args}')
            return
    if enfermedad_paciente is None:
        print(f'Unknown disease/injury. We do not have a clear diagnose based on your symptoms {args}. Please ask for a Doctor appointment')










a = None
b = True
c = False
"""
if not c: para False y None --> True

"""
# print(a)
# print(b)
# print(c)
# if b:
#     print('es b')
# if not b:
#     print('no b')
#
# if not c:
#     print('Falso')
if c:
    print('Verdadero')
elif not c and not c is None:
    print('No Verdadero')
else:
    print('Ni verdadero ni falso')

class Diagnose:
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

    diseases = {sprain, fracture, thrombosis, varicose, infection}
    symptoms = {pain, bruising, swelling, redness, deformity, purple}

    diseases_symptoms = {sprain: {symptoms['pain']: True, symptoms['pain']: True}, thrombosis: {symptoms['pain']: True, symptoms['pain']: True}}

    diseases_sintomas = {sprain: {'dolor': None, 'otro1': True, 'otro2': True}, thrombosis: {'dolor': True, 'otro1': False, 'otro2': False}}

    paciente_1_sintomas = {'dolor', 'otro2'}
    paciente_2_sintomas = {'dolor', 'otro2'}




print(Diagnose.Disease.__dict__)
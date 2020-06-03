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


diseases_and_symptoms = {disease: {symptom: int() for symptom in symptoms} for disease in diseases}


def fill_diseases_and_symptoms(disease, symptom_and_values):
    for symptom in symptom_and_values:
        diseases_and_symptoms[disease][symptom] = symptom_and_values[symptom]

fill_diseases_and_symptoms(sprain, {pain: 2, bruising: 2, swelling: 2, redness: 2})
fill_diseases_and_symptoms(fracture, {pain: 2, deformity: 2, bruising: 2, swelling: 2, redness: 2})
fill_diseases_and_symptoms(thrombosis, {deformity: 2, redness: 2})
fill_diseases_and_symptoms(varicose, {purple: 2, pain: 1, bruising: 1, swelling: 1, redness: 1, deformity: 1})
fill_diseases_and_symptoms(infection, {pain: 2, swelling: 2, redness: 2})


def get_disease(name, *args):
    patient_diseases = {}
    for disease in diseases:
        for symptom in symptoms:
            if diseases_and_symptoms[disease][symptom] == 2 and symptom in args:
                patient_diseases[disease] = True
            elif diseases_and_symptoms[disease][symptom] == 1 and symptom in args:
                for patient_symptom in args:
                    if diseases_and_symptoms[disease][patient_symptom] == 2:
                        patient_diseases[disease] = True
                        break
            elif diseases_and_symptoms[disease][symptom] == 2 and symptom not in args:
                break


    if patient_diseases:
        print(f'Dear Mr./Mrs. {name}. You probably suffer of {list(patient_diseases.keys())}, based on your symptoms {args}')
    else:
        print(f'Dear Mr./Mrs. {name}. Unknown disease/injury. We do not have a clear diagnose based on your symptoms {args}. Please ask for a Doctor appointment')

has_pain = True
has_deformity = False
has_bruising = False
has_swelling = True
has_redness = True
has_purple_veins = False

get_disease('Mark Andrew', pain, bruising, swelling, redness)
get_disease('Sarah van Smith', pain, deformity, bruising, swelling, redness)
get_disease('Ana del Carmen', deformity, redness)
get_disease('John van der Gong', purple, bruising)
get_disease('Carl Santos', pain, swelling, redness)
get_disease('Lisa Frankfurt', pain, deformity, bruising, swelling, redness, purple)
get_disease('Sam Alanson', pain)

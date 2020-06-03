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


def fill_diseases_and_symptons(disease, symptom_and_values):
    for symptom in symptom_and_values:
        diseases_and_symptoms[disease][symptom] = symptom_and_values[symptom]

fill_diseases_and_symptons(sprain, {pain: 2, bruising: 2, swelling: 2, redness: 2})
fill_diseases_and_symptons(fracture, {pain: 2, deformity: 2, bruising: 2, swelling: 2, redness: 2})
fill_diseases_and_symptons(thrombosis, {deformity: 2, redness: 2})
fill_diseases_and_symptons(varicose, {purple: 2, pain: 1, bruising: 1, swelling: 1, redness: 1, deformity: 1})
fill_diseases_and_symptons(infection, {pain: 2, swelling: 2, redness: 2})


def get_disease(*args):
    patient_diseases_status = {disease: 0 for disease in diseases}

    for sympton in args:
        for disease in diseases:
            if diseases_and_symptoms[disease][sympton] == 2:
                patient_diseases_status[disease] = 2
    for disease in diseases:
        for sympton in symptoms:
            if diseases_and_symptoms[disease][sympton] == 2 and sympton in args:
                patient_diseases_status[disease] = 2
            elif diseases_and_symptoms[disease][sympton] == 1 and sympton in args:
                for patient_symptom in args:
                    if diseases_and_symptoms[disease][patient_symptom] == 2:
                        patient_diseases_status[disease] = 2
                        break

    patient_diseases = [disease for disease, status in patient_diseases_status.items() if status]

    if patient_diseases:
        print(f'You probably suffer of : {patient_diseases}, based on your symptoms {args}')
    else:
        print(f'Unknown disease/injury. We do not have a clear diagnose based on your symptoms {args}. Please ask for a Doctor appointment')

get_disease(pain, bruising, swelling, redness)
get_disease(pain, deformity, bruising, swelling, redness)
get_disease(deformity, redness)
get_disease(purple, bruising)
get_disease(pain, swelling, redness)
get_disease(pain, deformity, bruising, swelling, redness, purple)

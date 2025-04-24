from fhir_parser import FHIR
from backend.services.data_warehouse import SnowflakeClient
import os

def run_fhir_etl():
    fhir = FHIR(base_url=os.getenv("FHIR_SERVER_URL"))
    sf_client = SnowflakeClient()
    
    patients = fhir.get_patients()
    for patient in patients:
        # Insert athlete bios
        sf_client.insert_biomechanical_data({
            'athlete_id': patient.id,
            'height_cm': patient.height,
            'weight_kg': patient.weight
        })
        
        observations = fhir.get_observations(patient.id)
        for obs in observations:
            if obs.code == 'biomechanical-analysis':
                sf_client.insert_biomechanical_data({
                    'athlete_id': patient.id,
                    'left_force': obs.value['left_force'],
                    'right_force': obs.value['right_force']
                })
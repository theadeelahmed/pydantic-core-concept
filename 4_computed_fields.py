from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email:EmailStr     
    age: int  
    weight:float    #in kgs
    height:float    #in meters
    married: bool  
    allergies: List[str]
    contact_details: Dict[str, str]
  
    @computed_field
    @property
    def _calculate_bmi(self)-> float:
        bmi = (self.weight/(self.height**2),2)
        return bmi     
def insert_patient_data(patient : Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight) 
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")

def update_patient_data(patient : Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI", patient._calculate_bmi)
    print("updated")

patient_info = {"name":"ahmed", "email": "ahmed@gmail.com","age":62,"weight": 70.1,"height": 1.72, "married":True, "allergies":["Pollen","dust"], "contact_details": {"phone": "021-2373427","emergency":"2578213"}}

Patient1 = Patient(**patient_info)
    
insert_patient_data(Patient1) 
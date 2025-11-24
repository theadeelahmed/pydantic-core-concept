from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title="name of the patient", description="Give the name of the patient in less than 50 characters", examples=["nitesh","amit"])]
    email:EmailStr       #validation of Email formate
    age: int  = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is a patient married or Not")]
    allergies: Optional[List[str]]  = None   #Optional 
    contact_details: Dict[str, str]

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
    print("updated")

patient_info = {"name":"ahmed", "email": "ahmed@gmail.com","age":26,"weight": 70.1, "married":True, "allergies":["Pollen","dust"], "contact_details": {"phone": "021-2373427"}}

Patient1 = Patient(**patient_info)
    
insert_patient_data(Patient1) 



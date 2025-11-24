from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr     
    age: int  
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Email validator for allowed domains
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hbl.com", "ubl.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value, ):
        if 0< value < 100:
            return value
        else:
            raise ValueError("age should be in between 0 and 100")
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
    


patient_info = {"name":"ahmed", "email": "ahmed@ubl.com","age":26,"weight": 70.1, "married":True, "allergies":["Pollen","dust"], "contact_details": {"phone": "021-2373427"}}

Patient1 = Patient(**patient_info)  # Validation , type coercion perform this step
    
insert_patient_data(Patient1) 
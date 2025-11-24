from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pin:str

class Patient(BaseModel):

    name:str
    gender: str
    age: int
    address: Address


address_dict ={"city": "karachi", "state":"sindh", "pin":"021"}


address1 = Address(**address_dict)


patient_dict= {"name": "Ali","gender":"male","age":21,"address":address1}

patient1 = Patient(**patient_dict)


print(patient1)






#better organization of related data (e.g , vital, address, insurance)

#Resuibility: use vitals in multiples models(e,g. patient medicalRecord)

#Readability: enter for develpors and API consumers to understand 

#Validation: Nested models are validated automatically -no extra work needed



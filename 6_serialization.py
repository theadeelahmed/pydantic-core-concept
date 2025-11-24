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


temp = patient1.model_dump(exclude={"address":["state"]})

print(temp)
print(type(temp))







#.model_dump(include=/exclude=[]/exclude_unset)
#.model_dump_json()
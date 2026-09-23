"""
This file demonstrates how to use Pydantic for data validation and serialization.
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Virat"  #setting default value
    age: Optional[int] = None  #have to set default value to None for optional fields
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=7.0, description="CGPA must be between 0 and 10") 

new_student = {
    "age": "33",  #type coercing
    "email": "virat@gmail.com",  #email validation will be done by pydantic
    # "cgpa": 9  #default value will be used if not provided
    }
student = Student(**new_student)

print(student)
print(student.name)
print(student.age)
print(student.email)
print(student.cgpa)

student_dict = student.model_dump()
print(type(student_dict))
print(student_dict)

student_json = student.model_dump_json()
print(type(student_json))
print(student_json)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    id: int
    name: str
    roll: int
    _class: str
    address: str
    phone_number: int

student_list: List[Student] = []

App = FastAPI()

@App.get("/")
def root():
    json = {
        "message": "Welcome to ICT private."
    }
    return json

@App.get("/students")
def student_data():
    return student_list

@App.post("/students")
def add_student(new_student: Student):
    student_list.append(new_student)
    return new_student

@App.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, studnet in enumerate(student_list):
        if studnet.id == student_id:
            student_list[index] = updated_student
            return updated_student
    return {"error": "Student not found!"}

@App.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(student_list):
        if student.id == student_id:
            deleted_data = student_list.pop(index)
            return deleted_data
    return {"error": "Student not found!"}
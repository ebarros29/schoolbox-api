import os
from db_connection import db, ma
from datetime import datetime

# dados para alimentar o banco (dictionary)
STUDENTS = [
    {
        "cpf":"05544433355", 
        "first_name": "Mateus", 
        "last_name": "Castro", 
        "birth_date":"2005-02-05",
        "phone":"(11)93333-5555",
        "grade": "9º Ano",
        "address":"Rua da Penha, 333. Alto, São Paulo-SP", 
        "email":"mateus.castro@mail.com",
        "mother_name":"Maria Castro", 
        "father_name":"Mario Castro", 
        "parents_phone":"97777-7777"
    },
    {
        "cpf":"77744443465", 
        "first_name":"Luiz", 
        "last_name":"Prado", 
        "birth_date":"2009-03-10",
        "phone":"(11)93327-2735",
        "grade": "6º Ano",
        "address":"Rua da Lua, 444. Jardins, São Paulo-SP", 
        "email": "luiz.henrique@mail.com", 
        "mother_name":"Livia Prado",
        "father_name":"",
        "parents_phone":"97373-7737"
    },    
    {
        "cpf":"33445677888", 
        "first_name":"Paulo", 
        "last_name":"Matos", 
        "birth_date":"2016-06-11",
        "phone":"(11)93223-5165",
        "grade":"8º Ano",
        "address":"Rua do Sol, 555. Paulista, São Paulo-SP", 
        "email":"paulo.matos@mail.com", 
        "mother_name":"Leila Matos",
        "father_name":"João Matos",  
        "parents_phone":"92443-1112"
    },
]

#model para criar a tabela
class Student(db.Model):
    __tablename__ = "students"
    student_id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(12), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(50))
    address = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mother_name = db.Column(db.String(50), nullable=False)
    father_name = db.Column(db.String(50))
    parents_phone = db.Column(db.String(50))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

#schema para adaptar os dados da resposta ao formato json 
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True

# criando o campos da tabela
db.create_all()

# looping no dict STUDENTS para armazenar o valores na tabela 
for student in STUDENTS:
    s = Student(
                cpf=student.get("cpf"),
                first_name=student.get("first_name"),
                last_name=student.get("last_name"),
                birth_date=student.get("birth_date"),
                phone=student.get("phone"),
                grade=student.get("grade"),
                address=student.get("address"),
                email=student.get("email"),
                mother_name=student.get("mother_name"),
                father_name=student.get("father_name"),
                parents_phone=student.get("parents_phone")
                )
    db.session.add(s)
db.session.commit()

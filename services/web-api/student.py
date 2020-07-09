## Student functions utilizadas para receber as ações REST


from flask import make_response, abort
from db_connection import db
from db_datatable import Student, StudentSchema

# Função para responder a um request /api/student e listar todos os alunos
def read_all():

    # Criar a lista de alunos a partir da DB
    student = Student.query.order_by(Student.student_id).all()

    # Serializando a resposta
    student_schema = StudentSchema(many=True)
    data = student_schema.dump(student)
    return data

# Função para responder a um request /api/student/{student_id} e listar 1 aluno de acordo com o ID informado
def read_oneByID(student_id):

    # Get do aluno a partir do ID
    student = Student.query.filter(Student.student_id == student_id).one_or_none()

    # Condição para checar a existência do ID
    if student is not None:

        # Serializando a resposta
        student_schema = StudentSchema()
        data = student_schema.dump(student)
        return data

    else:
        abort(
            404,
            "O aluno de ID: {student_id} não foi encontrado".format(student_id=student_id),
        )

#Função para responder a um request /api/student/listByCPF e listar 1 aluno de acordo com o CPF informado
def read_oneByCPF(cpf):

    # Get do aluno a partir do CPF
    student = Student.query.filter(Student.cpf == cpf).one_or_none()

    # Condição para checar a existência do CPF
    if student is not None:

        # Serialização da resposta
        student_schema = StudentSchema()
        data = student_schema.dump(student)
        return data

    else:
        abort(
            404,
            "O aluno de CPF: {cpf} não foi encontrado".format(cpf=cpf),
        )

#Função para criar um aluno na DB
def create(student):

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

    existing_student = (Student.query.filter(Student.cpf == cpf).one_or_none())

    # Condição para verificar a existencia do aluno na DB
    if existing_student is None:

        # Criação da instância "student" e passando como argumento os dados o aluno informado 
        schema = StudentSchema()
        new_student = schema.load(student, session=db.session)

        # Adiçao do aluno a DB
        db.session.add(new_student)
        db.session.commit()

        # Serialização e returno dos dados do aluno na resposta
        data = schema.dump(new_student)

        return data, 201

    else:
        abort(
            409,
            "Este CPF {cpf} já pertence ao aluno {first_name} {last_name}".format(
                cpf=cpf, first_name=first_name, last_name=last_name
            ),
        )

#Função para atualizar os dados de um aluno de acordo com o ID informado
def update(student_id, student):
  
    # Get do aluno informado a partir do ID
    update_student = Student.query.filter(
        Student.student_id == student_id
    ).one_or_none()

    # Checa se já existe um estudante cadastrado com o mesmo CPF
    cpf = student.get("cpf")
    existing_student = (Student.query.filter(Student.cpf == cpf).one_or_none())

    # Condição para chegar se realmente existe algum aluno com o ID informado
    if update_student is None:
        abort(
            404,
            "O aluno de ID: {student_id} não foi encontrado".format(student_id=student_id),
        )

    # Outra condição para evitar que as novas informações criem uma duplicata 
    elif (
        existing_student is not None and existing_student.student_id != student_id
    ):
        abort(
            409,
            "Já existe um aluno de CPF: {cpf}".format(
                cpf=cpf
            ),
        )

    else:

        # turn the passed in student into a DB object
        schema = StudentSchema()
        update = schema.load(student, session=db.session)

        # Seta ID do aluno que será atualizado
        update.student_id = update_student.student_id

        # Faz um merge do novo objeto com o antigo e manda um commit na DB
        db.session.merge(update)
        db.session.commit()

        # Retorna as informações atualizadas como resposta
        data = schema.dump(update_student)

        return data, 200

#Função para deletar os dados de um aluno de acordo com o ID informado
def delete(student_id):

    # Get do aluno através do ID informado
    student = Student.query.filter(Student.student_id == student_id).one_or_none()

    # Condição para checar se o ID existe
    if student is not None:
        db.session.delete(student)
        db.session.commit()
        return make_response(
            "O aluno de ID: {student_id} foi deletado".format(student_id=student_id), 200
        )

    else:
        abort(
            404,
            "O aluno de ID: {student_id} não foi encontrado".format(student_id=student_id),
        )

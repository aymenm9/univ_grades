from sqlalchemy import Column, Integer, String, Float,ForeignKey, JSON

from db import db
from login_manager import UserMixin

def get_id(user_obj):
    '''
    return user_id and user_type
    user_type: Admin, Teacher, Student class or none
    '''
    if user_obj is None:
        return None
    user = {'user_id': user_obj.id,
            'usr_type': user_obj.__class__}
    return user
class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Admin(id={self.id}, username='{self.username}')>"
    
    def get_id(self):
        return get_id(self)


class Department(db.Model):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)


class Level(db.Model):
    __tablename__ = 'level'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'))


class Class(db.Model):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_number = Column(Integer, nullable=False)
    level_id = Column(Integer, ForeignKey('level.id'))


class Teacher(db.Model, UserMixin):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    def get_id(self):
        return get_id(self)

class Student(db.Model, UserMixin):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    full_name = Column(String(50))
    class_id = Column(Integer, ForeignKey('class.id'))

    def get_id(self):
        return get_id(self)

class Subject(db.Model):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    level_id = Column(Integer, ForeignKey('level.id'))
    coefs = Column(JSON)  # Can be a dictionary or list representing coefficients

class LevelSubject(db.Model):
    __tablename__ = 'level_subject'

    level_id = Column(Integer, ForeignKey('level.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)
    coef = Column(Integer)


class TeacherClassSubject(db.Model):
    __tablename__ = 'teacher_class_subject'

    teacher_id = Column(Integer, ForeignKey('teacher.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('class.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)

class Grade(db.Model):
    __tablename__ = 'grade'

    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Float)
    exam = Column(Float)
    tp = Column(Float)
    td = Column(Float)
    student_id = Column(Integer, ForeignKey('student.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))

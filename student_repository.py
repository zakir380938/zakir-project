from sqlalchemy.orm import Session
from student_model import Student


class StudentRepository:

    def create_student(self, db:Session, student: Student):
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    def get_student_by_roll(self, db: Session, roll: str):
        return db.query(Student).filter(Student.roll == roll).first()

    def delete_student_by_roll(self, db: Session, roll: str):
        db_user = db.query(Student).filter(Student.roll == roll).first()
        if db_user:
            db.delete(db_user)
            db.commit()


    def update_student(self, db: Session, student: Student):
        db.merge(student)
        db.commit()
        db.refresh(student)
        return student
    
    def get_all_students(self, db: Session):
        return db.query(Student).all()

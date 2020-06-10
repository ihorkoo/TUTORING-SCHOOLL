from school import db

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String())
    second_name = db.Column(db.String())
    sex = db.Column(db.String())                          # 'F' or 'M'
    email = db.Column(db.String(), unique=True, nullable=False)
    birthday = db.Column(db.Date())
    city = db.Column(db.String())
    postal_code = db.Column(db.String())
    instagram = db.Column(db.String())
    status = db.Column(db.String())                       # активий, потенційний, випускник, встрачений



class Teachers(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    second_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    birthday = db.Column(db.Date())
    city = db.Column(db.String())
    postal_code = db.Column(db.String())
    instagram = db.Column(db.String())
    status = db.Column(db.String())   # активий, звільнений, відпустка

class Rate(db.Model):
    __tablename__ = 'rate'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    rate = db.Column(db.Integer(), nullable=False)
    teacher_id = db.Column(db.String(), db.ForeignKey('teachers.id'))
    
    
class Lessons(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    plan_date = db.Column(db.Date())
    teacher_id = db.Column(db.String(), db.ForeignKey('teachers.id'))
    student_id = db.Column(db.String(), db.ForeignKey('students.id'))
    lessons_price = db.Column(db.Integer()) 
    status = db.Column(db.String())   #заплановано, відхилено, проведено, оплачено

class Salary(db.Model):
    __tablename__ = 'salary'

    id = db.Column(db.Integer(), primary_key=True)
    type_oparation = db.Column(db.String())          #прихід - зароблено викладачем, розхід - виплата зп
    amount = db.Column(db.Integer())                 #беремо з таблички rate
    teacher_id = db.Column(db.String(), db.ForeignKey('teachers.id'))







    

from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SelectField

from school.models import db, Teachers, Students



#Приклад простої форми
class AddTeacher(FlaskForm):
    email = StringField()
    first_name = StringField() 
    

"""
Приклад для вибірки
Читайте документацію, як це працює
class AddRate(FlaskForm):
    rate = StringField()
    teacher = SelectField(choices= [ (g.first_name, g.second_name) for g in Students.query.all()])"""
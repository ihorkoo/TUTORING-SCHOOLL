from flask import render_template, request

from school import app, db
from school.models import Students
from school.forms import AddTeacher



@app.route('/add', methods=('GET', 'POST'))
def add():
    """s = Students.query.all()
    print(s)"""
    form = AddTeacher()
    if request.method == 'POST':
        new_student = Students(email = request.form['email'], 
                                first_name=request.form['first_name'])
        db.session.add(new_student)
        
        db.session.commit()
        return "OK"

    return render_template('index.html', form=form)




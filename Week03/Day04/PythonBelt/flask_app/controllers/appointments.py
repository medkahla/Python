from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.appointment import Appointment

@app.route('/appointments/new')
def adding_appointment():
    return render_template('appointment_add.html')

@app.route('/appointments/create', methods=["post"])
def create_appointment():
    print(request.form)
    if(Appointment.validate(request.form)):
        data = {
            **request.form,'user_id':session["user_id"]
        }
        Appointment.create_appointment(data)
        return redirect('/dashboard')
    return redirect('/appointments/new')

@app.route('/appointments/<int:appointment_id>/edit')
def edit_appointment(appointment_id):
    if not 'user_id' in session:
        return redirect('/')
    appointment = Appointment.get_by_id(appointment_id)
    return render_template('appointment_edit.html', appointment=appointment)

@app.route('/appointments/<int:appointment_id>/update', methods=['post'])
def update_appointment(appointment_id):
    if(Appointment.validate(request.form)):
        data = {
            **request.form,
            'id':appointment_id
        }
        Appointment.update(data)
        return redirect('/dashboard')
    return redirect('/appointments/<int:appointment_id>/edit')

@app.route('/appointments/<int:appointment_id>/del_confirm')
def confirm(appointment_id):
    if not 'user_id' in session:
        return redirect('/')
    appointment = Appointment.get_by_id(appointment_id)
    return render_template('appointment_delete.html', appointment=appointment)

@app.route('/appointments/<int:appointment_id>/destroy', methods=["post"])
def destroy(appointment_id):
    Appointment.destroy_appointment(appointment_id)
    return redirect('/dashboard')
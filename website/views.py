from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .import db
import json

views = Blueprint('views', __name__)  # we have setup a blueprint for our flask application

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too sort!', category = 'error')
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category = 'success')
    return render_template("home.html", user = current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)  # this is going to take some data from the post request and load in as a json object or a python dictionary
    noteId = note['noteId']    # then we are going to access the noteId attribute from the index.js file
    note = Note.query.get(noteId)  # we will look for the node that has that id 
    # when we use "get" it will access the primary key
    if note:  # checking if that id exists
    # if it exists then we can delete it or else we need not delete it
        if note.user_id == current_user.id:  # if the signed user owns the notes then only we will delete the notes
            db.session.delete(note)
            db.session.commit()
    return jsonify({})  # returning an empty response
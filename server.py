from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector('friends')
app.secret_key = 'AnthonyDoesNotKnow'

def validate():
    errors = 0
    #Check first name
    if request.form['first_name'] == '':
        flash('Name cannot be blank', 'firstNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('Name cannot have numbers', 'firstNameError')
        errors += 1
        pass
    else:
        pass
    #Check last name
    if request.form['last_name'] == '':
        flash('Name cannot be blank', 'lastNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Name cannot have numbers', 'lastNameError')
        errors += 1
        pass
    else:
        pass
    #Check occupation
    if request.form['occupation'] == '':
        flash('Occupation cannot be blank', 'occupationError')
        errors += 1
        pass
    else:
        pass
    #See if there are any errors
    if errors > 0:
        return False
    else:
        return True
@app.route('/')
def index():
    friends = mysql.fetch("SELECT * FROM friends")
    return render_template('index.html', friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
    if validate() == False:
        return redirect('/')
    else:
        mysql.run_mysql_query(query)
    return redirect('/')
@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id = '{}'".format(id)
	myfriends = mysql.fetch(query)
	print myfriends
	return render_template('edit.html', friends=myfriends)
@app.route('/friends/<id>', methods=['POST'])
def editInfo(id):
	query = "UPDATE friends SET first_name = '{}', last_name = '{}', occupation = '{}', updated_at = NOW() WHERE id = {}".format(request.form['first_name'], request.form['last_name'], request.form['occupation'], int(id))
	if validate() == False:
		return redirect('/')
	else:
		mysql.run_mysql_query(query)
	return redirect('/')
@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
	query = "DELETE FROM friends WHERE id = '{}'".format(id)
	print query
	mysql.run_mysql_query(query)
	return redirect('/')
app.run(debug=True)
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Connect Flask to database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Attach Flask app to database
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'project'
    project_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, project_id, user_id, name, budget, description):
        self.project_id = project_id
        self.user_id = user_id
        self.name = name
        self.budget = budget
        self.description = description

    def json(self):
        project_entry = {
            "project_id": self.project_id,
            "user_id": self.user_id,
            "name": self.name,
            "budget": self.budget,
            "description": self.description,
        }
        return project_entry


# Creation of Project Objects
class Expense(db.Model):
    __tablename__ = 'expense'
    expense_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float(precision=2), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    created_by = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_by = db.Column(db.Text, nullable=False)

    def __init__(self, expense_id, project_id, category_id, name, description, amount,
                 created_at, created_by, updated_at, updated_by):
        self.expense_id = expense_id
        self.project_id = project_id
        self.category_id = category_id
        self.name = name
        self.description = description
        self.amount = amount
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by

    def json(self):
        expense_entry = {
            "id": self.id,
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "amount": self.amount,
            "created_at": self.created_at,
            "created_by": self.created_by,
            "updated_at": self.updated_at,
            "updated_by": self.updated_by
        }
        return expense_entry

# POST a new project
@app.route("/addProject/<int:user_id>", methods=['POST'])
def addProject(user_id):
    new_user_id = request.json['user_id']
    new_name = request.json['name']
    new_budget = request.json['budget']
    new_description = request.json['description']

    try:
        new_project = Project(user_id = new_user_id, name= new_name, budget=new_budget, description=new_description)
        db.session.add(new_project)
        db.session.commit()
        return jsonify("{} was created".format(new_project))
    except Exception as e:
        return(str(e))

projects = [{"id": 1,"user_id": 4,"name": "RTF","budget": 12000,"description": "Realtime Face Recogniton"},{"id": 2,"user_id": 1,"name": "SWT","budget": 80000,"description": "Smart Watch Tracker"},{"id": 3,"user_id": 2,"name": "ULS","budget": 11000,"description": "Upgrade Legacy System"}]

# Return list of all details in a project
@app.route("/getAllProject/<int:user_id>", methods=['GET'])
@app.route("/getAllProject/", methods=['GET'])

def getAllProject():

    return jsonify({"projects":projects})


# Return list of all expenses in a project
@app.route("/getAllExpense/<int:project_id>", methods=['GET'])
def getAllExpense(project_id):
    project = Project.query.filter_by(project_id=project_id).first()

    # Project does not exist
    if not project:
        return jsonify({"Expenses": []}), 200

    expenses = Expense.query.filter_by(project_id=project_id).all()

    if not expenses:
        return jsonify({"Expenses": []}), 200

    return [expense.json for expense in expenses]


# Add an expense to a project
@app.route("/addExpense", methods=['POST'])
def addExpense():
    data = request.get_json()
    project_id = data['project_id']

    if not project_id:
        return "Project not found"

    db.session.add(data)
    db.session.commit()

# Update a particular expense
@app.route("/updateExpense", methods=['POST'])
def updateExpense():
    data = request.get_json()

    expense_id = data['expense_id']
    if not expense_id:
        return "Expense record not found"

    expense = Expense.query.filter_by(expense_id=expense_id).update(data)
    db.session.commit()
    return "Successful update"


# Delete an expense from the project
@app.route("/deleteExpense", methods=['DELETE'])
def deleteExpense():
    data = request.get_json()

    project_id = data['project_id']
    expense_id = data['expense_id']

    expense = Expense.query.filter_by(project_id=project_id, expense_id=expense_id).first()

    if expense:
        db.session.delete(expense)
        db.session.commit()
        return "Successfully Deleted"

    return "Record does not exist"

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


# Connect Flask to database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '???'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Attach Flask app to database
db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, id, user_id, name, budget, description):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.budget = budget
        self.description = description

    def json(self):
        project_entry = {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "budget": self.budget,
            "description": self.description,
        }
        return project_entry

# Creation of Project Objects
class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float(precision=2), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    created_by = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_by = db.Column(db.Text, nullable=False)

    def __init__(self, id, project_id, category_id, name, description, amount,
                 created_at, created_by, updated_at, updated_by):
        self.id = id
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

# Return list of all details in a project
@app.route("/getAllProject/<int:user_id>", methods=['GET'])
def getAllProject(user_id):
    project = Project.query.filter_by(user_id=user_id).first()

    # Project does not exist
    if not project:
        return jsonify({"Project" : []}), 200

    project = Project.query.filter_by(user_id=user_id).all()


    return [i.json for i in project]

# Return list of all expenses in a project
@app.route("/getAllExpense/<int:project_id>", methods=['GET'])
def getAllExpense(project_id):
    project = Project.query.filter_by(id=project_id).first()

    # Project does not exist
    if not project:
        return jsonify({"Expenses": []}), 200

    expenses = Expense.query.filter_by(project_id=project_id).all()

    if not expenses:
        return jsonify({"Expenses": []}), 200

    return [expense.json for expense in expenses]

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

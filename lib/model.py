from .extension import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, amount, cost):
        self.name = name
        self.amount = amount
        self.cost = cost
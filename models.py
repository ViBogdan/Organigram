from __init__ import db


class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    reporting_manager = db.Column(db.String)

    def __repr__(self):
        return "<Employee(id={}, name={}, position={}, reporting_manager={})>" \
            .format(self.id, self.name, self.position, self.reporting_manager)

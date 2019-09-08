

class User():
    """
    You can define you db model in this class
    """
    id = db.Column(db.Integer, primary_key=True)
    hashpawd = db.Column(db.String(80))
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(30))
    created = db.Column(db.DateTime())
    updated = b.Column(db.DateTime())


    def __init__(self):
        pass


    def serialize(self):
        return json.dumps(self)

    def create(self, args)

        model.hashpwd = args['hashpwd']
        model.name = args['pwd']
        model.email = args['email']
        model.update = datetime. now()
        model.create = datetime. now()
        db.seccions.add(model)
        db.commit()

        return model.serialize()


    def update(self, args)

        model.hashpwd = args['hashpwd']
        model.name = args['pwd']
        model.email = args['email']
        model.update = datetime. now()
        
        db.seccions.add(model)
        db.commit()

        return model.serialize()

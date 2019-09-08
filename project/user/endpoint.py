# aqui las restfullapii
from flask_restful import Resource


class UserItem(Resource):
    """
    REST API to implement method:
        GET/user/ITEM
        PUT/user/ITEM
        DELETE/user/ITEM

    """
    
    def get(self, user_id):
        # TODO get user

        return {user: user.serialize()}

    def put(self, user_id):
        # TODO update user

        return {user: user.serialize()}, 201


    def delete(self, user_id):
        # TODO remove user

        return "" ,204

class UserIndex(Resource):
    """
    Endpoint
    REST API to implement method:
        POST/user
        GET/user --> filter users (optain a list of user machin some criteria
                     recieve field "search" with json structure similar
                     than this
                     input1 = {
                      "expression": [
                            {
                          "field": "first_name",
                          "operator": "EQ",
                          "value": "Dixie"
                            },
                            "AND",
                            [
                              {
                            "field": "last_name",
                            "operator": "NEQ",
                            "value": "Smith"
                              },
                          "OR",
                              {
                                "field": "middle_name",
                                "operator": "EQ",
                                "value": "Sam"
                              }
                            ]
                      ],
                    }


    """
    def post(self):
        # TODO create user

        return new_user.serialize(), 201

    def get(self):
        # SEARCH USERS


        return User.serialize_list(users_filtered)

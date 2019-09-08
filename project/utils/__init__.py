
input2 = {
  "endpoint": "rfc",
  "expression": [
    {
      "field": "first_name",
      "operator": "EQ",
      "value": "Dixie"
    },
    "OR",
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
  "limit": 2
}

SQL_STR = str
SQL_INT = int
SQL_BOOLEAN = bool

OPERATOR = ['OR', 'AND']
SPECIAL_OPERATOR = ['limit']

SQL_OPERATORS={'EQ':'=',
               'NEQ':'>='}

def json_to_where(json_where, param):

    if 'expression' in json_where:
        return json_to_where(json_where['expression'],{})

    if isinstance(json_where, list):
        ret = ""
        for clause in json_where:
            if clause in OPERATOR:
                print("operator")
                ret += ' {()} '.format(json_to_where,{})
            elif clause in SPECIAL_OPERATOR:
                print("special")
            else:
                ret += json_to_where(clause, param)
#        print(len(json_where), json_where)
        # if len(json_where)>2:
        #    ret+=')'
        return ret
    if isinstance(json_where, dict):
        return ' {} {} {}'.format(json_where['field'], SQL_OPERATORS[json_where['operator']], json_where['value'])
    if isinstance(json_where, str):
        return " {} ".format(json_where) # json_where

    # return "frist_name = 'Dixie' AND (last_name != 'Smith' OR middle_name = 'Sam') limit 2"
LOGICAL_OPERATORS = ("AND", "OR")

COMPARISON_OPERATORS = {
    "LT": "<",
    "GT": ">",
    "LTE": "<=",
    "GTE": ">=",
    "EQ": "=",
    "NEQ": "!="
}

def process(data, parameters={}):
    """
    :param data: JSON Object (dict). 
    :param parameters: dict.
    :return: where clause (str) built from data
    """
    where_clause = ""
    if isinstance(data, list):
        for part in data:
            if part not in LOGICAL_OPERATORS:
                where_clause += " ({}) ".format(process(part, parameters))
            else:
                where_clause += process(part, parameters)
    elif isinstance(data, dict):
        where_clause += " {} {} %({})s ".format(data["field"], COMPARISON_OPERATORS[data["operator"]], data["field"])
        parameters[data["field"]] = data["value"]
    elif isinstance(data, str):
        return data
    return where_clause


def main():
    expression = input2["expression"]
    parameters = {}
    where_clause = process(expression, parameters)

    return "SELECT * FROM table WHERE {}".format(where_clause), parameters


if __name__ == '__main__':
    print(main())
    # print("END", json_to_where(input2,{}))




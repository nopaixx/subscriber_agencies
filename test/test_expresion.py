import pytest
from project.utils import json_to_where


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

input2 = {
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
}

expected1 = "frist_name = 'Dixie' AND (last_name != 'Smith' OR middle_name = 'Sam') limit 2"
expected2 = "frist_name = 'Dixie' OR (last_name != 'Smith' OR middle_name = 'Sam')"
expected3 = "frist_name = 'Dixie' AND (last_name != 'Smith' OR middle_name = 'Sam') limit 2"
        
@pytest.mark.parametrize("test_input,expected", [(input1, expected1), (input2, expected2)])
def test_expression(test_input, expected):
    assert expected == json_to_where(test_input)


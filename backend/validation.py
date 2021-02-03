import re

def validate(name,mark): 
    error={
        "isValid": True
    }
    if float(mark)<0 or float(mark)>20: 
        error['isValid'] = False
        error['mark'] = "Mark should be between 0 & 20"
    if not bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)):
        error['isValid'] = False
        error['name'] = "Name is not valid"

    return error
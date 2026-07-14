import datetime


def get_timestamp():

    return datetime.datetime.now().isoformat()



def calculate_percentage(value,max_value):

    if max_value == 0:
        return 0

    return round((value/max_value)*100,2)
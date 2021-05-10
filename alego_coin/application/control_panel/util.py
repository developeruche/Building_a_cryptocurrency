import time
import datetime

def create_timestamp():
    today_now = datetime.datetime.now()
    # __secs = today_now.second
    # __minutes = today_now.minute
    # __hour = today_now.hour
    # __days = today_now.day
    # __month = today_now.month
    # __year = today_now.year
    
    return today_now.timestamp()


def coin_data_formatter(list__):
    """ 
        The function would take a coin dictionary parameter and return formated string
        which would be used for hashing
    """
    data_to_hash = " _ ".join(list__)

    return data_to_hash



from datetime import datetime, timedelta

def get_current_time(minutes=0):
    now = datetime.now() + timedelta(minutes = minutes)
    return now.strftime("%H:%M:%S")
def get_current_date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d")
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")




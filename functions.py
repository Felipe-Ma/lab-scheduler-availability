from datetime import datetime

def get_time():
    current_datetime = datetime.now()
    print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")

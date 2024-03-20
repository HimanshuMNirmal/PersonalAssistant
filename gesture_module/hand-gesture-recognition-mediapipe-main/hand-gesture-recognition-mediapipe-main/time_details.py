from datetime import datetime

def get_time():
    now = datetime.now()

    currentTime = now.strftime('%H hours %M minutes')
    return (currentTime)
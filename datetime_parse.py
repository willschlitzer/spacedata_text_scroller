import datetime

def timedelta_parser(time_d):
    days = time_d.days
    remaining_seconds = time_d.seconds
    hours = int(remaining_seconds/3600)
    remaining_seconds = remaining_seconds - (hours*3600)
    minutes = int(remaining_seconds/60)
    seconds = int(remaining_seconds-minutes*60)
    return days, hours, minutes, seconds
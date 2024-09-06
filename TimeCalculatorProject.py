def add_time(start, duration, weekday = None):
    start_hour = start.split(':')[0]
    start_minute = start.rsplit()[1]
    day_part = start.rsplit()[2]
    duration_time = duration.split(':')
    hours = 0
    minutes = 0
    days_later = 0
    if start_minute + duration_time[1] >= 60:
        minutes = int(start_minute) + int(duration_time[1]) - 60
        hours += 1 + int(duration_time[0])
    else:
        minutes = int(start_minute) + int(duration_time[1])
        hours += int(duration_time[0])
    if day_part.upper() == 'PM':
        start_hour += 12

    hours += start_hour

    if hours < 12:
        new_time = str(hours) + ':' + minutes + 'AM'
        return new_time
    elif hours < 24:
        new_time = str(hours - 12) + ':' + minutes + 'PM'

    return new_time

print(add_time('11:30', '12:30'))
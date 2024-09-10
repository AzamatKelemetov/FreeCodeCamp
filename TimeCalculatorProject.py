def add_time(start, duration, weekday = None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def find_day_index(day):
        return days_of_week.index(day.capitalize())

    # Convert 12 hour format into 24 hour
    def time_to_24_hour(hour, minute, period):
        if period == 'PM' and hour != 12:
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0
        return hour, minute

    # Con 24 hour forman to 12 hour
    def time_to_12_hour(hour, minute):
        if hour < 12:
            period = 'AM'
        else:
            period = 'PM'
        hour = hour % 12
        if hour == 0:
            hour = 12
        return hour, minute, period

    # Parse start time
    start_time_parts = start.split()
    start_hour, start_minute = map(int, start_time_parts[0].split(':'))
    period = start_time_parts[1]

    # Convert to 24 format
    start_hour, start_minute = time_to_24_hour(start_hour, start_minute, period)

    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add duration time to start
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + (end_minute // 60)
    end_minute = end_minute % 60

    # Days passed calculation
    days_later = end_hour // 24
    end_hour = end_hour % 24

    # Convert back to 12 hour format
    final_hour, final_minute, final_period = time_to_12_hour(end_hour, end_minute)

    # Find the day of the week
    if weekday:
        day_index = find_day_index(weekday)
        new_day = days_of_week[(day_index + days_later) % 7]
    else:
        new_day = None

    # Build the output
    result = f'{final_hour}:{final_minute:02d} {final_period}'

    if new_day:
        result += f', {new_day}'

    if days_later == 1:
        result += ' (next day)'
    elif days_later > 1:
        result += f' ({days_later} days later)'

    return  result

print(add_time('11:59 PM', '24:05'))
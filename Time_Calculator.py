def add_time(start, duration, day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    duration_hour, duration_minute = map(int, duration.split(':'))

    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    new_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    new_hour_24 = total_hours % 24

    if new_hour_24 == 0:
        new_hour = 12
        new_period = "AM"
    elif new_hour_24 < 12:
        new_hour = new_hour_24
        new_period = "AM"
    elif new_hour_24 == 12:
        new_hour = 12
        new_period = "PM"
    else:
        new_hour = new_hour_24 - 12
        new_period = "PM"

    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    if day:
        index = days_of_week.index(day.capitalize())
        new_day_index = (index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

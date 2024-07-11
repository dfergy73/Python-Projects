'''This program contains a function that takes in two required and one
optional parameter. The two required are a start time and a duration,
and the optional is a starting day of the week. The function adds the
duration time to the start time and returns the result.'''

def add_time(start, duration, day=None):
    # Split the start time and duration into hours and minutes.
    time_list = start.split(':')
    add_time_list = duration.split(':')

    # Check if it's AM or PM, then add together the start hour and the
    # duration hours and remove 'AM' or 'PM' from the minute string.
    if ' PM' in time_list[1]:
        # If after 12PM, add 12 to the hours.
        hour = int(time_list[0]) + int(add_time_list[0]) + 12
        time_list[1] = time_list[1].strip(' PM')
    else:
        hour = int(time_list[0]) + int(add_time_list[0])
        time_list[1] = time_list[1].strip(' AM')

    # Add together the start minute and duration minutes.
    minute = int(time_list[1]) + int(add_time_list[1])

    # If minutes added together is over 60 minutes, add one to the hour
    # variable and assign the remainder to the minute variable.
    if minute > 60:
        hour += 1
        minute = minute % 60

    # If the hour variable is over 24, assign the extra days to their
    # own variable and assign the remaining hours to the hour variable.
    extra_days = 0
    if hour >= 24:
        extra_days = hour // 24
        hour = hour % 24

    # Check to see if the new hour is in the AM or PM and if the new
    # minute is less than 10.
    if hour >= 12:
        if hour > 12:
            hour -= 12
            if minute > 9:
                minute = f'{minute} PM'
            else:
                minute = f'0{minute} PM'
        else:
            if minute > 9:
                minute = f'{minute} PM'
            else:
                minute = f'0{minute} PM'
    # Check to see if the new hour is between midnight and 1AM.
    else:
        if hour == 0:
            hour += 12
        if minute > 9:
            minute = f'{minute} AM'
        else:
            minute = f'0{minute} AM'
    
    # Check if optional variable is provided. Create dictionary to hold
    # days of the week with associated number.
    if day:
        
        days_of_the_week = {
            'sunday': 1,
            'monday': 2,
            'tuesday': 3,
            'wednesday': 4,
            'thursday': 5,
            'friday': 6,
            'saturday': 7
        }
        
        # Get day number of start time.
        current_day = days_of_the_week.get(day.lower())
        # Add the extra days to the current day, then find the remainder
        # after dividing by 7 to find the new day in the dictionary.
        new_day = current_day + extra_days
        new_day = new_day % 7
        for day, number in days_of_the_week.items():
            if new_day == number:
                new_day = day

        # Format the output and include the day of the week.
        if extra_days == 1:
            new_time = f'{hour}:{minute}, {new_day.capitalize()} (next day)'
        elif extra_days > 1:
            new_time = f'{hour}:{minute}, {new_day.capitalize()} ({extra_days} days later)'
        else:
            new_time = f'{hour}:{minute}, {new_day.capitalize()}'
    
    # Format the output.
    else:
        if extra_days == 1:
            new_time = f'{hour}:{minute} (next day)'
        elif extra_days > 1:
            new_time = f'{hour}:{minute} ({extra_days} days later)'
        else:
            new_time = f'{hour}:{minute}'

    return new_time

print(add_time('6:30 PM', '205:12'))
print(add_time('11:43 PM', '24:20'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:55 AM', '3:12'))
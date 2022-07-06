def timerange_to_minutes(t_str):
    """ Return amount of minutes for timeranges in format HH:MM """
    hour = int(t_str.split(':')[0])
    hour_to_minute = hour * 60
    minute = int(t_str.split(':')[1])
    return hour_to_minute + minute

def minutes_to_timerange_str(m):
    hour = m // 60
    hour_str = f'{hour:02d}'
    minutes = m % 60
    minutes_str = f'{minutes:02d}'

    return f'{hour_str}:{minutes_str}'

def prettify_available_minutes(lst: list):
    group_list = []
    list_reset = []
    for element in lst:
        if list_reset == []:
            list_reset.append(element)
            continue
        if list_reset[-1] + 1 == element:
            list_reset.append(element)
        else:
            group_list.append(list_reset[:])
            list_reset.clear()
            list_reset.append(element)
    
    group_list.append(list_reset)
    
    time_ranges = []

    for group in group_list:
        start_time = minutes_to_timerange_str(m=group[0])
        end_time = minutes_to_timerange_str(m=group[-1])
        time_range_str = f'{start_time} - {end_time}'
        time_ranges.append(time_range_str)
    
    return time_ranges


def add_time(start_time, duration, starting_day = ''):
    week_days = ["ok","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]    
    week_days_dic = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
    n = 0
    start = start_time.split() # 3:00  & PM
    star = start[0].split(':') # 3  & 00
    if not star[0].isdigit() or not star[1].isdigit():
        return #"unsupported digit"    
    start_time_in_min = int(star[0]) * 60 + int(star[1])
    if start[1] == 'PM':
        start_time_in_24 = start_time_in_min + 12 * 60
    elif start[1] == 'AM':
        start_time_in_24 = start_time_in_min

    dhm = duration.split(':')  # 3 & 10    
    if not dhm[0].isdigit() or not dhm[1].isdigit():
        return #"unsupported digit"  
    duration_in_min = int(dhm[0]) * 60 + int(dhm[1])    

    final_time_in_min = start_time_in_24 + duration_in_min
    hrs = final_time_in_min /60
    hrs = int(hrs)
    mins = final_time_in_min % 60

    n = hrs / 24
    n = int(n)
    days_hrs = hrs % 24
    print(days_hrs)
    if days_hrs == 12:
        final_time = 12 
        meredian = 'PM'

    elif days_hrs == 0:
        final_time = 12 
        meredian = 'AM'

    elif days_hrs >= 13:
        final_time = days_hrs - 12       
        meredian = 'PM'

    else:   
        final_time = days_hrs
        meredian = 'AM'

    if len(starting_day) > 0:
        starting_day = starting_day.lower()
        starting_day_index = week_days_dic[starting_day]        
        result_date_index = n + starting_day_index
        while result_date_index > 7:
            result_date_index -= 7
        
        date = ', ' + week_days[result_date_index]
    else: 
        date = ''         
    hr_str = str(final_time)
        
    if mins < 10:
        mins_str = '0' + str(mins)
    else:
        mins_str = str(mins)
    result = hr_str + ':' + mins_str + ' ' + str(meredian)
    if n > 1:
        result = result + date + ' (' +str(n) + ' days later)'
    elif n == 1:
        result = result + date + ' (next day)'
    else:
        result = result + date

    return result

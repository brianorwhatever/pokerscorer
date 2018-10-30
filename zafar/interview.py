import datetime
import pprint

INTERVAL_MINS = 10

with open('nginx.log') as file:
    i = 0
    errors = {}
    current_interval = datetime.datetime.now()
    for line in file:
        line_split = line.split(' ')
        try:
            line_time = datetime.datetime.strptime(line_split[3][1:], '%d/%b/%Y:%H:%m:%S')
        except IndexError:
            print('error parsing line {line}'.format(line=i+1))
            break
        if i == 0 or line_time - current_interval > datetime.timedelta(minutes=INTERVAL_MINS):
            current_interval = datetime.datetime(month=line_time.month, day=line_time.day,
                                                 year=line_time.year, hour=line_time.hour,
                                                 minute=line_time.minute % INTERVAL_MINS)
            current_interval_string = current_interval.strftime('%m/%d/%Y:%H:%m')
            errors[current_interval_string] = 0
        if int(line_split[8]) >= 500 and int(line_split[8]) < 600:
            current_interval_string = current_interval.strftime('%m/%d/%Y:%H:%m')
            errors[current_interval_string] = errors[current_interval_string] + 1
        
        i = i + 1
    pprint.pprint(errors)

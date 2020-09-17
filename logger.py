#!/usr/bin/python3
import csv
import datetime
import sys

dt_now = datetime.datetime.now()
now_str = dt_now.strftime('%Y-%m-%d %H:%M')


rows = []
file = open('log.csv', 'r')
reader = csv.reader(file)
for row in reader:
    rows.append(row)
file.close()

last_log = rows.pop()
estimate = '--'
if (sys.argv[1] == '-s'):
    event = 'start'
    title = sys.argv[2]
    if (len(sys.argv) == 4):
        estimate = sys.argv[3]
else:
    if (last_log[2] == 'start' and sys.argv[1] == '-e'):
        event = 'end'
        title = last_log[3]
        last_task_start = datetime.datetime.strptime(last_log[0], '%Y-%m-%d %H:%M')
        delta = last_task_start - dt_now
        delta_sec = delta.total_seconds()
        estimate = abs(int(delta_sec / 60))


file = open('log.csv', 'a', newline='\n')
writer = csv.DictWriter(file, fieldnames=['time',  'est-real', 'event', 'title'])
writer.writerow({'time': now_str, 'est-real': estimate, 'event': event, 'title': title})
file.close()

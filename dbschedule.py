from dbdata import DataDatabase
from datetime import date, timedelta

class ScheduleDatabase():
    delta = timedelta(days=1)
    data_schedule = [
        {
            'id': '1',
            'film': DataDatabase.data_film[0],
            'studio': DataDatabase.data_studio[0],
            'time': '14:00',
            'date_start': date(2023,11,1),
            'date_end': date(2023,11,30),
        },
        {
            'id': '2',
            'film': DataDatabase.data_film[1],
            'studio': DataDatabase.data_studio[0],
            'time': '12:00',
            'date_start': date(2023,11,1),
            'date_end': date(2023,11,30),

        },
        {
            'id': '3',
            'film': DataDatabase.data_film[2],
            'studio': DataDatabase.data_studio[0],
            'time': '13:00',
            'date_start': date(2023,11,1),
            'date_end': date(2023,11,30),
        } 
    ]
    for data in data_schedule:
        data['mat_seat'] = {}
        while data['date_start'] <= data['date_end']:
            data['mat_seat'][data['date_start'].strftime("%Y-%m-%d")] = [[True for x in range (5)] for y in range (data['studio']['num_rows'])]
            data['date_start'] += delta
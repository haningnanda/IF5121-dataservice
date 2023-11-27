from datetime import date, timedelta
class DataDatabase():
    data_film = [
        {
            'id': '1',
            'name': 'Film 1',
            'synopsis': 'Sinopsis Film 1',
            'genre': 'Horor',
            'duration': '120',
            'poster': 'Ini poster 1'
        },
        {
            'id': '2',
            'name': 'Film 2',
            'synopsis': 'Sinopsis Film 2',
            'genre': 'Comedy',
            'duration': '110',
            'poster': 'Ini poster 2'
        },
        {
            'id': '3',
            'name': 'Film 3',
            'synopsis': 'Sinopsis Film 3',
            'genre': 'Horor',
            'duration': '100',
            'poster': 'Ini poster 3'
        }
    ]

    data_studio = [
        {
            'id': '1',
            'name': 'Studio 1',
            'num_rows': 10,
            'num_cols': 12
        },
        {
            'id': '2',
            'name': 'Studio 2',
            'num_rows': 10,
            'num_cols': 12
        },
        {
            'id': '3',
            'name': 'Studio 3',
            'num_rows': 10,
            'num_cols': 12
        }
    ]

    data_fnb = [
        {
            'id': '1',
            'name': 'Cocacola',
            'price': 20000,
            'poster': 'Poster',
            'detail_info': 'Detail info cocacola',
            'available_stock': 20,
        },
        {
            'id': '2',
            'name': 'Popcorn',
            'price': 20000,
            'poster': 'Poster',
            'detail_info': 'Detail info popcorn',
            'available_stock': 20,
        }
    ]

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
            'studio': DataDatabase.data_studio[1],
            'time': '12:00',
            'date_start': date(2023,11,1),
            'date_end': date(2023,11,30),

        },
        {
            'id': '3',
            'film': DataDatabase.data_film[2],
            'studio': DataDatabase.data_studio[2],
            'time': '13:00',
            'date_start': date(2023,11,1),
            'date_end': date(2023,11,30),
        } 
    ]
    for data in data_schedule:
        data['mat_seat'] = {}
        while data['date_start'] <= data['date_end']:
            data1 = data
            full_mat = []
            for i in range (data['studio']['num_rows']):
                mat = [True for x in range ((data['studio']['num_cols']))]
                full_mat.append(mat)
            data['mat_seat'][data['date_start'].strftime("%Y-%m-%d")] = full_mat
            data['date_start'] += delta
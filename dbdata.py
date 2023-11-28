from datetime import date, timedelta
from dataclass import Film, Studio, FnB, Schedule
class DataDatabase():
    data_film = [
        Film(name= 'Film 1',
            synopsis= 'Sinopsis Film 1',
            genre= 'Horor',
            duration= '120',
            poster= 'Ini poster 1',
            price=50000
        ),
        Film(name= 'Film 2',
            synopsis= 'Sinopsis Film 2',
            genre= 'Comedy',
            duration= '110',
            poster= 'Ini poster 2',
            price=50000
        ),
        Film(name= 'Film 3',
            synopsis= 'Sinopsis Film 3',
            genre= 'Horor',
            duration= '100',
            poster= 'Ini poster 3',
            price=50000
        )
    ]

    data_studio = [
        Studio(name='Studio 1',
            num_rows=10,
            num_cols=12
        ),
        Studio(name='Studio 2',
            num_rows=10,
            num_cols=12
        ),
        Studio(name='Studio 3',
            num_rows=10,
            num_cols=12
        )
    ]

    data_fnb = [
        FnB(name='Cocacola',
            price=20000,
            poster='Poster',
            detail_info='Detail info cocacola',
            available_stock=20,
        ),
        FnB(name='Popcorn',
            price=20000,
            poster='Poster',
            detail_info='Detail info popcorn',
            available_stock=20,
        )
    ]

class ScheduleDatabase():
    data_schedule = [
        Schedule(
            id='1',
            film=DataDatabase.data_film[0],
            studio=DataDatabase.data_studio[0],
            time='14:00',
            date_start=date(2023,11,1),
            date_end=date(2023,11,30),
        ),
        Schedule(
            id='2',
            film=DataDatabase.data_film[1],
            studio=DataDatabase.data_studio[1],
            time='12:00',
            date_start=date(2023,11,1),
            date_end=date(2023,11,30),

        ),
        Schedule(
            id='3',
            film=DataDatabase.data_film[2],
            studio=DataDatabase.data_studio[2],
            time='13:00',
            date_start=date(2023,11,1),
            date_end=date(2023,11,30),
        )
    ]
    # for data in data_schedule:
    #     data['mat_seat'] = {}
    #     while data['date_start'] <= data['date_end']:
    #         data1 = data
    #         full_mat = []
    #         for i in range (data['studio']['num_rows']):
    #             mat = [True for x in range ((data['studio']['num_cols']))]
    #             full_mat.append(mat)
    #         data['mat_seat'][data['date_start'].strftime("%Y-%m-%d")] = full_mat
    #         data['date_start'] += delta
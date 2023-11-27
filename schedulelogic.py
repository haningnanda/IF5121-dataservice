# from src.item.ticket import Ticket
from datalogic import Film
from datalogic import Studio
from datetime import date, timedelta
import string
class Schedule(object):
    def __init__(self, id: str, film: Film, studio: Studio, time: str, date_start: date, date_end: date):
        self.id = id
        self.film = film
        self.studio = studio
        self.time = time
        self.date_start = date_start
        self.date_end = date_end
        self.mat_seat = {}

        delta = timedelta(days=1)
        while date_start <= date_end:
            self.mat_seat[date_start.strftime("%Y-%m-%d")] = [[True for x in range (self.studio.num_cols)] for y in range (self.studio.num_rows)]
            date_start += delta

    def __str__(self) -> str:
        return f'{self.film.__str__()}'
    def get_id(self):
        return self.id
    def get_film(self):
        return self.film
    def get_studio(self):
        return self.studio
    def get_time(self):
        return self.time
    def get_date_start(self):
        return self.date_start
    def get_date_end(self):
        return self.date_end
    def set_film(self, film):
        self.film = film
    def set_studio(self, studio):
        self.studio = studio
    def set_time(self, time):
        self.time = time
    def set_date_start(self, date_start):
        self.date_start = date_start
    def set_date_end(self, date_end):
        self.date_end = date_end
    def get_available_seat(self):
        return self.mat_seat
    def take_seat(self, date, row, col) -> Ticket:
        if not self.mat_seat[date][row][col]:
            raise Exception("Seat is currently unavailable")
        self.mat_seat[date][row][col] = False
        return Ticket(self, date, row, col)

    def untake_seat(self, date, row, col):
        self.mat_seat[date][row][col] = True
    
    def show_seats(self, date):
        try :
            seats = self.mat_seat[date]
            print("Seat Availability:")
            print("Row/Col", end='\t')
            for col in range(len(seats[0])):
                print(col+1, end='\t')
            print()
            for i, row in enumerate(seats):
                row_label = string.ascii_uppercase[i]  # Convert numeric row index to alphabet
                print(f"Row {row_label}", end='\t')
                for seat in row:
                    if seat:  # If the seat is available (True)
                        print("◯", end='\t')  # Circle symbol for available seat
                    else:
                        print("⨉", end='\t')  # X symbol for occupied seat
                print()
        except KeyError as e :
            raise KeyError(e)
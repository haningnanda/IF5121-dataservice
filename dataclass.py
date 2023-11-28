from datetime import date, timedelta
import string

class Account:

    def __init__(self) -> None:
        self._email = None 
        self._password = None
        self._database = None
    
    @property
    def database(self):
        return self._database
    
    @database.setter
    def database(self, selection_database):
        self._database = selection_database
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_email):
        self._email = user_email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, user_password):
        self._password = user_password
      
    def login(self):
        pass

    def reset_password(self):
        pass

class User(Account):

    def __init__(self)-> None:
        super().__init__()
class Studio(object):
    def __init__(self, name, num_rows, num_cols):
        self.name = name
        self.num_rows = num_rows
        self.num_cols = num_cols
    def get_name(self):
        return self.name
    def get_num_rows(self):
        return self.num_rows
    def get_num_cols(self):
        return self.num_cols
    def set_name(self, name):
        self.name = name
    def set_num_rows(self, num_rows):
        self.name = num_rows
    def set_num_cols(self, num_cols):
        self.name = num_cols

    def serialize(self):
        return dict(
            name=self.name,
            num_rows=self.num_rows,
            num_cols=self.num_cols
        )
    # return result

class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price

class Film(Item):
    def __init__(self,name, price, synopsis, genre, duration, poster):
        Item.__init__(self, name, price)
        self.synopsis = synopsis
        self.genre = genre
        self.duration = duration
        self.poster = poster
    def __str__(self) -> str:
        return f"Film : {self.name}\nHarga: {self.price}\nGenre : {self.genre}\nDurasi: {self.duration} menit\nSinopsis: {self.synopsis}"
    def get_synopsis(self):
        return self.synopsis
    def get_genre(self):
        return self.genre
    def get_duration(self):
        return self.duration
    def get_poster(self):
        return self.poster
    def set_synopsis(self, synopsis):
        self.synopsis = synopsis
    def set_genre(self, genre):
        self.genre = genre
    def set_duration(self, duration):
        self.duration = duration
    def set_poster(self, poster):
        self.poster = poster
    
    def serialize(self):
        return dict(
            name=self.name,
            price=self.price,
            synopsis=self.synopsis,
            genre=self.genre,
            duration=self.duration,
            poster=self.poster
        )

class FnB(Item):
    def __init__(self, name, price, poster, detail_info, available_stock, is_available=True):
        Item.__init__(self,name, price)
        self.poster = poster
        self.detail_info = detail_info
        self.is_available = is_available
        self.available_stock = available_stock
    def __str__(self):
        return f'Nama Makanan / Minuman : {self.name}\nDetail Info : {self.detail_info}\nKetersediaan : {self.available_stock}'
    def get_poster(self):
        return self.poster
    def get_detail_info(self):
        return self.detail_info
    def get_available_stock(self):
        return self.available_stock
    def set_poster(self, poster):
        self.poster = poster
    def set_detail_info(self, detail_info):
        self.detail_info = detail_info
    def set_stock(self, available_stock):
        self.available_stock = available_stock
    def set_available(self, is_available):
        self.is_available= is_available
    def cancel(self):
        self.set_stock(self.get_available_stock()+1)
    def book(self):
        if (self.get_available_stock()-1) < 0:
            raise Exception(f"Stock {self.get_name} sudah habis")
        self.set_stock(self.get_available_stock()-1)
    
    def serialize(self):
        return dict(
            name=self.name,
            price=self.price,
            poster=self.poster,
            detail_info=self.detail_info,
            available_stock=self.available_stock,
            is_available=self.is_available
        )

class Ticket(Item):
    def __init__(self, schedule, date, seat_row, seat_col):
        self.schedule = schedule
        self.date = date
        self.seat_row = seat_row
        self.seat_col = seat_col
        self.set_price(schedule.get_film().get_price())

    def get_schedule(self):
        return self.schedule
    def get_date(self):
        return self.date
    def set_schedule(self, schedule):
        self.schedule = schedule
    def set_date(self,date):
        self.date = date
    def cancel(self):
        self.schedule.untake_seat(self.date, self.seat_row, self.seat_col)
    def book(self):
        self.status = "booked"
    def buy(self):
        self.status = "bought"
    def invalidate(self):
        if self.status != "bought":
            raise Exception("Only bought ticket can be invalidated")
        self.set_status("invalidated")
    def get_seat(self):
        return self.matrix_index_to_seat_number(self.seat_row, self.seat_col)

    def matrix_index_to_seat_number(self, row_index, col_index):
        # Convert the column index to a letter representing the row
        row_letter = chr(ord('A') + row_index)

        seat_number = f"{row_letter}{col_index+1}"

        return seat_number

    def serialize(self):
        s = self.schedule.serialize()
        del s["mat_seat"]
        return dict(
            schedule=s,
            date=self.date,
            seat_row=self.seat_row,
            seat_col=self.seat_col
        )
    
    
class Schedule(object):
    def __init__(self,
    id: str, film: Film, studio: Studio, time: str, date_start: date, date_end: date, mat_seat={}):
        self.id = id
        self.film = film
        self.studio = studio
        self.time = time
        self.date_start = date_start
        self.date_end = date_end
        self.mat_seat = mat_seat

        if not mat_seat:
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
    def take_seat(self, date, row, col) :
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

    def serialize(self):
        return dict(
            id=self.id,
            film=self.film.serialize(),
            studio=self.studio.serialize(),
            time=self.time,
            date_start=self.date_start.strftime('%Y-%m-%d'),
            date_end=self.date_end.strftime('%Y-%m-%d'),
            mat_seat=self.mat_seat,
        )


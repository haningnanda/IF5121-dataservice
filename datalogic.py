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
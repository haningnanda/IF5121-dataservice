from flask import Flask, request, jsonify
from dbdata import DataDatabase
from dbschedule import ScheduleDatabase
import string

app = Flask(__name__)

def convert_seat_to_index(chosen_seats):
    row_dict = {letter: index for index, letter in enumerate(string.ascii_uppercase)}
    matrix_indices = []
    for seat in chosen_seats:
        row_label, col_label = seat[0], int(seat[1:])  # Extracting row label and column number
        row_index = row_dict[row_label]  # Convert row label to numeric index
        col_index = col_label - 1  # Adjusting column to 0-based index
        matrix_indices.append((row_index, col_index))
    return matrix_indices

@app.route('/fnbs', methods=['GET'])
def get_fnbs():
    data = DataDatabase.data_fnb
    return data

@app.route('/schedule', methods=['GET'])
def get_schedule():
    data = ScheduleDatabase.data_schedule
    return data

@app.route('/show-seats', methods=['GET'])
def show_seats():
    args = request.args
    schedule_id = args['schedule-id']
    date = args['date']
    data_schedule = ScheduleDatabase.data_schedule
    for data in data_schedule:
        if data['id']==schedule_id:
            return data['mat_seat'][date]

@app.route('take-seats/', methods=['POST'])
def take_seats():
    args = request.args
    schedule_id = args['schedule-id']
    date = args['date']
    seats = request.json['seats']
    # ticket = 
    

@app.route('/fnb/book', methods=['POST'])
def fnb_book():
    fnbs = request.json(['fnbs'])
    with open("test.txt", "w") as fo:
        fo.write("This is Test Data")

@app.route('/ticket/book', methods=['POST'])
def ticket_book():
    schedule_id = request.json(['schedule_id'])
    date = request.json(['date'])
    seats = request.json(['seats'])

@app.route('/fnb/cancel', methods=['POST'])
def fnb_cancel():
    fnbs = request.json(['fnbs'])

@app.route('/ticket/cancel', methods=['POST'])
def ticket_cancel():
    schedule_id = request.json(['schedule_id'])
    date = request.json(['date'])
    seats = request.json(['seats'])

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
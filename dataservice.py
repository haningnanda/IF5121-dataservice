from flask import Flask, request, jsonify, Response
from dbdata import DataDatabase, ScheduleDatabase
import string
from localStoragePy import localStoragePy
import json as JSON
from dataclass import Schedule
from datetime import timedelta
from helper import serialize

app = Flask(__name__)
localStorage = localStoragePy('IF5121-dataservice', 'json')
localStorage.setItem('FNBS', JSON.dumps([]))
localStorage.setItem('TICKET', JSON.dumps([]))


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
    return serialize(DataDatabase.data_fnb)
    

@app.route('/fnb/<name>', methods=['GET'])
def get_fnb(name):
    data = [s for s in DataDatabase.data_fnb if s.name == name]
    if data:
        return serialize(data[0])
    return jsonify({"msg":"FnB not found"}), 404

@app.route('/schedules', methods=['GET'])
def get_schedules():
    data = serialize(ScheduleDatabase.data_schedule)
    return data

@app.route('/schedule/<id>', methods=['GET'])
def get_schedule(id):
    data = [s for s in ScheduleDatabase.data_schedule if s.id == id]
    if data:
        return serialize(data[0])
    return jsonify({"msg":"Schedule not found"}), 404

@app.route('/show-seats/<schedule_id>/<schedule_date>', methods=['GET'])
def show_seats(schedule_id, schedule_date):
    data = [s for s in ScheduleDatabase.data_schedule if s.id == schedule_id]
    return data[0].mat_seat[schedule_date]

@app.route('/take-seats/<schedule_id>/<schedule_date>', methods=['POST'])
def take_seats(schedule_id, schedule_date):
    tickets = []
    seats = request.json['seats']
    data = [s for s in ScheduleDatabase.data_schedule if s.id == schedule_id]

    if not data:
        return jsonify({"msg":"Schedule not found"}), 404
    
    schedule = data[0]
    conv = convert_seat_to_index(seats)
    for seat in conv :
        tickets.append(schedule.take_seat(schedule_date, seat[0], seat[1]))
    DataDatabase.data_ticket += tickets
    return serialize(tickets)
    

@app.route('/fnb/book', methods=['POST'])
def fnb_book():
    names = request.json['fnbs']
    fnbs = [f for f in DataDatabase.data_fnb if f.name in names]
    for f in fnbs:
        f.book()
    return Response(status=204)

@app.route('/fnb/cancel', methods=['POST'])
def fnb_cancel():
    names = request.json['fnbs']
    fnbs = [f for f in DataDatabase.data_fnb if f.name in names]
    for f in fnbs:
        f.cancel()
    
    return Response(status=204)

@app.route('/ticket/book/<schedule_id>/<schedule_date>', methods=['POST'])
def ticket_book(schedule_id, schedule_date):
    tickets = []
    seats = request.json['seats']
    seat_index = convert_seat_to_index(seats)
    for t in DataDatabase.data_ticket:
        for s in seat_index:
            if t.get_schedule().id == schedule_id and t.date == schedule_date and t.seat_row == s[0] and t.seat_col == s[1]:
                t.book()
    return Response(status=204)
    
@app.route('/ticket/cancel/<schedule_id>/<schedule_date>', methods=['POST'])
def ticket_cancel(schedule_id, schedule_date):
    tickets = []
    seats = request.json['seats']
    seat_index = convert_seat_to_index(seats)
    for t in DataDatabase.data_ticket:
        for s in seat_index:
            if t.get_schedule().id == schedule_id and t.date == schedule_date and t.seat_row == s[0] and t.seat_col == s[1]:
                t.cancel()
    return Response(status=204)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5003)
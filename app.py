# app.py
from flask import Flask, request
from tools import str_to_date,\
    diff_between_dates
from datetime import datetime

app = Flask(__name__)

HTML_NAME_FOR_THE_DATE = "d"

# decorator
@app.route("/distance", methods=['POST'])
def respond_to_distance_request():
    the_user_date:str =\
        request.form[HTML_NAME_FOR_THE_DATE]

    the_date:datetime = \
        str_to_date(the_user_date)

    response:dict = diff_between_dates(
        the_date
    )

    return response
# def respond_to_distance_request

app.run(
    host="0.0.0.0", # all network interfaces
    port=5555,
    debug=True
)
# app.py
from flask import Flask, request, render_template
from tools import str_to_date,\
    diff_between_dates
from datetime import datetime

app = Flask(__name__)

HTML_NAME_FOR_THE_DATE = "d"

# decorator
@app.route("/", methods=['POST', 'GET'])

def respond_to_distance_request():
    b_there_is_date:bool =\
        HTML_NAME_FOR_THE_DATE in request.form.keys()

    if (b_there_is_date):
        the_user_date:str =\
            request.form[HTML_NAME_FOR_THE_DATE]

        the_date:datetime = \
            str_to_date(the_user_date)

        response:dict = diff_between_dates(
            the_date
        )

        return response
    #
    else:
        return render_template(
            "date_input.html"
        )
# def respond_to_distance_request

app.run(
    host="0.0.0.0", # all network interfaces
    port=5555,
    debug=True
)
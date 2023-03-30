# app.py
from flask import Flask, request, render_template
from tools import str_to_date,\
    diff_between_dates
from datetime import datetime

app = Flask(__name__)

HTML_NAME_FOR_THE_DATE = "d"

# NOT a view
def obtain_user_date():
    str_user_date = None
    b_GET:bool = request.method=='GET'
    b_POST:bool = request.method=='POST'

    if(b_GET):
        b_caution:bool = HTML_NAME_FOR_THE_DATE in\
            request.args.keys()
        if(b_caution):
            str_user_date = \
                request.args[HTML_NAME_FOR_THE_DATE]
            return str_user_date
        # if
    else:
        if(b_POST):
            b_caution:bool = HTML_NAME_FOR_THE_DATE in\
                request.form.keys()
            if(b_caution):
                str_user_date = \
                    request.form[HTML_NAME_FOR_THE_DATE]
                return str_user_date
            # if
        # if
    # if-else
    #return "no user date"
    return None
# obtain_user_date

# decorator
@app.route("/", methods=['POST', 'GET'])
def respond_to_distance_request():
    the_user_date = obtain_user_date()

    if(the_user_date!=None):
        the_date:datetime = \
            str_to_date(the_user_date)

        response:dict = diff_between_dates(
            the_date
        )

        #return response # dict (appears as a JSON response }
        return render_template(
            "date_input.html",
            response_available=True,
            d_days=response['days'],
            d_hours=response['hours']
        )
    #
    else:
        # tested OK - displays the input form
        return render_template(
            "date_input.html"
        )
# def respond_to_distance_request

if __name__=='__main__':
    app.run(
        host="0.0.0.0", # all network interfaces
        port=5000,
        debug=True
    )
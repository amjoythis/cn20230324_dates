# tools.py
from datetime import\
    datetime, timedelta

def str_to_date(
    p_date:str,
    p_format:str="%Y-%m-%d"
):
    d:datetime =\
        datetime.strptime(
            p_date,
            p_format
        )
    return d
# def str_to_date

def diff_between_dates(
    p_d1:datetime,
    p_d2:datetime=None
):
    if(p_d2==None):
        p_d2=datetime.now()
    # if
    diff:timedelta = abs(p_d1-p_d2)
    diff_days:float = diff.days
    diff_seconds:float = diff.total_seconds()
    diff_hours:float = diff_seconds/60/60
    """
    dict_response:dict = dict()
    dict_response['days']=diff_days
    dict_response['hours']=diff_hours
    """
    dict_response:dict = {
        "days":diff_days,
        "hours":diff_hours
    }
    # import json
    # return json.dumps(dict_response)
    return dict_response
# def diff_between_dates
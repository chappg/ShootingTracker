import json
import urllib
import urllib.request
import urllib.error
import datetime
import us_state_abbrev

from calendar import calendar
from datetime import date
from dateutil import parser


def get_current_year() -> str:
    current_year = date.today().year
    return str(current_year)


def get_friendly_day(input_date) -> str:
    curr_date = datetime.datetime.now()
    shooting_date = parser.parse(input_date).replace(tzinfo=None)

    if (curr_date - shooting_date).days == 0:
        return "Today"
    elif (curr_date - shooting_date).days == 1:
        return "Yesterday"
    else:
        return str(calendar.day_name[curr_date.weekday()])


def get_shootings_data() -> str:
    try:
        url = f"https://mass-shooting-tracker-data.s3.us-east-2.amazonaws.com/{get_current_year()}-data.json"
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        # print('HTTPError: {}'.format(e.code))
        print("There were no mass shootings found this year.")
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        print(f'URLError: {e.reason}')
        print("An error occurred while fetching Mass Shooting Tracker data")
    else:
        data = json.loads(response.read())
        print(data)
        return data


def get_recent_speech(data) -> str:
    shooting_date = (data[0]["date"])
    wounded = str(data[0]["wounded"])
    killed = str(data[0]["killed"])
    city = (data[0]["city"])
    state = (data[0]["state"])
    names = (data[0]["names"])
    sources = (data[0]["sources"])

    if (killed != "0" and wounded != "0"):
        return f"{get_friendly_day(shooting_date)}, {killed} people were killed and {wounded}people were wounded in a mass shooting in {city}, {us_state_abbrev.us_state_abbrev[state]}"
    else:
        return (
            f"{get_friendly_day(shooting_date)}, {killed} people were killed in a mass shooting in {city}, {us_state_abbrev.us_state_abbrev[state]}"
            if (killed != "0")
            else f"{get_friendly_day(shooting_date)}, {wounded} people were wounded in a mass shooting in {city}, {us_state_abbrev.us_state_abbrev[state]}"
        )


def get_data_and_return_recent_speech():
    return get_recent_speech(get_shootings_data())

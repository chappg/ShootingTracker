import shootings
import sys
import unittest

sys.path.insert(1, '/')
sys.path.insert(1, '../lambda/')


class test_shootings(unittest.TestCase):
    def test_get_data_and_return_recent_speech(self):
        print(shootings.get_data_and_return_recent_speech())

    def get_recent_speech(self):
        data = shootings.get_shootings_data()
        shooting_date = (data[0]["date"])
        wounded = str(data[0]["wounded"])
        killed = str(data[0]["killed"])
        city = (data[0]["city"])
        state = (data[0]["state"])
        names = (data[0]["names"])
        sources = (data[0]["sources"])

        speech = shootings.get_recent_speech(data)

        print(speech)

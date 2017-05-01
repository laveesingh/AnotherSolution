import requests
import json


def report(username):
    url = "http://codeforces.com/api/user.status?handle=%s" % str(username)
    data = requests.get(url)
    json_data = json.loads(data.text)
    return_dict = {}
    for submission in json_data['result']:
        if return_dict.get(submission['verdict']) is None:
            return_dict[submission['verdict']] = 1
        else:
            return_dict[submission['verdict']] += 1
    return return_dict

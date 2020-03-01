import requests
import json

from src import response_creator


def get_train_statuses():
    statuses = _get_statuses()
    train_statuses = [_create_condensed_status(status) for status in statuses]
    return response_creator.create_response(train_statuses)


def _get_statuses():
    url = "https://api.tfl.gov.uk/line/mode/tube/status"
    response = requests.get(url)
    return json.loads(response.text)


def _get_status_reason(status):
    first_status = status["lineStatuses"][0]
    return first_status["reason"] if "reason" in first_status else ""


def _create_condensed_status(status):
    return {
        "name": status["name"],
        "description": status["lineStatuses"][0]["statusSeverityDescription"],
        "reason": _get_status_reason(status)
    }


print(get_train_statuses())

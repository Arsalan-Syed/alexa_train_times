import requests
import json

url = "https://api.tfl.gov.uk/line/mode/tube/status"
response = requests.get(url)
statuses = json.loads(response.text)


def get_status_reason(status):
    first_status = status["lineStatuses"][0]
    return first_status["reason"] if "reason" in first_status else ""


def create_condensed_status(status):
    return {
        "name": status["name"],
        "description": status["lineStatuses"][0]["statusSeverityDescription"],
        "reason": get_status_reason(status)
    }


def lambda_handler(event, context):
    print([create_condensed_status(status) for status in statuses])

def create_response(train_statuses):
    if _is_good_service_on_all_lines(train_statuses):
        return "Good service on all lines"
    else:
        bad_service_on_all_lines = _create_response_all_lines(train_statuses)
        bad_service_on_favorite_lines = _create_response_favorite_lines(train_statuses)
        return bad_service_on_all_lines + bad_service_on_favorite_lines


def _is_good_service_on_all_lines(train_statuses):
    good_service_statuses = [x for x in train_statuses if x["description"] == "Good Service"]
    return len(good_service_statuses) == len(train_statuses)


def _create_response_all_lines(train_statuses):
    bad_service_statuses = [x for x in train_statuses if x["description"] != "Good Service"]
    return "Bad service on %d lines. " % len(bad_service_statuses)


def _create_response_favorite_lines(train_statuses):
    favorite_lines_disrupted = _favorite_lines_disrupted(train_statuses)
    if len(favorite_lines_disrupted) > 0:
        return "Your journey may be affected on the following lines, " + _to_string(favorite_lines_disrupted)
    else:
        return ""


def _favorite_lines_disrupted(train_statuses):
    favorite_tube_lines = ["Piccadilly", "District", "Circle", "Jubilee"]
    return [x["name"] for x in train_statuses if x["description"] != "Good Service"
            and x["name"] in favorite_tube_lines]


def _to_string(list):
    return ",".join(list)

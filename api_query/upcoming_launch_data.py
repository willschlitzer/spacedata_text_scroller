import requests
import time
import datetime


def get_launch_url():
    """Creates the URL string with the requested number of launches"""
    basic_launch_url = "https://launchlibrary.net/1.4/launch/next/"
    launch_num = 5
    return basic_launch_url + str(launch_num)


def get_launch_json(url):
    """Retrieves the upcoming launch data and returns it as a JSON object"""
    # Create a Boolean object for error handling.
    data_retrieval = False
    error_count = 0
    while not data_retrieval:
        try:
            launch_data = requests.get(url).json()
            data_retrieval = True
        except:
            print("Error querying API, sleeping for 10 seconds")
            error_count += 1
            if error_count > 10:
                raise
            time.sleep(10)

    return launch_data["launches"]


def get_launch_info(launch_json, launch_num=1):
    confirmed_launches = confirm_launch_status(launch_json=launch_json)
    return confirmed_launches[:launch_num]


def confirm_launch_status(launch_json, launch_status=1):
    confirmed_launches = []
    for launch in launch_json:
        if launch["status"] == launch_status:
            launch_info = parse_launch_data(launch)
            confirmed_launches.append(launch_info)
    return confirmed_launches


def parse_launch_data(single_launch):
    launch_dict = {}
    launch_dict["name"] = single_launch["name"]
    launch_dict["date"] = single_launch["windowstart"]
    launch_dict["date_obj"] = datetime.datetime.strptime(
        single_launch["windowstart"], "%B %d, %Y %H:%M:%S %Z"
    )
    return launch_dict


def main():
    upcoming_launch_url = get_launch_url()
    launch_json = get_launch_json(upcoming_launch_url)
    upcoming_launches = get_launch_info(launch_json=launch_json, launch_num=1)
    return upcoming_launches


if __name__ == "__main__":
    main()

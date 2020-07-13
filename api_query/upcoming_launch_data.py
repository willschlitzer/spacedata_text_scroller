import requests
import time


def get_launch_url():
    """Creates the URL string with the requested number of launches"""
    basic_launch_url = "https://launchlibrary.net/1.4/launch/next/"
    launch_num = 1
    return basic_launch_url + str(launch_num)


def get_launch_json(url):
    """Retrieves the upcoming launch data and returns it as a JSON object"""
    # Create a Boolean object for error handling.
    data_retrieval = False
    while not data_retrieval:
        try:
            launch_data = requests.get(url).json()
            data_retrieval = True
        except:
            print("Error querying API, sleeping for 10 seconds")
            time.sleep(10)

    return launch_data["launches"]


def main():
    upcoming_launch_url = get_launch_url()
    launch_json = get_launch_json(upcoming_launch_url)
    print(launch_json)


if __name__ == "__main__":
    main()

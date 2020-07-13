import api_query.upcoming_launch_data as uld
import datetime_parse as dt_parse
import time
import datetime

def main():
    update_time = 1800
    start_time = time.time()
    data_dict = update_data()
    while True:
        if (time.time()-start_time) > update_time:
            data_dict = update_data()
            start_time = time.time()
        display_time_to_launch(launch_data=data_dict['launch'])
        display_launch(launch_data=data_dict['launch'])

def display_time_to_launch(launch_data, display_time = 10):
    display_start = time.time()
    while (time.time() - display_start) < display_time:
        time_to_launch = launch_data['date_obj'] - datetime.datetime.now()
        days, hours, minutes, seconds = dt_parse.timedelta_parser(time_to_launch)
        print(launch_data['name'])
        print("{}D {}H {}M {}S".format(days, hours, minutes, seconds))
        time.sleep(1)


def display_launch(launch_data, display_time=5):
    print(launch_data['name'])
    print(launch_data['date'])
    time.sleep(display_time)



def update_data():
    next_launch = uld.main()[0]
    data_dict = {'launch':next_launch}
    return data_dict

if __name__ == "__main__":
    main()
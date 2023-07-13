from datetime import datetime


def get_timestamp():
    #print(datetime.now()) #2023-06-20 23:29:58.157425 required format(20230620232956)
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    #print(formatted_time)
    return formatted_time
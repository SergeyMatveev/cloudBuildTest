# This Python script generates logs every 10 seconds
import logging
import time


def print_log():
    current_time = int(time.time())
    logging.info(f'Logging. Seconds past from 1st of January 1970 till now: {current_time}')
    print(f'Printing. Seconds past from 1st of January 1970 till now: {current_time}')


if __name__ == '__main__':
    while True:
        print_log()
        time.sleep(10)

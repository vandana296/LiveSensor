from Sensor.exception import SalesException
import sys

from Sensor.logger import logging

def test_exception():
    try:
        logging.info("yha division by Zero wali error ayegi")
        a = 1 / 0  # interntional ZeroDivisionError
    except Exception as e:
        raise SalesException(e, sys)

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)

            
                  
    
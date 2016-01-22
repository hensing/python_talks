#!/usr/bin/python
# coding: utf-8
"""
    module without logging
"""
import logging


logging.basicConfig(level=logging.DEBUG)


def get_divmod(arg1, arg2):
    """
    returns the tuple
    ((arg1 - arg1 % arg2) / arg2, arg1 % arg2)
    """
    logging.info("Berechne divmod von {} und {}".format(
        arg1, arg2))
    logging.debug("arg1: {} arg2: {}".format(
        type(arg1), type(arg2)))
    try:
        res = ((arg1 - arg1 % arg2) / arg2, arg1 % arg2)
        return res
    except ZeroDivisionError:
        logging.warning("Durch Null teilen geht nicht!")
        print(arg1, arg2)
        return "nan"
    except Exception as err:
        logging.error(err.message)

def main():
    """
    calculates divmod from 4 pairs of floats
    """
    logging.info("Starte divmod")
    get_divmod(9, 2)
    get_divmod(3, -2)
    get_divmod(1, 0)
    get_divmod(9, "a")
    logging.info("fertig :)")

if __name__ == '__main__':
    main()

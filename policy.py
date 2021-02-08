#!/usr/bin/env python
""" Postfix policy service, just for demo purposes """
import sys
import logging


LOGPATH = '/tmp/python-policy-service.log'
logging.basicConfig(filename=LOGPATH,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


def dunno():
    """Answer with  to stop restriction processing
    and permit the message
    """
    print("action=dunno\n")


def reject():
    """Answer with dunno to proceed further processing
    of restriction follwed the policy service
    """
    print("action=reject Rejected by python-policy-service \n")


def permit():
    """Answer with permit to stop restriction processing
    and permit the message
    """
    print("action=permit\n")


def read_input():
    """Write input from stdin into buffer until we
    encounter an empty line which signals that postfix
    finished delivering the message
    """
    buff = []
    while True:
        line = sys.stdin.readline().rstrip('\n')
        if line == '':
            break
        buff.append(line)
    return buff


def main():
    """ Main function that wraps things up """
    lines = read_input()
    try:
        # convert key=value pairs into dict
        attributes = dict(line.split('=') for line in lines)

        # example to the the get the sender mail address
        sender = attributes.get('sender', 'missing_sender')

        logging.debug('Sender address: %s', sender)
        logging.debug(attributes)

        # answer postfix with dunno to proceed restrictions
        dunno()
    except ValueError:
        logging.critical("Can't parse attributes: %s", lines)
        dunno()


if __name__ == '__main__':
    main()

'''
BASIC SETUP CODE FOR LOGGING IN PYTHON
BUGGY FACTORIAL PROGRAM

'''

import logging

logging.basicConfig(filename = 'logging_text_file.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(loggin.CRITICAL)


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n+1):
        if not i == n:
            print('{} *'.format(i))
        else:
            print('{} = '.format(i))
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')


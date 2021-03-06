from core.spider import Spider
from core.taskTable import Tasktable
from core.Logger import Logger
from core.util import banner
import optparse

from pprint import pprint

def main():

    banner()


    '''
    command line option parser
    '''

    option_parser = optparse.OptionParser()

    option_parser.usage = \
        """
        search_register.py -e [email] [options]
        search_register.py -c [cellphone] [options]"""

    option_parser.add_option('-e', '--email', dest='email', action='store',default=None)
    option_parser.add_option('-c', '--cellphone', dest='cellphone', action='store',default=None)
    option_parser.add_option('-t', '--thread', dest='thread', action='store', default=1,help="")

    """
    parse options
    """
    (options, args) = option_parser.parse_args()

    """
    new logger object
    """
    logger = Logger(5)

    """
    specific the search type (email or cellphone)
    """
    email = options.email
    cellphone = options.cellphone



    if email:
        task_list = Tasktable('email').tasklist
        target = email
        query_method = "email"
    else:
        if cellphone:
            task_list = Tasktable('cellphone').tasklist
            target = cellphone
            query_method = "cellphone"
        else:
            option_parser.error("must specify email OR cellphone")
            return


    logger.info("search websites registered using "+query_method
                +":"+target)


    spider = Spider(task_list,target,query_method,logger)
    spider.controller()

if __name__ == '__main__':
    main()

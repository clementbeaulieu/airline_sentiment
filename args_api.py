import sys
import argparse
import utils

def parse_args():
    parser = argparse.ArgumentParser(description='')

    # Name of the CSV File
    parser.add_argument('--file-name', default='AirlineSentiment.csv', type=str, help='name of the CSV file')
    parser.add_argument('--root-dir', default='', type=str, help='path of the data dir repository')

    # Keys and Tokens
    parser.add_argument('--consumer-key', default='peUmMnf8QFYkzzDTyrBRXKdIM', type=str, help='Consumer Key')
    parser.add_argument('--consumer-secret', default='O3GpR5WX7wxcr9H21DJn87Yyt8jQEL1UggZsviv5XK31eOqG9H', type=str, help='Consumer Key Secret')
    parser.add_argument('--access-token', default='1443127801855500296-8VVbrkj0auq0bFkLMpP064oiymIGy5', type=str, help='Access Token')
    parser.add_argument('--access-token-secret', default='DOa8uY7sGovxZB92gyFly2d3aytQ6pUqMQODE42ihbCDJ', type=str, help='Access Token Secret')

    # Query
    parser.add_argument('--query', default='americanair', type=str, help='Query')

    # Query Parameters
    parser.add_argument('--count', default=1000, type=int, help='Count')
    parser.add_argument('--page', default=1, type=str, help='Page')
    parser.add_argument('--start', default=None, type=str, help='Starting Date. Accepted values : YYYY-mm-dd. If no value is specified, start date is ending date - time-delta.')
    parser.add_argument('--end', default='today', type=str, help='Ending Date. Accepted values : YYYY-mm-dd or today.')
    parser.add_argument('--time-delta', default=7, type=int, help='Time delta. Accepted values : int (number of days)')

    # Real-Time Parameters
    parser.add_argument('--real-time', default=False, type=bool, help='Real-Time')
    parser.add_argument('--sleep-time', default=20000, type=int, help='Sleep Time')

    args = parser.parse_args()

    # update args
    args.file = '{}/{}'.format(args.root_dir, args.file_name)

    # update dates
    args.end = utils.get_end_date(args)
    args.start = utils.get_start_date(args)
    args.time_delta = utils.get_time_delta(args)

    #assert args.root_dir is not None

    print(' '.join(sys.argv))
    print(args)

    return args
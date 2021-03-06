import os
import sys
import shutil

from args_api import parse_args
from twitter_api import fetch_tweets

def main():
    global args
    if len(sys.argv) > 1:
        args = parse_args()
        print('----- Experiments parameters -----')
        for k, v in args.__dict__.items():
            print(k, ':', v)
    else:
        print('Please provide some parameters for the current experiment. Check-out args.py for more info!')
        sys.exit()

    fetch_tweets(args)

    print(" ***** Processes all done. *****")

if __name__ == '__main__':
    main()
import datetime, time, sys

def get_end_date(args):
    if args.end == 'today':
        return datetime.date.today()
    else:
        try:
            input = args.end
            format = "%Y-%m-%d"
            return datetime.datetime.strptime(input, format).date()
        except ValueError:
            print('Wrong date format. Accepted format : YYYY-mm-dd or today.')
            sys.exit()

def get_start_date(args):
    if args.start is None:
        return args.end-datetime.timedelta(days=args.time_delta)
    else:
        try:
            input = args.start
            format = "%Y-%m-%d"
            return datetime.datetime.strptime(input, format).date()
        except ValueError:
            print('Wrong date format. Accepted format : YYYY-mm-dd.')
            sys.exit()

def get_time_delta(args):
    return (args.end - args.start).days
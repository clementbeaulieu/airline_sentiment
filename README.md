# Sentiment Analysis and Topic Modelling for Airline Companies Management

Business Analytics project - HEC Paris.

This project analyses sentiment from Tweets for airline companies and outputs the explaining topics for negative sentiments.

## Twitter API

Data from tweets were extracted from Twitter using the Tweepy Twitter API. The customed API extracts all the tweets between a start date and an ending date. It saves the text of tweets, their sentiment polarities (value of sentiment using TextBlob) and their sentiment (positive, negative or neutral) in a CSV File of a specified name and location.

### Launching Twitter API

Twitter API can be launched by calling `run_api.py` and a set of input arguments to customize the extraction. You can find the list of available arguments in `args_api.py` and some default values. Note that not all parameters are mandatory for launching and most of them will be assigned their default value if the user does not modify them.

Here is a typical launch command and some comments:

`run_api.py --file-name AirlineSentiment.csv --root-dir /home/data --consumer-key <CONSUMER-KEY> --consumer-secret <CONSUMER-KEY-SECRET> --access-token <ACCESS-TOKEN> --access-token-secret <ACCESS-TOKEN-SECRET> --query @americanair --count 10000 --page 1 --start 2021-10-05 --end 2021-10-10`
  + this command line creates a TwitterClient object able to fetch tweets from Twitter. To communicate with the Twitter API, one should create an account on : https://developer.twitter.com/en/portal/petition/use-case to obtain the following codes: `<CONSUMER-KEY>, <CONSUMER-KEY-SECRET>, <ACCESS-TOKEN> and <ACCESS-TOKEN-SECRET>`.
  + the fetched tweets are the one satisfying the `--query` flag. Here the API will fetch the tweets tagging AmericanAir account, hence the tweets containing the phrase `@americanair` 
  + the fetched tweets are the ones between the dates `--start-date` and `--end-date` in the format `YYYY-mm-dd`. If `--end-date` is not specified, by default it is `today`'s date (which is an acceptable value for this flag).
  + if `--start-date` is not mentionned, the user can use the `--time-delta` in the command-line to specify the number of days preceding the `--end-date` it will fetch tweets. By default `--time-delta`is 7 days.

## Topic Modeling

## Project structure

```bash
.
├── run_api.py # main file for the Twitter API calling all necessary functions
├── twitter_api.py # main function for the Twitter API which fetches tweets and stores the output in a CSV File
├── args_api.py # parsing all command line arguments for Twitter API
```

## Output

## Requirements
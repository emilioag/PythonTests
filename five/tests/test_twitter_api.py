from script.helpers import get_tweets_url


def test_get_tweets_url_no_parameters():
    assert get_tweets_url(api="statuses/user_timeline.json", screen_name="user", **{}) == "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=emil"


def test_get_tweets_url_name_parameter():
    assert get_tweets_url(api="statuses/user_timeline.json", screen_name="user",) == "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=user"


def test_get_tweets_url_parameters():
    assert get_tweets_url(api="statuses/user_timeline.json", screen_name="user", count=2) == "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=user&count=2"

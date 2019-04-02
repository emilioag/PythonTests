import click
import requests
from rethinkdb import RethinkDB
from script.helpers import get_tweets_url, create_pdf
from script.settings import HEADERS, RETHINK_HOST, RETHINK_PORT
import json
import os


@click.group()
def main():
    """Example script."""
    pass


@main.command()
@click.option('--parameter', '-p', help="URL parameters", default=[])
@click.option('--user', '-u', help="Twitter user")
@click.option('--pdf', '-p', help="Output pdf file", default="output.pdf")
def get(user, parameter, pdf):
    url = get_tweets_url(
        api="statuses/user_timeline.json",
        screen_name=user,
        **{p.split("=")[0]: p.split("=")[1] for p in parameter}
    )

    try:
        response = requests.get(url=url, headers=HEADERS)
        tweets = response.json()
    except Exception as e:
        print(e)
        exit(1)

    if response.status_code != 200:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/five_response.json", "r", encoding="latin-1") as f:
            tweets = json.load(f)

    create_pdf(tweets=tweets, out=pdf)

    r = RethinkDB()
    conn = r.connect(host=RETHINK_HOST, port=RETHINK_PORT)

    try:
        r.db_create('twitter').run(conn)
    except Exception as e:
        print(e)

    try:
        r.db('twitter').table_create('tweets').run(conn)
    except Exception as e:
        print(e)

    r.db('twitter').table('tweets').insert(tweets).run(conn)


if __name__ == "__main__":
    main()
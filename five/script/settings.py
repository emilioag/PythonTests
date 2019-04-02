import os

RETHINK_HOST = os.getenv('RETHINK_HOST', 'rethink')
RETHINK_PORT = os.getenv('RETHINK_PORT', 28015)
TWITTER_BEARER = os.getenv('TWITTER_BEARER')
TWITTER_BASE_URL = os.getenv('TWITTER_BASE_URL', "https://api.twitter.com/1.1")
TWITTER_PDF_TEMPLATE = {
    "id": "Tweet ID",
    "created_at": "Created at",
    "text": "Text"
}


HEADERS = {
    'authorization': 'Bearer {}'.format(TWITTER_BEARER),
    'content-type': 'application/json'
}

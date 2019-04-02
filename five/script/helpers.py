from script.settings import TWITTER_BASE_URL, TWITTER_PDF_TEMPLATE
from jinja2 import Template
import pdfkit


def get_tweets_url(api, **parameters):
    return "{base}/{api}{parameters}".format(
        base=TWITTER_BASE_URL,
        api=api,
        parameters="?" + "&".join(["{}={}".format(k, v) for k, v in parameters.items()]) if parameters else ""
    )


def create_pdf(tweets, out):
    tweets_template = []

    for tweet in tweets:
        elem = {}
        for k, v in TWITTER_PDF_TEMPLATE.items():
            elem[v] = tweet.get(k, '')
        tweets_template.append(elem)

    html = Template("""
    <table border="0" align="center" width="80%">
        <thead>
            <tr>
                {% for header in tweets[0].keys() %}
                <th width="{{ width }}%">{{ header }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
        {% for tweet in tweets %}
        <tr>
            {% for value in tweet.values() %}<td width="{{ width }}%">{{ value }}</td>{% endfor %}
        </tr>
        {% endfor %}
        </tbody>
    </table>
    """).render(tweets=tweets_template, width=int(100 / len(tweets_template[0].keys())))

    pdfkit.from_string(html, output_path=out)

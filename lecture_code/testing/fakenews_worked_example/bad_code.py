from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy.sql import exists
from urllib.parse import urlparse


app = Flask(__name__)

@app.route('/scoreURL/<url>')
def scoreURL(url=None):
    #first indicator - whitelist
    # bad code - just to put in a single slide!
    whitelist = {'www.theguardian.com': 1.0, 'www.foxnews.com': 0.1, 'www.theguardian.com': 1.0}
    tldlist = {'.gov': 0.001}
    hostName = urlparse(url).hostname
    whiteListScore = 0
    if hostName in whitelist:
        whiteListScore = whitelist[hostName]
    elif hostName in tldlist:
        whiteListScore = tldlist[hostName]

    #second indicator - keyword scrape
    # blah blah
    # more code for downloading the URL
    # more code for scraping for keywords
    keyWordScore = 0

    #third indicator - look at the URL
    # More code for decomposing the URL
    # set of rules - whatever the logic
    urlScore = 0

    # Now aggregate them
    # Are all indicators weighted evenly?
    # What about if one of them can not render an opinion?
    aggregateScore = whiteListScore + keyWordScore + urlScore

    return jsonify(
            success=True,
            fakeScore=aggregateScore
        )
from flask import Flask
from indicators.indicators import *
from flask import jsonify

app = Flask(__name__)

indicator = IndicatorFactory().makeIndicator()

@app.route('/scoreLink/<url>')
def scoreLink(url: str):
    score = indicator.scoreLink(url)
    return jsonify(
            success=True,
            score = score
        )

if __name__ == "__main__":
    app.run()
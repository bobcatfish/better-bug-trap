import flask
import rates

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    coin = flask.request.args.get("coin_type")
    if coin is None:
        return 'Hello from fancy coin rate service!'
    if coin not in rates.KNOWN_TYPES:
        return 'Coin type {} is unknown'.format(coin)
    r = rates.get_daily_rates(coin)
    return 'Daily rates for {} are {}'.format(coin, r)

MAX = 0
KNOWN_TYPES = ['catcoin', 'dogcoin']


class DogCoinHub(object):
    def get_rates(self, num_days):
        if num_days == MAX:
            return [1.0] * 100
        return [1.0] * num_days


class CatCoinHub(object):
    def get_rates(self, num_days):
        if num_days == MAX:
            return [2.5] * 100
        return [2.5] * num_days


def get_rate_hub(coin):
    if coin == "dogcoin":
        return DogCoinHub()
    return CatCoinHub()


def get_daily_rates(coin, num_days=MAX):
    rate_hub = get_rate_hub(coin)
    rates = rate_hub.get_rates(num_days)
    return rates

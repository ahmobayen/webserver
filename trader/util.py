from requests import get
from json import loads
from django.utils import timezone

from datetime import datetime

from .models import SymbolsInfo


def get_price(ticker):
    request_time = datetime.now(tz=timezone.utc)
    try:
        cached_info = SymbolsInfo.objects.get(symbol=ticker)
        last_request_time = cached_info.last_request_time
        time_delta = request_time.timestamp() - last_request_time.timestamp()
        if abs(time_delta) > 1:
            ticker = loads(get(f'https://api.binance.com/api/v3/ticker/price?symbol={ticker}').text)
            cached_info.price = ticker['price']
            cached_info.last_request_time = request_time
            cached_info.save()
    except SymbolsInfo.DoesNotExist:
        ticker = loads(get(f'https://api.binance.com/api/v3/ticker/price?symbol={ticker}').text)
        cached_info = SymbolsInfo.objects.create(symbol=ticker['symbol'], price=ticker['price'],
                                                 last_request_time=request_time)
        cached_info.save()
    finally:
        return cached_info.serialize()

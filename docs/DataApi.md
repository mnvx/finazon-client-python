# swagger_client.DataApi

All URIs are relative to *https://api.finazon.io/v1.2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_benzinga_dividends_calendar**](DataApi.md#get_benzinga_dividends_calendar) | **GET** /benzinga/dividends_calendar | Dividends calendar
[**get_benzinga_earnings_calendar**](DataApi.md#get_benzinga_earnings_calendar) | **GET** /benzinga/earnings_calendar | Earnings calendar
[**get_benzinga_ipo**](DataApi.md#get_benzinga_ipo) | **GET** /benzinga/ipo | IPO data
[**get_benzinga_news**](DataApi.md#get_benzinga_news) | **GET** /benzinga/news | News articles
[**get_binance_quotes**](DataApi.md#get_binance_quotes) | **GET** /binance/time_series | Time series
[**get_crypto_quotes**](DataApi.md#get_crypto_quotes) | **GET** /crypto/time_series | Time series
[**get_filings**](DataApi.md#get_filings) | **GET** /sec/archive | Filings
[**get_forex_quotes**](DataApi.md#get_forex_quotes) | **GET** /forex/time_series | Time series
[**get_price_binance**](DataApi.md#get_price_binance) | **GET** /binance/price | Price
[**get_price_common**](DataApi.md#get_price_common) | **GET** /price | Price
[**get_price_crypto**](DataApi.md#get_price_crypto) | **GET** /crypto/price | Price
[**get_price_forex**](DataApi.md#get_price_forex) | **GET** /forex/price | Forex price
[**get_price_sip**](DataApi.md#get_price_sip) | **GET** /sip_non_pro/price | Price
[**get_price_sip_0**](DataApi.md#get_price_sip_0) | **GET** /sip_pro/price | Price
[**get_price_us_stocks**](DataApi.md#get_price_us_stocks) | **GET** /us_stocks_essential/price | Price
[**get_quotes**](DataApi.md#get_quotes) | **GET** /time_series | Time series
[**get_sip_trades**](DataApi.md#get_sip_trades) | **GET** /sip/trades | SIP trades
[**get_technical_indicator_atr**](DataApi.md#get_technical_indicator_atr) | **GET** /time_series/atr | ATR Technical indicators
[**get_technical_indicator_b_bands**](DataApi.md#get_technical_indicator_b_bands) | **GET** /time_series/bbands | Overlap Studies
[**get_technical_indicator_ichimoku**](DataApi.md#get_technical_indicator_ichimoku) | **GET** /time_series/ichimoku | Overlap Studies
[**get_technical_indicator_ma**](DataApi.md#get_technical_indicator_ma) | **GET** /time_series/ma | Overlap Studies
[**get_technical_indicator_macd**](DataApi.md#get_technical_indicator_macd) | **GET** /time_series/macd | Momentum Indicators
[**get_technical_indicator_obv**](DataApi.md#get_technical_indicator_obv) | **GET** /time_series/obv | Volume Indicators
[**get_technical_indicator_rsi**](DataApi.md#get_technical_indicator_rsi) | **GET** /time_series/rsi | Momentum Indicators
[**get_technical_indicator_sar**](DataApi.md#get_technical_indicator_sar) | **GET** /time_series/sar | Overlap Studies
[**get_technical_indicator_stoch**](DataApi.md#get_technical_indicator_stoch) | **GET** /time_series/stoch | Momentum Indicators
[**get_ticker_snapshot**](DataApi.md#get_ticker_snapshot) | **GET** /ticker/snapshot | Ticker snapshot
[**get_trades**](DataApi.md#get_trades) | **GET** /trades | Trades

# **get_benzinga_dividends_calendar**
> BenzingaDividendsCalendarResponseBody get_benzinga_dividends_calendar(ticker, _date=_date, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)

Dividends calendar

Returns the dividends calendar from Benzinga.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Filter by ticker symbol
_date = '_date_example' # str | Specifies the exact date to get the data for (optional)
start_at = 789 # int | Filter events by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter events by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 100 # int | Number of items displayed per page in a paginated result (optional) (default to 100)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)

try:
    # Dividends calendar
    api_response = api_instance.get_benzinga_dividends_calendar(ticker, _date=_date, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_benzinga_dividends_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Filter by ticker symbol | 
 **_date** | **str**| Specifies the exact date to get the data for | [optional] 
 **start_at** | **int**| Filter events by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter events by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 100]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 

### Return type

[**BenzingaDividendsCalendarResponseBody**](BenzingaDividendsCalendarResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benzinga_earnings_calendar**
> BenzingaEarningsCalendarResponseBody get_benzinga_earnings_calendar(ticker, _date=_date, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)

Earnings calendar

Returns the earnings calendar from Benzinga.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Filter by ticker symbol
_date = '_date_example' # str | Specifies the exact date to get the data for (optional)
start_at = 789 # int | Filter events by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter events by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 100 # int | Number of items displayed per page in a paginated result (optional) (default to 100)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)

try:
    # Earnings calendar
    api_response = api_instance.get_benzinga_earnings_calendar(ticker, _date=_date, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_benzinga_earnings_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Filter by ticker symbol | 
 **_date** | **str**| Specifies the exact date to get the data for | [optional] 
 **start_at** | **int**| Filter events by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter events by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 100]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 

### Return type

[**BenzingaEarningsCalendarResponseBody**](BenzingaEarningsCalendarResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benzinga_ipo**
> BenzingaIPOResponseBody get_benzinga_ipo(start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, exchange=exchange)

IPO data

Returns IPO data from Benzinga.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
start_at = 789 # int | Filter events by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter events by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 100 # int | Number of items displayed per page in a paginated result (optional) (default to 100)
order = 'asc' # str | Sorting order of the output series (optional) (default to asc)
exchange = 'exchange_example' # str | Exchange where instrument is traded (optional)

try:
    # IPO data
    api_response = api_instance.get_benzinga_ipo(start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, exchange=exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_benzinga_ipo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_at** | **int**| Filter events by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter events by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 100]
 **order** | **str**| Sorting order of the output series | [optional] [default to asc]
 **exchange** | **str**| Exchange where instrument is traded | [optional] 

### Return type

[**BenzingaIPOResponseBody**](BenzingaIPOResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benzinga_news**
> BenzingaNewsResponseBody get_benzinga_news(ticker, _date=_date, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)

News articles

Returns the news articles from Benzinga.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Filter by ticker symbol
_date = '_date_example' # str | Specifies the exact date to get the data for (optional)
start_at = 789 # int | Filter events by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter events by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 100 # int | Number of items displayed per page in a paginated result (optional) (default to 100)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)

try:
    # News articles
    api_response = api_instance.get_benzinga_news(ticker, _date=_date, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_benzinga_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Filter by ticker symbol | 
 **_date** | **str**| Specifies the exact date to get the data for | [optional] 
 **start_at** | **int**| Filter events by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter events by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 100]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 

### Return type

[**BenzingaNewsResponseBody**](BenzingaNewsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_binance_quotes**
> list[QuoteBinanceItem] get_binance_quotes(ticker, interval, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order)

Time series

This endpoint returns a time series of data points for any given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)

try:
    # Time series
    api_response = api_instance.get_binance_quotes(ticker, interval, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_binance_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]

### Return type

[**list[QuoteBinanceItem]**](QuoteBinanceItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_quotes**
> list[QuoteItem] get_crypto_quotes(interval, ticker, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order)

Time series

This endpoint returns a time series of data points for any given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
interval = 'interval_example' # str | Interval between two consecutive points in time series
ticker = 'ticker_example' # str | Filter by ticker symbol
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)

try:
    # Time series
    api_response = api_instance.get_crypto_quotes(interval, ticker, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_crypto_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **str**| Interval between two consecutive points in time series | 
 **ticker** | **str**| Filter by ticker symbol | 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]

### Return type

[**list[QuoteItem]**](QuoteItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filings**
> list[Filing] get_filings(cik_code=cik_code, ticker=ticker, form_type=form_type, filled_from_ts=filled_from_ts, filled_to_ts=filled_to_ts, page=page, page_size=page_size, cqs=cqs, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)

Filings

Real-time and historical access to all forms, filings, and exhibits directly from the SEC's EDGAR system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
cik_code = 789 # int | Filter by Central Index Key (optional)
ticker = 'ticker_example' # str | Filter by ticker (optional)
form_type = 'form_type_example' # str | Filter by form types (optional)
filled_from_ts = 789 # int | Filter by filled time from (optional)
filled_to_ts = 789 # int | Filter by filled time to (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 10 # int | Number of items displayed per page in a paginated result (optional) (default to 10)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)

try:
    # Filings
    api_response = api_instance.get_filings(cik_code=cik_code, ticker=ticker, form_type=form_type, filled_from_ts=filled_from_ts, filled_to_ts=filled_to_ts, page=page, page_size=page_size, cqs=cqs, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_filings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik_code** | **int**| Filter by Central Index Key | [optional] 
 **ticker** | **str**| Filter by ticker | [optional] 
 **form_type** | **str**| Filter by form types | [optional] 
 **filled_from_ts** | **int**| Filter by filled time from | [optional] 
 **filled_to_ts** | **int**| Filter by filled time to | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 10]
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 

### Return type

[**list[Filing]**](Filing.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forex_quotes**
> list[QuoteForexItem] get_forex_quotes(interval, ticker, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order)

Time series

This endpoint returns a time series of data points for any given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
interval = 'interval_example' # str | Interval between two consecutive points in time series
ticker = 'ticker_example' # str | Filter by ticker symbol
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)

try:
    # Time series
    api_response = api_instance.get_forex_quotes(interval, ticker, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_forex_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **str**| Interval between two consecutive points in time series | 
 **ticker** | **str**| Filter by ticker symbol | 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]

### Return type

[**list[QuoteForexItem]**](QuoteForexItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_binance**
> PriceResponseBody get_price_binance(at=at, ticker=ticker)

Price

Returns price value for given binance ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
at = 789 # int | Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at <= at (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # Price
    api_response = api_instance.get_price_binance(at=at, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_price_binance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **int**| Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at &lt;&#x3D; at | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**PriceResponseBody**](PriceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_common**
> PriceResponseBody get_price_common(dataset, at=at, prepost=prepost, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)

Price

Returns price value for given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
at = 789 # int | Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at <= at (optional)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # Price
    api_response = api_instance.get_price_common(dataset, at=at, prepost=prepost, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_price_common: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **at** | **int**| Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at &lt;&#x3D; at | [optional] 
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**PriceResponseBody**](PriceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_crypto**
> PriceResponseBody get_price_crypto(at=at, ticker=ticker)

Price

Returns price value for given crypto ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
at = 789 # int | Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at <= at (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # Price
    api_response = api_instance.get_price_crypto(at=at, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_price_crypto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **int**| Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at &lt;&#x3D; at | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**PriceResponseBody**](PriceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_forex**
> PriceResponseBody get_price_forex(at=at, ticker=ticker)

Forex price

Returns price value for given forex ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
at = 789 # int | Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at <= at (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # Forex price
    api_response = api_instance.get_price_forex(at=at, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_price_forex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **int**| Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at &lt;&#x3D; at | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**PriceResponseBody**](PriceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_sip**
> PriceResponseBody get_price_sip(at=at, prepost=prepost, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)

Price

Returns price value for given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
at = 789 # int | Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at <= at (optional)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # Price
    api_response = api_instance.get_price_sip(at=at, prepost=prepost, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_price_sip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **int**| Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at &lt;&#x3D; at | [optional] 
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**PriceResponseBody**](PriceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_sip_0**
> PriceResponseBody get_price_sip_0(at=at, prepost=prepost, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)

Price

Returns price value for given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
at = 789 # int | Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at <= at (optional)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # Price
    api_response = api_instance.get_price_sip_0(at=at, prepost=prepost, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_price_sip_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **int**| Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at &lt;&#x3D; at | [optional] 
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**PriceResponseBody**](PriceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_us_stocks**
> PriceResponseBody get_price_us_stocks(at=at, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)

Price

Returns price value for given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
at = 789 # int | Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at <= at (optional)
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # Price
    api_response = api_instance.get_price_us_stocks(at=at, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_price_us_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **int**| Filter by start time using a UNIX timestamp. If not specified - last price. Else - last price from 1min interval at the event_at &lt;&#x3D; at | [optional] 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**PriceResponseBody**](PriceResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes**
> list[QuoteItem] get_quotes(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust)

Time series

This endpoint returns a time series of data points for any given ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)

try:
    # Time series
    api_response = api_instance.get_quotes(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]

### Return type

[**list[QuoteItem]**](QuoteItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sip_trades**
> list[SipTradesItem] get_sip_trades(ticker, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, start_at=start_at, end_at=end_at, tape=tape, page=page, page_size=page_size, order=order)

SIP trades

Returns detailed information on trades executed through the Securities Information Processor (SIP).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Filter by ticker symbol
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market center (optional)
start_at = 789 # int | Filter trades by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter trades by end time using a UNIX timestamp (optional)
tape = 'tape_example' # str | Filter by tape (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 10 # int | Number of items displayed per page in a paginated result (optional) (default to 10)
order = 'DESC' # str | Sorting order of the output series (optional) (default to DESC)

try:
    # SIP trades
    api_response = api_instance.get_sip_trades(ticker, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, start_at=start_at, end_at=end_at, tape=tape, page=page, page_size=page_size, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_sip_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Filter by ticker symbol | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market center | [optional] 
 **start_at** | **int**| Filter trades by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter trades by end time using a UNIX timestamp | [optional] 
 **tape** | **str**| Filter by tape | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 10]
 **order** | **str**| Sorting order of the output series | [optional] [default to DESC]

### Return type

[**list[SipTradesItem]**](SipTradesItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_atr**
> list[TechnicalIndicatorResponseAtr] get_technical_indicator_atr(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, time_period=time_period)

ATR Technical indicators

The Average True Range (ATR) is a volatility indicator that measures the average range of price movement over a specified period, helping traders assess market volatility.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
time_period = 14 # int | Number of periods to average over. (optional) (default to 14)

try:
    # ATR Technical indicators
    api_response = api_instance.get_technical_indicator_atr(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_atr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **time_period** | **int**| Number of periods to average over. | [optional] [default to 14]

### Return type

[**list[TechnicalIndicatorResponseAtr]**](TechnicalIndicatorResponseAtr.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_b_bands**
> list[TechnicalIndicatorResponseBBands] get_technical_indicator_b_bands(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, time_period=time_period, sd=sd, ma_type=ma_type)

Overlap Studies

Bollinger Bands (BBANDS) are volatility bands placed above and below a moving average, measuring price volatility and helping traders identify potential overbought or oversold conditions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
series_type = 'close' # str | Specifies the price data type on which technical indicator is calculated (optional) (default to close)
time_period = 20 # int | Number of periods to average over. (optional) (default to 20)
sd = 2.0 # float | Number of standard deviations (optional) (default to 2.0)
ma_type = 'SMA' # str | The type of moving average used, such as SMA or EMA (optional) (default to SMA)

try:
    # Overlap Studies
    api_response = api_instance.get_technical_indicator_b_bands(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, time_period=time_period, sd=sd, ma_type=ma_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_b_bands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **series_type** | **str**| Specifies the price data type on which technical indicator is calculated | [optional] [default to close]
 **time_period** | **int**| Number of periods to average over. | [optional] [default to 20]
 **sd** | **float**| Number of standard deviations | [optional] [default to 2.0]
 **ma_type** | **str**| The type of moving average used, such as SMA or EMA | [optional] [default to SMA]

### Return type

[**list[TechnicalIndicatorResponseBBands]**](TechnicalIndicatorResponseBBands.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_ichimoku**
> list[TechnicalIndicatorResponseIchimoku] get_technical_indicator_ichimoku(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, conversion_line_period=conversion_line_period, base_line_period=base_line_period, leading_span_b_period=leading_span_b_period, lagging_span_period=lagging_span_period, include_ahead_span_period=include_ahead_span_period)

Overlap Studies

The Ichimoku Cloud (ICHIMOKU) is a comprehensive trend-following indicator that combines multiple moving averages and support/resistance levels to help traders identify potential entry and exit points, trend direction, and momentum.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
conversion_line_period = 9 # int | The time period used for generating the conversation line (optional) (default to 9)
base_line_period = 26 # int | The time period used for generating the base line (optional) (default to 26)
leading_span_b_period = 52 # int | The time period used for generating the leading span B line (optional) (default to 52)
lagging_span_period = 26 # int | The time period used for generating the lagging span line (optional) (default to 26)
include_ahead_span_period = true # bool | Indicates whether to include ahead span period (optional) (default to true)

try:
    # Overlap Studies
    api_response = api_instance.get_technical_indicator_ichimoku(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, conversion_line_period=conversion_line_period, base_line_period=base_line_period, leading_span_b_period=leading_span_b_period, lagging_span_period=lagging_span_period, include_ahead_span_period=include_ahead_span_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_ichimoku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **conversion_line_period** | **int**| The time period used for generating the conversation line | [optional] [default to 9]
 **base_line_period** | **int**| The time period used for generating the base line | [optional] [default to 26]
 **leading_span_b_period** | **int**| The time period used for generating the leading span B line | [optional] [default to 52]
 **lagging_span_period** | **int**| The time period used for generating the lagging span line | [optional] [default to 26]
 **include_ahead_span_period** | **bool**| Indicates whether to include ahead span period | [optional] [default to true]

### Return type

[**list[TechnicalIndicatorResponseIchimoku]**](TechnicalIndicatorResponseIchimoku.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_ma**
> list[TechnicalIndicatorResponseMa] get_technical_indicator_ma(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, time_period=time_period, ma_type=ma_type)

Overlap Studies

The Moving Average (MA) is a smoothing indicator that calculates the average price of a security over a specified period, helping traders identify trends and potential support or resistance levels.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
series_type = 'close' # str | Specifies the price data type on which technical indicator is calculated (optional) (default to close)
time_period = 9 # int | Number of periods to average over. (optional) (default to 9)
ma_type = 'SMA' # str | The type of moving average used, such as SMA or EMA (optional) (default to SMA)

try:
    # Overlap Studies
    api_response = api_instance.get_technical_indicator_ma(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, time_period=time_period, ma_type=ma_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_ma: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **series_type** | **str**| Specifies the price data type on which technical indicator is calculated | [optional] [default to close]
 **time_period** | **int**| Number of periods to average over. | [optional] [default to 9]
 **ma_type** | **str**| The type of moving average used, such as SMA or EMA | [optional] [default to SMA]

### Return type

[**list[TechnicalIndicatorResponseMa]**](TechnicalIndicatorResponseMa.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_macd**
> list[TechnicalIndicatorResponseMacd] get_technical_indicator_macd(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, fast_period=fast_period, slow_period=slow_period, signal_period=signal_period)

Momentum Indicators

The Moving Average Convergence Divergence (MACD) is a momentum indicator that measures the difference between two moving averages, with a signal line used to identify potential trend reversals and trading opportunities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
series_type = 'close' # str | Specifies the price data type on which technical indicator is calculated (optional) (default to close)
fast_period = 12 # int | Number of periods for fast moving average (optional) (default to 12)
slow_period = 26 # int | Number of periods for slow moving average (optional) (default to 26)
signal_period = 9 # int | The time period used for generating the signal line (optional) (default to 9)

try:
    # Momentum Indicators
    api_response = api_instance.get_technical_indicator_macd(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, fast_period=fast_period, slow_period=slow_period, signal_period=signal_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_macd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **series_type** | **str**| Specifies the price data type on which technical indicator is calculated | [optional] [default to close]
 **fast_period** | **int**| Number of periods for fast moving average | [optional] [default to 12]
 **slow_period** | **int**| Number of periods for slow moving average | [optional] [default to 26]
 **signal_period** | **int**| The time period used for generating the signal line | [optional] [default to 9]

### Return type

[**list[TechnicalIndicatorResponseMacd]**](TechnicalIndicatorResponseMacd.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_obv**
> list[TechnicalIndicatorResponseObv] get_technical_indicator_obv(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type)

Volume Indicators

The On Balance Volume (OBV) indicator is a cumulative volume-based tool used to measure buying and selling pressure, helping traders identify potential price trends and reversals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
series_type = 'close' # str | Specifies the price data type on which technical indicator is calculated (optional) (default to close)

try:
    # Volume Indicators
    api_response = api_instance.get_technical_indicator_obv(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_obv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **series_type** | **str**| Specifies the price data type on which technical indicator is calculated | [optional] [default to close]

### Return type

[**list[TechnicalIndicatorResponseObv]**](TechnicalIndicatorResponseObv.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_rsi**
> list[TechnicalIndicatorResponseRsi] get_technical_indicator_rsi(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, time_period=time_period)

Momentum Indicators

The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements, helping traders identify potential overbought or oversold conditions and trend reversals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
series_type = 'close' # str | Specifies the price data type on which technical indicator is calculated (optional) (default to close)
time_period = 14 # int | Number of periods to average over (optional) (default to 14)

try:
    # Momentum Indicators
    api_response = api_instance.get_technical_indicator_rsi(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, series_type=series_type, time_period=time_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_rsi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **series_type** | **str**| Specifies the price data type on which technical indicator is calculated | [optional] [default to close]
 **time_period** | **int**| Number of periods to average over | [optional] [default to 14]

### Return type

[**list[TechnicalIndicatorResponseRsi]**](TechnicalIndicatorResponseRsi.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_sar**
> list[TechnicalIndicatorResponseSar] get_technical_indicator_sar(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, acceleration=acceleration, maximum=maximum)

Overlap Studies

The Parabolic SAR (SAR) is a trend-following indicator that calculates potential support and resistance levels based on a security's price and time, helping traders identify potential entry and exit points.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
acceleration = 0.02 # float | Initial acceleration factor (optional) (default to 0.02)
maximum = 0.2 # float | Maximum value for the acceleration factor (optional) (default to 0.2)

try:
    # Overlap Studies
    api_response = api_instance.get_technical_indicator_sar(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, acceleration=acceleration, maximum=maximum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_sar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **acceleration** | **float**| Initial acceleration factor | [optional] [default to 0.02]
 **maximum** | **float**| Maximum value for the acceleration factor | [optional] [default to 0.2]

### Return type

[**list[TechnicalIndicatorResponseSar]**](TechnicalIndicatorResponseSar.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_indicator_stoch**
> list[TechnicalIndicatorResponseStoch] get_technical_indicator_stoch(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, fast_k_period=fast_k_period, slow_k_period=slow_k_period, slow_d_period=slow_d_period, slow_kma_type=slow_kma_type, slow_dma_type=slow_dma_type)

Momentum Indicators

The Stochastic Oscillator (STOCH) is a momentum indicator that compares a security's closing price to its price range over a specified period, helping traders identify potential overbought or oversold conditions and trend reversals.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
interval = 'interval_example' # str | Interval between two consecutive points in time series
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter output by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter output by end time using a UNIX timestamp (optional)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 30 # int | Number of items displayed per page in a paginated result (optional) (default to 30)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
prepost = false # bool | Indicates whether data should be included for extended hours of trading (optional) (default to false)
adjust = 'all' # str | Apply adjusting for data (all, splits, dividends, none) (optional) (default to all)
fast_k_period = 14 # int | The time period for the fast %K line in the Stochastic Oscillator (optional) (default to 14)
slow_k_period = 1 # int | The time period for the slow %K line in the Stochastic Oscillator (optional) (default to 1)
slow_d_period = 3 # int | The time period for the slow %D line in the Stochastic Oscillator (optional) (default to 3)
slow_kma_type = 'SMA' # str | The type of slow %K Moving Average used (optional) (default to SMA)
slow_dma_type = 'SMA' # str | The type of slow Displaced Moving Average used (optional) (default to SMA)

try:
    # Momentum Indicators
    api_response = api_instance.get_technical_indicator_stoch(dataset, ticker, interval, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country, start_at=start_at, end_at=end_at, page=page, page_size=page_size, order=order, prepost=prepost, adjust=adjust, fast_k_period=fast_k_period, slow_k_period=slow_k_period, slow_d_period=slow_d_period, slow_kma_type=slow_kma_type, slow_dma_type=slow_dma_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_technical_indicator_stoch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **interval** | **str**| Interval between two consecutive points in time series | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter output by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter output by end time using a UNIX timestamp | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 30]
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **prepost** | **bool**| Indicates whether data should be included for extended hours of trading | [optional] [default to false]
 **adjust** | **str**| Apply adjusting for data (all, splits, dividends, none) | [optional] [default to all]
 **fast_k_period** | **int**| The time period for the fast %K line in the Stochastic Oscillator | [optional] [default to 14]
 **slow_k_period** | **int**| The time period for the slow %K line in the Stochastic Oscillator | [optional] [default to 1]
 **slow_d_period** | **int**| The time period for the slow %D line in the Stochastic Oscillator | [optional] [default to 3]
 **slow_kma_type** | **str**| The type of slow %K Moving Average used | [optional] [default to SMA]
 **slow_dma_type** | **str**| The type of slow Displaced Moving Average used | [optional] [default to SMA]

### Return type

[**list[TechnicalIndicatorResponseStoch]**](TechnicalIndicatorResponseStoch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticker_snapshot**
> InlineResponse200 get_ticker_snapshot(dataset, ticker, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country)

Ticker snapshot

This endpoint returns a combination of different data points, such as daily performance, last quote, last trade, minute data, and previous day performance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
market = 'market_example' # str | Filter by market (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)

try:
    # Ticker snapshot
    api_response = api_instance.get_ticker_snapshot(dataset, ticker, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, market=market, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_ticker_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **market** | **str**| Filter by market | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trades**
> list[TradesItem] get_trades(dataset, ticker, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, country=country, start_at=start_at, end_at=end_at, order=order, page=page, page_size=page_size)

Trades

Returns general information on executed trades.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code
ticker = 'ticker_example' # str | Filter by ticker symbol
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
start_at = 789 # int | Filter trades by start time using a UNIX timestamp (optional)
end_at = 789 # int | Filter trades by end time using a UNIX timestamp (optional)
order = 'desc' # str | Sorting order of the output series (optional) (default to desc)
page = 0 # int | Specific page of a paginated result to be displayed (optional) (default to 0)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # Trades
    api_response = api_instance.get_trades(dataset, ticker, cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, country=country, start_at=start_at, end_at=end_at, order=order, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->get_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | 
 **ticker** | **str**| Filter by ticker symbol | 
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **start_at** | **int**| Filter trades by start time using a UNIX timestamp | [optional] 
 **end_at** | **int**| Filter trades by end time using a UNIX timestamp | [optional] 
 **order** | **str**| Sorting order of the output series | [optional] [default to desc]
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] [default to 0]
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**list[TradesItem]**](TradesItem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


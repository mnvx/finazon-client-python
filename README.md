# swagger-client
## API reference  Finazon is a comprehensive financial data marketplace that enables developers to effortlessly integrate a wide variety of global datasets, including stocks, ETFs, cryptocurrencies, and more, all with fully customizable parameters.  The Finazon API is built around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles, featuring resource-oriented URLs with predictable behavior. The API accepts [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms) request bodies, returns JSON-encoded responses, and utilizes standard HTTP response codes, authentication methods, and verbs.  The Finazon API doesn't support bulk updates. You can work on only one instrument per request.  ## Authentification  To authenticate requests, the Finazon API requires [API keys](https://finazon.io/account/developers/api-keys). You can obtain, view, and manage your API keys through the [Finazon Dashboard](https://finazon.io/account/home).  Your API keys hold significant privileges, so ensure their security by not sharing your secret API keys in publicly accessible areas, such as GitHub repositories, client-side code, or any other public platforms.  All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls over plain HTTP will fail, as will API requests without authentication.  Once you have your API key, include it in the parameters as follows:  ```bash https://api.finazon.io/latest?apikey=YOUR_API_KEY ```  Alternatively, pass it as a request header:  ```bash Authorization: apikey YOUR_API_KEY ```  ## Versioning  Whenever [backwards-incompatible](https://support.finazon.io/en/articles/7792859-api-upgrades#h_1e014217bf) changes are introduced to the API, a new dated version is released. Consult our [API upgrades guide](https://support.finazon.io/en/articles/7792859-api-upgrades) for more information on backwards compatibility, and view our API changelog for all API updates.  To always use the most up-to-date version, specify it as `/latest`:  ```bash https://api.finazon.io/latest ```  To access the most recent version of `v1.*`, use the following:  ```bash https://api.finazon.io/v1  ```  Or, to retrieve a specific version, call:  ```bash  https://api.finazon.io/v1.0 ```  Finazon will provide advance notice before deprecating older API versions, giving developers ample time to migrate to the updated version.  ## Endpoints structure  The Finazon API adheres to a consistent and structured pattern for its endpoints. The base URL for all requests is:  ```bash https://api.finazon.io/ ```  API endpoints are organized by resource types, including universal resources accessible across all publishers and publisher-specific resources. For example, the `/time_series` endpoint is compatible with all publishers that support this data format. Such responses will be standardized across all datasets, facilitating rapid integration of new markets into your applications.  ```bash https://api.finazon.io/latest/{{resource}} https://api.finazon.io/latest/time_series ```  Additionally, datasets may contain unique data exclusive to that dataset. In such cases, you might want to call a separate endpoint specifying the publisher to gather more data. For instance, the [Binance](https://finazon.io/dataset/binance) dataset time series can be requested as:  ```bash  https://api.finazon.io/latest/{{publisher}}/{{resource}} https://api.finazon.io/latest/binance/time_series ```  ## Parameters  Each API request has its own set of required and optional parameters. Parameters should be separated by an ampersand. Parameter names are case-sensitive, while parameter values are not. Each API request has its own set of required and optional parameters. Parameters should be separated by an ampersand. Parameter names and parameter values are case-sensitive  ```bash https://api.finazon.io/latest/time_series?dataset=sip_non_pro&ticker=AAPL&interval=1m&apikey= ```  ### Pagination  All API resources supporting bulk fetches are retrieved via \"list\" API methods. For example, you can list time series, list trades, and list quotes. These list API methods share a common structure, accepting at least these five parameters: `page`, `page_size`, `order`, `start_at`, and `end_at`.  The response of a list API method represents a single page in a reverse chronological stream of objects. If you do not specify `start_at` or `end_at`, you will receive the first page of this list, containing the newest objects. By default, you will receive 10 objects if you do not specify an alternative value for `page_size`. You can specify `start_at` equal to the T (timestamp) value of an item to retrieve the page of older objects occurring immediately after the specified timestamp in the reverse chronological stream. Similarly, you can specify `end_at` to receive a page of newer objects occurring immediately before the named object in the stream. You can use one of `start_at` or `end_at` or both. Objects in a page always appear in reverse chronological order, unless `order` is specified.  ## Errors  Finazon employs standard HTTP response codes to signify the success or failure of an API request. Generally, the response codes can be interpreted as follows:  `2xx` range codes indicate a successful request.  `4xx` range codes signify an error resulting from the provided information (e.g., invalid API key, API rate limit exceeded, etc.).  `5xx` range codes represent errors originating from Finazon's servers (these are rare occurrences).  For all `4xx`errors that can be addressed programmatically (e.g., endpoint not found), an error message is included to succinctly explain the reported issue. This allows developers to quickly identify and resolve errors in their API requests.   status | code | message | --------|:-----|:--------|  400 |  INVALID_PARAMETER | The **{parameter_name}** parameter is missing or invalid. |  400 |  INVALID_DATE_RANGE | The requested date range is invalid or unsupported. |  400 |  UNSUPPORTED_MARKET | The requested market or exchange is not supported by the API. Please check the supported markets and try again. |  400 |  INVALID_TICKER | The provided ticker is invalid or unsupported. |  401 |  UNAUTHORIZED_ACCESS | You are not authorized to access the requested endpoint or you have insufficient permissions. |  404 |  ENDPOINT_NOT_FOUND | The requested endpoint **{endpoint_name}** does not exist or could not be found. |  429 |  API_RATE_LIMIT_EXCEEDED | You have exceeded the allowed number of API calls within the minute. Please wait and try again later. |  401 |  INVALID_API_KEY | The provided API key is invalid or has expired. Please check your API key and try again |  408 |  REQUEST_TIMEOUT | The request took too long to complete and timed out. Please try again later or reduce the complexity of your query. |  503 |  DATA_UNAVAILABLE | The requested data is temporarily unavailable or not supported. Please try again later or check the availability of the data. |  500 |  INTERNAL_SERVER_ERROR | An error occurred on the server-side while processing the request. Please try again later. If the issue persists, contact support. |

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.2
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.finazon.io/v1.2/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataApi* | [**get_benzinga_dividends_calendar**](docs/DataApi.md#get_benzinga_dividends_calendar) | **GET** /benzinga/dividends_calendar | Dividends calendar
*DataApi* | [**get_benzinga_earnings_calendar**](docs/DataApi.md#get_benzinga_earnings_calendar) | **GET** /benzinga/earnings_calendar | Earnings calendar
*DataApi* | [**get_benzinga_ipo**](docs/DataApi.md#get_benzinga_ipo) | **GET** /benzinga/ipo | IPO data
*DataApi* | [**get_benzinga_news**](docs/DataApi.md#get_benzinga_news) | **GET** /benzinga/news | News articles
*DataApi* | [**get_binance_quotes**](docs/DataApi.md#get_binance_quotes) | **GET** /binance/time_series | Time series
*DataApi* | [**get_crypto_quotes**](docs/DataApi.md#get_crypto_quotes) | **GET** /crypto/time_series | Time series
*DataApi* | [**get_filings**](docs/DataApi.md#get_filings) | **GET** /sec/archive | Filings
*DataApi* | [**get_forex_quotes**](docs/DataApi.md#get_forex_quotes) | **GET** /forex/time_series | Time series
*DataApi* | [**get_price_binance**](docs/DataApi.md#get_price_binance) | **GET** /binance/price | Price
*DataApi* | [**get_price_common**](docs/DataApi.md#get_price_common) | **GET** /price | Price
*DataApi* | [**get_price_crypto**](docs/DataApi.md#get_price_crypto) | **GET** /crypto/price | Price
*DataApi* | [**get_price_forex**](docs/DataApi.md#get_price_forex) | **GET** /forex/price | Forex price
*DataApi* | [**get_price_sip**](docs/DataApi.md#get_price_sip) | **GET** /sip_non_pro/price | Price
*DataApi* | [**get_price_sip_0**](docs/DataApi.md#get_price_sip_0) | **GET** /sip_pro/price | Price
*DataApi* | [**get_price_us_stocks**](docs/DataApi.md#get_price_us_stocks) | **GET** /us_stocks_essential/price | Price
*DataApi* | [**get_quotes**](docs/DataApi.md#get_quotes) | **GET** /time_series | Time series
*DataApi* | [**get_sip_trades**](docs/DataApi.md#get_sip_trades) | **GET** /sip/trades | SIP trades
*DataApi* | [**get_technical_indicator_atr**](docs/DataApi.md#get_technical_indicator_atr) | **GET** /time_series/atr | ATR Technical indicators
*DataApi* | [**get_technical_indicator_b_bands**](docs/DataApi.md#get_technical_indicator_b_bands) | **GET** /time_series/bbands | Overlap Studies
*DataApi* | [**get_technical_indicator_ichimoku**](docs/DataApi.md#get_technical_indicator_ichimoku) | **GET** /time_series/ichimoku | Overlap Studies
*DataApi* | [**get_technical_indicator_ma**](docs/DataApi.md#get_technical_indicator_ma) | **GET** /time_series/ma | Overlap Studies
*DataApi* | [**get_technical_indicator_macd**](docs/DataApi.md#get_technical_indicator_macd) | **GET** /time_series/macd | Momentum Indicators
*DataApi* | [**get_technical_indicator_obv**](docs/DataApi.md#get_technical_indicator_obv) | **GET** /time_series/obv | Volume Indicators
*DataApi* | [**get_technical_indicator_rsi**](docs/DataApi.md#get_technical_indicator_rsi) | **GET** /time_series/rsi | Momentum Indicators
*DataApi* | [**get_technical_indicator_sar**](docs/DataApi.md#get_technical_indicator_sar) | **GET** /time_series/sar | Overlap Studies
*DataApi* | [**get_technical_indicator_stoch**](docs/DataApi.md#get_technical_indicator_stoch) | **GET** /time_series/stoch | Momentum Indicators
*DataApi* | [**get_ticker_snapshot**](docs/DataApi.md#get_ticker_snapshot) | **GET** /ticker/snapshot | Ticker snapshot
*DataApi* | [**get_trades**](docs/DataApi.md#get_trades) | **GET** /trades | Trades
*ReferenceApi* | [**get_api_usage**](docs/ReferenceApi.md#get_api_usage) | **GET** /api_usage | Api usage
*ReferenceApi* | [**get_datasets**](docs/ReferenceApi.md#get_datasets) | **GET** /datasets | List of Finazon datasets
*ReferenceApi* | [**get_exchanges_crypto**](docs/ReferenceApi.md#get_exchanges_crypto) | **GET** /markets/crypto | List of crypto markets
*ReferenceApi* | [**get_exchanges_stocks**](docs/ReferenceApi.md#get_exchanges_stocks) | **GET** /markets/stocks | List of stock markets
*ReferenceApi* | [**get_market_center**](docs/ReferenceApi.md#get_market_center) | **GET** /sip/market_center | List of market centers
*ReferenceApi* | [**get_publishers**](docs/ReferenceApi.md#get_publishers) | **GET** /publishers | List of Finazon publishers
*ReferenceApi* | [**get_symbols_crypto**](docs/ReferenceApi.md#get_symbols_crypto) | **GET** /tickers/crypto | List of crypto pairs
*ReferenceApi* | [**get_symbols_forex**](docs/ReferenceApi.md#get_symbols_forex) | **GET** /tickers/forex | List of forex ticker symbols
*ReferenceApi* | [**get_symbols_stocks**](docs/ReferenceApi.md#get_symbols_stocks) | **GET** /tickers/stocks | List of stock ticker symbols
*ReferenceApi* | [**get_symbols_us_stocks**](docs/ReferenceApi.md#get_symbols_us_stocks) | **GET** /tickers/us_stocks | List of US stock ticker symbols
*DefaultApi* | [**reference**](docs/DefaultApi.md#reference) | **GET** /my_datasets | My Datasets
*TechnicalIndicatorApi* | [**get_technical_indicator_atr**](docs/TechnicalIndicatorApi.md#get_technical_indicator_atr) | **GET** /time_series/atr | ATR Technical indicators
*TechnicalIndicatorApi* | [**get_technical_indicator_b_bands**](docs/TechnicalIndicatorApi.md#get_technical_indicator_b_bands) | **GET** /time_series/bbands | Overlap Studies
*TechnicalIndicatorApi* | [**get_technical_indicator_ichimoku**](docs/TechnicalIndicatorApi.md#get_technical_indicator_ichimoku) | **GET** /time_series/ichimoku | Overlap Studies
*TechnicalIndicatorApi* | [**get_technical_indicator_ma**](docs/TechnicalIndicatorApi.md#get_technical_indicator_ma) | **GET** /time_series/ma | Overlap Studies
*TechnicalIndicatorApi* | [**get_technical_indicator_macd**](docs/TechnicalIndicatorApi.md#get_technical_indicator_macd) | **GET** /time_series/macd | Momentum Indicators
*TechnicalIndicatorApi* | [**get_technical_indicator_obv**](docs/TechnicalIndicatorApi.md#get_technical_indicator_obv) | **GET** /time_series/obv | Volume Indicators
*TechnicalIndicatorApi* | [**get_technical_indicator_rsi**](docs/TechnicalIndicatorApi.md#get_technical_indicator_rsi) | **GET** /time_series/rsi | Momentum Indicators
*TechnicalIndicatorApi* | [**get_technical_indicator_sar**](docs/TechnicalIndicatorApi.md#get_technical_indicator_sar) | **GET** /time_series/sar | Overlap Studies
*TechnicalIndicatorApi* | [**get_technical_indicator_stoch**](docs/TechnicalIndicatorApi.md#get_technical_indicator_stoch) | **GET** /time_series/stoch | Momentum Indicators

## Documentation For Models

 - [ApiCalls](docs/ApiCalls.md)
 - [ApiUsageItem](docs/ApiUsageItem.md)
 - [ApiUsageResponseBody](docs/ApiUsageResponseBody.md)
 - [BaseResponseBody](docs/BaseResponseBody.md)
 - [BenzingaDividendsCalendarResponseBody](docs/BenzingaDividendsCalendarResponseBody.md)
 - [BenzingaEarningsCalendarResponseBody](docs/BenzingaEarningsCalendarResponseBody.md)
 - [BenzingaIPOResponseBody](docs/BenzingaIPOResponseBody.md)
 - [BenzingaNewsResponseBody](docs/BenzingaNewsResponseBody.md)
 - [DatasetDetailItem](docs/DatasetDetailItem.md)
 - [DatasetItem](docs/DatasetItem.md)
 - [DatasetsResponseBody](docs/DatasetsResponseBody.md)
 - [DividendsCalendarItem](docs/DividendsCalendarItem.md)
 - [EarningsCalendarItem](docs/EarningsCalendarItem.md)
 - [EarningsCalendarItemEps](docs/EarningsCalendarItemEps.md)
 - [EarningsCalendarItemRevenue](docs/EarningsCalendarItemRevenue.md)
 - [ExchangeCryptoItem](docs/ExchangeCryptoItem.md)
 - [ExchangeStocksItem](docs/ExchangeStocksItem.md)
 - [ExchangesCryptoResponseBody](docs/ExchangesCryptoResponseBody.md)
 - [ExchangesStocksResponseBody](docs/ExchangesStocksResponseBody.md)
 - [Filing](docs/Filing.md)
 - [FilingFile](docs/FilingFile.md)
 - [IPOItem](docs/IPOItem.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [MarketCenterItem](docs/MarketCenterItem.md)
 - [MarketCenterResponseBody](docs/MarketCenterResponseBody.md)
 - [Meta](docs/Meta.md)
 - [MyDatasetItem](docs/MyDatasetItem.md)
 - [NewsItem](docs/NewsItem.md)
 - [PaginationMeta](docs/PaginationMeta.md)
 - [PriceResponseBody](docs/PriceResponseBody.md)
 - [PublisherItem](docs/PublisherItem.md)
 - [PublishersResponseBody](docs/PublishersResponseBody.md)
 - [QuoteBinanceItem](docs/QuoteBinanceItem.md)
 - [QuoteForexItem](docs/QuoteForexItem.md)
 - [QuoteItem](docs/QuoteItem.md)
 - [SipTradesItem](docs/SipTradesItem.md)
 - [SymbolCrypto](docs/SymbolCrypto.md)
 - [SymbolForex](docs/SymbolForex.md)
 - [SymbolStocks](docs/SymbolStocks.md)
 - [SymbolUSStocks](docs/SymbolUSStocks.md)
 - [SymbolsCryptoResponseBody](docs/SymbolsCryptoResponseBody.md)
 - [SymbolsForexResponseBody](docs/SymbolsForexResponseBody.md)
 - [SymbolsStocksResponseBody](docs/SymbolsStocksResponseBody.md)
 - [SymbolsUSStocksResponseBody](docs/SymbolsUSStocksResponseBody.md)
 - [TechnicalIndicatorResponseAtr](docs/TechnicalIndicatorResponseAtr.md)
 - [TechnicalIndicatorResponseBBands](docs/TechnicalIndicatorResponseBBands.md)
 - [TechnicalIndicatorResponseData](docs/TechnicalIndicatorResponseData.md)
 - [TechnicalIndicatorResponseIchimoku](docs/TechnicalIndicatorResponseIchimoku.md)
 - [TechnicalIndicatorResponseMa](docs/TechnicalIndicatorResponseMa.md)
 - [TechnicalIndicatorResponseMacd](docs/TechnicalIndicatorResponseMacd.md)
 - [TechnicalIndicatorResponseObv](docs/TechnicalIndicatorResponseObv.md)
 - [TechnicalIndicatorResponseRsi](docs/TechnicalIndicatorResponseRsi.md)
 - [TechnicalIndicatorResponseSar](docs/TechnicalIndicatorResponseSar.md)
 - [TechnicalIndicatorResponseStoch](docs/TechnicalIndicatorResponseStoch.md)
 - [TickerSnapshotChange](docs/TickerSnapshotChange.md)
 - [TickerSnapshotLastDay](docs/TickerSnapshotLastDay.md)
 - [TickerSnapshotLastFiftyTwoWeek](docs/TickerSnapshotLastFiftyTwoWeek.md)
 - [TickerSnapshotLastMonth](docs/TickerSnapshotLastMonth.md)
 - [TickerSnapshotLastTrade](docs/TickerSnapshotLastTrade.md)
 - [TickerSnapshotPreviousDay](docs/TickerSnapshotPreviousDay.md)
 - [TradesItem](docs/TradesItem.md)

## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author



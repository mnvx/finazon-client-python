# swagger_client.ReferenceApi

All URIs are relative to *https://api.finazon.io/v1.2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_usage**](ReferenceApi.md#get_api_usage) | **GET** /api_usage | Api usage
[**get_datasets**](ReferenceApi.md#get_datasets) | **GET** /datasets | List of Finazon datasets
[**get_exchanges_crypto**](ReferenceApi.md#get_exchanges_crypto) | **GET** /markets/crypto | List of crypto markets
[**get_exchanges_stocks**](ReferenceApi.md#get_exchanges_stocks) | **GET** /markets/stocks | List of stock markets
[**get_market_center**](ReferenceApi.md#get_market_center) | **GET** /sip/market_center | List of market centers
[**get_publishers**](ReferenceApi.md#get_publishers) | **GET** /publishers | List of Finazon publishers
[**get_symbols_crypto**](ReferenceApi.md#get_symbols_crypto) | **GET** /tickers/crypto | List of crypto pairs
[**get_symbols_forex**](ReferenceApi.md#get_symbols_forex) | **GET** /tickers/forex | List of forex ticker symbols
[**get_symbols_stocks**](ReferenceApi.md#get_symbols_stocks) | **GET** /tickers/stocks | List of stock ticker symbols
[**get_symbols_us_stocks**](ReferenceApi.md#get_symbols_us_stocks) | **GET** /tickers/us_stocks | List of US stock ticker symbols

# **get_api_usage**
> ApiUsageResponseBody get_api_usage(product=product)

Api usage

Returns a list of datasets with available API calls and limits.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
product = 'product_example' # str | Product code (optional)

try:
    # Api usage
    api_response = api_instance.get_api_usage(product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_api_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| Product code | [optional] 

### Return type

[**ApiUsageResponseBody**](ApiUsageResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> DatasetsResponseBody get_datasets(code=code, page=page, page_size=page_size)

List of Finazon datasets

Returns a list of all datasets available at Finazon.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Filter by Finazon's dataset code (optional)
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # List of Finazon datasets
    api_response = api_instance.get_datasets(code=code, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Filter by Finazon&#x27;s dataset code | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**DatasetsResponseBody**](DatasetsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchanges_crypto**
> ExchangesCryptoResponseBody get_exchanges_crypto(page=page, page_size=page_size)

List of crypto markets

Returns a list of supported crypto markets.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # List of crypto markets
    api_response = api_instance.get_exchanges_crypto(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_exchanges_crypto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**ExchangesCryptoResponseBody**](ExchangesCryptoResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchanges_stocks**
> ExchangesStocksResponseBody get_exchanges_stocks(country=country, name=name, code=code, page=page, page_size=page_size)

List of stock markets

Returns a list of supported stock markets.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str | Filter by ISO 3166 alpha-2 code (optional)
name = 'name_example' # str | Filter by market name (optional)
code = 'code_example' # str | Filter by market identifier code (MIC) under ISO 10383 standard (optional)
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # List of stock markets
    api_response = api_instance.get_exchanges_stocks(country=country, name=name, code=code, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_exchanges_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Filter by ISO 3166 alpha-2 code | [optional] 
 **name** | **str**| Filter by market name | [optional] 
 **code** | **str**| Filter by market identifier code (MIC) under ISO 10383 standard | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**ExchangesStocksResponseBody**](ExchangesStocksResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_center**
> MarketCenterResponseBody get_market_center()

List of market centers

Returns a list of market centers.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))

try:
    # List of market centers
    api_response = api_instance.get_market_center()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_market_center: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketCenterResponseBody**](MarketCenterResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publishers**
> PublishersResponseBody get_publishers(code=code, page=page, page_size=page_size)

List of Finazon publishers

Returns a list of all publishers available at Finazon.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
code = 'code_example' # str | Filter by Finazon's publisher code (optional)
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # List of Finazon publishers
    api_response = api_instance.get_publishers(code=code, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_publishers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Filter by Finazon&#x27;s publisher code | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**PublishersResponseBody**](PublishersResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symbols_crypto**
> SymbolsCryptoResponseBody get_symbols_crypto(dataset=dataset, ticker=ticker, page=page, page_size=page_size)

List of crypto pairs

Returns a list of cryptocurrency ticker symbols (pairs). This list is updated daily.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
dataset = 'dataset_example' # str | Filter by Finazon's dataset code (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # List of crypto pairs
    api_response = api_instance.get_symbols_crypto(dataset=dataset, ticker=ticker, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_symbols_crypto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**SymbolsCryptoResponseBody**](SymbolsCryptoResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symbols_forex**
> SymbolsForexResponseBody get_symbols_forex(ticker=ticker, page=page, page_size=page_size)

List of forex ticker symbols

Returns a list of forex ticker symbols (pairs). This list is updated daily.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # List of forex ticker symbols
    api_response = api_instance.get_symbols_forex(ticker=ticker, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_symbols_forex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Filter by ticker symbol | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**SymbolsForexResponseBody**](SymbolsForexResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symbols_stocks**
> SymbolsStocksResponseBody get_symbols_stocks(cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, dataset=dataset, ticker=ticker, page=page, page_size=page_size)

List of stock ticker symbols

Returns a list of stock ticker symbols. This list is updated daily.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
dataset = 'dataset_example' # str | Filter by Finazon's dataset code (optional)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)

try:
    # List of stock ticker symbols
    api_response = api_instance.get_symbols_stocks(cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, dataset=dataset, ticker=ticker, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_symbols_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **dataset** | **str**| Filter by Finazon&#x27;s dataset code | [optional] 
 **ticker** | **str**| Filter by ticker symbol | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]

### Return type

[**SymbolsStocksResponseBody**](SymbolsStocksResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_symbols_us_stocks**
> SymbolsUSStocksResponseBody get_symbols_us_stocks(cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, page=page, page_size=page_size, ticker=ticker)

List of US stock ticker symbols

Returns a list of US stock ticker symbols. This list is updated daily.

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
api_instance = swagger_client.ReferenceApi(swagger_client.ApiClient(configuration))
cqs = 'cqs_example' # str | Filter by cqs symbol (optional)
cik = 'cik_example' # str | Filter by cik code (optional)
cusip = 'cusip_example' # str | Filter by cusip code (optional)
isin = 'isin_example' # str | Filter by isin code (optional)
composite_figi = 'composite_figi_example' # str | Filter by composite figi code (optional)
share_figi = 'share_figi_example' # str | Filter by share class figi code (optional)
lei = 'lei_example' # str | Filter by lei code (optional)
page = 56 # int | Specific page of a paginated result to be displayed (optional)
page_size = 1000 # int | Number of items displayed per page in a paginated result (optional) (default to 1000)
ticker = 'ticker_example' # str | Filter by ticker symbol (optional)

try:
    # List of US stock ticker symbols
    api_response = api_instance.get_symbols_us_stocks(cqs=cqs, cik=cik, cusip=cusip, isin=isin, composite_figi=composite_figi, share_figi=share_figi, lei=lei, page=page, page_size=page_size, ticker=ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->get_symbols_us_stocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cqs** | **str**| Filter by cqs symbol | [optional] 
 **cik** | **str**| Filter by cik code | [optional] 
 **cusip** | **str**| Filter by cusip code | [optional] 
 **isin** | **str**| Filter by isin code | [optional] 
 **composite_figi** | **str**| Filter by composite figi code | [optional] 
 **share_figi** | **str**| Filter by share class figi code | [optional] 
 **lei** | **str**| Filter by lei code | [optional] 
 **page** | **int**| Specific page of a paginated result to be displayed | [optional] 
 **page_size** | **int**| Number of items displayed per page in a paginated result | [optional] [default to 1000]
 **ticker** | **str**| Filter by ticker symbol | [optional] 

### Return type

[**SymbolsUSStocksResponseBody**](SymbolsUSStocksResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


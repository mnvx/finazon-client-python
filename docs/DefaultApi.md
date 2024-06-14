# swagger_client.DefaultApi

All URIs are relative to *https://api.finazon.io/v1.2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reference**](DefaultApi.md#reference) | **GET** /my_datasets | My Datasets

# **reference**
> DatasetsResponseBody reference()

My Datasets

Returns a list of datasets available for the workspace

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # My Datasets
    api_response = api_instance.reference()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->reference: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatasetsResponseBody**](DatasetsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


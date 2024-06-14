# coding: utf-8

"""
    Finazon API

    ## API reference  Finazon is a comprehensive financial data marketplace that enables developers to effortlessly integrate a wide variety of global datasets, including stocks, ETFs, cryptocurrencies, and more, all with fully customizable parameters.  The Finazon API is built around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles, featuring resource-oriented URLs with predictable behavior. The API accepts [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms) request bodies, returns JSON-encoded responses, and utilizes standard HTTP response codes, authentication methods, and verbs.  The Finazon API doesn't support bulk updates. You can work on only one instrument per request.  ## Authentification  To authenticate requests, the Finazon API requires [API keys](https://finazon.io/account/developers/api-keys). You can obtain, view, and manage your API keys through the [Finazon Dashboard](https://finazon.io/account/home).  Your API keys hold significant privileges, so ensure their security by not sharing your secret API keys in publicly accessible areas, such as GitHub repositories, client-side code, or any other public platforms.  All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls over plain HTTP will fail, as will API requests without authentication.  Once you have your API key, include it in the parameters as follows:  ```bash https://api.finazon.io/latest?apikey=YOUR_API_KEY ```  Alternatively, pass it as a request header:  ```bash Authorization: apikey YOUR_API_KEY ```  ## Versioning  Whenever [backwards-incompatible](https://support.finazon.io/en/articles/7792859-api-upgrades#h_1e014217bf) changes are introduced to the API, a new dated version is released. Consult our [API upgrades guide](https://support.finazon.io/en/articles/7792859-api-upgrades) for more information on backwards compatibility, and view our API changelog for all API updates.  To always use the most up-to-date version, specify it as `/latest`:  ```bash https://api.finazon.io/latest ```  To access the most recent version of `v1.*`, use the following:  ```bash https://api.finazon.io/v1  ```  Or, to retrieve a specific version, call:  ```bash  https://api.finazon.io/v1.0 ```  Finazon will provide advance notice before deprecating older API versions, giving developers ample time to migrate to the updated version.  ## Endpoints structure  The Finazon API adheres to a consistent and structured pattern for its endpoints. The base URL for all requests is:  ```bash https://api.finazon.io/ ```  API endpoints are organized by resource types, including universal resources accessible across all publishers and publisher-specific resources. For example, the `/time_series` endpoint is compatible with all publishers that support this data format. Such responses will be standardized across all datasets, facilitating rapid integration of new markets into your applications.  ```bash https://api.finazon.io/latest/{{resource}} https://api.finazon.io/latest/time_series ```  Additionally, datasets may contain unique data exclusive to that dataset. In such cases, you might want to call a separate endpoint specifying the publisher to gather more data. For instance, the [Binance](https://finazon.io/dataset/binance) dataset time series can be requested as:  ```bash  https://api.finazon.io/latest/{{publisher}}/{{resource}} https://api.finazon.io/latest/binance/time_series ```  ## Parameters  Each API request has its own set of required and optional parameters. Parameters should be separated by an ampersand. Parameter names are case-sensitive, while parameter values are not. Each API request has its own set of required and optional parameters. Parameters should be separated by an ampersand. Parameter names and parameter values are case-sensitive  ```bash https://api.finazon.io/latest/time_series?dataset=sip_non_pro&ticker=AAPL&interval=1m&apikey= ```  ### Pagination  All API resources supporting bulk fetches are retrieved via \"list\" API methods. For example, you can list time series, list trades, and list quotes. These list API methods share a common structure, accepting at least these five parameters: `page`, `page_size`, `order`, `start_at`, and `end_at`.  The response of a list API method represents a single page in a reverse chronological stream of objects. If you do not specify `start_at` or `end_at`, you will receive the first page of this list, containing the newest objects. By default, you will receive 10 objects if you do not specify an alternative value for `page_size`. You can specify `start_at` equal to the T (timestamp) value of an item to retrieve the page of older objects occurring immediately after the specified timestamp in the reverse chronological stream. Similarly, you can specify `end_at` to receive a page of newer objects occurring immediately before the named object in the stream. You can use one of `start_at` or `end_at` or both. Objects in a page always appear in reverse chronological order, unless `order` is specified.  ## Errors  Finazon employs standard HTTP response codes to signify the success or failure of an API request. Generally, the response codes can be interpreted as follows:  `2xx` range codes indicate a successful request.  `4xx` range codes signify an error resulting from the provided information (e.g., invalid API key, API rate limit exceeded, etc.).  `5xx` range codes represent errors originating from Finazon's servers (these are rare occurrences).  For all `4xx`errors that can be addressed programmatically (e.g., endpoint not found), an error message is included to succinctly explain the reported issue. This allows developers to quickly identify and resolve errors in their API requests.   status | code | message | --------|:-----|:--------|  400 |  INVALID_PARAMETER | The **{parameter_name}** parameter is missing or invalid. |  400 |  INVALID_DATE_RANGE | The requested date range is invalid or unsupported. |  400 |  UNSUPPORTED_MARKET | The requested market or exchange is not supported by the API. Please check the supported markets and try again. |  400 |  INVALID_TICKER | The provided ticker is invalid or unsupported. |  401 |  UNAUTHORIZED_ACCESS | You are not authorized to access the requested endpoint or you have insufficient permissions. |  404 |  ENDPOINT_NOT_FOUND | The requested endpoint **{endpoint_name}** does not exist or could not be found. |  429 |  API_RATE_LIMIT_EXCEEDED | You have exceeded the allowed number of API calls within the minute. Please wait and try again later. |  401 |  INVALID_API_KEY | The provided API key is invalid or has expired. Please check your API key and try again |  408 |  REQUEST_TIMEOUT | The request took too long to complete and timed out. Please try again later or reduce the complexity of your query. |  503 |  DATA_UNAVAILABLE | The requested data is temporarily unavailable or not supported. Please try again later or check the availability of the data. |  500 |  INTERNAL_SERVER_ERROR | An error occurred on the server-side while processing the request. Please try again later. If the issue persists, contact support. |  # noqa: E501

    OpenAPI spec version: v1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_1d': 'TickerSnapshotLastDay',
        '_1m': 'TickerSnapshotLastMonth',
        '_52w': 'TickerSnapshotLastFiftyTwoWeek',
        'ch': 'TickerSnapshotChange',
        'lt': 'TickerSnapshotLastTrade',
        'p1d': 'TickerSnapshotPreviousDay'
    }

    attribute_map = {
        '_1d': '1d',
        '_1m': '1m',
        '_52w': '52w',
        'ch': 'ch',
        'lt': 'lt',
        'p1d': 'p1d'
    }

    def __init__(self, _1d=None, _1m=None, _52w=None, ch=None, lt=None, p1d=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self.__1d = None
        self.__1m = None
        self.__52w = None
        self._ch = None
        self._lt = None
        self._p1d = None
        self.discriminator = None
        self._1d = _1d
        self._1m = _1m
        self._52w = _52w
        self.ch = ch
        self.lt = lt
        self.p1d = p1d

    @property
    def _1d(self):
        """Gets the _1d of this InlineResponse200.  # noqa: E501


        :return: The _1d of this InlineResponse200.  # noqa: E501
        :rtype: TickerSnapshotLastDay
        """
        return self.__1d

    @_1d.setter
    def _1d(self, _1d):
        """Sets the _1d of this InlineResponse200.


        :param _1d: The _1d of this InlineResponse200.  # noqa: E501
        :type: TickerSnapshotLastDay
        """
        if _1d is None:
            raise ValueError("Invalid value for `_1d`, must not be `None`")  # noqa: E501

        self.__1d = _1d

    @property
    def _1m(self):
        """Gets the _1m of this InlineResponse200.  # noqa: E501


        :return: The _1m of this InlineResponse200.  # noqa: E501
        :rtype: TickerSnapshotLastMonth
        """
        return self.__1m

    @_1m.setter
    def _1m(self, _1m):
        """Sets the _1m of this InlineResponse200.


        :param _1m: The _1m of this InlineResponse200.  # noqa: E501
        :type: TickerSnapshotLastMonth
        """
        if _1m is None:
            raise ValueError("Invalid value for `_1m`, must not be `None`")  # noqa: E501

        self.__1m = _1m

    @property
    def _52w(self):
        """Gets the _52w of this InlineResponse200.  # noqa: E501


        :return: The _52w of this InlineResponse200.  # noqa: E501
        :rtype: TickerSnapshotLastFiftyTwoWeek
        """
        return self.__52w

    @_52w.setter
    def _52w(self, _52w):
        """Sets the _52w of this InlineResponse200.


        :param _52w: The _52w of this InlineResponse200.  # noqa: E501
        :type: TickerSnapshotLastFiftyTwoWeek
        """
        if _52w is None:
            raise ValueError("Invalid value for `_52w`, must not be `None`")  # noqa: E501

        self.__52w = _52w

    @property
    def ch(self):
        """Gets the ch of this InlineResponse200.  # noqa: E501


        :return: The ch of this InlineResponse200.  # noqa: E501
        :rtype: TickerSnapshotChange
        """
        return self._ch

    @ch.setter
    def ch(self, ch):
        """Sets the ch of this InlineResponse200.


        :param ch: The ch of this InlineResponse200.  # noqa: E501
        :type: TickerSnapshotChange
        """
        if ch is None:
            raise ValueError("Invalid value for `ch`, must not be `None`")  # noqa: E501

        self._ch = ch

    @property
    def lt(self):
        """Gets the lt of this InlineResponse200.  # noqa: E501


        :return: The lt of this InlineResponse200.  # noqa: E501
        :rtype: TickerSnapshotLastTrade
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this InlineResponse200.


        :param lt: The lt of this InlineResponse200.  # noqa: E501
        :type: TickerSnapshotLastTrade
        """
        if lt is None:
            raise ValueError("Invalid value for `lt`, must not be `None`")  # noqa: E501

        self._lt = lt

    @property
    def p1d(self):
        """Gets the p1d of this InlineResponse200.  # noqa: E501


        :return: The p1d of this InlineResponse200.  # noqa: E501
        :rtype: TickerSnapshotPreviousDay
        """
        return self._p1d

    @p1d.setter
    def p1d(self, p1d):
        """Sets the p1d of this InlineResponse200.


        :param p1d: The p1d of this InlineResponse200.  # noqa: E501
        :type: TickerSnapshotPreviousDay
        """
        if p1d is None:
            raise ValueError("Invalid value for `p1d`, must not be `None`")  # noqa: E501

        self._p1d = p1d

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

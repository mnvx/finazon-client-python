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

class TickerSnapshotLastFiftyTwoWeek(object):
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
        'h': 'object',
        'ht': 'int',
        'l': 'object',
        'lt': 'int',
        'ch': 'float',
        'chp': 'float',
        'av': 'int'
    }

    attribute_map = {
        'h': 'h',
        'ht': 'ht',
        'l': 'l',
        'lt': 'lt',
        'ch': 'ch',
        'chp': 'chp',
        'av': 'av'
    }

    def __init__(self, h=None, ht=None, l=None, lt=None, ch=None, chp=None, av=None):  # noqa: E501
        """TickerSnapshotLastFiftyTwoWeek - a model defined in Swagger"""  # noqa: E501
        self._h = None
        self._ht = None
        self._l = None
        self._lt = None
        self._ch = None
        self._chp = None
        self._av = None
        self.discriminator = None
        if h is not None:
            self.h = h
        if ht is not None:
            self.ht = ht
        if l is not None:
            self.l = l
        if lt is not None:
            self.lt = lt
        if ch is not None:
            self.ch = ch
        if chp is not None:
            self.chp = chp
        if av is not None:
            self.av = av

    @property
    def h(self):
        """Gets the h of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501

        Highest price  # noqa: E501

        :return: The h of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :rtype: object
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this TickerSnapshotLastFiftyTwoWeek.

        Highest price  # noqa: E501

        :param h: The h of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :type: object
        """

        self._h = h

    @property
    def ht(self):
        """Gets the ht of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501

        Highest price timestamp  # noqa: E501

        :return: The ht of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :rtype: int
        """
        return self._ht

    @ht.setter
    def ht(self, ht):
        """Sets the ht of this TickerSnapshotLastFiftyTwoWeek.

        Highest price timestamp  # noqa: E501

        :param ht: The ht of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :type: int
        """

        self._ht = ht

    @property
    def l(self):
        """Gets the l of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501

        Lowest price  # noqa: E501

        :return: The l of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :rtype: object
        """
        return self._l

    @l.setter
    def l(self, l):
        """Sets the l of this TickerSnapshotLastFiftyTwoWeek.

        Lowest price  # noqa: E501

        :param l: The l of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :type: object
        """

        self._l = l

    @property
    def lt(self):
        """Gets the lt of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501

        Lowest price timestamp  # noqa: E501

        :return: The lt of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :rtype: int
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this TickerSnapshotLastFiftyTwoWeek.

        Lowest price timestamp  # noqa: E501

        :param lt: The lt of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :type: int
        """

        self._lt = lt

    @property
    def ch(self):
        """Gets the ch of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501

        Change price  # noqa: E501

        :return: The ch of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :rtype: float
        """
        return self._ch

    @ch.setter
    def ch(self, ch):
        """Sets the ch of this TickerSnapshotLastFiftyTwoWeek.

        Change price  # noqa: E501

        :param ch: The ch of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :type: float
        """

        self._ch = ch

    @property
    def chp(self):
        """Gets the chp of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501

        Change price percent  # noqa: E501

        :return: The chp of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :rtype: float
        """
        return self._chp

    @chp.setter
    def chp(self, chp):
        """Sets the chp of this TickerSnapshotLastFiftyTwoWeek.

        Change price percent  # noqa: E501

        :param chp: The chp of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :type: float
        """

        self._chp = chp

    @property
    def av(self):
        """Gets the av of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501

        Average volume  # noqa: E501

        :return: The av of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :rtype: int
        """
        return self._av

    @av.setter
    def av(self, av):
        """Sets the av of this TickerSnapshotLastFiftyTwoWeek.

        Average volume  # noqa: E501

        :param av: The av of this TickerSnapshotLastFiftyTwoWeek.  # noqa: E501
        :type: int
        """

        self._av = av

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
        if issubclass(TickerSnapshotLastFiftyTwoWeek, dict):
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
        if not isinstance(other, TickerSnapshotLastFiftyTwoWeek):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
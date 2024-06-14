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

class QuoteBinanceItem(object):
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
        't': 'int',
        'o': 'float',
        'h': 'float',
        'l': 'float',
        'c': 'float',
        'tr': 'float',
        'bv': 'float',
        'qv': 'float',
        'tbv': 'float',
        'tqv': 'float'
    }

    attribute_map = {
        't': 't',
        'o': 'o',
        'h': 'h',
        'l': 'l',
        'c': 'c',
        'tr': 'tr',
        'bv': 'bv',
        'qv': 'qv',
        'tbv': 'tbv',
        'tqv': 'tqv'
    }

    def __init__(self, t=None, o=None, h=None, l=None, c=None, tr=None, bv=None, qv=None, tbv=None, tqv=None):  # noqa: E501
        """QuoteBinanceItem - a model defined in Swagger"""  # noqa: E501
        self._t = None
        self._o = None
        self._h = None
        self._l = None
        self._c = None
        self._tr = None
        self._bv = None
        self._qv = None
        self._tbv = None
        self._tqv = None
        self.discriminator = None
        if t is not None:
            self.t = t
        if o is not None:
            self.o = o
        if h is not None:
            self.h = h
        if l is not None:
            self.l = l
        if c is not None:
            self.c = c
        if tr is not None:
            self.tr = tr
        if bv is not None:
            self.bv = bv
        if qv is not None:
            self.qv = qv
        if tbv is not None:
            self.tbv = tbv
        if tqv is not None:
            self.tqv = tqv

    @property
    def t(self):
        """Gets the t of this QuoteBinanceItem.  # noqa: E501

        Timestamp indicating when the trading interval opened  # noqa: E501

        :return: The t of this QuoteBinanceItem.  # noqa: E501
        :rtype: int
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this QuoteBinanceItem.

        Timestamp indicating when the trading interval opened  # noqa: E501

        :param t: The t of this QuoteBinanceItem.  # noqa: E501
        :type: int
        """

        self._t = t

    @property
    def o(self):
        """Gets the o of this QuoteBinanceItem.  # noqa: E501

        Price at the opening of the trading interval  # noqa: E501

        :return: The o of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._o

    @o.setter
    def o(self, o):
        """Sets the o of this QuoteBinanceItem.

        Price at the opening of the trading interval  # noqa: E501

        :param o: The o of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._o = o

    @property
    def h(self):
        """Gets the h of this QuoteBinanceItem.  # noqa: E501

        Highest price reached during the trading interval  # noqa: E501

        :return: The h of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this QuoteBinanceItem.

        Highest price reached during the trading interval  # noqa: E501

        :param h: The h of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._h = h

    @property
    def l(self):
        """Gets the l of this QuoteBinanceItem.  # noqa: E501

        Lowest price reached during the trading interval  # noqa: E501

        :return: The l of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._l

    @l.setter
    def l(self, l):
        """Sets the l of this QuoteBinanceItem.

        Lowest price reached during the trading interval  # noqa: E501

        :param l: The l of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._l = l

    @property
    def c(self):
        """Gets the c of this QuoteBinanceItem.  # noqa: E501

        Closing price at the end of the trading interval  # noqa: E501

        :return: The c of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._c

    @c.setter
    def c(self, c):
        """Sets the c of this QuoteBinanceItem.

        Closing price at the end of the trading interval  # noqa: E501

        :param c: The c of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._c = c

    @property
    def tr(self):
        """Gets the tr of this QuoteBinanceItem.  # noqa: E501

        Trades  # noqa: E501

        :return: The tr of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._tr

    @tr.setter
    def tr(self, tr):
        """Sets the tr of this QuoteBinanceItem.

        Trades  # noqa: E501

        :param tr: The tr of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._tr = tr

    @property
    def bv(self):
        """Gets the bv of this QuoteBinanceItem.  # noqa: E501

        Trading base volume recorded during the trading interval  # noqa: E501

        :return: The bv of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._bv

    @bv.setter
    def bv(self, bv):
        """Sets the bv of this QuoteBinanceItem.

        Trading base volume recorded during the trading interval  # noqa: E501

        :param bv: The bv of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._bv = bv

    @property
    def qv(self):
        """Gets the qv of this QuoteBinanceItem.  # noqa: E501

        Trading quote volume recorded during the trading interval  # noqa: E501

        :return: The qv of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._qv

    @qv.setter
    def qv(self, qv):
        """Sets the qv of this QuoteBinanceItem.

        Trading quote volume recorded during the trading interval  # noqa: E501

        :param qv: The qv of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._qv = qv

    @property
    def tbv(self):
        """Gets the tbv of this QuoteBinanceItem.  # noqa: E501

        Taker buy base asset volume recorded during the trading interval  # noqa: E501

        :return: The tbv of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._tbv

    @tbv.setter
    def tbv(self, tbv):
        """Sets the tbv of this QuoteBinanceItem.

        Taker buy base asset volume recorded during the trading interval  # noqa: E501

        :param tbv: The tbv of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._tbv = tbv

    @property
    def tqv(self):
        """Gets the tqv of this QuoteBinanceItem.  # noqa: E501

        Taker buy quote asset volume recorded during the trading interval  # noqa: E501

        :return: The tqv of this QuoteBinanceItem.  # noqa: E501
        :rtype: float
        """
        return self._tqv

    @tqv.setter
    def tqv(self, tqv):
        """Sets the tqv of this QuoteBinanceItem.

        Taker buy quote asset volume recorded during the trading interval  # noqa: E501

        :param tqv: The tqv of this QuoteBinanceItem.  # noqa: E501
        :type: float
        """

        self._tqv = tqv

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
        if issubclass(QuoteBinanceItem, dict):
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
        if not isinstance(other, QuoteBinanceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

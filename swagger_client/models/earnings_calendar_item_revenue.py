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

class EarningsCalendarItemRevenue(object):
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
        'estimated': 'float',
        'prior': 'float',
        'reported': 'float',
        'surprise': 'float',
        'surprise_percent': 'float',
        'type': 'str'
    }

    attribute_map = {
        'estimated': 'estimated',
        'prior': 'prior',
        'reported': 'reported',
        'surprise': 'surprise',
        'surprise_percent': 'surprise_percent',
        'type': 'type'
    }

    def __init__(self, estimated=None, prior=None, reported=None, surprise=None, surprise_percent=None, type=None):  # noqa: E501
        """EarningsCalendarItemRevenue - a model defined in Swagger"""  # noqa: E501
        self._estimated = None
        self._prior = None
        self._reported = None
        self._surprise = None
        self._surprise_percent = None
        self._type = None
        self.discriminator = None
        if estimated is not None:
            self.estimated = estimated
        if prior is not None:
            self.prior = prior
        if reported is not None:
            self.reported = reported
        if surprise is not None:
            self.surprise = surprise
        if surprise_percent is not None:
            self.surprise_percent = surprise_percent
        if type is not None:
            self.type = type

    @property
    def estimated(self):
        """Gets the estimated of this EarningsCalendarItemRevenue.  # noqa: E501

        Revenue predicted  # noqa: E501

        :return: The estimated of this EarningsCalendarItemRevenue.  # noqa: E501
        :rtype: float
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated):
        """Sets the estimated of this EarningsCalendarItemRevenue.

        Revenue predicted  # noqa: E501

        :param estimated: The estimated of this EarningsCalendarItemRevenue.  # noqa: E501
        :type: float
        """

        self._estimated = estimated

    @property
    def prior(self):
        """Gets the prior of this EarningsCalendarItemRevenue.  # noqa: E501

        Revenue reported for the same period a year ago  # noqa: E501

        :return: The prior of this EarningsCalendarItemRevenue.  # noqa: E501
        :rtype: float
        """
        return self._prior

    @prior.setter
    def prior(self, prior):
        """Sets the prior of this EarningsCalendarItemRevenue.

        Revenue reported for the same period a year ago  # noqa: E501

        :param prior: The prior of this EarningsCalendarItemRevenue.  # noqa: E501
        :type: float
        """

        self._prior = prior

    @property
    def reported(self):
        """Gets the reported of this EarningsCalendarItemRevenue.  # noqa: E501

        Revenue reported  # noqa: E501

        :return: The reported of this EarningsCalendarItemRevenue.  # noqa: E501
        :rtype: float
        """
        return self._reported

    @reported.setter
    def reported(self, reported):
        """Sets the reported of this EarningsCalendarItemRevenue.

        Revenue reported  # noqa: E501

        :param reported: The reported of this EarningsCalendarItemRevenue.  # noqa: E501
        :type: float
        """

        self._reported = reported

    @property
    def surprise(self):
        """Gets the surprise of this EarningsCalendarItemRevenue.  # noqa: E501

        Difference between the predicted and the actual reported value  # noqa: E501

        :return: The surprise of this EarningsCalendarItemRevenue.  # noqa: E501
        :rtype: float
        """
        return self._surprise

    @surprise.setter
    def surprise(self, surprise):
        """Sets the surprise of this EarningsCalendarItemRevenue.

        Difference between the predicted and the actual reported value  # noqa: E501

        :param surprise: The surprise of this EarningsCalendarItemRevenue.  # noqa: E501
        :type: float
        """

        self._surprise = surprise

    @property
    def surprise_percent(self):
        """Gets the surprise_percent of this EarningsCalendarItemRevenue.  # noqa: E501

        Percentage difference between the predicted and the actual reported value  # noqa: E501

        :return: The surprise_percent of this EarningsCalendarItemRevenue.  # noqa: E501
        :rtype: float
        """
        return self._surprise_percent

    @surprise_percent.setter
    def surprise_percent(self, surprise_percent):
        """Sets the surprise_percent of this EarningsCalendarItemRevenue.

        Percentage difference between the predicted and the actual reported value  # noqa: E501

        :param surprise_percent: The surprise_percent of this EarningsCalendarItemRevenue.  # noqa: E501
        :type: float
        """

        self._surprise_percent = surprise_percent

    @property
    def type(self):
        """Gets the type of this EarningsCalendarItemRevenue.  # noqa: E501

        Type of the revenue  # noqa: E501

        :return: The type of this EarningsCalendarItemRevenue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EarningsCalendarItemRevenue.

        Type of the revenue  # noqa: E501

        :param type: The type of this EarningsCalendarItemRevenue.  # noqa: E501
        :type: str
        """
        allowed_values = ["Adj", "GAAP", "FFO"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(EarningsCalendarItemRevenue, dict):
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
        if not isinstance(other, EarningsCalendarItemRevenue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

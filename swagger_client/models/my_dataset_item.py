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

class MyDatasetItem(object):
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
        'active_until': 'int',
        'code': 'str',
        'details': 'list[DatasetDetailItem]',
        'finish_at': 'int',
        'name': 'str',
        'next_renewal': 'int',
        'price_period': 'str',
        'price_total': 'float',
        'start_at': 'int',
        'status': 'str'
    }

    attribute_map = {
        'active_until': 'active_until',
        'code': 'code',
        'details': 'details',
        'finish_at': 'finish_at',
        'name': 'name',
        'next_renewal': 'next_renewal',
        'price_period': 'price_period',
        'price_total': 'price_total',
        'start_at': 'start_at',
        'status': 'status'
    }

    def __init__(self, active_until=None, code=None, details=None, finish_at=None, name=None, next_renewal=None, price_period=None, price_total=None, start_at=None, status=None):  # noqa: E501
        """MyDatasetItem - a model defined in Swagger"""  # noqa: E501
        self._active_until = None
        self._code = None
        self._details = None
        self._finish_at = None
        self._name = None
        self._next_renewal = None
        self._price_period = None
        self._price_total = None
        self._start_at = None
        self._status = None
        self.discriminator = None
        if active_until is not None:
            self.active_until = active_until
        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if finish_at is not None:
            self.finish_at = finish_at
        if name is not None:
            self.name = name
        if next_renewal is not None:
            self.next_renewal = next_renewal
        if price_period is not None:
            self.price_period = price_period
        if price_total is not None:
            self.price_total = price_total
        if start_at is not None:
            self.start_at = start_at
        if status is not None:
            self.status = status

    @property
    def active_until(self):
        """Gets the active_until of this MyDatasetItem.  # noqa: E501

        Dataset subscription active until date  # noqa: E501

        :return: The active_until of this MyDatasetItem.  # noqa: E501
        :rtype: int
        """
        return self._active_until

    @active_until.setter
    def active_until(self, active_until):
        """Sets the active_until of this MyDatasetItem.

        Dataset subscription active until date  # noqa: E501

        :param active_until: The active_until of this MyDatasetItem.  # noqa: E501
        :type: int
        """

        self._active_until = active_until

    @property
    def code(self):
        """Gets the code of this MyDatasetItem.  # noqa: E501

        Dataset alias  # noqa: E501

        :return: The code of this MyDatasetItem.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this MyDatasetItem.

        Dataset alias  # noqa: E501

        :param code: The code of this MyDatasetItem.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def details(self):
        """Gets the details of this MyDatasetItem.  # noqa: E501


        :return: The details of this MyDatasetItem.  # noqa: E501
        :rtype: list[DatasetDetailItem]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this MyDatasetItem.


        :param details: The details of this MyDatasetItem.  # noqa: E501
        :type: list[DatasetDetailItem]
        """

        self._details = details

    @property
    def finish_at(self):
        """Gets the finish_at of this MyDatasetItem.  # noqa: E501

        Dataset finish subscription date  # noqa: E501

        :return: The finish_at of this MyDatasetItem.  # noqa: E501
        :rtype: int
        """
        return self._finish_at

    @finish_at.setter
    def finish_at(self, finish_at):
        """Sets the finish_at of this MyDatasetItem.

        Dataset finish subscription date  # noqa: E501

        :param finish_at: The finish_at of this MyDatasetItem.  # noqa: E501
        :type: int
        """

        self._finish_at = finish_at

    @property
    def name(self):
        """Gets the name of this MyDatasetItem.  # noqa: E501

        Dataset name  # noqa: E501

        :return: The name of this MyDatasetItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MyDatasetItem.

        Dataset name  # noqa: E501

        :param name: The name of this MyDatasetItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def next_renewal(self):
        """Gets the next_renewal of this MyDatasetItem.  # noqa: E501

        Dataset subscription next renewal date  # noqa: E501

        :return: The next_renewal of this MyDatasetItem.  # noqa: E501
        :rtype: int
        """
        return self._next_renewal

    @next_renewal.setter
    def next_renewal(self, next_renewal):
        """Sets the next_renewal of this MyDatasetItem.

        Dataset subscription next renewal date  # noqa: E501

        :param next_renewal: The next_renewal of this MyDatasetItem.  # noqa: E501
        :type: int
        """

        self._next_renewal = next_renewal

    @property
    def price_period(self):
        """Gets the price_period of this MyDatasetItem.  # noqa: E501

        Dataset subscription price period  # noqa: E501

        :return: The price_period of this MyDatasetItem.  # noqa: E501
        :rtype: str
        """
        return self._price_period

    @price_period.setter
    def price_period(self, price_period):
        """Sets the price_period of this MyDatasetItem.

        Dataset subscription price period  # noqa: E501

        :param price_period: The price_period of this MyDatasetItem.  # noqa: E501
        :type: str
        """

        self._price_period = price_period

    @property
    def price_total(self):
        """Gets the price_total of this MyDatasetItem.  # noqa: E501

        Dataset subscription total price  # noqa: E501

        :return: The price_total of this MyDatasetItem.  # noqa: E501
        :rtype: float
        """
        return self._price_total

    @price_total.setter
    def price_total(self, price_total):
        """Sets the price_total of this MyDatasetItem.

        Dataset subscription total price  # noqa: E501

        :param price_total: The price_total of this MyDatasetItem.  # noqa: E501
        :type: float
        """

        self._price_total = price_total

    @property
    def start_at(self):
        """Gets the start_at of this MyDatasetItem.  # noqa: E501

        Dataset start subscription date  # noqa: E501

        :return: The start_at of this MyDatasetItem.  # noqa: E501
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this MyDatasetItem.

        Dataset start subscription date  # noqa: E501

        :param start_at: The start_at of this MyDatasetItem.  # noqa: E501
        :type: int
        """

        self._start_at = start_at

    @property
    def status(self):
        """Gets the status of this MyDatasetItem.  # noqa: E501

        Dataset status  # noqa: E501

        :return: The status of this MyDatasetItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MyDatasetItem.

        Dataset status  # noqa: E501

        :param status: The status of this MyDatasetItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "canceled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(MyDatasetItem, dict):
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
        if not isinstance(other, MyDatasetItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class EarningsCalendarItem(object):
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
        'currency': 'str',
        '_date': 'str',
        'date_confirmed': 'bool',
        'eps': 'EarningsCalendarItemEps',
        'importance': 'int',
        'mic': 'str',
        'name': 'str',
        'notes': 'str',
        'period': 'str',
        'period_year': 'int',
        'record_id': 'str',
        'revenue': 'EarningsCalendarItemRevenue',
        'ticker': 'str',
        'time': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'currency': 'currency',
        '_date': 'date',
        'date_confirmed': 'date_confirmed',
        'eps': 'eps',
        'importance': 'importance',
        'mic': 'mic',
        'name': 'name',
        'notes': 'notes',
        'period': 'period',
        'period_year': 'period_year',
        'record_id': 'record_id',
        'revenue': 'revenue',
        'ticker': 'ticker',
        'time': 'time',
        'updated': 'updated'
    }

    def __init__(self, currency=None, _date=None, date_confirmed=None, eps=None, importance=None, mic=None, name=None, notes=None, period=None, period_year=None, record_id=None, revenue=None, ticker=None, time=None, updated=None):  # noqa: E501
        """EarningsCalendarItem - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self.__date = None
        self._date_confirmed = None
        self._eps = None
        self._importance = None
        self._mic = None
        self._name = None
        self._notes = None
        self._period = None
        self._period_year = None
        self._record_id = None
        self._revenue = None
        self._ticker = None
        self._time = None
        self._updated = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if _date is not None:
            self._date = _date
        if date_confirmed is not None:
            self.date_confirmed = date_confirmed
        if eps is not None:
            self.eps = eps
        if importance is not None:
            self.importance = importance
        if mic is not None:
            self.mic = mic
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if period is not None:
            self.period = period
        if period_year is not None:
            self.period_year = period_year
        if record_id is not None:
            self.record_id = record_id
        if revenue is not None:
            self.revenue = revenue
        if ticker is not None:
            self.ticker = ticker
        if time is not None:
            self.time = time
        if updated is not None:
            self.updated = updated

    @property
    def currency(self):
        """Gets the currency of this EarningsCalendarItem.  # noqa: E501

        The currency code of the security according to the ISO 4217 standard  # noqa: E501

        :return: The currency of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EarningsCalendarItem.

        The currency code of the security according to the ISO 4217 standard  # noqa: E501

        :param currency: The currency of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def _date(self):
        """Gets the _date of this EarningsCalendarItem.  # noqa: E501

        Date when earnings are disbursed  # noqa: E501

        :return: The _date of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EarningsCalendarItem.

        Date when earnings are disbursed  # noqa: E501

        :param _date: The _date of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def date_confirmed(self):
        """Gets the date_confirmed of this EarningsCalendarItem.  # noqa: E501

        Indicates if the predicted date has been verified by the company  # noqa: E501

        :return: The date_confirmed of this EarningsCalendarItem.  # noqa: E501
        :rtype: bool
        """
        return self._date_confirmed

    @date_confirmed.setter
    def date_confirmed(self, date_confirmed):
        """Sets the date_confirmed of this EarningsCalendarItem.

        Indicates if the predicted date has been verified by the company  # noqa: E501

        :param date_confirmed: The date_confirmed of this EarningsCalendarItem.  # noqa: E501
        :type: bool
        """

        self._date_confirmed = date_confirmed

    @property
    def eps(self):
        """Gets the eps of this EarningsCalendarItem.  # noqa: E501


        :return: The eps of this EarningsCalendarItem.  # noqa: E501
        :rtype: EarningsCalendarItemEps
        """
        return self._eps

    @eps.setter
    def eps(self, eps):
        """Sets the eps of this EarningsCalendarItem.


        :param eps: The eps of this EarningsCalendarItem.  # noqa: E501
        :type: EarningsCalendarItemEps
        """

        self._eps = eps

    @property
    def importance(self):
        """Gets the importance of this EarningsCalendarItem.  # noqa: E501

        Significance of the event  # noqa: E501

        :return: The importance of this EarningsCalendarItem.  # noqa: E501
        :rtype: int
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        """Sets the importance of this EarningsCalendarItem.

        Significance of the event  # noqa: E501

        :param importance: The importance of this EarningsCalendarItem.  # noqa: E501
        :type: int
        """

        self._importance = importance

    @property
    def mic(self):
        """Gets the mic of this EarningsCalendarItem.  # noqa: E501

        Market identifier code (MIC) under ISO 10383 standard  # noqa: E501

        :return: The mic of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._mic

    @mic.setter
    def mic(self, mic):
        """Sets the mic of this EarningsCalendarItem.

        Market identifier code (MIC) under ISO 10383 standard  # noqa: E501

        :param mic: The mic of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self._mic = mic

    @property
    def name(self):
        """Gets the name of this EarningsCalendarItem.  # noqa: E501

        Full name of the instrument  # noqa: E501

        :return: The name of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EarningsCalendarItem.

        Full name of the instrument  # noqa: E501

        :param name: The name of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this EarningsCalendarItem.  # noqa: E501

        Notes  # noqa: E501

        :return: The notes of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EarningsCalendarItem.

        Notes  # noqa: E501

        :param notes: The notes of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def period(self):
        """Gets the period of this EarningsCalendarItem.  # noqa: E501

        Fiscal period being reported  # noqa: E501

        :return: The period of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this EarningsCalendarItem.

        Fiscal period being reported  # noqa: E501

        :param period: The period of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Q1", "Q2", "Q3", "Q4", "FY", "H1", "H2"]  # noqa: E501
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"  # noqa: E501
                .format(period, allowed_values)
            )

        self._period = period

    @property
    def period_year(self):
        """Gets the period_year of this EarningsCalendarItem.  # noqa: E501

        Fiscal year being reported  # noqa: E501

        :return: The period_year of this EarningsCalendarItem.  # noqa: E501
        :rtype: int
        """
        return self._period_year

    @period_year.setter
    def period_year(self, period_year):
        """Sets the period_year of this EarningsCalendarItem.

        Fiscal year being reported  # noqa: E501

        :param period_year: The period_year of this EarningsCalendarItem.  # noqa: E501
        :type: int
        """

        self._period_year = period_year

    @property
    def record_id(self):
        """Gets the record_id of this EarningsCalendarItem.  # noqa: E501

        Unique record ID from Benzinga  # noqa: E501

        :return: The record_id of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this EarningsCalendarItem.

        Unique record ID from Benzinga  # noqa: E501

        :param record_id: The record_id of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self._record_id = record_id

    @property
    def revenue(self):
        """Gets the revenue of this EarningsCalendarItem.  # noqa: E501


        :return: The revenue of this EarningsCalendarItem.  # noqa: E501
        :rtype: EarningsCalendarItemRevenue
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """Sets the revenue of this EarningsCalendarItem.


        :param revenue: The revenue of this EarningsCalendarItem.  # noqa: E501
        :type: EarningsCalendarItemRevenue
        """

        self._revenue = revenue

    @property
    def ticker(self):
        """Gets the ticker of this EarningsCalendarItem.  # noqa: E501

        Ticker symbol of the instrument  # noqa: E501

        :return: The ticker of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this EarningsCalendarItem.

        Ticker symbol of the instrument  # noqa: E501

        :param ticker: The ticker of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def time(self):
        """Gets the time of this EarningsCalendarItem.  # noqa: E501

        Time when earnings are disbursed  # noqa: E501

        :return: The time of this EarningsCalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this EarningsCalendarItem.

        Time when earnings are disbursed  # noqa: E501

        :param time: The time of this EarningsCalendarItem.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def updated(self):
        """Gets the updated of this EarningsCalendarItem.  # noqa: E501

        Last updated timestamp (UNIX)  # noqa: E501

        :return: The updated of this EarningsCalendarItem.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this EarningsCalendarItem.

        Last updated timestamp (UNIX)  # noqa: E501

        :param updated: The updated of this EarningsCalendarItem.  # noqa: E501
        :type: int
        """

        self._updated = updated

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
        if issubclass(EarningsCalendarItem, dict):
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
        if not isinstance(other, EarningsCalendarItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

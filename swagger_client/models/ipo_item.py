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

class IPOItem(object):
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
        'deal_status': 'str',
        'description': 'str',
        'initial_filing_date': 'str',
        'insider_lockup_date': 'str',
        'insider_lockup_days': 'int',
        'ipo_type': 'str',
        'last_yr_income': 'float',
        'last_yr_income_year': 'float',
        'last_yr_revenue': 'float',
        'last_yr_revenue_year': 'float',
        'lead_underwriters': 'list[str]',
        'market_cap_at_offer': 'float',
        'mic': 'str',
        'name': 'str',
        'notes': 'str',
        'offering_shares': 'float',
        'offering_shares_ord_adr': 'float',
        'offering_value': 'float',
        'open_date_verified': 'bool',
        'ord_shares_out_after_offer': 'float',
        'other_underwriters': 'list[str]',
        'price_max': 'float',
        'price_min': 'float',
        'price_open': 'float',
        'price_public_offering': 'float',
        'pricing_date': 'str',
        'record_id': 'str',
        'sec_accession_number': 'str',
        'sec_filing_url': 'str',
        'shares_outstanding': 'float',
        'sic': 'float',
        'spac_converted_to_target': 'bool',
        'state_location': 'str',
        'ticker': 'str',
        'time': 'str',
        'underwriter_quiet_expiration_date': 'str',
        'underwriter_quiet_expiration_days': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'currency': 'currency',
        '_date': 'date',
        'deal_status': 'deal_status',
        'description': 'description',
        'initial_filing_date': 'initial_filing_date',
        'insider_lockup_date': 'insider_lockup_date',
        'insider_lockup_days': 'insider_lockup_days',
        'ipo_type': 'ipo_type',
        'last_yr_income': 'last_yr_income',
        'last_yr_income_year': 'last_yr_income_year',
        'last_yr_revenue': 'last_yr_revenue',
        'last_yr_revenue_year': 'last_yr_revenue_year',
        'lead_underwriters': 'lead_underwriters',
        'market_cap_at_offer': 'market_cap_at_offer',
        'mic': 'mic',
        'name': 'name',
        'notes': 'notes',
        'offering_shares': 'offering_shares',
        'offering_shares_ord_adr': 'offering_shares_ord_adr',
        'offering_value': 'offering_value',
        'open_date_verified': 'open_date_verified',
        'ord_shares_out_after_offer': 'ord_shares_out_after_offer',
        'other_underwriters': 'other_underwriters',
        'price_max': 'price_max',
        'price_min': 'price_min',
        'price_open': 'price_open',
        'price_public_offering': 'price_public_offering',
        'pricing_date': 'pricing_date',
        'record_id': 'record_id',
        'sec_accession_number': 'sec_accession_number',
        'sec_filing_url': 'sec_filing_url',
        'shares_outstanding': 'shares_outstanding',
        'sic': 'sic',
        'spac_converted_to_target': 'spac_converted_to_target',
        'state_location': 'state_location',
        'ticker': 'ticker',
        'time': 'time',
        'underwriter_quiet_expiration_date': 'underwriter_quiet_expiration_date',
        'underwriter_quiet_expiration_days': 'underwriter_quiet_expiration_days',
        'updated': 'updated'
    }

    def __init__(self, currency=None, _date=None, deal_status=None, description=None, initial_filing_date=None, insider_lockup_date=None, insider_lockup_days=None, ipo_type=None, last_yr_income=None, last_yr_income_year=None, last_yr_revenue=None, last_yr_revenue_year=None, lead_underwriters=None, market_cap_at_offer=None, mic=None, name=None, notes=None, offering_shares=None, offering_shares_ord_adr=None, offering_value=None, open_date_verified=None, ord_shares_out_after_offer=None, other_underwriters=None, price_max=None, price_min=None, price_open=None, price_public_offering=None, pricing_date=None, record_id=None, sec_accession_number=None, sec_filing_url=None, shares_outstanding=None, sic=None, spac_converted_to_target=None, state_location=None, ticker=None, time=None, underwriter_quiet_expiration_date=None, underwriter_quiet_expiration_days=None, updated=None):  # noqa: E501
        """IPOItem - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self.__date = None
        self._deal_status = None
        self._description = None
        self._initial_filing_date = None
        self._insider_lockup_date = None
        self._insider_lockup_days = None
        self._ipo_type = None
        self._last_yr_income = None
        self._last_yr_income_year = None
        self._last_yr_revenue = None
        self._last_yr_revenue_year = None
        self._lead_underwriters = None
        self._market_cap_at_offer = None
        self._mic = None
        self._name = None
        self._notes = None
        self._offering_shares = None
        self._offering_shares_ord_adr = None
        self._offering_value = None
        self._open_date_verified = None
        self._ord_shares_out_after_offer = None
        self._other_underwriters = None
        self._price_max = None
        self._price_min = None
        self._price_open = None
        self._price_public_offering = None
        self._pricing_date = None
        self._record_id = None
        self._sec_accession_number = None
        self._sec_filing_url = None
        self._shares_outstanding = None
        self._sic = None
        self._spac_converted_to_target = None
        self._state_location = None
        self._ticker = None
        self._time = None
        self._underwriter_quiet_expiration_date = None
        self._underwriter_quiet_expiration_days = None
        self._updated = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if _date is not None:
            self._date = _date
        if deal_status is not None:
            self.deal_status = deal_status
        if description is not None:
            self.description = description
        if initial_filing_date is not None:
            self.initial_filing_date = initial_filing_date
        if insider_lockup_date is not None:
            self.insider_lockup_date = insider_lockup_date
        if insider_lockup_days is not None:
            self.insider_lockup_days = insider_lockup_days
        if ipo_type is not None:
            self.ipo_type = ipo_type
        if last_yr_income is not None:
            self.last_yr_income = last_yr_income
        if last_yr_income_year is not None:
            self.last_yr_income_year = last_yr_income_year
        if last_yr_revenue is not None:
            self.last_yr_revenue = last_yr_revenue
        if last_yr_revenue_year is not None:
            self.last_yr_revenue_year = last_yr_revenue_year
        if lead_underwriters is not None:
            self.lead_underwriters = lead_underwriters
        if market_cap_at_offer is not None:
            self.market_cap_at_offer = market_cap_at_offer
        if mic is not None:
            self.mic = mic
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if offering_shares is not None:
            self.offering_shares = offering_shares
        if offering_shares_ord_adr is not None:
            self.offering_shares_ord_adr = offering_shares_ord_adr
        if offering_value is not None:
            self.offering_value = offering_value
        if open_date_verified is not None:
            self.open_date_verified = open_date_verified
        if ord_shares_out_after_offer is not None:
            self.ord_shares_out_after_offer = ord_shares_out_after_offer
        if other_underwriters is not None:
            self.other_underwriters = other_underwriters
        if price_max is not None:
            self.price_max = price_max
        if price_min is not None:
            self.price_min = price_min
        if price_open is not None:
            self.price_open = price_open
        if price_public_offering is not None:
            self.price_public_offering = price_public_offering
        if pricing_date is not None:
            self.pricing_date = pricing_date
        if record_id is not None:
            self.record_id = record_id
        if sec_accession_number is not None:
            self.sec_accession_number = sec_accession_number
        if sec_filing_url is not None:
            self.sec_filing_url = sec_filing_url
        if shares_outstanding is not None:
            self.shares_outstanding = shares_outstanding
        if sic is not None:
            self.sic = sic
        if spac_converted_to_target is not None:
            self.spac_converted_to_target = spac_converted_to_target
        if state_location is not None:
            self.state_location = state_location
        if ticker is not None:
            self.ticker = ticker
        if time is not None:
            self.time = time
        if underwriter_quiet_expiration_date is not None:
            self.underwriter_quiet_expiration_date = underwriter_quiet_expiration_date
        if underwriter_quiet_expiration_days is not None:
            self.underwriter_quiet_expiration_days = underwriter_quiet_expiration_days
        if updated is not None:
            self.updated = updated

    @property
    def currency(self):
        """Gets the currency of this IPOItem.  # noqa: E501

        The currency code of the security according to the ISO 4217 standard  # noqa: E501

        :return: The currency of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IPOItem.

        The currency code of the security according to the ISO 4217 standard  # noqa: E501

        :param currency: The currency of this IPOItem.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def _date(self):
        """Gets the _date of this IPOItem.  # noqa: E501

        Date when earnings are disbursed  # noqa: E501

        :return: The _date of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this IPOItem.

        Date when earnings are disbursed  # noqa: E501

        :param _date: The _date of this IPOItem.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def deal_status(self):
        """Gets the deal_status of this IPOItem.  # noqa: E501

        Activity tracked for the IPO status  # noqa: E501

        :return: The deal_status of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._deal_status

    @deal_status.setter
    def deal_status(self, deal_status):
        """Sets the deal_status of this IPOItem.

        Activity tracked for the IPO status  # noqa: E501

        :param deal_status: The deal_status of this IPOItem.  # noqa: E501
        :type: str
        """

        self._deal_status = deal_status

    @property
    def description(self):
        """Gets the description of this IPOItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IPOItem.

        Description  # noqa: E501

        :param description: The description of this IPOItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def initial_filing_date(self):
        """Gets the initial_filing_date of this IPOItem.  # noqa: E501

        Initial filing date  # noqa: E501

        :return: The initial_filing_date of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._initial_filing_date

    @initial_filing_date.setter
    def initial_filing_date(self, initial_filing_date):
        """Sets the initial_filing_date of this IPOItem.

        Initial filing date  # noqa: E501

        :param initial_filing_date: The initial_filing_date of this IPOItem.  # noqa: E501
        :type: str
        """

        self._initial_filing_date = initial_filing_date

    @property
    def insider_lockup_date(self):
        """Gets the insider_lockup_date of this IPOItem.  # noqa: E501

        Date range that represents the insider lock up period  # noqa: E501

        :return: The insider_lockup_date of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._insider_lockup_date

    @insider_lockup_date.setter
    def insider_lockup_date(self, insider_lockup_date):
        """Sets the insider_lockup_date of this IPOItem.

        Date range that represents the insider lock up period  # noqa: E501

        :param insider_lockup_date: The insider_lockup_date of this IPOItem.  # noqa: E501
        :type: str
        """

        self._insider_lockup_date = insider_lockup_date

    @property
    def insider_lockup_days(self):
        """Gets the insider_lockup_days of this IPOItem.  # noqa: E501

        Amount of days for the insider lockup period  # noqa: E501

        :return: The insider_lockup_days of this IPOItem.  # noqa: E501
        :rtype: int
        """
        return self._insider_lockup_days

    @insider_lockup_days.setter
    def insider_lockup_days(self, insider_lockup_days):
        """Sets the insider_lockup_days of this IPOItem.

        Amount of days for the insider lockup period  # noqa: E501

        :param insider_lockup_days: The insider_lockup_days of this IPOItem.  # noqa: E501
        :type: int
        """

        self._insider_lockup_days = insider_lockup_days

    @property
    def ipo_type(self):
        """Gets the ipo_type of this IPOItem.  # noqa: E501

        IPO type  # noqa: E501

        :return: The ipo_type of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._ipo_type

    @ipo_type.setter
    def ipo_type(self, ipo_type):
        """Sets the ipo_type of this IPOItem.

        IPO type  # noqa: E501

        :param ipo_type: The ipo_type of this IPOItem.  # noqa: E501
        :type: str
        """

        self._ipo_type = ipo_type

    @property
    def last_yr_income(self):
        """Gets the last_yr_income of this IPOItem.  # noqa: E501

        Last year income  # noqa: E501

        :return: The last_yr_income of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._last_yr_income

    @last_yr_income.setter
    def last_yr_income(self, last_yr_income):
        """Sets the last_yr_income of this IPOItem.

        Last year income  # noqa: E501

        :param last_yr_income: The last_yr_income of this IPOItem.  # noqa: E501
        :type: float
        """

        self._last_yr_income = last_yr_income

    @property
    def last_yr_income_year(self):
        """Gets the last_yr_income_year of this IPOItem.  # noqa: E501

        Last year income  # noqa: E501

        :return: The last_yr_income_year of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._last_yr_income_year

    @last_yr_income_year.setter
    def last_yr_income_year(self, last_yr_income_year):
        """Sets the last_yr_income_year of this IPOItem.

        Last year income  # noqa: E501

        :param last_yr_income_year: The last_yr_income_year of this IPOItem.  # noqa: E501
        :type: float
        """

        self._last_yr_income_year = last_yr_income_year

    @property
    def last_yr_revenue(self):
        """Gets the last_yr_revenue of this IPOItem.  # noqa: E501

        Last year revenue  # noqa: E501

        :return: The last_yr_revenue of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._last_yr_revenue

    @last_yr_revenue.setter
    def last_yr_revenue(self, last_yr_revenue):
        """Sets the last_yr_revenue of this IPOItem.

        Last year revenue  # noqa: E501

        :param last_yr_revenue: The last_yr_revenue of this IPOItem.  # noqa: E501
        :type: float
        """

        self._last_yr_revenue = last_yr_revenue

    @property
    def last_yr_revenue_year(self):
        """Gets the last_yr_revenue_year of this IPOItem.  # noqa: E501

        Last year revenue  # noqa: E501

        :return: The last_yr_revenue_year of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._last_yr_revenue_year

    @last_yr_revenue_year.setter
    def last_yr_revenue_year(self, last_yr_revenue_year):
        """Sets the last_yr_revenue_year of this IPOItem.

        Last year revenue  # noqa: E501

        :param last_yr_revenue_year: The last_yr_revenue_year of this IPOItem.  # noqa: E501
        :type: float
        """

        self._last_yr_revenue_year = last_yr_revenue_year

    @property
    def lead_underwriters(self):
        """Gets the lead_underwriters of this IPOItem.  # noqa: E501

        Firm that lead the underwriting process  # noqa: E501

        :return: The lead_underwriters of this IPOItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._lead_underwriters

    @lead_underwriters.setter
    def lead_underwriters(self, lead_underwriters):
        """Sets the lead_underwriters of this IPOItem.

        Firm that lead the underwriting process  # noqa: E501

        :param lead_underwriters: The lead_underwriters of this IPOItem.  # noqa: E501
        :type: list[str]
        """

        self._lead_underwriters = lead_underwriters

    @property
    def market_cap_at_offer(self):
        """Gets the market_cap_at_offer of this IPOItem.  # noqa: E501

        Market cap at offer  # noqa: E501

        :return: The market_cap_at_offer of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._market_cap_at_offer

    @market_cap_at_offer.setter
    def market_cap_at_offer(self, market_cap_at_offer):
        """Sets the market_cap_at_offer of this IPOItem.

        Market cap at offer  # noqa: E501

        :param market_cap_at_offer: The market_cap_at_offer of this IPOItem.  # noqa: E501
        :type: float
        """

        self._market_cap_at_offer = market_cap_at_offer

    @property
    def mic(self):
        """Gets the mic of this IPOItem.  # noqa: E501

        Market identifier code (MIC) under ISO 10383 standard  # noqa: E501

        :return: The mic of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._mic

    @mic.setter
    def mic(self, mic):
        """Sets the mic of this IPOItem.

        Market identifier code (MIC) under ISO 10383 standard  # noqa: E501

        :param mic: The mic of this IPOItem.  # noqa: E501
        :type: str
        """

        self._mic = mic

    @property
    def name(self):
        """Gets the name of this IPOItem.  # noqa: E501

        Full name of the instrument  # noqa: E501

        :return: The name of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IPOItem.

        Full name of the instrument  # noqa: E501

        :param name: The name of this IPOItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this IPOItem.  # noqa: E501

        Notes  # noqa: E501

        :return: The notes of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this IPOItem.

        Notes  # noqa: E501

        :param notes: The notes of this IPOItem.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def offering_shares(self):
        """Gets the offering_shares of this IPOItem.  # noqa: E501

        Amount of shares being offered  # noqa: E501

        :return: The offering_shares of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._offering_shares

    @offering_shares.setter
    def offering_shares(self, offering_shares):
        """Sets the offering_shares of this IPOItem.

        Amount of shares being offered  # noqa: E501

        :param offering_shares: The offering_shares of this IPOItem.  # noqa: E501
        :type: float
        """

        self._offering_shares = offering_shares

    @property
    def offering_shares_ord_adr(self):
        """Gets the offering_shares_ord_adr of this IPOItem.  # noqa: E501

        Amount of ordinary shares being offered  # noqa: E501

        :return: The offering_shares_ord_adr of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._offering_shares_ord_adr

    @offering_shares_ord_adr.setter
    def offering_shares_ord_adr(self, offering_shares_ord_adr):
        """Sets the offering_shares_ord_adr of this IPOItem.

        Amount of ordinary shares being offered  # noqa: E501

        :param offering_shares_ord_adr: The offering_shares_ord_adr of this IPOItem.  # noqa: E501
        :type: float
        """

        self._offering_shares_ord_adr = offering_shares_ord_adr

    @property
    def offering_value(self):
        """Gets the offering_value of this IPOItem.  # noqa: E501

        Number of shares being offered x price per share  # noqa: E501

        :return: The offering_value of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._offering_value

    @offering_value.setter
    def offering_value(self, offering_value):
        """Sets the offering_value of this IPOItem.

        Number of shares being offered x price per share  # noqa: E501

        :param offering_value: The offering_value of this IPOItem.  # noqa: E501
        :type: float
        """

        self._offering_value = offering_value

    @property
    def open_date_verified(self):
        """Gets the open_date_verified of this IPOItem.  # noqa: E501

        Indicates if the predicted date has been verified by the company  # noqa: E501

        :return: The open_date_verified of this IPOItem.  # noqa: E501
        :rtype: bool
        """
        return self._open_date_verified

    @open_date_verified.setter
    def open_date_verified(self, open_date_verified):
        """Sets the open_date_verified of this IPOItem.

        Indicates if the predicted date has been verified by the company  # noqa: E501

        :param open_date_verified: The open_date_verified of this IPOItem.  # noqa: E501
        :type: bool
        """

        self._open_date_verified = open_date_verified

    @property
    def ord_shares_out_after_offer(self):
        """Gets the ord_shares_out_after_offer of this IPOItem.  # noqa: E501

        Ordinary shares out after offer  # noqa: E501

        :return: The ord_shares_out_after_offer of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._ord_shares_out_after_offer

    @ord_shares_out_after_offer.setter
    def ord_shares_out_after_offer(self, ord_shares_out_after_offer):
        """Sets the ord_shares_out_after_offer of this IPOItem.

        Ordinary shares out after offer  # noqa: E501

        :param ord_shares_out_after_offer: The ord_shares_out_after_offer of this IPOItem.  # noqa: E501
        :type: float
        """

        self._ord_shares_out_after_offer = ord_shares_out_after_offer

    @property
    def other_underwriters(self):
        """Gets the other_underwriters of this IPOItem.  # noqa: E501

        Additional firms that were a part of the underwriting  # noqa: E501

        :return: The other_underwriters of this IPOItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._other_underwriters

    @other_underwriters.setter
    def other_underwriters(self, other_underwriters):
        """Sets the other_underwriters of this IPOItem.

        Additional firms that were a part of the underwriting  # noqa: E501

        :param other_underwriters: The other_underwriters of this IPOItem.  # noqa: E501
        :type: list[str]
        """

        self._other_underwriters = other_underwriters

    @property
    def price_max(self):
        """Gets the price_max of this IPOItem.  # noqa: E501

        Maximum projected IPO price range  # noqa: E501

        :return: The price_max of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._price_max

    @price_max.setter
    def price_max(self, price_max):
        """Sets the price_max of this IPOItem.

        Maximum projected IPO price range  # noqa: E501

        :param price_max: The price_max of this IPOItem.  # noqa: E501
        :type: float
        """

        self._price_max = price_max

    @property
    def price_min(self):
        """Gets the price_min of this IPOItem.  # noqa: E501

        Minimum  projected IPO price range  # noqa: E501

        :return: The price_min of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._price_min

    @price_min.setter
    def price_min(self, price_min):
        """Sets the price_min of this IPOItem.

        Minimum  projected IPO price range  # noqa: E501

        :param price_min: The price_min of this IPOItem.  # noqa: E501
        :type: float
        """

        self._price_min = price_min

    @property
    def price_open(self):
        """Gets the price_open of this IPOItem.  # noqa: E501

        The opening price at the beginning of the first trading day (only available for priced IPOs)  # noqa: E501

        :return: The price_open of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._price_open

    @price_open.setter
    def price_open(self, price_open):
        """Sets the price_open of this IPOItem.

        The opening price at the beginning of the first trading day (only available for priced IPOs)  # noqa: E501

        :param price_open: The price_open of this IPOItem.  # noqa: E501
        :type: float
        """

        self._price_open = price_open

    @property
    def price_public_offering(self):
        """Gets the price_public_offering of this IPOItem.  # noqa: E501

        Public offering price  # noqa: E501

        :return: The price_public_offering of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._price_public_offering

    @price_public_offering.setter
    def price_public_offering(self, price_public_offering):
        """Sets the price_public_offering of this IPOItem.

        Public offering price  # noqa: E501

        :param price_public_offering: The price_public_offering of this IPOItem.  # noqa: E501
        :type: float
        """

        self._price_public_offering = price_public_offering

    @property
    def pricing_date(self):
        """Gets the pricing_date of this IPOItem.  # noqa: E501

        Pricing date  # noqa: E501

        :return: The pricing_date of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._pricing_date

    @pricing_date.setter
    def pricing_date(self, pricing_date):
        """Sets the pricing_date of this IPOItem.

        Pricing date  # noqa: E501

        :param pricing_date: The pricing_date of this IPOItem.  # noqa: E501
        :type: str
        """

        self._pricing_date = pricing_date

    @property
    def record_id(self):
        """Gets the record_id of this IPOItem.  # noqa: E501

        Unique record ID from Benzinga  # noqa: E501

        :return: The record_id of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this IPOItem.

        Unique record ID from Benzinga  # noqa: E501

        :param record_id: The record_id of this IPOItem.  # noqa: E501
        :type: str
        """

        self._record_id = record_id

    @property
    def sec_accession_number(self):
        """Gets the sec_accession_number of this IPOItem.  # noqa: E501

        SEC accession number  # noqa: E501

        :return: The sec_accession_number of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._sec_accession_number

    @sec_accession_number.setter
    def sec_accession_number(self, sec_accession_number):
        """Sets the sec_accession_number of this IPOItem.

        SEC accession number  # noqa: E501

        :param sec_accession_number: The sec_accession_number of this IPOItem.  # noqa: E501
        :type: str
        """

        self._sec_accession_number = sec_accession_number

    @property
    def sec_filing_url(self):
        """Gets the sec_filing_url of this IPOItem.  # noqa: E501

        The IRL to the company's S-1, S-1/A, F-1, or F-1/A SEC filing, which is required to be filed before an IPO takes place.  # noqa: E501

        :return: The sec_filing_url of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._sec_filing_url

    @sec_filing_url.setter
    def sec_filing_url(self, sec_filing_url):
        """Sets the sec_filing_url of this IPOItem.

        The IRL to the company's S-1, S-1/A, F-1, or F-1/A SEC filing, which is required to be filed before an IPO takes place.  # noqa: E501

        :param sec_filing_url: The sec_filing_url of this IPOItem.  # noqa: E501
        :type: str
        """

        self._sec_filing_url = sec_filing_url

    @property
    def shares_outstanding(self):
        """Gets the shares_outstanding of this IPOItem.  # noqa: E501

        Outstanding shares  # noqa: E501

        :return: The shares_outstanding of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._shares_outstanding

    @shares_outstanding.setter
    def shares_outstanding(self, shares_outstanding):
        """Sets the shares_outstanding of this IPOItem.

        Outstanding shares  # noqa: E501

        :param shares_outstanding: The shares_outstanding of this IPOItem.  # noqa: E501
        :type: float
        """

        self._shares_outstanding = shares_outstanding

    @property
    def sic(self):
        """Gets the sic of this IPOItem.  # noqa: E501

        SIC  # noqa: E501

        :return: The sic of this IPOItem.  # noqa: E501
        :rtype: float
        """
        return self._sic

    @sic.setter
    def sic(self, sic):
        """Sets the sic of this IPOItem.

        SIC  # noqa: E501

        :param sic: The sic of this IPOItem.  # noqa: E501
        :type: float
        """

        self._sic = sic

    @property
    def spac_converted_to_target(self):
        """Gets the spac_converted_to_target of this IPOItem.  # noqa: E501

        ISs Spac converted to target  # noqa: E501

        :return: The spac_converted_to_target of this IPOItem.  # noqa: E501
        :rtype: bool
        """
        return self._spac_converted_to_target

    @spac_converted_to_target.setter
    def spac_converted_to_target(self, spac_converted_to_target):
        """Sets the spac_converted_to_target of this IPOItem.

        ISs Spac converted to target  # noqa: E501

        :param spac_converted_to_target: The spac_converted_to_target of this IPOItem.  # noqa: E501
        :type: bool
        """

        self._spac_converted_to_target = spac_converted_to_target

    @property
    def state_location(self):
        """Gets the state_location of this IPOItem.  # noqa: E501

        State location  # noqa: E501

        :return: The state_location of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._state_location

    @state_location.setter
    def state_location(self, state_location):
        """Sets the state_location of this IPOItem.

        State location  # noqa: E501

        :param state_location: The state_location of this IPOItem.  # noqa: E501
        :type: str
        """

        self._state_location = state_location

    @property
    def ticker(self):
        """Gets the ticker of this IPOItem.  # noqa: E501

        Ticker symbol of the instrument  # noqa: E501

        :return: The ticker of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this IPOItem.

        Ticker symbol of the instrument  # noqa: E501

        :param ticker: The ticker of this IPOItem.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def time(self):
        """Gets the time of this IPOItem.  # noqa: E501

        Time when earnings are disbursed  # noqa: E501

        :return: The time of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this IPOItem.

        Time when earnings are disbursed  # noqa: E501

        :param time: The time of this IPOItem.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def underwriter_quiet_expiration_date(self):
        """Gets the underwriter_quiet_expiration_date of this IPOItem.  # noqa: E501

        Date of expiration for the underwriter quiet period  # noqa: E501

        :return: The underwriter_quiet_expiration_date of this IPOItem.  # noqa: E501
        :rtype: str
        """
        return self._underwriter_quiet_expiration_date

    @underwriter_quiet_expiration_date.setter
    def underwriter_quiet_expiration_date(self, underwriter_quiet_expiration_date):
        """Sets the underwriter_quiet_expiration_date of this IPOItem.

        Date of expiration for the underwriter quiet period  # noqa: E501

        :param underwriter_quiet_expiration_date: The underwriter_quiet_expiration_date of this IPOItem.  # noqa: E501
        :type: str
        """

        self._underwriter_quiet_expiration_date = underwriter_quiet_expiration_date

    @property
    def underwriter_quiet_expiration_days(self):
        """Gets the underwriter_quiet_expiration_days of this IPOItem.  # noqa: E501

        Days of expiration for the underwriter quiet period  # noqa: E501

        :return: The underwriter_quiet_expiration_days of this IPOItem.  # noqa: E501
        :rtype: int
        """
        return self._underwriter_quiet_expiration_days

    @underwriter_quiet_expiration_days.setter
    def underwriter_quiet_expiration_days(self, underwriter_quiet_expiration_days):
        """Sets the underwriter_quiet_expiration_days of this IPOItem.

        Days of expiration for the underwriter quiet period  # noqa: E501

        :param underwriter_quiet_expiration_days: The underwriter_quiet_expiration_days of this IPOItem.  # noqa: E501
        :type: int
        """

        self._underwriter_quiet_expiration_days = underwriter_quiet_expiration_days

    @property
    def updated(self):
        """Gets the updated of this IPOItem.  # noqa: E501

        Last updated timestamp (UNIX)  # noqa: E501

        :return: The updated of this IPOItem.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this IPOItem.

        Last updated timestamp (UNIX)  # noqa: E501

        :param updated: The updated of this IPOItem.  # noqa: E501
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
        if issubclass(IPOItem, dict):
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
        if not isinstance(other, IPOItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

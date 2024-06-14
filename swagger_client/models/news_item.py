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

class NewsItem(object):
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
        'author': 'str',
        'channels': 'list[str]',
        'created_at': 'datetime',
        'images': 'list[str]',
        'record_id': 'int',
        'tags': 'list[str]',
        'tickers': 'list[str]',
        'title': 'str',
        'updated_at': 'datetime',
        'url': 'str'
    }

    attribute_map = {
        'author': 'author',
        'channels': 'channels',
        'created_at': 'created_at',
        'images': 'images',
        'record_id': 'record_id',
        'tags': 'tags',
        'tickers': 'tickers',
        'title': 'title',
        'updated_at': 'updated_at',
        'url': 'url'
    }

    def __init__(self, author=None, channels=None, created_at=None, images=None, record_id=None, tags=None, tickers=None, title=None, updated_at=None, url=None):  # noqa: E501
        """NewsItem - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._channels = None
        self._created_at = None
        self._images = None
        self._record_id = None
        self._tags = None
        self._tickers = None
        self._title = None
        self._updated_at = None
        self._url = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if channels is not None:
            self.channels = channels
        if created_at is not None:
            self.created_at = created_at
        if images is not None:
            self.images = images
        if record_id is not None:
            self.record_id = record_id
        if tags is not None:
            self.tags = tags
        if tickers is not None:
            self.tickers = tickers
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at
        if url is not None:
            self.url = url

    @property
    def author(self):
        """Gets the author of this NewsItem.  # noqa: E501

        Author of the news article  # noqa: E501

        :return: The author of this NewsItem.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this NewsItem.

        Author of the news article  # noqa: E501

        :param author: The author of this NewsItem.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def channels(self):
        """Gets the channels of this NewsItem.  # noqa: E501

        Channels of the news article  # noqa: E501

        :return: The channels of this NewsItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this NewsItem.

        Channels of the news article  # noqa: E501

        :param channels: The channels of this NewsItem.  # noqa: E501
        :type: list[str]
        """

        self._channels = channels

    @property
    def created_at(self):
        """Gets the created_at of this NewsItem.  # noqa: E501

        Timestamp indicating when the news article was generated  # noqa: E501

        :return: The created_at of this NewsItem.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NewsItem.

        Timestamp indicating when the news article was generated  # noqa: E501

        :param created_at: The created_at of this NewsItem.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def images(self):
        """Gets the images of this NewsItem.  # noqa: E501

        Images of the news article  # noqa: E501

        :return: The images of this NewsItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this NewsItem.

        Images of the news article  # noqa: E501

        :param images: The images of this NewsItem.  # noqa: E501
        :type: list[str]
        """

        self._images = images

    @property
    def record_id(self):
        """Gets the record_id of this NewsItem.  # noqa: E501

        Unique record ID from Benzinga  # noqa: E501

        :return: The record_id of this NewsItem.  # noqa: E501
        :rtype: int
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this NewsItem.

        Unique record ID from Benzinga  # noqa: E501

        :param record_id: The record_id of this NewsItem.  # noqa: E501
        :type: int
        """

        self._record_id = record_id

    @property
    def tags(self):
        """Gets the tags of this NewsItem.  # noqa: E501

        Tags of the news article  # noqa: E501

        :return: The tags of this NewsItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NewsItem.

        Tags of the news article  # noqa: E501

        :param tags: The tags of this NewsItem.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def tickers(self):
        """Gets the tickers of this NewsItem.  # noqa: E501

        The ticker symbols related to the news article  # noqa: E501

        :return: The tickers of this NewsItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._tickers

    @tickers.setter
    def tickers(self, tickers):
        """Sets the tickers of this NewsItem.

        The ticker symbols related to the news article  # noqa: E501

        :param tickers: The tickers of this NewsItem.  # noqa: E501
        :type: list[str]
        """

        self._tickers = tickers

    @property
    def title(self):
        """Gets the title of this NewsItem.  # noqa: E501

        Title of the news article  # noqa: E501

        :return: The title of this NewsItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewsItem.

        Title of the news article  # noqa: E501

        :param title: The title of this NewsItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this NewsItem.  # noqa: E501

        Timestamp indicating when the news article was last updated  # noqa: E501

        :return: The updated_at of this NewsItem.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NewsItem.

        Timestamp indicating when the news article was last updated  # noqa: E501

        :param updated_at: The updated_at of this NewsItem.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this NewsItem.  # noqa: E501

        URL link directing to the complete news story  # noqa: E501

        :return: The url of this NewsItem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NewsItem.

        URL link directing to the complete news story  # noqa: E501

        :param url: The url of this NewsItem.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(NewsItem, dict):
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
        if not isinstance(other, NewsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
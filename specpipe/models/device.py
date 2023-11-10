# coding: utf-8

"""
    SpecPipe Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Device(object):
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
        'name': 'str',
        'sample_rate': 'str',
        'freq': 'str',
        'longitude': 'float',
        'latitude': 'float'
    }

    attribute_map = {
        'name': 'name',
        'sample_rate': 'sample_rate',
        'freq': 'freq',
        'longitude': 'longitude',
        'latitude': 'latitude'
    }

    def __init__(self, name=None, sample_rate=None, freq=None, longitude=None, latitude=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._sample_rate = None
        self._freq = None
        self._longitude = None
        self._latitude = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if freq is not None:
            self.freq = freq
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501


        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.


        :param name: The name of this Device.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sample_rate(self):
        """Gets the sample_rate of this Device.  # noqa: E501


        :return: The sample_rate of this Device.  # noqa: E501
        :rtype: str
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this Device.


        :param sample_rate: The sample_rate of this Device.  # noqa: E501
        :type: str
        """

        self._sample_rate = sample_rate

    @property
    def freq(self):
        """Gets the freq of this Device.  # noqa: E501


        :return: The freq of this Device.  # noqa: E501
        :rtype: str
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this Device.


        :param freq: The freq of this Device.  # noqa: E501
        :type: str
        """

        self._freq = freq

    @property
    def longitude(self):
        """Gets the longitude of this Device.  # noqa: E501


        :return: The longitude of this Device.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Device.


        :param longitude: The longitude of this Device.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this Device.  # noqa: E501


        :return: The latitude of this Device.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Device.


        :param latitude: The latitude of this Device.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
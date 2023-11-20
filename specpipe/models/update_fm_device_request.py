# coding: utf-8

"""
    SpecPipe Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateFmDeviceRequest(object):
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
        'freq': 'str',
        'sample_rate': 'str',
        'resample_rate': 'str'
    }

    attribute_map = {
        'freq': 'freq',
        'sample_rate': 'sample_rate',
        'resample_rate': 'resample_rate'
    }

    def __init__(self, freq=None, sample_rate=None, resample_rate=None):  # noqa: E501
        """UpdateFmDeviceRequest - a model defined in Swagger"""  # noqa: E501
        self._freq = None
        self._sample_rate = None
        self._resample_rate = None
        self.discriminator = None
        self.freq = freq
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if resample_rate is not None:
            self.resample_rate = resample_rate

    @property
    def freq(self):
        """Gets the freq of this UpdateFmDeviceRequest.  # noqa: E501


        :return: The freq of this UpdateFmDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this UpdateFmDeviceRequest.


        :param freq: The freq of this UpdateFmDeviceRequest.  # noqa: E501
        :type: str
        """
        if freq is None:
            raise ValueError("Invalid value for `freq`, must not be `None`")  # noqa: E501

        self._freq = freq

    @property
    def sample_rate(self):
        """Gets the sample_rate of this UpdateFmDeviceRequest.  # noqa: E501


        :return: The sample_rate of this UpdateFmDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this UpdateFmDeviceRequest.


        :param sample_rate: The sample_rate of this UpdateFmDeviceRequest.  # noqa: E501
        :type: str
        """

        self._sample_rate = sample_rate

    @property
    def resample_rate(self):
        """Gets the resample_rate of this UpdateFmDeviceRequest.  # noqa: E501


        :return: The resample_rate of this UpdateFmDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._resample_rate

    @resample_rate.setter
    def resample_rate(self, resample_rate):
        """Sets the resample_rate of this UpdateFmDeviceRequest.


        :param resample_rate: The resample_rate of this UpdateFmDeviceRequest.  # noqa: E501
        :type: str
        """

        self._resample_rate = resample_rate

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
        if issubclass(UpdateFmDeviceRequest, dict):
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
        if not isinstance(other, UpdateFmDeviceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

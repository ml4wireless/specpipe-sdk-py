# coding: utf-8

"""
    SpecPipe Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import specpipe
from specpipe.api.device_api import DeviceApi  # noqa: E501
from specpipe.rest import ApiException


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self):
        self.api = DeviceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fm_devices_devicename_get(self):
        """Test case for fm_devices_devicename_get

        Read FM device configuration  # noqa: E501
        """
        pass

    def test_fm_devices_devicename_put(self):
        """Test case for fm_devices_devicename_put

        Update FM device  # noqa: E501
        """
        pass

    def test_fm_devices_get(self):
        """Test case for fm_devices_get

        List FM devices  # noqa: E501
        """
        pass

    def test_iq_devices_devicename_get(self):
        """Test case for iq_devices_devicename_get

        Read IQ device configuration  # noqa: E501
        """
        pass

    def test_iq_devices_devicename_put(self):
        """Test case for iq_devices_devicename_put

        Update IQ device  # noqa: E501
        """
        pass

    def test_iq_devices_get(self):
        """Test case for iq_devices_get

        List IQ devices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

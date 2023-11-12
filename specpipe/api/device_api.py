# coding: utf-8

"""
    SpecPipe Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from specpipe.api_client import ApiClient


class DeviceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fm_devices_devicename_get(self, devicename, **kwargs):  # noqa: E501
        """Read FM device configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fm_devices_devicename_get(devicename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str devicename: device name (required)
        :return: FmDeviceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fm_devices_devicename_get_with_http_info(devicename, **kwargs)  # noqa: E501
        else:
            (data) = self.fm_devices_devicename_get_with_http_info(devicename, **kwargs)  # noqa: E501
            return data

    def fm_devices_devicename_get_with_http_info(self, devicename, **kwargs):  # noqa: E501
        """Read FM device configuration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fm_devices_devicename_get_with_http_info(devicename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str devicename: device name (required)
        :return: FmDeviceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['devicename']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fm_devices_devicename_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'devicename' is set
        if ('devicename' not in params or
                params['devicename'] is None):
            raise ValueError("Missing the required parameter `devicename` when calling `fm_devices_devicename_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'devicename' in params:
            path_params['devicename'] = params['devicename']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/fm/devices/{devicename}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FmDeviceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fm_devices_devicename_put(self, body, devicename, **kwargs):  # noqa: E501
        """Update FM device  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fm_devices_devicename_put(body, devicename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateFmDeviceRequest body: (required)
        :param str devicename: device name (required)
        :return: FmDeviceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fm_devices_devicename_put_with_http_info(body, devicename, **kwargs)  # noqa: E501
        else:
            (data) = self.fm_devices_devicename_put_with_http_info(body, devicename, **kwargs)  # noqa: E501
            return data

    def fm_devices_devicename_put_with_http_info(self, body, devicename, **kwargs):  # noqa: E501
        """Update FM device  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fm_devices_devicename_put_with_http_info(body, devicename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateFmDeviceRequest body: (required)
        :param str devicename: device name (required)
        :return: FmDeviceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'devicename']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fm_devices_devicename_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `fm_devices_devicename_put`")  # noqa: E501
        # verify the required parameter 'devicename' is set
        if ('devicename' not in params or
                params['devicename'] is None):
            raise ValueError("Missing the required parameter `devicename` when calling `fm_devices_devicename_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'devicename' in params:
            path_params['devicename'] = params['devicename']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/fm/devices/{devicename}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FmDeviceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fm_devices_get(self, **kwargs):  # noqa: E501
        """List FM devices  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fm_devices_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FmDevicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fm_devices_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fm_devices_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def fm_devices_get_with_http_info(self, **kwargs):  # noqa: E501
        """List FM devices  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fm_devices_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FmDevicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fm_devices_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/fm/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FmDevicesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

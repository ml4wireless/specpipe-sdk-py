# specpipe.DeviceApi

All URIs are relative to */v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fm_devices_deviceid_get**](DeviceApi.md#fm_devices_deviceid_get) | **GET** /fm/devices/{deviceid} | Read FM device configuration
[**fm_devices_deviceid_put**](DeviceApi.md#fm_devices_deviceid_put) | **PUT** /fm/devices/{deviceid} | Update FM device
[**fm_devices_get**](DeviceApi.md#fm_devices_get) | **GET** /fm/devices | List FM devices

# **fm_devices_deviceid_get**
> FmDeviceResponse fm_devices_deviceid_get(deviceid)

Read FM device configuration

### Example
```python
from __future__ import print_function
import time
import specpipe
from specpipe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = specpipe.DeviceApi()
deviceid = 'deviceid_example' # str | deviceid

try:
    # Read FM device configuration
    api_response = api_instance.fm_devices_deviceid_get(deviceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->fm_devices_deviceid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceid** | **str**| deviceid | 

### Return type

[**FmDeviceResponse**](FmDeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fm_devices_deviceid_put**
> FmDeviceResponse fm_devices_deviceid_put(body, deviceid)

Update FM device

### Example
```python
from __future__ import print_function
import time
import specpipe
from specpipe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = specpipe.DeviceApi()
body = specpipe.UpdateFmDeviceRequest() # UpdateFmDeviceRequest | 
deviceid = 'deviceid_example' # str | deviceid

try:
    # Update FM device
    api_response = api_instance.fm_devices_deviceid_put(body, deviceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->fm_devices_deviceid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFmDeviceRequest**](UpdateFmDeviceRequest.md)|  | 
 **deviceid** | **str**| deviceid | 

### Return type

[**FmDeviceResponse**](FmDeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fm_devices_get**
> FmDevicesResponse fm_devices_get()

List FM devices

### Example
```python
from __future__ import print_function
import time
import specpipe
from specpipe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = specpipe.DeviceApi()

try:
    # List FM devices
    api_response = api_instance.fm_devices_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->fm_devices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FmDevicesResponse**](FmDevicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


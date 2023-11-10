# specpipe.DeviceApi

All URIs are relative to */v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_deviceid_get**](DeviceApi.md#devices_deviceid_get) | **GET** /devices/{deviceid} | Read device configuration
[**devices_deviceid_put**](DeviceApi.md#devices_deviceid_put) | **PUT** /devices/{deviceid} | Update device
[**devices_get**](DeviceApi.md#devices_get) | **GET** /devices | List devices

# **devices_deviceid_get**
> DeviceResponse devices_deviceid_get(deviceid)

Read device configuration

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
    # Read device configuration
    api_response = api_instance.devices_deviceid_get(deviceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->devices_deviceid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceid** | **str**| deviceid | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_deviceid_put**
> DeviceResponse devices_deviceid_put(body, deviceid)

Update device

### Example
```python
from __future__ import print_function
import time
import specpipe
from specpipe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = specpipe.DeviceApi()
body = specpipe.UpdateDeviceRequest() # UpdateDeviceRequest | 
deviceid = 'deviceid_example' # str | deviceid

try:
    # Update device
    api_response = api_instance.devices_deviceid_put(body, deviceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->devices_deviceid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDeviceRequest**](UpdateDeviceRequest.md)|  | 
 **deviceid** | **str**| deviceid | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get**
> DevicesResponse devices_get()

List devices

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
    # List devices
    api_response = api_instance.devices_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->devices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevicesResponse**](DevicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


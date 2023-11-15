from specpipe.rest import ApiException
from pprint import pprint
from specpipe.models.update_fm_device_request import UpdateFmDeviceRequest
from specpipe.models.update_iq_device_request import UpdateIqDeviceRequest


class Device(object):
    def __init__(self, api_instance):
        self.api_instance = api_instance
    def fm_get_device(self, devicename=None):
        # Read FM device configuration
        try:
            response = self.api_instance.fm_devices_devicename_get(devicename)
            return response.device
        except ApiException as e:
            print("Exception when calling DeviceApi->fm_devices_devicename_get: %s\n" % e)
    def fm_update_device(self, devicename, freq=None, sample_rate=None):
        # Update FM device
        try:
            body = UpdateFmDeviceRequest(freq, sample_rate)
            api_response = self.api_instance.fm_devices_devicename_put(body, devicename)
        except ApiException as e:
            print("Exception when calling DeviceApi->fm_devices_devicename_put: %s\n" % e)
    def fm_get_devices(self):
        # List FM devices
        try:
            reponse = self.api_instance.fm_devices_get()
            return reponse.devices    
        except ApiException as e:
            print("Exception when calling DeviceApi->fm_devices_get: %s\n" % e)
    def iq_get_device(self, devicename=None):
        # Read IQ device configuration
        try:
            response = self.api_instance.iq_devices_devicename_get(devicename)
            return response.devices
        except ApiException as e:
            print("Exception when calling DeviceApi->iq_devices_devicename_get: %s\n" % e)
    def iq_update_device(self, devicename, freq=None, sample_rate=None):
        # Update IQ device
        try:
            body = UpdateIqDeviceRequest(freq, sample_rate)
            response = self.api_instance.iq_devices_devicename_put(body, devicename)
            pprint(response)
        except ApiException as e:
            print("Exception when calling DeviceApi->iq_devices_devicename_put: %s\n" % e)
    def iq_get_devices(self):
        # List IQ devices
        try:
            response = self.api_instance.iq_devices_get()
            return response.devices
        except ApiException as e:
            print("Exception when calling DeviceApi->iq_devices_get: %s\n" % e)

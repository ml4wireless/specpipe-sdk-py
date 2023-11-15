from __future__ import absolute_import

from specpipe.api.device_api import DeviceApi
# import ApiClient
from specpipe.api_client import ApiClient
from specpipe.configuration import Configuration
from specpipe.models.fm_device import FmDevice
from device import Device

class SpecPipe(object):
    def __init__(self, api_url, nats_url):
        self.nats_url = nats_url
        self.api_url = api_url
        _api_client_config = Configuration()
        _api_client_config.host = api_url + "/v0"
        self._api_client_config =  _api_client_config
        self._api_instance = DeviceApi(ApiClient(_api_client_config))
        self.device = Device(self._api_instance)

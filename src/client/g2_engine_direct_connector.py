import sys
import warnings
import json

try:
    from senzing import G2Engine
except ModuleNotFoundError:
    warnings.warn('Cannot import Senzing python libraries.')
    warnings.warn('Please verify your PYTHONPATH includes the path to senzing python libs')
    warnings.warn('Environment can be setup by sourcing "setupEnv" '\
                  'from your senzing project directory')
    sys.exit(-1)


class G2EngineDirectConnector:
    def __init__(self):
        self.g2_handle = None

    # startup/shutdown methods
    def init(self, url, module_name, ini_params, verbose_logging=False):
        if isinstance(ini_params, str):
            ini_params = json.loads(ini_params)
        self.g2_handle = G2Engine()
        return self.g2_handle.init(module_name, ini_params, verbose_logging)

    def init_with_url(self, url):
        warnings.warn('init_with_url is not valid for direct connections')

    def init_direct_from_environment(self, module_name, verbose_logging=False):
        import senzing_module_config
        json_config = senzing_module_config.get_json_config()
        self.g2_handle = G2Engine()
        return self.g2_handle.init(module_name, json_config, verbose_logging)

    def init_direct_with_config_id(self, config_id):
        pass

    def reinit(self, config_id):
        config_id = bytes(config_id, 'utf-8')
        self.g2_handle.reinit(config_id)

    def destroy(self):
        self.g2_handle.destroy()
        self.g2_handle = None

    def prime_engine(self):
        self.g2_handle.prime_engine()

    def get_active_config_id(self):
        response = bytearray()
        self.g2_handle.getActiveConfigID(response)
        return int(response.decode())





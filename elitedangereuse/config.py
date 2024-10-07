import configparser as cp
import os.path

from elitedangereuse.debug import Debug

FOLDERNAME = "config"
MAIN_FILENAME = "config.ini"


class Config(object):
    """
    Manages the plugin config files
    """
    def __init__(self, elitedangereuse):
        self.config: cp.ConfigParser = cp.ConfigParser()

        main_filepath: str = os.path.join(elitedangereuse.plugin_dir, FOLDERNAME, MAIN_FILENAME)
        if os.path.exists(main_filepath):
            try:
                self.config.read(main_filepath)
            except Exception as e:
                Debug.logger.error(f"Unable to load main config file {main_filepath}")


    def apikey_sentry(self) -> str | None:
        """Get the Sentry API key from config

        Returns:
            str | None: The Sentry API key
        """
        return self.config.get('apikeys', 'sentry', fallback = None)


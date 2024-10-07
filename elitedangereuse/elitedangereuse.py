import sys
from os import mkdir, path
from threading import Thread
from time import sleep

import semantic_version

from config import appversion, config
from elitedangereuse.config import Config
from elitedangereuse.debug import Debug
from elitedangereuse.httprequestmanager import HTTPRequestManager
from elitedangereuse.ui import UI
from elitedangereuse.updatemanager import UpdateManager
from elitedangereuse.websocketmanager import WebsocketManager

TIME_WORKER_PERIOD_S = 60


class EliteDangereuse:
    """
    Main plugin class
    """
    def __init__(self, plugin_name: str, version: semantic_version.Version):
        self.plugin_name: str = plugin_name
        self.version: semantic_version.Version = version


    def plugin_start(self, plugin_dir: str):
        """
        The plugin is starting up. Initialise all our objects.
        """
        self.plugin_dir = plugin_dir

        # Debug and Config Classes
        self.debug: Debug = Debug(self)
        self.config: Config = Config(self)

        # True only if we are running a dev version
        self.dev_mode: bool = False

        # Load sentry to track errors during development - Hard check on "dev" versions ONLY (which never go out to testers)
        # If you are a developer and want to use sentry, install the sentry_sdk inside the ./thirdparty folder and add your full dsn
        # (starting https://) to a 'sentry' entry in config.ini file. Set the plugin version in load.py to include a 'dev' prerelease,
        # e.g. "3.3.0-dev"
        if type(self.version.prerelease) is tuple and len(self.version.prerelease) > 0 and self.version.prerelease[0] == "dev":
            self.dev_mode = True
            sys.path.append(path.join(plugin_dir, 'thirdparty'))
            try:
                import sentry_sdk
                sentry_sdk.init(
                    dsn=self.config.apikey_sentry()
                )
                Debug.logger.info("Enabling Sentry Error Logging")
            except ImportError:
                pass

        # Main Classes
        self.request_manager: HTTPRequestManager = HTTPRequestManager(self)
        self.update_manager: UpdateManager = UpdateManager(self)
        self.websocket_manager: WebsocketManager = WebsocketManager(self)
        self.ui: UI = UI(self)

        self.thread: Thread = Thread(target=self._worker, name="EliteDangereuse Main worker")
        self.thread.daemon = True
        self.thread.start()


    def plugin_stop(self):
        """
        The plugin is shutting down.
        """
        self.save_data()


    def journal_entry(self, cmdr: str, is_beta: bool, system: str | None, station: str | None, entry: dict, state: dict):
        """
        Parse an incoming journal entry and store the data we need
        """


    def save_data(self):
        """
        Save all data structures
        """


    def _worker(self) -> None:
        """
        Handle thread work
        """
        Debug.logger.debug("Starting Main Worker...")

        while True:
            if config.shutting_down:
                Debug.logger.debug("Shutting down Main Worker...")
                return

            Debug.logger.debug("Main Worker Working...")
            sleep(TIME_WORKER_PERIOD_S)


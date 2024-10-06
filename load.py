from os import path

import semantic_version

import elitedangereuse.globals
from elitedangereuse.debug import Debug
from elitedangereuse.elitedangereuse import EliteDangereuse

PLUGIN_NAME = "EliteDangereuse"
PLUGIN_VERSION = semantic_version.Version.coerce("1.0.0-dev")

# Initialise the main plugin class
elitedangereuse.globals.this = this = EliteDangereuse(PLUGIN_NAME, PLUGIN_VERSION)


def plugin_start3(plugin_dir):
    """
    Load this plugin into EDMC
    """
    this.plugin_start(plugin_dir)

    return this.plugin_name


def plugin_stop():
    """
    EDMC is closing
    """
    this.plugin_stop()


def plugin_app(parent):
    """
    Return a TK Frame for adding to the EDMC main window
    """
    return this.ui.get_plugin_frame(parent)


def plugin_prefs(parent, cmdr: str, is_beta: bool):
    """
    Return a TK Frame for adding to the EDMC settings dialog
    """
    return this.ui.get_prefs_frame(parent)


def prefs_changed(cmdr: str, is_beta: bool) -> None:
    """
    Save settings.
    """
    this.ui.save_prefs()


def journal_entry(cmdr, is_beta, system, station, entry, state):
    """
    Parse an incoming journal entry and store the data we need
    """
    this.journal_entry(cmdr, is_beta, system, station, entry, state)
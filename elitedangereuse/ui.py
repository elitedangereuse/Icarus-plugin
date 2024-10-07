import tkinter as tk

import myNotebook as nb
from ttkHyperlinkLabel import HyperlinkLabel

from config import config
from elitedangereuse.debug import Debug

URL_LATEST_RELEASE = "https://github.com/elitedangereuse/Icarus-plugin/releases/latest"


class UI:
    """
    Display the user's activity
    """

    def __init__(self, elitedangereuse):
        self.elitedangereuse = elitedangereuse
        self.frame: tk.Frame = None


    def get_plugin_frame(self, parent_frame: tk.Frame) -> tk.Frame:
        """
        Return a TK Frame for adding to the EDMC main window
        """
        self.frame: tk.Frame = tk.Frame(parent_frame)

        current_row: int = 0
        self.lbl_version: HyperlinkLabel = HyperlinkLabel(self.frame, text=f"EliteDangereuse v{str(self.elitedangereuse.version)}", background=nb.Label().cget('background'), url=URL_LATEST_RELEASE, underline=True)
        self.lbl_version.grid(row=current_row, column=1, sticky=tk.W)
        current_row += 1

        return self.frame


    def get_prefs_frame(self, parent_frame: tk.Frame):
        """
        Return a TK Frame for adding to the EDMC settings dialog
        """
        self.plugin_frame: tk.Frame = parent_frame
        frame: nb.Frame = nb.Frame(parent_frame)

        return frame


    def save_prefs(self):
        """
        Preferences frame has been saved (from EDMC core or any plugin)
        """

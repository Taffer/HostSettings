# Apply host-specific settings based on hostname.
#
# Original source - https://stackoverflow.com/a/56588149
# Posted by OdatNurd
# Retrieved 2026-02-20, License - CC BY-SA 4.0

# TODO: Python 3.7+, not necessary in 3.14+
from __future__ import annotations

import socket
import sublime
import sublime_plugin
import typing

# TODO: Is there any way to call Package Control to disable/enable packages?
#
# from package_control import package_disabler
# package_disabler.PackageDisabler.disable_packages({package_disabler.PackageDisabler.DISABLE: ("CUE", "Terraform")})


class HostSettingsListener(sublime_plugin.EventListener):
    """Tweak settings per-host when necessary."""

    preferences: sublime.Settings | None = None
    hostname: str | None = None

    def settings_changed(self: HostSettingsListener) -> None:
        """Update every view in every window if the settings change."""
        for window in sublime.windows():
            for view in window.views():
                self.on_new(view)

    def on_init(self: HostSettingsListener, views: typing.List[sublime.View]) -> None:
        """Update settings when the plugin is initialized."""
        if not self.hostname:
            self.hostname = socket.gethostname() or "localhost"

        if not self.preferences:
            self.preferences = sublime.load_settings("Preferences.sublime-settings") or {}
            self.preferences.add_on_change("HostSettingsListener", self.settings_changed)

        for view in views:
            self.on_new(view)

    def on_new(self: HostSettingsListener, view: sublime.View) -> None:
        """Update settings when a new view is created."""
        host_prefs = self.preferences.get("host-specific", {})
        prefs = host_prefs.get(self.hostname, {})
        settings = view.settings()
        for key in prefs:
            settings.set(key, prefs[key])

    """ Update settings when a view is cloned. """
    on_clone = on_new  # Do we need this one?

    """ Update settings when a view loads a file. """
    on_load = on_new  # Do we need this one?

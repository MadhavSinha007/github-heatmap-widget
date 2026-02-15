#!/usr/bin/env python3
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("GdkX11", "4.0")

from gi.repository import Gtk, Gdk, GdkX11, GLib
import subprocess
import re
from datetime import datetime, timedelta


# ============================================================================
# FETCHER
# ============================================================================
class GitHubFetcher:
    def __init__(self, username):
        self.username = username

    def fetch(self):
        try:
            url = f"https://github.com/users/{self.username}/contributions"
            result = subprocess.run(
                ["curl", "-L", "-s", "-H", "User-Agent: Mozilla/5.0", url],
                capture_output=True,
                text=True,
                timeout=10
            )

            pattern = r'data-date="([^"]+)"[^>]*data-level="(\d)"'
            matches = re.findall(pattern, result.stdout)

            data = {}
            for date_str, level in matches:
                try:
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                    data[date_obj] = int(level)
                except:
                    pass
            return data
        except:
            return {}

    def color(self, level):
        colors = {
            0: "#ebedf0",
            1: "#c6e48b",
            2: "#7bc96f",
            3: "#239a3b",
            4: "#196c2e",
        }
        return colors.get(level, "#ebedf0")


# ============================================================================
# SQUARE
# ============================================================================
class Square(Gtk.DrawingArea):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.set_content_width(13)
        self.set_content_height(13)
        self.set_draw_func(self.draw)

    def draw(self, area, cr, w, h):
        c = self.color.lstrip("#")
        r = int(c[0:2], 16) / 255
        g = int(c[2:4], 16) / 255
        b = int(c[4:6], 16) / 255
        cr.set_source_rgb(r, g, b)
        cr.rectangle(0, 0, w, h)
        cr.fill()


# ============================================================================
# HEATMAP
# ============================================================================
class Heatmap(Gtk.Box):
    def __init__(self, data, color_func):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        grid = Gtk.Grid()
        grid.set_row_spacing(2)
        grid.set_column_spacing(2)
        self.append(grid)

        today = datetime.now().date()
        start = today - timedelta(days=364)
        start -= timedelta(days=(start.weekday() + 1) % 7)

        current = start
        col = 0

        while current <= today:
            for row in range(7):
                level = data.get(current, 0)
                square = Square(color_func(level))
                grid.attach(square, col, row, 1, 1)
                current += timedelta(days=1)
            col += 1


# ============================================================================
# DESKTOP WIDGET
# ============================================================================
class DesktopWidget(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_decorated(False)
        self.set_resizable(False)

        handle = Gtk.WindowHandle()
        self.set_child(handle)

        box = Gtk.Box()
        handle.set_child(box)

        fetcher = GitHubFetcher("SUnset-06")  # change username
        data = fetcher.fetch()
        heatmap = Heatmap(data, fetcher.color)
        box.append(heatmap)

        self.connect("realize", self.on_realize)

    def on_realize(self, *args):
        surface = self.get_surface()

        # Only apply if running under X11
        if isinstance(surface, GdkX11.X11Surface):
            surface.set_skip_taskbar_hint(True)
            surface.set_skip_pager_hint(True)
            surface.set_type_hint(Gdk.WindowTypeHint.DOCK)


# ============================================================================
# RUN (GTK4 CORRECT WAY)
# ============================================================================
win = DesktopWidget()
win.present()

loop = GLib.MainLoop()
loop.run()
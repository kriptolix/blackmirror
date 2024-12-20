# window.py
#
# Copyright 2024 k
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

import subprocess

@Gtk.Template(resource_path='/io/github/kriptolix/BlackMirror'
              '/src/gtk/ui/MainWindow.ui')
class BlackmirrorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'BlackmirrorWindow'

    test = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.test.connect("clicked", self._test)

    def _test(self, button):
       subprocess.Popen('scrcpy --video-codec=h265 -m1920 --max-fps=60 --no-audio -K', shell=True)
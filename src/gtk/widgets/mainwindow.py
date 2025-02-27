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


import random


@Gtk.Template(resource_path='/io/github/kriptolix/BlackMirror'
              '/src/gtk/ui/MainWindow.ui')
class BlackmirrorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'BlackmirrorWindow'

    test = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.test.connect("clicked", self._test)

    def calcular_chance_base(self):
        return {
            "preto": 45,
            "marrom_escuro": 30,
            "marrom_claro": 15,
            "loiro": 5,
            "ruivo": 5,
            "branco":1
        }

    def ajustar_chances_por_etnia(self, chances, etnia):
        if etnia == "Reino de Rohin":
            chances["loiro"] = 70
            chances["ruivo"] = 70
            chances["marrom_claro"] = 65
            
        return chances

    def ajustar_chances_por_idade(self, chances, idade):
        if idade > 60:
            chances["branco"] = 80
            
        return chances

    def normalizar_chances(self, chances):
        total = sum(chances.values())

        resultados = {}
        for cor, chance in chances.items():
            resultados[cor] = chance / total
        
        # print(resultados)
        return resultados

    def gerar_npc(self, etnia, idade):
        chances = self.calcular_chance_base()
        chances = self.ajustar_chances_por_etnia(chances, etnia)
        chances = self.ajustar_chances_por_idade(chances, idade)
        chances = self.normalizar_chances(chances)

        cores = list(chances.keys())
        probabilidades = list(chances.values())

        cor_cabelo = random.choices(cores, probabilidades)[0]

        return cor_cabelo

    def _test(self, button):
        # Exemplo de uso
        etnia = "Reino de Rohin"
        idade = 65
        cor_cabelo = self.gerar_npc(etnia, idade)
        print(f"NPC gerado com cabelo {cor_cabelo}")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# JANGAN COPAS INI LU KEK KONTOL
# TANYA KE SUPPORT @KillerXSupport

from pyrogram import Client, filters
from pyrogram.types import Message
from base64 import b64decode
import requests
import base64
from io import BytesIO

class WebShotUrl:
    def __init__(
        self,
        url=None,
        width: int=1280,
        height: int=720,
        scale: int=1,
        delay: int=0,
        screenshot_full: bool=None
    ):
        self.url = url
        self.width = width
        self.height = height
        self.scale = scale
        self.delay = delay
        self.screenshot_full = screenshot_full

    def send_screenshot(self):
        api_url = b64decode("aHR0cHM6Ly9hcGkuc2Fmb25lLm1lL3dlYnNob3Q=").decode("utf-8")
        if self.screenshot_full:
            data = {
                "url": self.url,
                "width": self.width,
                "height": self.height,
                "scale": self.scale,
                "delay": self.delay,
                "full": True
            }
            x = requests.post(f"{api_url}", json=data)
            if x.status_code != 200:
                return "Error request:"
            try:
                y = x.json()
                iseeyou = base64.b64decode(y["image"])
                hack = BytesIO(iseeyou)
                hack.name = "screenshot.jpg"
                return hack
            except Exception as e:
                return f"Error: {e}"
        else:
            data = {
                "url": self.url,
                "width": self.width,
                "height": self.height,
                "scale": self.scale,
                "delay": self.delay,
                "full": False
            }
            x = requests.post(f"{api_url}", json=data)
            if x.status_code != 200:
                return "Error request:"
            try:
                y = x.json()
                iseeyou = base64.b64decode(y["image"])
                hack = BytesIO(iseeyou)
                hack.name = "screenshot.jpg"
                return hack
            except Exception as e:
                return f"Error: {e}"
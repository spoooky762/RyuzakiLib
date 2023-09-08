# RyuzakiLib

[![pykillerx - Version](https://img.shields.io/pypi/v/RyuzakiLib?style=round)](https://pypi.org/project/RyuzakiLib)    
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pykillerx?label=DOWNLOADS&style=round)](https://pypi.org/project/RyuzakiLib)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TeamKillerX/RyuzakiLib/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/TeamKillerX/RyuzakiLib)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

# Disclaimer
```
        ⚠️ WARNING FOR YOU ️ ️⚠️
RyuzakiLib is used to help your account activities on Telegram
We are not responsible for what you misuse in this repository
!  Be careful when using this repository!
If one of the members misuses this repository, we are forced to ban you
Never ever abuse this repository 
```

# Installing 
* `pip3 install -U RyuzakiLib`
* add your in requirements.txt
```
git+https://github.com/TeamKillerX/RyuzakiLib/
```

### Learn Python 
```python
import asyncio

class example_python:
      def __init__(self):
         pass

      def hello_world(self):
          asyncio.sleep(5)

# examples usage
ok = example_python()
test = ok.hello_world()
```

### Import Here 
```python
from RyuzakiLib.hackertools.chatgpt import RendyDevChat
from RyuzakiLib.hackertools.api_github import GithubUsername
from RyuzakiLib.hackertools.rmbg import RemoveBg
from RyuzakiLib.hackertools.reverse import GoogleReverseImage
from RyuzakiLib.hackertools.ipinfo import WhoisIpHacker
from RyuzakiLib.hackertools.ocrapi import OcrApiUrl
```

### Example Chatgpt
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools import RendyDevChat, GoogleReverseImage

query = "Hello World"
response = RendyDevChat(query).get_response(message)
await message.reply(response)
```

### Example Google Reverse Image
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools import RendyDevChat, GoogleReverseImage

url = "https://example/jpg"
apikey = "api key token"
response = GoogleReverseImage(url, apikey)
results = response.get_reverse()
print(results)
```
### New Features
```python
# Create by @xtdevs
# Prefixes Custom

from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools import custom_prefixes
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

db_name = "custom_prefixes"
user_id = message.from_user.id
prefix = [".", "+", "-"]
set_handler = custom_prefixes(db_name, user_id, prefix, collection, True) # parameter upsert using set True or False
set_handler.add_prefixes()
now_show_prefix = set_handler.get_prefix()
print(now_show_prefix)
```
* you can ask support [@KillerXSupport](https://t.me/KillerXSupport)

# License 
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
TeamKillerX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

<h4 align="center">Copyright (C) 2019 - 2023 <a href="https://github.com/TeamKillerX">TeamKillerX</a></h4>

Project [RyuzakiLib](https://github.com/TeamKillerX/) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

# Credits 
* [![TeamKillerX-Devs](https://img.shields.io/static/v1?label=TeamkillerX&message=devs&color=critical)](https://t.me/xtdevs)
* Pyrogram by : [Dan](https://github.com/pyrogram/pyrogram)

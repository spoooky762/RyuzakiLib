### Import All
```python
from RyuzakiLib.hackertools.chatgpt import RendyDevChat
from RyuzakiLib.hackertools.github import GithubUsername
from RyuzakiLib.hackertools.rmbg import RemoveBg
from RyuzakiLib.hackertools.reverse import GoogleReverseImage
from RyuzakiLib.hackertools.ipinfo import WhoisIpHacker
from RyuzakiLib.hackertools.ocrapi import OcrApiUrl
from RyuzakiLib.hackertools.prefixes import CustomPrefixes
```
### Example Chatgpt
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools.chatgpt import RendyDevChat

query = "Hello World"
response = RendyDevChat(query).get_response(message)
await message.reply(response)
```

### Example Reverse
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools.reverse import GoogleReverseImage

url = "https://example/jpg"
apikey = "api key token"
response = GoogleReverseImage(url, apikey)
results = response.get_reverse()
print(results)
```

### Github Info Data
```python
# < class RyuzakiLib.hackertools.github.GithubUsername >

hacking = await GithubUsername(username).get_github_data()
# code here
```
### Ocr image to text
```python

# < class RyuzakiLib.hackertools.ocrapi.OcrApiUrl >

code = await OcrApiUrl(api_key, url, language)
send = code.now_send_text()
# code here
```
### Whois Ip Address
```python
# < class RyuzakiLib.hackertools.ipinfo.WhoisIpHacker >

code = await WhoisIpHacker(1243003)
test = code.get_ipaddres_data()
# code here
```

### Openai Ai Token
```python
# < class RyuzakiLib.hackertools.openai.OpenAiToken >

code = await OpenAiToken("apikey token")
text = code.message_output()
img = code.photo_output()
# code here
```
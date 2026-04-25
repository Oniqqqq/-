import os
path = "/home/dzhalil/Рабочий стол/антигравити/nikamed/artifacts/myhealthprac/static/index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = "</section><div class=\"footer\">"
if target in content:
    new_content = content.replace(target, "</section>\n<div class=\"footer\">")
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("SUCCESS")
else:
    print("TARGET NOT FOUND")

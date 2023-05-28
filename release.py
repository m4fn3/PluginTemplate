import json
import os.path

projects_path = "../"
name = input("plugin name >")
plugin_path = projects_path + name
if not os.path.exists(f"{plugin_path}/manifest.json"):
    raise RuntimeError("Plugin not found")
with open(f"{plugin_path}/manifest.json") as f:
    manifest = json.load(f)
text = f"""
・{name}

{manifest["description"]}

Install: enmity://enmity?id=-1&command=install-plugin&params=https://raw.githubusercontent.com/m4fn3/{name}/master/dist/{name}.js
Download: https://raw.githubusercontent.com/m4fn3/{name}/master/dist/{name}.js
Source: https://github.com/m4fn3/{name}
"""
print(text)

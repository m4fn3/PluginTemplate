import json
import os
import shutil

print("--- Enmity Plugin Template of @m4fn3---")
print("[-] Enter the information of a plugin.")
plugin_name = input("name >")
if os.path.isdir(f"./{plugin_name}"):
    raise RuntimeError(f"Project '{plugin_name}' already exists!")
plugin_description = input("description >")
plugin_color = input("color (Optional: #000000) >")

print(f"[*] Creating a project folder to ./{plugin_name}")
shutil.copytree("./template", f"./{plugin_name}")

manifest: dict
with open(f"./{plugin_name}/manifest.json", "r") as f:
    manifest = json.load(f)
    manifest["name"] = plugin_name
    manifest["description"] = plugin_description
    if plugin_color:
        manifest["color"] = plugin_color
with open(f"./{plugin_name}/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

paths = ["src/index.tsx", "src/components/Settings.tsx", "README.md"]
for path in paths:
    text: str
    with open(f"./{plugin_name}/{path}", "r") as f:
        text = f.read()
    text = text.replace("PLUGIN_NAME", plugin_name)
    with open(f"./{plugin_name}/{path}", "w") as f:
        f.write(text)

print(f"[o] Done!")

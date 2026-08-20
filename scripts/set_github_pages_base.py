import os, json, glob, shutil

BASE_DIR = "/Users/israeltorres/Documents/antigravity/calm-babbage"
DESKTOP_DIR = "/Users/israeltorres/Desktop/SKILL PPT"
KIT_DIR = os.path.join(BASE_DIR, "company-kits", "artefact")

GH_PAGES_BASE = "https://israeltorres-artefact.github.io/MKTKITARTEFACT/assets/"
CDN_BASE = "https://cdn.jsdelivr.net/gh/israeltorres-artefact/MKTKITARTEFACT@main/assets/"

# Files to update
files_to_update = [
    os.path.expanduser("~/.gemini/config/skills/presentaciones-ejecutivas-artefact/SKILL.md"),
    os.path.join(KIT_DIR, "llm", "skill.md"),
    os.path.join(KIT_DIR, "llm", "system_prompt.md"),
    os.path.join(BASE_DIR, "artefact-llm-presentation-kit", "02_SYSTEM_PROMPT_FOR_LLMS.md"),
    os.path.join(KIT_DIR, "guidelines", "ELEMENTS_AND_CONTEXT_PLAYBOOK.md"),
    os.path.join(BASE_DIR, "docs", "ELEMENTS_AND_CONTEXT_PLAYBOOK.md"),
    os.path.join(KIT_DIR, "templates", "template.html"),
    os.path.join(KIT_DIR, "templates", "full_deck_example.html"),
    os.path.join(BASE_DIR, "artefact-llm-presentation-kit", "03_PRESENTATION_TEMPLATE.html"),
    os.path.join(BASE_DIR, "artefact-llm-presentation-kit", "04_FULL_DECK_ARTEFACT_PITCH_EXAMPLE.html")
]

for fpath in files_to_update:
    if os.path.exists(fpath):
        with open(fpath, "r") as f:
            content = f.read()
        content = content.replace(CDN_BASE, GH_PAGES_BASE)
        with open(fpath, "w") as f:
            f.write(content)

# Update manifests
for mpath in [
    os.path.join(BASE_DIR, "tokens", "colors.json"),
    os.path.join(KIT_DIR, "tokens", "colors.json"),
    os.path.join(KIT_DIR, "manifest.json")
]:
    if os.path.exists(mpath):
        with open(mpath, "r") as f:
            data = json.load(f)
        data["assetBaseUrl"] = GH_PAGES_BASE
        data["githubPagesUrl"] = "https://israeltorres-artefact.github.io/MKTKITARTEFACT/"
        with open(mpath, "w") as f:
            json.dump(data, f, indent=2)

# Mirror to Desktop
shutil.copytree(KIT_DIR, os.path.join(DESKTOP_DIR, "company-kits", "artefact"), dirs_exist_ok=True)

print("All files successfully updated to use direct GitHub Pages URLs!")

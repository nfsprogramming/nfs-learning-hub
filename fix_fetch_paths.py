import os
import re

hub_dir = r"e:\NFS Learning Hub"
folders = [f for f in os.listdir(hub_dir) if os.path.isdir(os.path.join(hub_dir, f)) and not f.startswith('.')]

for folder in folders:
    script_path = os.path.join(hub_dir, folder, "script.js")
    if not os.path.exists(script_path):
        continue
    
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update fetch('lessons_data.json') to use absolute path
    # Search for fetch(`lessons_data.json?v=${new Date().getTime()}`)
    # or similar
    
    old_fetch = r'fetch\(`lessons_data.json'
    new_fetch = f'fetch(`/{folder}/lessons_data.json'
    content = re.sub(old_fetch, new_fetch, content)
    
    # Also update any other relative fetches if they exist
    # (The script seems to mainly fetch lessons_data.json and READMEs)
    
    # In openReadme, it fetches ${fullPath}
    # If fullPath is relative, it will fail.
    # In script.js:
    # const fullPath = cleanPath.endsWith('.md') ? cleanPath : `${cleanPath}/README.md`;
    # try { const response = await fetch(`${fullPath}?v=${new Date().getTime()}`); ... }
    
    # We should make the base folder part of the path if it's not absolute.
    # Actually, the path passed to openReadme comes from lessons_data.json.
    # In lessons_data.json, paths are relative: "path": "10-ai-framework-project/README.md"
    
    # So in script.js, we should prefix with the folder name.
    
    if f'const baseCoursePath = "/{folder}/";' not in content:
        # Add a constant at the top
        content = f'const baseCoursePath = "/{folder}/";\n' + content
        
    # Update the fetch in openReadme
    # Old: const response = await fetch(`${fullPath}?v=${new Date().getTim...
    # New: const response = await fetch(`${baseCoursePath}${fullPath}?v=${new Date().getTim...
    
    content = content.replace('await fetch(`${fullPath}', 'await fetch(`${baseCoursePath}${fullPath}')
    
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Absolute fetch paths fixed for {folder}")

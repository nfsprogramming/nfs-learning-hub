import os
import re

def fix_styles_collision(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'styles.css':
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Scope the navbar button
                # Finding the first .btn-hub (which is for the navbar)
                # We'll use a more specific selector
                
                new_content = content
                
                # Replace the first .btn-hub with .top-nav .btn-hub
                # And the second .btn-hub with .hidden-sidebar .btn-hub
                
                matches = list(re.finditer(r'\.btn-hub\s*\{', new_content))
                if len(matches) >= 2:
                    # Replace first instance
                    start, end = matches[0].span()
                    # We need to be careful with string slicing
                    # Actually, let's do it in one go if possible
                    pass
                
                # Better approach: string replacement for known blocks
                # The first one usually starts with padding: 11px 20px 9px; (now)
                # The second one usually has margin-bottom: 2rem;
                
                # Fix navbar one
                new_content = re.sub(
                    r'\.btn-hub\s*\{([^}]*?padding:\s*1[01]px\s+20px\s+[0-9]px;[^}]*?)\}',
                    r'.top-nav .btn-hub {\1\n    margin: 0;\n}', # Added margin: 0 to be safe
                    new_content
                )
                
                # Fix sidebar one
                new_content = re.sub(
                    r'\.btn-hub\s*\{([^}]*?margin-bottom:\s*2rem;[^}]*?)\}',
                    r'.hidden-sidebar .btn-hub {\1}',
                    new_content
                )
                
                # 2. Fix internal padding to be perfectly symmetric
                # 11px 20px 9px -> 10px 20px
                new_content = re.sub(r'padding:\s*11px\s+20px\s+9px;', 'padding: 10px 20px;', new_content)
                new_content = re.sub(r'padding:\s*11px\s+15px\s+9px;', 'padding: 10px 15px;', new_content)

                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Scoped and balanced {path}")

if __name__ == "__main__":
    fix_styles_collision(".")

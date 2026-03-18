import os
import re

def add_global_scrollbar(directory):
    scrollbar_css = """
/* Custom Scrollbar Design */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: #05060a;
}

::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    border: 2px solid #05060a;
    transition: all 0.3s ease;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 242, 255, 0.4);
}

/* Firefox */
* {
    scrollbar-width: thin;
    scrollbar-color: rgba(255, 255, 255, 0.1) #05060a;
}
"""

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'styles.css':
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if global scrollbar already exists
                if '::-webkit-scrollbar' in content and 'Track' not in content: # Simple check
                    # We might want to prepend it anyway or replace existing global if found
                    pass
                
                # Prepend the global scrollbar styles after :root or at the top
                if '/* Custom Scrollbar Design */' not in content:
                    # Find a good place to insert - after :root block
                    root_match = re.search(r'\}\s*\n', content)
                    if root_match:
                        insertion_point = root_match.end()
                        new_content = content[:insertion_point] + scrollbar_css + content[insertion_point:]
                    else:
                        new_content = scrollbar_css + content
                    
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Added custom scrollbar to {path}")

if __name__ == "__main__":
    add_global_scrollbar(".")

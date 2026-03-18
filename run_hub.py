import http.server
import socketserver
import webbrowser
import threading
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # We handle /firebase.js specifically to inject the API Key from the environment
        if self.path == "/firebase.js" or self.path.endswith("firebase.js"):
            try:
                # Always read from the root firebase.js
                file_path = os.path.join(DIRECTORY, "firebase.js")
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Try to get the key from .env or system environment
                api_key = os.environ.get('FIREBASE_API_KEY')
                if not api_key:
                    # Fallback to reading .env file if it exists
                    env_path = os.path.join(DIRECTORY, ".env")
                    if os.path.exists(env_path):
                        with open(env_path, 'r', encoding='utf-8') as ef:
                            for line in ef:
                                if line.startswith("FIREBASE_API_KEY="):
                                    api_key = line.split("=")[1].strip()
                                    break
                
                if api_key:
                    # Replace the placeholder in the content
                    content = content.replace("ENV_FIREBASE_API_KEY", api_key)
                
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
                return
            except Exception as e:
                print(f"Error serving firebase.js: {e}")
                self.send_error(500, f"Internal Server Error during key injection: {e}")
                return
        
        return super().do_GET()

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Microsoft Course Hub running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()

if __name__ == "__main__":
    # Change to root directory
    os.chdir(DIRECTORY)
    
    # Start server in a separate thread
    threading.Thread(target=start_server, daemon=True).start()
    
    # Open the browser
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    
    print("\n--- NFS Microsoft Course Hub ---")
    print(f"Serving files from: {DIRECTORY}")
    print(f"URL: http://localhost:{PORT}/index.html")
    print("------------------------------------\n")
    
    try:
        # Keep main thread alive
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down hub...")
        sys.exit(0)

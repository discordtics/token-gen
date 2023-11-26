import os, subprocess

try: subprocess.run(["python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "library/pycache/cached/dist/cache.py")], check=True)
except Exception as e: print(f"Error: {e}")

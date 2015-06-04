#!/usr/bin/env python
# encoding: utf-8
from __future__ import with_statement
import sys
import subprocess

    def scp(source, server, path = ""):
	return not subprocess.Popen(["scp", source, "%s:%s" % (server, path)]).wait()

    def main(*args):
	filename = "example.txt"
	server = "myaccount@example.com"
	
	with open(filename, "w") as f:
		f.write("Hello world.")
	
	if scp(filename, server):
		print("File uploaded successfully.")
		return 0
		else:
	print("File upload failed.")
	return 1
	

if __name__ == "__main__": sys.exit(main(*sys.argv[1:]))

#!/usr/bin/env python3

import sys
import os.path

def usage():
	print("text-include [file path] (raw string token)")


if len(sys.argv) < 2:
	usage()
	quit()

if sys.argv[1] == "-h":
	usage()
	quit()

filename = os.path.basename(sys.argv[1])
varname = filename.replace(" ", "_").replace(".", "_")

token = ""

if len(sys.argv) == 3:
	token = sys.argv[2]

print("static const char* " + varname + " = R\"" + token + "(")
textfile = open(sys.argv[1], 'r')
print(textfile.read())
textfile.close()
print(")" + token + "\"R;")


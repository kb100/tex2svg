#!/usr/bin/env python3

import sys, subprocess, os

argc = len(sys.argv)
assert argc == 3 or arc == 4

snippet = sys.argv[1]
outPrefix = sys.argv[2]
packages = sys.argv[3] if argc == 4 else ""

tex = """
\\documentclass{{article}}
{}
\\begin{{document}}
\\thispagestyle{{empty}}
{}
\\end{{document}}
""".format("\\usepackage{" + packages + "}" if packages else "", snippet)


texFileName = outPrefix+".tex"
with open(texFileName,'w') as texFile:
    texFile.write(tex)

subprocess.check_call(["pdflatex","--halt-on-error", texFileName])
os.remove(outPrefix + ".tex")
os.remove(outPrefix + ".log")
os.remove(outPrefix + ".aux")
subprocess.check_call(["pdfcrop", outPrefix+".pdf", outPrefix+".pdf"])
subprocess.check_call(["pdf2svg", outPrefix+".pdf", outPrefix+".svg"])
os.remove(outPrefix+".pdf")


#!/usr/bin/env python3
import re, tempfile, subprocess, os, sys 


assert len(sys.argv) in [2, 3]
inFile = os.path.abspath(sys.argv[1])
outFile = os.path.abspath(sys.argv[2]) if sys.argv[2] else ""

TEX2SVG = os.path.abspath("./tex2svg.py")
BASE64ENCODE = "base64"
TAGTEMPLATE = '<img class="math" src="data:image/svg+xml;base64,{}" alt="{}" align="middle"/>'

with open(inFile) as f:
    html = f.read()

p = re.compile('<math>(.*?)</math>', re.DOTALL)
subs = []
with tempfile.TemporaryDirectory() as tempDirName:
    os.chdir(tempDirName)
    for match in p.finditer(html):
        tex = match.group(1)
        outPrefix = tempDirName + "/htmltexmatch"
        subprocess.check_call([TEX2SVG, tex, outPrefix], universal_newlines=True)
        b64svg = subprocess.check_output([BASE64ENCODE, outPrefix + ".svg"], universal_newlines=True)
        subs.append(TAGTEMPLATE.format(b64svg, tex))

frags = p.split(html)
for i in range(1, len(frags),2):
    frags[i] = subs[(i-1)//2]

html = "".join(frags)

if outFile:
    with open(outFile,'w') as f:
        f.write(html)
else:
    print(html)


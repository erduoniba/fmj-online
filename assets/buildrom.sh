#!/bin/sh

python3 ./bin2js.py DAT.LIB ASC16 HZK16
rm -rf rom.js
cat *.js > rom.js

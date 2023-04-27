#!/bin/bash

echo "running Motion_Extraction.sh"
./Motion_Extraction.sh
echo "pvpython createWGs_*.py"
pvpython createWGs_*.py
echo "running python3 extractSE.py"
python3 extractSE.py

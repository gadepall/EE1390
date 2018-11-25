#!/bin/bash

for f in *.png; do
#  convert ./"$f" ./"${f%.jpg}.eps"
  convert ./"$f" ./"${f%}.eps"
done

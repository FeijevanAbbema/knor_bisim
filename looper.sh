#!/bin/bash
for filename in examples/*; do
    build/knor --sym --bisim-min "$filename"
done
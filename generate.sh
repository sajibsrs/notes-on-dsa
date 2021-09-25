#!/bin/bash

pandoc \
    -o data-structures-and-algorithms-hyperdrive.pdf header.yml \
    *.md \
    1.data-structures/*.md \
    1.data-structures/1.linear/*.md \
    2.algorithms/*.md \
    2.algorithms/1.searching/*.md \
    2.algorithms/2.sorting/*.md \
    2.algorithms/3.performance/*.md \
    --pdf-engine=xelatex
    # data-structures/2_non-linear/*.md \
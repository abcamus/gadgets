#!/bin/bash

src_line=`find $1 -name "*.[cSs]" | xargs wc -l`
header_line=`find $1 -name "*.h" | xargs wc -l`

echo "$src_line\n"
echo "$header_line\n"

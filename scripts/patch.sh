#!/usr/bin/sh

# Pass in two json dictionaries to generate a patch file

diff -U 0 <(jq -S '.' <(cat $1)) <(jq -S '.' <(cat $2))

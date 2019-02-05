# Octalap

Octalap is run in two modes. The first takes a font and calculates new octaboxes
for the glyphs to generate a .json file which is then committed and used in the
build to replace the positions from grcompiler.

The first mode, to calculate new boxes takes a command like:

`tools/bin/octalap -q -j 0 -o source/octabox.json results/AwamiNastaliq-Regular.ttf`

then in the wscript is a command based on:

`tools/bin/octalap -m source/octabox.json -o results/AwamiNastaliq-Regular.ttf results/tmp/AwamiNastaliq-Regular.ttf`


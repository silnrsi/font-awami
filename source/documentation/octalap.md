# Octalap

Octalap is run in two modes. The first takes a font and calculates new octaboxes
for the glyphs to generate a .json file which is then committed and used in the
build to replace the octaboxes calculated within grcompiler.

The first mode, to calculate new boxes, takes a command like:

`tools/bin/octalap -q -j 0 -o source/graphite/octabox_AwamiNastaliq-Regular.json results/AwamiNastaliq-Regular.ttf`

then in the wscript is a command based on:

`tools/bin/octalap -m source/graphite/octabox.json -o results/AwamiNastaliq-Regular.ttf results/tmp/AwamiNastaliq-Regular.ttf`


To create extra weights of the font:
* Create a generic octabox.json file; modify the wscript to use it.
* Run the smith build to create TTFs of the new weights.
* Run octalap in the first mode above for each of the new weights:
		`tools/bin/octalap -q -j 0 -o source/graphite/octabox_AwamiNastaliq-WEIGHT.json results/AwamiNastaliq-WEIGHT.ttf`
* Return the wscript to its original state and rebuild.

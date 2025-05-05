#!/usr/bin/python3

# One-off script to add the anchor '_4mk' to all the "mk..." glyphs in order
# to get them to be treated as marks.

# Run this script from the tools/scripts directory where the file is located:
#		python3 addBaseMarkAnchors.py


from fontParts.world import *
import sys


# -----------------------------
# Main routine

# Open UFO
#ufo = sys.argv[1]
ufo = '../../source/masters/AwamiNastaliq-Black.ufo'
font = OpenFont(ufo)

# skipglyphset = set(font.lib.get('public.skipExportGlyphs', []))

for glyph in font:
	aw = glyph.width
	gname = glyph.name
	# if gname in skipglyphset:
	# 	continue
		
	if gname[0:2] == "mk":
		print(glyph.name)
		# anchorList = glyph.anchors

		glyph.appendAnchor("_4mk", (0, 0))

# end of for glyph

font.save()

font.close()

#FLM: Dump XML
####################################################################
#
#	Font to XML Dump
#
#	Dumps some basic information about a font and its glyphs
#
#	Author: 	Peter K. Martin
#	Date:		26-APR-2003
#	Copyright:	SIL Global
#
#	Usage:		Run from within FontLab 4.5
#				To compare two output files from this script, use
#					diff --side-by-side -6 -t file1 file2 > diff.txt
#					or BBEdit's Search/Find Differences... command
#
####################################################################

from time import gmtime, strftime
from types import *
import hashlib

properties = [
'**IDENTIFICATION',
'file_name',
'family_name',
'style_name',
'full_name',
'font_name',
'font_style',
'menu_name',
'apple_name',
'fond_id',
'pref_family_name',
'pref_style_name',
'mac_compatible',
'default_character',
'weight',
'weight_code',
'width',
'designer',
'designer_url',
'fontnames',
'copyright',
'notice',
'note',
'unique_id',
'tt_u_id',
'tt_version',
'trademark',
#'x_u_id_num',
#'x_u_id',
'vendor',
'vendor_url',
'version',
'year',
'version_major',
'version_minor',
'vp_id',
'ms_charset',
'ms_id',
'panose',
'pcl_chars_set',
'pcl_id',

'**DIMENSIONS ',
'upm',
'ascender',
'descender',
'cap_height',
'x_height',
'default_width',
'slant_angle',
'italic_angle',
'is_fixed_pitch',
'underline_position',
'underline_thickness',

'**ALIGNMENT ',
'blue_fuzz',
'blue_scale',
'blue_shift',
'blue_values_num',
'blue_values',
'other_blues_num',
'other_blues',
'family_blues_num',
'family_blues',
'family_other_blues_num',
'family_other_blues',
'force_bold',
'stem_snap_h_num',
'stem_snap_h',
'stem_snap_v_num',
'stem_snap_v ',

'**OTHER ',
'modified',
'classes',
'ot_classes',
'features',
'customdata',
'truetypetables',
'ttinfo',
'encoding',
'codepages',
'unicoderanges',
#'glyphs',
'source',
'weight_vector'
]



def USVstr(usv):
    if usv != None:
        USV_str = "%04X" % usv
    else:
        USV_str = ""
    return USV_str

# Grab the font properties object for the current font
ThisFont = fl.font

# Prepare the output filename and file
filename = ThisFont.file_name[:-4] + "-dump.xml"
    
# KLUDGE for Awami:
newName = fl.font.file_name.replace(" ", "")
newName2 = newName.replace(".VFB", ".vfb")
filename = newName2.replace(".vfb", "-dump.xml")
print "filename=",filename
if filename[25:31] == "AWAMIN" or filename[25:28] == "AWB" :
    filename = "AwamiNastaliqRegular-dump.xml"
###############

print
print "Output to", filename
f = file( filename, "wb" )

# Write a header block
start = "<!-- Generated on " + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + " by " + fl.username + " -->\n"
f.write( start )
if ThisFont.modified:
	f.write( "\n<!-- *** WARNING: This font has not been saved since modifications were made *** -->\n" )

f.write( "\n<font>\n" )

# Process each of the font-level properties
for property in properties:

#	print "[", type( value ), "] ", value
#	print "--" + property[:2] + "--"

	# Property groups are marked with names preceded by two asterisks,
	# marked in the output by a comment line
	if property[:2] == "**":
		f.write( "\n\t<!-- " + property[2:] + " -->\n" )

	else:
		# Generate the variable reference
		value = eval( "ThisFont." + property )
		value = str( value )

		# Cast some value types
		if type( value ) is IntType:
			value = str( value )
		if type( value ) is NoneType:
			value = "???"
		
		# KLUDGE for Awami:
		if property == "file_name" :
			#dirName = "Nastaliq"
			dirName = "source"
			pathStart = dirName + "\\AWAMIN~"
			tpath = value.find(pathStart)
			tNext0 = tpath + len(pathStart)
			tNext1 = tpath + len(pathStart) + 1
			if tpath > 0 and (value[tNext0] == "1" or value[tNext0] == "2" or value[tNext0] == "3" or value[tNext0] == "4") and value[tNext1] == "\\" :
				value = value[0:tpath] + dirName + "\\AwamiNastaliq" + value[tNext1:]
			tfname = value.find("AWAMIN~", tNext0)
			if tfname >= tNext0 :
				value = value[0:tfname] + "AwamiNastaliqRegular.vfb"
		###################

		open_tag = "\t<" + property + ">"
		close_tag = "</" + property + ">\n"
		f.write( open_tag + value + close_tag )

# Generate some basic info for each glyph
f.write( "\n\t<glyphs>\n" )

# Iterate though the glyph collection
for glyph in ThisFont.glyphs:
	f.write( "\t\t<glyph>\n")
	f.write( "\t\t\t<name>" + glyph.name + "</name>\n" )
	f.write( "\t\t\t<note>" + str( glyph.note ) + "</note>\n" )
	f.write( "\t\t\t<node_count>" + str( len( glyph.nodes ) ) + "</node_count>\n" )
	f.write( "\t\t\t<node_hash>" + hashlib.sha224(str(glyph.nodes)).hexdigest() + "</node_hash>\n" )
	if len( glyph.anchors ) > 0:
		f.write( "\t\t\t<anchors>\n" )
		for anchor in glyph.anchors:
			f.write( "\t\t\t\t<anchor>" + str( anchor.name ) + ": " + str( anchor.x ) + "," + str( anchor.y ) + "</anchor>\n" )
		f.write( "\t\t\t</anchors>\n" )
	
	# Process components

	f.write( "\t\t\t<component_count>" + str( len( glyph.components ) ) + "</component_count>\n" )
	if len( glyph.components ) > 0:
		f.write( "\t\t\t<components>\n" )
		for component in glyph.components:
			componentGlyph = ThisFont.glyphs[component.index]
			f.write( "\t\t\t\t<component>" + str( componentGlyph.name ) + ": " \
				+ "delta: " + str( component.delta.x ) + "," + str( component.delta.y ) \
				+ ", scale: " + str( component.scale.x ) + "," + str( component.scale.y ) + "</component>\n" )

		f.write( "\t\t\t</components>\n" )

	f.write( "\t\t\t<width>" + str( glyph.width ) + "</width>\n" )
	f.write( "\t\t\t<unicode>" + USVstr( glyph.unicode ) + "</unicode>\n" )
	f.write( "\t\t\t<unicode_count>" + str( len( glyph.unicodes ) ) + "</unicode_count>\n" )
	f.write( "\t\t</glyph>\n");

# Terminate the <glyphs> element
f.write( "\t</glyphs>\n" )

# Terminate the <font> element
f.write( "</font>\n" )

# Wrap up
f.close()

print "Output complete."

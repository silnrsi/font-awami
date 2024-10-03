#FLM: Output XML for APs
# Author: M. Hosken
# Description: Outputs attachment point information and notes as XML file for TTFBuilder
# 
# Copyright M. Hosken and SIL Global, licensed under Perl Artistic license.
# martin_hosken@sil.org
#
# 1.02a JVG   18-MAY-2005 Revised to eliminate reformatting using tidy or saxon
# 1.02  AKW   10-FEB-2005 Rename to FLWriteXml from write_xml.
#                         Revise to ouput XML using SAX
# 1.01  AKW   10-MAR-2004 Output glyph notes to conform to DTD (inside <note> element)
#                         Add Escape() to handle characters with special meaning in XML
# 1.00  MJPH  7-FEB-2003  First public release

# user controls

# output entries for all glyphs even those with nothing interesting to say about them
all_glyphs = 1

# output the glyph id as part of the information
output_gid = 1


# no user serviceable parts under here!
from xml.sax.saxutils import XMLGenerator
import os

def print_glyph(font, glyph, index):
    if index % 100 == 0:
        print "%d: %s" % (index, glyph.name)
      
    if (not all_glyphs and len(glyph.anchors) == 0 and len(glyph.components) == 0 and not glyph.note):
        return
    attribs = {}
    if output_gid:
        attribs["GID"] = unicode(index)
    if glyph.unicode:
        attribs["UID"] = unicode("U+%04X" % glyph.unicode)
    if glyph.name:
        attribs["PSName"] = unicode(glyph.name)
    xg.startElement("glyph", attribs)
    
    for anchor in (glyph.anchors):
        xg.startElement("point", {"type":unicode(anchor.name), "mark":unicode(anchor.mark)})
        xg.startElement("location", {"x":unicode(anchor.x), "y":unicode(anchor.y)})
        xg.endElement("location")
        xg.endElement("point")

    for comp in (glyph.components):
        g = font.glyphs[comp.index]
        r = g.GetBoundingRect()
        x0 = 0.5 * (r.ll.x * (1 + comp.scale.x) + r.ur.x * (1 - comp.scale.x)) + comp.delta.x
        y0 = 0.5 * (r.ll.y * (1 + comp.scale.y) + r.ur.y * (1 - comp.scale.y)) + comp.delta.y
        x1 = 0.5 * (r.ll.x * (1 - comp.scale.x) + r.ur.x * (1 + comp.scale.x)) + comp.delta.x
        y1 = 0.5 * (r.ll.y * (1 - comp.scale.x) + r.ur.y * (1 + comp.scale.y)) + comp.delta.y

        attribs = {"bbox":unicode("%d, %d, %d, %d" % (x0, y0, x1, y1))}
        attribs["GID"] = unicode(comp.index)
        if (g.unicode):
            attribs["UID"] = unicode("U+%04X" % g.unicode)
        if (g.name):
            attribs["PSName"] = unicode(g.name)
        xg.startElement("compound", attribs)
        xg.endElement("compound")
        
    if glyph.mark:
        xg.startElement("property", {"name":unicode("mark"), "value":unicode(glyph.mark)})
        xg.endElement("property")
        
    if glyph.customdata:
        xg.startElement("customdata", {})
        xg.characters(unicode(glyph.customdata.strip()))
        xg.endElement("customdata")
        
    if glyph.note:
        xg.startElement("note", {})
        xg.characters(glyph.note)
        xg.endElement("note")
    xg.endElement("glyph")

# KLUDGE for Awami:
newName = fl.font.file_name.replace(" ", "")
newName2 = newName.replace(".VFB", ".vfb")
outname = newName2.replace(".vfb", "_AP.xml")
if outname[25:31] == "AWAMIN" or outname[25:28] == "AWB":
    outname = "AwamiNastaliqRegular_AP.xml"
###############
fh = open(outname, "w")
print "filename =", outname
xg = XMLGenerator(fh, "utf-8")
xg.startDocument()

xg.startElement("font", {'name':unicode(fl.font.font_name), "upem":unicode(fl.font.upm)})
for i in range(0, len(fl.font.glyphs)):
    print_glyph(fl.font, fl.font.glyphs[i], i)
xg.endElement("font")

xg.endDocument()
fh.close()

print 'done'

# FL script to select composite glyphs which have overlapping components (based on contours)
# Expand to handle glyphs containing both contours and composites
# add logging of selected glyphs
# handle glyphs with more than one overlapping contour

#can set to None to disable report file
strRptFn = None  # r"c:\Roman Font\rfs_code\build\FLSelectOverlap_rpt.txt"

print "Selecting composite and hybrid glyphs with overlapping components"

def UniStr(u):
    if u:
        return "U+" + "%04X" % u
    else:
        return "No USV" #length same as above

#args are FL Rect and list of FL Rect
#return list of indexes in the list where rects overlap
def FindOverlapping (rect, lst_rect):
    lst_ix = []
    for i in range(len(lst_rect)):
        if rect.Check(lst_rect[i]):
            lst_ix.append(i)
    return lst_ix

#fl.Unselect() #unselect all glyphs
lst_overlap = [] #store info for reporting
for g in fl.font.glyphs:
    if (len(g.components) > 1) or (g.GetContoursNumber() and g.components):
        #process glyphs with more than one component or a mix of contours and components
        #create a list of glyphs with one glyph for each item to be checked for overlap
        lst_glyph = []
        g1 = Glyph(g)
        g1.components.clean() #create a glyph containing only contours (could be empty)
        lst_glyph.append(g1)
        for c in g.components:
            #add one glyph per component
            #Get() returns a Glyph object adjusted by delta (and scale?) in Component object
            lst_glyph.append(c.Get())
            
        lst_BoundingRect = []
        for g1 in lst_glyph:
            #create a list of bounding rects
            #calling GetBoundingRect more than once on a glyph destablizes FL
            lst_BoundingRect.append(g1.GetBoundingRect()) 

        fOverlap = 0
        for i in range(len(lst_BoundingRect)):
            overlap_ix = FindOverlapping(lst_BoundingRect[i], lst_BoundingRect[i + 1:])
            for ix in overlap_ix:
                #test glyphs with overlapping bounding boxes for overlapping contours
                #don't really need to use bounding boxes but it could be a useful hook for later
                g1 = Glyph(lst_glyph[i]) #make copy to protect original during Bintersect()
                g2 = lst_glyph[i + 1 + ix]
                g1.Bintersect(g2)
                if len(g1.nodes) > 0:
                    fl.Select(g.index)
                    lst_overlap.append((g.index, UniStr(g.unicode), g.name))
                    fOverlap = 1
                    break
            if fOverlap:
                break

#for t in lst_overlap:
#    print "glyph id: %d  USV: %s  name: %s" % t
print "%s glyphs selected" % len(lst_overlap)

if strRptFn:
	fRpt = open(strRptFn, "w")
	fRpt.write("Glyphs which were selected by SelectOverlap for subsequent dereferencing and merging.\n")
	for t in lst_overlap:
		fRpt.write("glyph id: %d  USV: %s  name: %s\n" % t)
	fRpt.write("%s glyphs selected" % len(lst_overlap))
	fRpt.close()

#FL script to select all glyphs which have scaled components. Use Python 2.2

logfn = None  # r"c:\Roman Font\rfs_code\build\FLSelectScaled_rpt.txt"

#***************

print "Selecting composite glyphs with scaled components"

def UniStr(u):
    if u:
        return "U+" + "%04X" % u
    else:
        return "No USV" #length same as above

if logfn:
    logf = open(logfn, "w")
    logf.write("Glyphs which were selected by SelectScaled for subsequent dereferencing and merging.\n")

#fl.Unselect() #unselect all glyphs - comment out so as to not undo FLSelectOverlap.py
ct = 0
for g in fl.font.glyphs:
    if g.components:
        for c in g.components:
            if c.scale.x != 1.0 or c.scale.y != 1.0:
                fl.Select(g.index)
                ct += 1
                #print g.name, c
                if logfn:
                    logf.write("glyph id: %s   USV: %s   name: %s\n" % (g.index, UniStr(g.unicode), g.name))

if logfn:
    logf.write("%d glyphs selected\n" % ct)
    logf.close()

print "%d glyphs selected" % ct

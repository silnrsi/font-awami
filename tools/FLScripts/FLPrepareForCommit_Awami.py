#FLM: FL Prepare for Commit
import os
import shutil

user = "PM"
#user = "SC"

if user == "SC" :
    vfb2ufo_util = "C:/FontUtils/VFB2UFO/exe/vfb2ufo"
    vfb_path = '"C:\\Awami-Git\\source\\AwamiNastaliqRegular.vfb"'
    ttf_output_path = "C:\\Awami-Git\\source\\"
    fl_macro_path = "C:\\Awami-Git\\tools\\FLScripts\\"
    
else : # user = PM
    vfb2ufo_util = "/usr/local/bin/vfb2ufo"
    vfb_path = "/Users/martinpk/Documents/Fonts/ABS/font-awami/source/AwamiNastaliqRegular.vfb"
    ttf_output_path = "/Users/martinpk/Documents/Fonts/ABS/font-awami/source/"
    fl_macro_path = "/Users/martinpk/Library/Application Support/FontLab/Studio 5/Macros/Custom/"


print "---------------------------------------------------------------"
print "Processing VFB " + vfb_path
print

# Save before doing anything
print "Saving VFB..."
fl.Save( vfb_path )

# Do XML dump

execfile(fl_macro_path + "FontToXMLDump_Awami.py")
execfile(fl_macro_path + "FLWriteAPXml_Awami.py")

if user == "SC" :
    # The Windows version of vfb2ufo gets confused about the slashes in the paths.
    # It helps to delete the folder first.
    ufo_dir = ttf_output_path + "AwamiNastaliqRegular.ufo\\"
    shutil.rmtree(ufo_dir)

# Generate the UFO
print "Generating UFO..."
# -fo to force overwrite
command = vfb2ufo_util + " -fo " + vfb_path
print command
os.system(command)
print "Done."

if user != "SC" :
    # De-reference components
    print
    print "De-referencing components..."
    #fl.CallCommand(32873) #EditSelectAll constant matches "Edit-Select All" menu item   -- doesn't seem to work
    for g in fl.font.glyphs:
        fl.Select(g.index) #select all glyphs
    fl.CallCommand(32925) #SymbolDecompose constant matches "Glyph-Decompose menu" item
    
    # Merge overlaps
    print "Merging contours on all glyphs..."
    fl.CallCommand(32846) #ActionRemoveOverlap constant matches "Tools-Outline-Merge Outlines" menu item

# Generate TTF
ttf_output_file = ttf_output_path + "AwamiNastaliqRegular.ttf"
print
print "Generating TTF to " + ttf_output_file
fl.GenerateFont(ftTRUETYPE, ttf_output_file)
print "Done."

# Discard VFB (the components are all de-referenced and the overlaps are merged, so we don't want to keep it)
fl.Close(0)

# Re-open the original VFB
fl.Open( vfb_path )

print

print "Processing complete"
print "---------------------------------------------------------------"
print
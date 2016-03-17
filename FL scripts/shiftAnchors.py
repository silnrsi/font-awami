# FontLab script to shift anchors with a given name by a certain amount.

##############################################
##
##  Awami-specific code
##
##############################################

def anchorShifts() :
    anchorDict = {
		"nUpper"        :   Point(0, 110),
		"tahUpper"      :   Point(0, 110),
		"hamzaUpper"    :   Point(0, 110),
		"n1Lower"       :   Point(0, -110),
		"n23Lower"      :   Point(0, -110),
		"tahLower"      :   Point(0, -110),
		"hamzaLower"    :   Point(0, -110)
	}
    return anchorDict
    
    
def isBaseGlyph(glyphName) :
	if glyphName == "absNoonGunnaMark"	: return False
	
	if glyphName[0:7] == "absAlef"			:	return True
	if glyphName[0:6] == "absBeh"				: return True
	if glyphName[0:6] == "absTeh"				: return True
	if glyphName[0:7] == "absTheh"			: return True
	if glyphName[0:6] == "absPeh"				: return True
	if glyphName[0:7] == "absTteh"			: return True
	if glyphName[0:7] == "absBeeh"			: return True
	if glyphName[0:7] == "absJeem"			:	return True
	if glyphName[0:6] == "absHah"				: return True
	if glyphName[0:7] == "absKhah"			: return True
	if glyphName[0:7] == "absDyeh"			: return True
	if glyphName[0:8] == "absTcheh"			: return True
	if glyphName[0:7] == "absSeen"			: return True
	if glyphName[0:8] == "absSheen"			: return True
	if glyphName[0:6] == "absSad"				: return True
	if glyphName[0:6] == "absDad"				: return True
	if glyphName[0:6] == "absTah"				: return True
	if glyphName[0:6] == "absZah"				: return True
	if glyphName[0:6] == "absAin"				: return True
	if glyphName[0:8] == "absGhain"			: return True
	if glyphName[0:6] == "absFeh"				: return True
	if glyphName[0:6] == "absQaf"				: return True
	if glyphName[0:6] == "absLam"				: return True
	if glyphName[0:8] == "absKeheh"			: return True
	if glyphName[0:6] == "absKaf"				: return True
	if glyphName[0:6] == "absGaf"				: return True
	if glyphName[0:8] == "absNgoeh"			: return True
	if glyphName[0:7] == "absGueh"			: return True
	if glyphName[0:6] == "absLam"				: return True
	if glyphName[0:7] == "absMeem"			: return True
	if glyphName[0:7] == "absNoon"			: return True
	if glyphName[0:8] == "absRnoon"			: return True
	if glyphName[0:17] == "absHehDoachashmee" :  return True
	if glyphName[0:10] == "absHehGoal"	: return True
	if glyphName[0:6] == "absDal"				: return True
	if glyphName[0:7] == "absThal"			: return True
	if glyphName[0:7] == "absDdal"			: return True
	if glyphName[0:6] == "absReh"				: return True
	if glyphName[0:7] == "absZain"			: return True
	if glyphName[0:7] == "absRreh"			: return True
	if glyphName[0:6] == "absJeh"				: return True
	if glyphName[0:6] == "absWaw"				: return True
	if glyphName[0:11] == "nlqChotiyeh"	:	return True
	if glyphName[0:6] == "absYeh"				: return True
	if glyphName[0:14] == "absKashmiriYeh" : return True
	if glyphName[0:10] == "nlqBariyeh"	: return True
	
	if glyphName[0:8] == "absComma"			: return True
	if glyphName[0:11] == "absFullStop"	: return True
	if glyphName[0:12] == "absSemicolon" : return True
		
	# components
	if glyphName[0:4] == "_beh"			: return True
	if glyphName[0:5] == "_Jeem" 		: return True
	if glyphName[0:4] == "_Reh"			: return True
	
	return False


def shouldFix(glyph) :
	glyphName = glyph.name

	# Don't fix it if it's not yet designed - composite of empty glyph.
	if glyph.components :
		for oneComp in glyph.components :
			if oneComp.index == 0 :
				#print glyphName," - not yet designed"
				return False
				
	if glyphName[0:1] == "_" :
		return False
				
	# Fix only initials and medials:
	if isBaseGlyph(glyphName) and ("Ini" in glyphName or "Med" in glyphName):
		return True
	else :
		return False


def shouldAdjustAnchor(glyph, anchorName) :
	if not shouldFix(glyph) :
		return False
	
	# Don't adjust lower nuqtas for pre-bariyeh forms:
	if "Lower" in anchorName and ".by" in glyph.name :
		return False
	
	# Dont' adjust upper nuqtas for Tah forms:
	if "Upper" in anchorName and "Tah" in glyph.name :
		return False
		
	return True
	

##############################################
##
##  General code
##
##############################################


def shiftAnchors(glyph, anchorDict) :
	newAnchorList = list()
	adjustedList = list()
	#print "adjustAnchors",len(glyph.anchors)
	for oneAnchor in glyph.anchors :
		anchorName = oneAnchor.name
		deltaX = 0
		deltaY = 0
		if anchorDict.has_key(anchorName) and shouldAdjustAnchor(glyph, anchorName) :
			deltaPt = anchorDict[anchorName]
			deltaX = deltaPt.x
			deltaY = deltaPt.y
			adjustedList.append(anchorName)
		newX = oneAnchor.x + deltaX
		newY = oneAnchor.y + deltaY
		newAnchor = Anchor(anchorName, newX, newY)
		newAnchorList.append(newAnchor)
		#if anchorDict.has_key(anchorName) :
		#	print anchorName,"(",oneAnchor.x,",",oneAnchor.y, ") -> (",newAnchor.x,",",newAnchor.y,")"
		#else :
		#    print anchorName,"unchanged"
        
	while len(glyph.anchors) > 0 :
		del glyph.anchors[0]
        
	for oneAnchor in newAnchorList :
		glyph.anchors.append(oneAnchor)
	
	fl.UpdateGlyph(glyph.index)
	
	print glyph.name,adjustedList
	
	#print "resulting anchors:",len(glyph.anchors)


##############################################
##
##  Main routine
##
##############################################

print "\n==============\nShift Anchor Points\n"
##print "Fonts  opened: ", len(fl)

anchorDict = anchorShifts()

processAll = False  # only do the selected glyph

for oneGlyph in fl.font.glyphs :
	
	glyphName = oneGlyph.name
	if processAll or (oneGlyph != None and glyphName == fl.glyph.name) :
	    if shouldFix(oneGlyph) :
	        shiftAnchors(oneGlyph, anchorDict)

print "\nDone\n"

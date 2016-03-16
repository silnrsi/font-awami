# FontLab script to adjust side bearings of certain glyphs to be a specified width.

##############################################
##
##  Awami-specific code
##
##############################################

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
		
	# components
	if glyphName[0:4] == "_beh"			: return True
	if glyphName[0:5] == "_Jeem" 		: return True
	if glyphName[0:4] == "_Reh"			: return True
#	if glyphName[0:10] == "_gafStroke" 	: return True
	
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
				
	# Fix isolates, initials, and finals, but not medials.
	if isBaseGlyph(glyphName) and not "Med" in glyphName :
		return True


def specialLeft(glyphName) :
	if glyphName[0:6] == "absDal"				: return True
	if glyphName[0:7] == "absThal"			: return True
	if glyphName[0:7] == "absDdal"			: return True
	if glyphName[0:6] == "absReh"				: return True
	if glyphName[0:7] == "absZain"			: return True
	if glyphName[0:7] == "absRreh"			: return True
	if glyphName[0:6] == "absJeh"				: return True
	if glyphName[0:6] == "absWaw"				: return True
	return False


##############################################
##
##  General code
##
##############################################


def getOutlineLeft(glyph) :
	if len(glyph) :
		glyphBb = glyph.GetBoundingRect()
		return glyphBb.x
	else :
		return 32700 # arbitrary big number
		
def getOutlineRight(glyph) :
	if len(glyph) :
		glyphBb = glyph.GetBoundingRect()
		return glyphBb.x + glyphBb.width
	else :
		return -32700 # arbitrary small number


def getComponentsLeft(glyph) :
	curLeft = 32700
	for oneComp in glyph.components :
		cnentGlyph = fl.font.glyphs[oneComp.index]
		if isBaseGlyph(cnentGlyph.name) :
			#####print cnentGlyph.name
			cnentBb = cnentGlyph.GetBoundingRect() # replace with recursive function
			cnentLeft = cnentBb.x
			deltaLeft = oneComp.delta.x + cnentLeft
			#>>>>print cnentGlyph.name, oneComp.delta, cnentLsb, "=>", deltaLsb
			curLeft = min(curLeft, deltaLeft)
		#else :
			#print oneComp.index,cnentGlyph.name
	return curLeft
	
def getComponentsRight(glyph) :
	curRight = -32700
	for oneComp in glyph.components :
		cnentGlyph = fl.font.glyphs[oneComp.index]
		if isBaseGlyph(cnentGlyph.name) :
			#####print cnentGlyph.name
			cnentBb = cnentGlyph.GetBoundingRect() # replace with recursive function
			cnentRight = cnentBb.x + cnentBb.width
			deltaRight = oneComp.delta.x + cnentRight
			#>>>>print cnentGlyph.name, oneComp.delta, cnentLsb, "=>", deltaLsb
			curRight = max(curRight, deltaRight)
		#else :
			#print oneComp.index,cnentGlyph.name
	return curRight


def calcLeftShift(glyph, newLsb) :
	leftOutline = getOutlineLeft(glyph)
	leftComponents = getComponentsLeft(glyph)
	#print "leftOutline=",leftOutline
	#print "leftComponents=",leftComponents
	curLeft = min(leftOutline, leftComponents)
	deltaLeft = newLsb - curLeft
	#print "delta=",deltaLeft
	return deltaLeft
		
def calcRightAdjustment(glyph, newRsb) :
	rightOutline = getOutlineRight(glyph)
	rightComponents = getComponentsRight(glyph)
	#print "rightOutline=",rightOutline
	#print "rightComponents=",rightComponents
	curRight = max(rightOutline, rightComponents)
	curSize = glyph.GetMetrics()
	curRsb = curSize.x - curRight
	#print "curRsb=",curRsb
	deltaRight = newRsb - curRsb
	#print "delta=",deltaRight
	return deltaRight
	
	
def adjustOutline(glyph, delta) :
	if len(glyph) :
		i = 0;
		for oneNode in glyph.nodes :
			t = oneNode.type
			pt = oneNode.point
			newPt = Point(pt.x + delta, pt.y)
			pt.Assign(newPt)
			i = i + 1

# OBSOLETE
def adjustComponents_XXX(glyph, delta) :
	for oneComp in glyph.components :
		cnentGlyph = fl.font.glyphs[oneComp.index]
		if shouldFix(cnentGlyph) :
		    print cnentGlyph.name,"shifted separately"
		elif specialLeft(cnentGlyph) :
		    pass
		else :
			print "shifting",cnentGlyph.name
			shiftPt = Point(delta, 0)
			oneComp.delta.Shift(shiftPt)
			
			idx = oneComp.index
			fl.UpdateGlyph(idx)
			print "UpdateGlyph(",idx,")"
#####

def adjustComponents(glyph, deltaLeft) :
	##print " num of comp=",len(glyph.components)
	newComponentList = list()
	for oneComp in glyph.components :
		compGlyph = fl.font.glyphs[oneComp.index]
		if shouldFix(compGlyph) :
			##print " ",compGlyph.name, "shifted separately"
			newComponentList.append(Component(oneComp)) #copy
		elif specialLeft(compGlyph) :
			newComponentList.append(Component(oneComp)) #copy
		else :
			##print " shifting",compGlyph.name			
			idx = oneComp.index
			newPt = Point(oneComp.delta.x + deltaLeft, oneComp.delta.y)
			newComp = Component(idx, newPt)
			newComponentList.append(newComp)
    
	while len(glyph.components) > 0 :
		del glyph.components[0]
        
	for oneComp in newComponentList :
		glyph.components.append(oneComp)


def adjustAnchors(glyph, deltaLeft) :
	newAnchorList = list()
	##print "adjustAnchors",len(glyph.anchors)
	for oneAnchor in glyph.anchors :
		anchorName = oneAnchor.name
		newX = oneAnchor.x + deltaLeft
		newY = oneAnchor.y
		newAnchor = Anchor(anchorName, newX, newY)
		newAnchorList.append(newAnchor)
		##print anchorName,oneAnchor.x, "->",newAnchor.x
        
	while len(glyph.anchors) > 0 :
		del glyph.anchors[0]
        
	for oneAnchor in newAnchorList :
		glyph.anchors.append(oneAnchor)
		
	##print "resulting anchors:",len(glyph.anchors)


def shiftLeft(glyph, deltaX) :
	print "shiftLeft",glyph.name,"-",deltaX
	ptDelta = Point(deltaX, 0)
	glyph.Shift(ptDelta)
	adjustAnchors(glyph, deltaX)
	adjustComponents(glyph, deltaX)

	
def fixRightSideBearing(glyph, newRsb) :
	print "fixRightSideBearing",glyph.name,"-",newRsb
	deltaX = calcRightAdjustment(glyph, newRsb)
	oldSize = glyph.GetMetrics()
	#print "oldSize=",oldSize
	newSize = Point(oldSize.x + deltaX, oldSize.y)
	#print "newSize=",newSize
	glyph.SetMetrics(newSize)
	idx = glyph.index
	fl.UpdateGlyph(idx)
	

##############################################
##
##  Main routine
##
##############################################

print "\n==============\nFix Side Bearings\n"
##print "Fonts  opened: ", len(fl)

newLsb = 90
newRsb = 90

processAll = False  # only do the selected glyph

glyphsToShift = dict()

for oneGlyph in fl.font.glyphs :
	if oneGlyph != None :
		if shouldFix(oneGlyph) :
			if "Ini" in oneGlyph.name or "Med" in oneGlyph.name :
				#print "don't fix LSB -",oneGlyph.name
				pass
			else :
				glyphsToShift[oneGlyph.name] = calcLeftShift(oneGlyph, newLsb)
			

for oneGlyph in fl.font.glyphs :
	
	glyphName = oneGlyph.name
	if processAll or (oneGlyph != None and glyphName == fl.glyph.name) :
		
		# Fix right side bearings:
		
		if "Fin" in oneGlyph.name or "Med" in oneGlyph.name:
			#print "don't fix RSB"
			pass
		elif shouldFix(oneGlyph) :
			print oneGlyph.name
			fixRightSideBearing(oneGlyph, newRsb)

		# Fix left side bearings:
		
#		if glyphName in glyphsToShift and glyphsToShift[glyphName] != 0 :
#			if "Ini" in oneGlyph.name :
#				#print "don't fix LSB for",glyphName
#				pass
#			else :
#				delta = glyphsToShift[glyphName]
#				#print "adjust LSB for", glyphName," - ",delta
#				shiftLeft(oneGlyph, delta)				
				
	  #else :
	  #	print "don't fix: ",oneGlyph.name

print "\nDone\n"

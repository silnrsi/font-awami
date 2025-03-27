#!/usr/bin/python3

# Outputs a set of rules to perform arithmetic

# Run this script from the tools/scripts directory where the file is located:
#		python3 genArithmeticLookups.py
#
# See the individual functions for examples of output.

kwMin = 0
kwMax = 1600

dxMin = -500
dxMax = 2500
pxMin = 0
pxMax = 4000
pxfMin = 0
pxfMax = 3000

dyMin = -300
dyMax = 3000
pyMin = 0
pyMax = 3000

ascMin = -500
ascMax = 3000
dscMin = -1500
dscMax = 3000

ytMin = 0
ytMax = 3000
ybMin = -1500
ybMax = 3000

inc = 100

# These lists should match the _InsertNuqtaDiacMarker lookup:
# upperMarkHts = [600, 950]	# 1 dot, 3 dots
# lowerMarkHts = [600, 700, 950]	# 1 dot/shadda, hehhook, zabar/zair/pesh,

upperMarkHts = [600, 1000]	# 1 dot, 3 dots
lowerMarkHts = [600, 700, 1000]	# 1 dot/shadda, hehhook, zabar/zair/pesh,

#import sys

def GenClasses(prefix, cname, minv, maxv):

	outstr = "@" + cname + " = ["
	v = minv
	while v <= maxv:
		outstr += prefix + ValueName(v) + " "
		if (v % 1000) == 0 and v > minv and v < maxv:
			print(outstr, file=fout)  # output and start a new line
			outstr = "  ";
		v += inc
	print(outstr + "];", file=fout)

# end of GenClasses

def GenLookups_MarkersYtb2AscDsc():

	### Example:
	# lookup MarkersYtb2AscDsc {
	# 	sub yt0 by asc0;
	# 	sub yt50 by asc50;
	# 	...
	# 	sub ybN1500 by dscN1500;
	# 	sub ybN1450 by dscN1450;
	# 	...
	# } MarkersYtb2AscDsc;

	print("lookup MarkersYtb2AscDsc {", file=fout)
	print("  lookupflag UseMarkFilteringSet [@YtMarker @YbMarker];", file=fout)

	minv = max(ascMin, ytMin)
	maxv = min(ascMax, ytMax)
	for v in range(minv, maxv+inc, inc):
		print("  sub yt" + ValueName(v) + " by asc" + ValueName(v) + ";", file=fout)

	minv = max(dscMin, ybMin)
	maxv = min(dscMax, ybMax)
	for v in range(minv, maxv+inc, inc):
		print("  sub yb" + ValueName(v) + " by dsc" + ValueName(v) + ";", file=fout)

	print("} MarkersYtb2AscDsc;", file=fout)

# end of GenLookups_MarkersYtb2AscDsc

def GenLookup_InitPos(axis, dminv, dmaxv, pminv, pmaxv):
	
	if axis == "x":
		lname = "_InitPosX"
		filterSet = "@XMarkers"
		dGname = "dx"
		pGname = "px"
	else:
		lname = "_InitPosY"
		filterSet = "@YMarkers"
		dGname = "dy"
		pGname = "py"
	
	print("lookup " + lname + " {", file=fout)
	print("  lookupflag UseMarkFilteringSet " + filterSet + ";", file=fout)
	
	dv = dminv
	while dv <= dmaxv:
		pv = dv
		if pv < pminv: pv = pminv
		# sub pxNULL'  lookup _Set100  dx100;
		print("  sub " + pGname + "NULL'  lookup _Set" + ValueName(pv) + "\t\t" + dGname + ValueName(dv) + ";", file=fout)
		dv += inc
	
	print("} " + lname + ";\n", file=fout)

# end of GenLookup_InitPos

def GenLookup_SetValues():

	### Example:
	# lookup _Set150 {
	# 	sub pxNULL  by  px150;
	# 	sub pxfNULL by  pxf150;
	# 	sub pyNULL  by  py150;
	# 	sub @AscMarker by  yt150;
  	# 	sub @YtMarker  by  yt150;
	# 	sub @DscMarker by  yb150;
	# 	sub @YbMarker  by  yb150;
	# } _Set150;
	
	minv = min(min(min(min(min(pxMin, pyMin), ascMin), dscMin), ytMin), ybMin)
	maxv = max(max(max(max(max(pxMax, pyMax), ascMax), dscMax), ytMax), ybMax)
	
	v = minv
	while v <= maxv:
		print("lookup " + "_Set" + ValueName(v) + " {", file=fout)
		if pxMin <= v and v <= pxMax:
			print("  sub pxNULL  by  px" + ValueName(v) + ";", file=fout)
		if pxfMin <= v and v <= pxfMax:
			print("  sub pxfNULL by  pxf" + ValueName(v) + ";", file=fout)
		if pyMin <= v and v <= pyMax:
			print("  sub pyNULL  by  py" + ValueName(v) + ";", file=fout)
		if ytMin <= v and v <= ytMax:
			print("  sub @AscMarker by  yt" + ValueName(v) + ";", file=fout)
			print("  sub @YtMarker  by  yt" + ValueName(v) + ";", file=fout)
		if ybMin <= v and v <= ybMax:
			print("  sub @DscMarker by  yb" + ValueName(v) + ";", file=fout)
			print("  sub @YbMarker  by  yb" + ValueName(v) + ";", file=fout)
		print("} _Set" + ValueName(v) + ";\n", file=fout)
		
		v += inc
	# end of while

# end of GenLookup_SetValues

def GenLookup_AddMarkers(axis, dminv, dmaxv, pminv, pmaxv):
	
	### Example:
	# lookup _AddMarkersX {
	# 	lookupflag UseMarkFilteringSet @XMarkers;
	# 	sub pxNULL'  lookup _PosPlusX0	@DxMarker  px0;
	# 	sub pxNULL'  lookup _PosPlusX50	@DxMarker  px50;
	# 	sub pxNULL'  lookup _PosPlusX100	@DxMarker  px100;
	# 	...
	# } _AddMarkersX;

	if axis == "x":
		lname = "_AddMarkersX"
		lname2 = "_PosPlusX"
		filterSet = "@XMarkers"
		dClass = "@DxMarker"
		dGname = "dx"
		pGname = "px"
	else:
		lname = "_AddMarkersY"
		lname2 = "_PosPlusY"
		filterSet = "@YMarkers"
		dClass = "@DyMarker"
		dGname = "dy"
		pGname = "py"

	print("lookup " + lname + " {", file=fout)
	print("  lookupflag UseMarkFilteringSet " + filterSet + ";", file=fout)
	
	pv = pminv
	while pv <= pmaxv:
		# sub pxNULL'  lookup _PosPlus100  @DxMarker  px100;
		print("  sub " + pGname + "NULL'  lookup " + lname2 + ValueName(pv) + "\t" + dClass + "  " +  pGname + ValueName(pv) + ";", file=fout)
		pv += inc
	# overflow 
	#print("  sub " + pGname + "NULL'  lookup " + "_Set" + ValueName(pmaxv) + "\t" + dClass + "  " + filterSet + ";", file=fout)
		
	print("} " + lname + ";\n", file=fout)

# end of GenLookup_AddMarkers

def GenLookup_AddMarkersForward(axis, dminv, dmaxv, pminv, pmaxv):

	### Example:
	# lookup _AddMarkersXforward {
	# 	lookupflag UseMarkFilteringSet @XfMarkers;
	# 	sub pxf0		@DxMarker		pxfNULL'  lookup _PosPlusXf0;
	# 	sub pxf50		@DxMarker		pxfNULL'  lookup _PosPlusXf50;
	# 	sub pxf100		@DxMarker		pxfNULL'  lookup _PosPlusXf100;
	# 	sub pxf150		@DxMarker		pxfNULL'  lookup _PosPlusXf150;'
	# 	...
	# } _AddMarkerXforward;

	if axis == "x":
		lname = "_AddMarkersXforward"
		lname2 = "_PosPlusXf"
		filterSet = "@XfMarkers"
		dClass = "@DxMarker"
		dGname = "dx"
		pGname = "pxf"
	else:  # not used
		lname = "_AddMarkersYforward"
		lname2 = "_PosPlusYf"
		filterSet = "@YfMarkers"
		dClass = "@DyMarker"
		dGname = "dy"
		pGname = "pyf"

	print("lookup " + lname + " {", file=fout)
	print("  lookupflag UseMarkFilteringSet " + filterSet + ";", file=fout)
	
	pv = pminv
	while pv <= pmaxv:
		# sub pxf100	 @DxMarker  pxfNULL'  lookup _PosPlusXf100;
		print("  sub " + pGname + ValueName(pv) + "\t\t" + dClass + "\t\t" + pGname + "NULL'  lookup " + lname2 + ValueName(pv) + ";", file=fout)
		pv += inc
		
	print("} " + lname + ";\n", file=fout)

# end of GenLookup_AddMarkers

def GenLookups_PosPlus(axis, forward, dminv, dmaxv, pminv, pmaxv):

	### Example:
	# lookup _PosPlusX250 {
	# 	lookupflag UseMarkFilteringSet @XMarkers;
	# 	...
	# 	sub pxNULL'  lookup _Set600		dx350;
	# 	sub pxNULL'  lookup _Set650		dx400;
	# 	...
	# } _PosPlusX250;
	#
	# or for the forward calculation:
	#
	# lookup _PosPlusXf250 {
	# 	lookupflag UseMarkFilteringSet @XfMarkers;
	# 	...
	# 	sub dx350		pxfNULL'  lookup _Set600;
	# 	sub dx400		pxfNULL'  lookup _Set650;
	# 	sub dx450		pxfNULL'  lookup _Set700;'
	# 	...
	# } _PosPlusXf250;

	if (axis == 'x'):
		lookupName = "_PosPlusX"
		filterSet = "@XMarkers"
		dClass = "@DxMarker"
		dGname = "dx"
		pGname = "px"
		if forward: 
			lookupName += "f"
			filterSet = "@XfMarkers"
			pGname = "pxf"
	else:
		lookupName = "_PosPlusY"
		filterSet = "@YMarkers"
		dClass = "@DyMarker"
		dGname = "dy"
		pGname = "py"

	pv = pminv
	while pv <= pmaxv:
		if forward:
			GenLookup_PosPlusForward(lookupName, filterSet, dClass, dGname, pGname, dminv, dmaxv, pminv, pmaxv, pv)
		else:
			GenLookup_PosPlusBackward(lookupName, filterSet, dClass, dGname, pGname, dminv, dmaxv, pminv, pmaxv, pv)
		pv += inc

# end of GenLookups_PosPlus


def GenLookup_PosPlusBackward(lname, fset, dClass, dGname, pGname, dminv, dmaxv, pminv, pmaxv, pv):
	print("lookup " + lname + ValueName(pv) + " {", file=fout)
	print("  lookupflag UseMarkFilteringSet " + fset + ";", file=fout)
	
	v2 = dminv
	while v2 <= dmaxv:
		pnewv = v2 + pv
		if pnewv + inc > pmaxv:
			# output a fall-back rule and quit
			# sub pxNULL'  lookup _Set4000  @DxMarker;
			print("  sub " + pGname + "NULL'  lookup _Set" + ValueName(pmaxv) + "\t\t" + dClass + ";", file=fout)
			break

		if pnewv < pminv:
			pnewv = pminv
			
		# sub pxNULL'  lookup _Set150  dx50;
		print("  sub " + pGname + "NULL'  lookup _Set" + ValueName(pnewv) + "\t\t" + dGname + ValueName(v2) + ";", file=fout)
		v2 += inc
		
	print("} " + lname + str(pv) + ";\n", file=fout)
	
# end of GenLookup_PosPlusBackwards

def GenLookup_PosPlusForward(lname, fset, dClass, dGname, pGname, dminv, dmaxv, pminv, pmaxv, pv):
	print("lookup " + lname + ValueName(pv) + " {", file=fout)
	print("  lookupflag UseMarkFilteringSet " + fset + ";", file=fout)
	
	v2 = dminv
	while v2 <= dmaxv:
		pnewv = v2 + pv
		if pnewv + inc > pmaxv:
			# output a fall-back rule and quit
			# sub @DxMarker  pxNULL'  lookup _Set4000;
			print("  sub " + dClass + "\t\t" + pGname + "NULL'  lookup _Set" + ValueName(pmaxv) + ";", file=fout)
			break

		if pnewv < pminv:
			pnewv = pminv

		# sub dx200  pxNULL'  lookup _Set300;
		print("  sub " + dGname + ValueName(v2) + "\t\t" + pGname + "NULL'  lookup _Set" + ValueName(pnewv) + ";", file=fout)
		v2 += inc
		
	print("} " + lname + str(pv) + ";\n", file=fout)
	
# end of GenLookup_PosPlusForward

def GenLookups_HtPlus() :

	### Example:
	# lookup _HtPlus1500 {
	# 	...
	# 	sub asc500' lookup _Set2000;
	# 	sub asc550' lookup _Set2050;
	# 	...
	# 	sub dsc500' lookup _Set2000;
	# 	sub dsc550'	lookup _set2050;
	# 	...
	# } lookup _HtPlus1500;

	for v in range(pyMin, pyMax+inc, inc):
		print("lookup _HtPlus" + ValueName(v) + "  {", file=fout)
		minv = ascMin
		maxv = ascMax
		for v2 in range(minv, maxv + inc, inc):
			if v + v2 >= ytMax:
				print("  sub @AscMarker' lookup _Set" + ValueName(v + v2) + ";", file=fout)
				break;
			print("  sub asc" + ValueName(v2) + "' lookup _Set" + ValueName(v + v2) + ";", file=fout)

		minv = dscMin
		maxv = dscMax
		for v2 in range(minv, maxv + inc, inc):
			if v + v2 >= ybMax:
				print("  sub @DscMarker' lookup _Set" + ValueName(v + v2) + ";", file=fout)
				break;
			print("  sub dsc" + ValueName(v2) + "' lookup _Set" + ValueName(v + v2) + ";", file=fout)

		print("} _HtPlus" + ValueName(v) + ";\n", file=fout)

# end of GenLookups_HtPlus

def GenLookups_AddNuqtaHt(valuesList, dir) :

	### Example:
	# lookup _AddNuqtaHt600 {
	# 	...
	# 	sub asc500' lookup _Set1100;
	# 	sub asc550' lookup _Set1150;
	# 	...
	# } _AddNuqtaHt600;

	if dir == 1:	# add
		lname = "_AddNuqtaHt"
		prefix = "asc"
		minv = ascMin
		maxv = ascMax
		cName = "AscMarker"
	else:			# subtract
		lname = "_SubtractNuqtaHt"
		prefix = "dsc"
		minv = dscMin
		maxv = dscMax
		cName = "DscMarker"

	for v in valuesList:
		print("\nlookup " + lname + ValueName(v) + "{", file=fout)
		for v2 in range(minv, maxv+inc, inc):
			newv = (v * dir) + v2
			if dir > 0 and newv + inc > maxv:
				# output a fall-back rule and quit
				# sub @YtMarker lookup _Set3000;
				print( "  sub @" + cName + "' lookup _Set" + ValueName(newv) + ";", file=fout)
				break
			elif dir < 0 and newv < minv:
				newv = minv

			print("  sub " + prefix + ValueName(v2) + "' lookup _Set" + ValueName(newv) + ";", file=fout)

		print("} " + lname + ValueName(v) + ";", file=fout)

# end of GenLookups_AddNuqtaHt

def GenLookup_AddNuqtaUpLowHeight(valueList, dir) :

	### Example:
	# lookup _AddNuqtaUpperHt {
	# 	lookupflag UseMarkFilteringSet [@AscMarker @AscXMarker];
	# 	sub ascx600	@AscMarker' lookup _AddNuqtaHt600;
	# 	sub ascx950 @AscMarker' lookup _AddNuqtaHt950;
	# } _AddNuqtqUpperHt;

	if dir == 1:	# add
		lname = "_AddNuqtaUpperHt"
		lname2 = "_AddNuqtaHt"
		prefixX = 'ascx'
		cname = "@AscMarker"
		cnameX = "@AscXMarker"
	else:  # subtract
		lname = "_SubtractNuqtaLowerHt"
		lname2 = "_SubtractNuqtaHt"
		prefixX = 'dscx'
		cname = "@DscMarker"
		cnameX = "@DscXMarker"

	print("\nlookup " + lname + "{", file=fout)
	print("  lookupflag UseMarkFilteringSet [" + cname + " " + cnameX + "];", file=fout)
	for v in valueList:
		print("  sub " + prefixX + ValueName(v) + " " + cname + "' lookup " + lname2 + ValueName(v) + ";", file=fout)	
	print("} " + lname + ";", file=fout)

# end of GenLookup_AddNuqtaUpLowHeight

def GenLookup_MakeAscDscAbsolute(prefix) :

	### Example:
	# lookup _MakeAscAbsolute {
	# 	lookupflag UseMarkFilteringSet  [@PyMarker @AscMarker];
	# 	sub py0			@AscMarker'	lookup _HtPlus0;
	# 	sub py50		@AscMarker' lookup _HtPlus50;
	# 	sub py100		@AscMarker' lookup _HtPlus100;
	# 	...
	# } _MakeAscAbsolute;

	if prefix == "asc":
		lname = "_MakeAscAbsolute"
		cname = "@AscMarker"
		maxv = ytMax
		minv = ytMin
	else:
		lname = "_MakeDscAbsolute"
		cname = "@DscMarker"
		maxv = ybMax
		minv = ybMin

	print("\nlookup " + lname + "{", file=fout)
	print("  lookupflag UseMarkFilteringSet [@PyMarker " + cname + "];", file=fout)
	for v in range(pyMin, pyMax + inc, inc) :
		vAdj = v
		if v < minv:
			vAdj = minv
		print("  sub py" + ValueName(v) + "  " + cname + "' lookup _HtPlus" + ValueName(vAdj) + ";", file=fout)
	print("} " + lname + ";", file=fout)

# end of GenLookup_MakeAscDscAbsolute


def GenLookup_AdjustHeights(valueList, dir, lName, cName, prefix, dminv, dmaxv):

	# CURRENTLY NOT USED

	### Example:
	# lookup _AddAsc600{
	# 	lookupflag UseMarkFilteringSet @YtMarker;
	# 	sub ytN500' lookup _Set100;
	# 	sub ytN450' lookup _Set150;
	# 	sub ytN400' lookup _Set200;
	# 	...
	# } _AddAsc600;

	# The values correspond to the heights of nuqtas and diacritics.
	# We don't need a full set of these.

	for v in valueList:
		print("lookup " + lName + ValueName(v) + "{", file=fout)
		print("  lookupflag UseMarkFilteringSet @" + cName + ";", file=fout)	# do we need this?
		v2 = dminv
		while v2 < dmaxv:
			newv = v2 + (v * dir)  # dir = -1 for subtraction
			if dir > 0 and newv + inc > dmaxv:
				# output a fall-back rule and quit
				# sub @YtMarker lookup _Set3000;
				print( "  sub @" + cName + "' lookup _Set" + ValueName(newv) + ";", file=fout)
				break
			elif dir < 0 and newv < dminv:
				newv = dminv

			# sub yt100 lookup _Set700;
			print("  sub " + prefix + ValueName(v2) + "' lookup _Set" + ValueName(newv) + ";", file=fout)
			v2 += inc
		print("} " + lName + ValueName(v) + ";\n", file=fout)

# end of GetLookup_AdjustHeights

	
def ValueName(v):
	if v < 0:
		vstr = "N" + str(abs(v))  # negative number
	else:
		vstr = str(v)
	return vstr
	
# -----------------------------
# Main routine

# Classes

outfile = "../../source/opentype/arithClasses.feax"
fout = open(outfile, 'w');
print("# This file was generated by the genArithmeticLookups.py script.", file=fout)

print("\n# Classes\n", file=fout)
GenClasses('dx', "DxMarker", dxMin, dxMax)
GenClasses('dy', "DyMarker", dyMin, dyMax)
GenClasses('kw', "KwMarker", kwMin, kwMax)
GenClasses("px", "PxMarker", pxMin, pxMax)
GenClasses("pxf", "PxfMarker", pxfMin, pxfMax)
GenClasses("py", "PyMarker", pyMin, pyMax)
GenClasses("asc", "AscMarker", ascMin, ascMax)
GenClasses("dsc", "DscMarker", dscMin, dscMax)
GenClasses("yt", "YtMarker", ytMin, ytMax)
GenClasses("yb", "YbMarker", ybMin, ybMax)

print("\n@AscXMarker = [ascx600 ascx700 ascx950 ascx1000 ascx1050 ascx1500];", file=fout)
print("@DscXMarker = [dscx600 dscx700 dscx950 dscx1000 dscx1050];", file=fout)

print("\n@XMarkers = [@PxMarker @DxMarker pxNULL];", file=fout);
print("@XfMarkers = [@PxfMarker @DxMarker pxfNULL];", file=fout);
print("@YMarkers = [@PyMarker @DyMarker pyNULL];", file=fout);
#print("@YtbMarkers = [@YtMarker @YbMarker ]")

fout.close()
print("Classes written to '" + outfile + "'")

# Top-level lookup.

outfile = "../../source/opentype/arithMarkersYtb2AscDsc.feax"
fout = open(outfile, 'w');
print("# This file was generated by the genArithmeticLookups.py script.", file=fout)
print("# This is a top-level lookup that must go in a specific place relative to the other lookups.", file=fout)

print("\n# Marker Manipulation\n", file=fout)
GenLookups_MarkersYtb2AscDsc();

fout.close()
print("Lookup MarkerYtb2AscDsc written to '" + outfile + "'")

# Referenced lookups called by chaining rules

outfile = "../../source/opentype/arithmetic.feax"
fout = open(outfile, 'w');
print("# This file was generated by the genArithmeticLookups.py script.", file=fout)
print("# It contains low-level lookups called by chaining rules.", file=fout)


print("\n# Setting Arithmetic Values\n", file=fout)
GenLookup_SetValues()

print("\n# Arithmetic for X-axis\n", file=fout)
GenLookups_PosPlus('x', False, dxMin, dxMax, pxMin, pxMax)

print("\n# Arithmetic for Y-axis\n", file=fout)
GenLookups_PosPlus('y', False, dyMin, dyMax, pyMin, pyMax)

print("\n# Forward arithmetic for X-axis\n", file=fout)
GenLookups_PosPlus('x', True, dxMin, dxMax, pxMin, pxMax)

print("\n# Arithmetic callers\n", file=fout)

GenLookup_AddMarkers('x', dxMin, dxMax, pxMin, pxMax)
GenLookup_AddMarkers('y', dyMin, dyMax, pyMin, pyMax)

GenLookup_AddMarkersForward('x', dxMin, dxMax, pxfMin, pxfMax)

print("\n# Adjusting ascent and descent\n", file=fout)

GenLookups_HtPlus();

GenLookups_AddNuqtaHt(upperMarkHts, 1)
GenLookups_AddNuqtaHt(lowerMarkHts, -1)

GenLookup_AddNuqtaUpLowHeight(upperMarkHts, 1)
GenLookup_AddNuqtaUpLowHeight(lowerMarkHts, -1)

GenLookup_MakeAscDscAbsolute("asc")
GenLookup_MakeAscDscAbsolute("dsc")


# GenLookup_AdjustHeights(upperMarkHts, 1, "_AddAsc", "YtMarker", "yt", ascMin, ascMax)
# GenLookup_AdjustHeights(lowerMarkHts, -1, "_SubtractDsc", "YbMarker", "yb", dscMin, dscMax)

# These are simple lookups, but we auto-generate them so they get put in the right
# place in the file relative to the other lookup definitions - after the
# _AddAsc and _SubtractDsc lookups and outside of the feature.
#
# print("lookup _AddToAscent {", file=fout)
# print("  lookupflag UseMarkFilteringSet [@AscMarker @NuqtaLikeUpper];", file=fout)
# print("  sub @YtMarker' lookup _AddAsc600	_dot1u;", file=fout)
# print("  sub @YtMarker' lookup _AddAsc600	_dot2u;", file=fout)
# print("  sub @YtMarker' lookup _AddAsc950	_dot3u;", file=fout)
# print("  sub @YtMarker' lookup _AddAsc950	_dot4u;", file=fout)
# print("  sub @YtMarker' lookup _AddAsc900	_smallTah;", file=fout)		# maybe just use 950?
# print("} _AddToAscent;", file=fout)

# print("lookup _SubtractFromAscent {", file=fout)
# print("  lookupflag UseMarkFilteringSet [@DscMarker @NuqtaLikeLower];", file=fout)
# print("  sub @YbMarker' lookup _SubtractDsc600	_dot1l;", file=fout)
# print("  sub @YbMarker' lookup _SubtractDsc600	_dot2u;", file=fout)
# print("  sub @YbMarker' lookup _SubtractDsc950	_dot3u;", file=fout)
# print("  sub @YbMarker' lookup _SubtractDsc950	_dot4u;", file=fout)
# print("  sub @YbMarker' lookup _SubtractDsc700	_hehHook.small;", file=fout)
# print("} _SubtractFromAscent;", file=fout)

# print("\n# Initialization\n", file=fout)
# 
# GenLookup_InitPos('x', dxMin, dxMax, pxMin, pxMax)
# GenLookup_InitPos('y', dyMin, dyMax, pyMin, pyMax)

fout.close()
print("Chaining lookups written to '" + outfile + "'")
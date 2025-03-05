#!/usr/bin/python3

# Outputs a set of rules to perform arithmetic

# Run this script from the tools/scripts directory where the file is located:
#		python3 genArithmeticLookups.py
#
# It generates a group of lookups like this:
#		lookup _Set100 {
#			sub pxNULL by px100;
#		} _Set100;
#		etc.
#
#		lookup _PosPlusX100 {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub pxNULL' lookup _Set100		dx0;
#			sub pxNULL'	lookup _Set150		dx50;
#			sub pxNULL'	lookup _Set200		dx100;
#			# etc.
#		} _PosPlusX100;
#		# and many more similar lookups
#
#		lookup _InitPosX {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub pxNULL' lookup _Set50		dx50;
#			sub pxNULL' lookup _Set100		dx100;
#			sub pxNULL' lookup _Set150		dx150;
#			# etc.
#		} _InitPosX;
#
#		lookup _AddMarkersX {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub pxNULL' lookup _PosPlus50		@DxMarker px50;
#			sub pxNULL'	lookup _PosPlus100		@DxMarker px100;
#			sub pxNULL'	lookup _PosPlus150		@DxMarker px150;
#			# etc.
#		} _AddMarkersX;
#
# ...and a similar set for Y. Also for X only:
#
#		lookup _PosPlusXf100 {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub dx50	pxNULL' lookup _Set150;
#			sub dx100	pxNULL' lookup _Set200;
#			sub dx150	pxNULL' lookup _Set250;
#			etc.
#		} _PosPlusXf100;
#
#		lookup _AddMarkersXforward {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub px50	@DxMarker	pxNULL' lookup _PosPlusXf50;
#			sub px100	@DxMarker	pxNULL' lookup _PosPlusXf100;
#			etc.
#		} _AddMarkersXforward;


dxMin = -200
dxMax = 2500
pxMin = 0
pxMax = 4000

dyMin = 0
dyMax = 2500
pyMin = 0
pyMax = 3000

inc = 50

#import sys

def GenClasses(axis, dminv, dmaxv, pminv, pmaxv):
	if axis == "x":
		outstr = "@DxMarker = ["
		dGname = "dx"
		pGname = "px"
	else:
		outstr = "@DyMarker = ["
		dGname = "dy"
		pGname = "py"
	
	v = dminv
	while v <= dmaxv:
		outstr += dGname + ValueName(v) + " "
		if (v % 500) == 0 and v > dminv and v < dmaxv:
			print(outstr, file=fout)
			outstr = "  ";
		v += inc
	print(outstr + "];", file=fout)
	
	if axis == "x":
		outstr = "@PxMarker = ["
	else:
		outstr = "@PyMarker = ["
	
	v = pminv
	while v <= pmaxv:
		outstr += pGname + ValueName(v) + " "
		if (v % 500) == 0  and v > pminv and v < pmaxv:
			print(outstr, file=fout)
			outstr = "  ";
		v += inc
	print(outstr + "];", file=fout)
	
# end of GenClasses

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

def GenLookup_SetValues(pminvX, pmaxvX, pminvY, pmaxvY):
	minv = min(pminvX, pminvY)
	maxv = max(pmaxvX, pmaxvY)
	
	pv = minv
	while pv <= maxv:
		print("lookup " + "_Set" + ValueName(pv) + " {", file=fout)
		if pminvX <= pv and pv <= pmaxvX:
			print("  sub pxNULL  by  px" + ValueName(pv) + ";", file=fout)
		if pminvY <= pv and pv <= pmaxvY:
			print("  sub pyNULL  by  py" + ValueName(pv) + ";", file=fout)
		print("} _Set" + ValueName(pv) + ";\n", file=fout)
		
		pv += inc
	# end of while

# end of GenLookup_SetValues

def GenLookup_AddMarkers(axis, dminv, dmaxv, pminv, pmaxv):
	
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
		
	print("} " + lname + ";\n", file=fout)

# end of GenLookup_AddMarkers

def GenLookup_AddMarkersForward(axis, dminv, dmaxv, pminv, pmaxv):
	
	if axis == "x":
		lname = "_AddMarkersXforward"
		lname2 = "_PosPlusXf"
		filterSet = "@XMarkers"
		dClass = "@DxMarker"
		dGname = "dx"
		pGname = "px"
	else:
		lname = "_AddMarkersYforward"
		lname2 = "_PosPlusYf"
		filterSet = "@YMarkers"
		dClass = "@DyMarker"
		dGname = "dy"
		pGname = "py"

	print("lookup " + lname + " {", file=fout)
	print("  lookupflag UseMarkFilteringSet " + filterSet + ";", file=fout)
	
	
	pv = pminv
	while pv <= pmaxv:
		# sub px100	 @DxMarker  pxNULL'  lookup _PosPlusXf100;
		print("  sub " + pGname + ValueName(pv) + "\t" + dClass + "\t" + pGname + "NULL'  lookup " + lname2 + ValueName(pv) + ";", file=fout)
		pv += inc
		
	print("} " + lname + ";\n", file=fout)

# end of GenLookup_AddMarkers

def GenLookups_PosPlus(axis, forward, dminv, dmaxv, pminv, pmaxv):
	
	if (axis == 'x'):
		lookupName = "_PosPlusX"
		filterSet = "@XMarkers"
		dClass = "@DxMarker"
		dGname = "dx"
		pGname = "px"
	else:
		lookupName = "_PosPlusY"
		filterSet = "@YMarkers"
		dClass = "@DyMarker"
		dGname = "dy"
		pGname = "py"

	if forward: lookupName += "f"

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

	
def ValueName(v):
	if v < 0:
		vstr = "N" + str(abs(v))  # negative number
	else:
		vstr = str(v)
	return vstr
	
# -----------------------------
# Main routine

outfile = "../../source/opentype/arithmetic.feax"
fout = open(outfile, 'w');

print("# This file was generated by the genArithmeticLookups.py script.", file=fout)

print("\n# Classes\n", file=fout)
GenClasses('x', dxMin, dxMax, pxMin, pxMax)
GenClasses('y', dyMin, dyMax, pyMin, pyMax)

print("\n@XMarkers = [@PxMarker @DxMarker pxNULL];", file=fout);
print("@YMarkers = [@PyMarker @DyMarker pyNULL];", file=fout);

print("\n# Setting Arithmetic Values\n", file=fout)
GenLookup_SetValues(pxMin, pxMax, pyMin, pyMax)

print("\n# Arithmetic for X-axis\n", file=fout)
GenLookups_PosPlus('x', False, dxMin, dxMax, pxMin, pxMax)

print("\n# Arithmetic for Y-axis\n", file=fout)
GenLookups_PosPlus('y', False, dyMin, dyMax, pyMin, pyMax)

print("\n# Forward arithmetic for X-axis\n", file=fout)
GenLookups_PosPlus('x', True, dxMin, dxMax, pxMin, pxMax)

print("\n# Arithmetic callers\n", file=fout)

GenLookup_AddMarkers('x', dxMin, dxMax, pxMin, pxMax)
GenLookup_AddMarkers('y', dyMin, dyMax, pyMin, pyMax)

GenLookup_AddMarkersForward('x', dxMin, dxMax, pxMin, pxMax)

print("\n# Initialization\n", file=fout)

GenLookup_InitPos('x', dxMin, dxMax, pxMin, pxMax)
GenLookup_InitPos('y', dyMin, dyMax, pyMin, pyMax)

fout.close()

print("Written to '" + outfile + "'")
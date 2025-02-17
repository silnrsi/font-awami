#!/usr/bin/python3

# Outputs a set of rules to perform arithmetic

# Run this script from the tools/scripts directory where the file is located:
#		python3 genArithmeticLookups.py
#
# It generates a group of lookups like this:
#
#		lookup _PosPlusX100 {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub pxNULL' dx0			by	px100;
#			sub pxNULL'	dx50		by	px150;
#			sub pxNULL'	dx100		by	px200;
#			# etc.
#		} _PosPlusX100;
#		# and many more similar lookups
#
#		lookup _InitPosX {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub pxNULL' dx100		by  px100;
#			sub pxNULL' dx100		by  px100;
#			sub pxNULL' dx100		by  px100;
#			# etc.
#		} _InitPosX;
#
#		lookup _AddMarkersX {
#			lookupflag UseMarkFilteringSet @XMarkers;
#			sub pxNULL' lookup _PosPlus50			@DxMarker px50;
#			sub pxNULL'	lookup _PosPlus100		@DxMarker px100;
#			sub pxNULL'	lookup _PosPlus150		@DxMarker px150;
#			# etc.
#		} _AddMarkersX;
#
# ...and a similar set for Y.


dxMin = -200
dxMax = 2000
pxMin = 0
pxMax = 4000

dyMin = 0
dyMax = 2000
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
		outstr += dGname + GlyphNumber(v) + " "
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
		outstr += pGname + GlyphNumber(v) + " "
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
		print("  sub " + pGname + "NULL'  " + dGname + GlyphNumber(dv) + "  by  " + pGname + GlyphNumber(pv) + ";", file=fout)
		dv += inc
	
	print("} " + lname + ";\n", file=fout)

# end of GenLookup_InitPos

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
		print("  sub " + pGname + "NULL' lookup " + lname2 + GlyphNumber(pv) + "  " + dClass + "  " +  pGname + GlyphNumber(pv) + ";", file=fout)
		pv += inc
		
	print("} " + lname + ";\n", file=fout)

# end of GenLookup_AddMarkers

def GenLookups_PosPlus(axis, dminv, dmaxv, pminv, pmaxv):
	
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

	pv = pminv
	while pv <= pmaxv:
		GenLookup_PosPlus(lookupName, filterSet, dClass, dGname, pGname, dminv, dmaxv, pminv, pmaxv, pv)
		pv += inc

# end of GenLookups_PosPlus


def GenLookup_PosPlus(lname, fset, dClass, dGname, pGname, dminv, dmaxv, pminv, pmaxv, pv):
	print("lookup " + lname + GlyphNumber(pv) + " {", file=fout)
	print("  lookupflag UseMarkFilteringSet " + fset + ";", file=fout)
	
	v2 = dminv
	while v2 <= dmaxv:
		pnewv = v2 + pv
		if pnewv + inc > pmaxv:
			# output a fall-back rule and quit
			print("  sub " + pGname + "NULL'  " + dClass + "  by  " + pGname + GlyphNumber(pmaxv) + ";", file=fout)
			break

		if pnewv < pminv:
			pnewv = pminv
			
		print("  sub " + pGname + "NULL'  " + dGname + GlyphNumber(v2) + "  by  " + pGname + GlyphNumber(pnewv) + ";", file=fout)
		v2 += inc
		
	print("} " + lname + str(pv) + ";\n", file=fout)
	
# end of GenLookups_PosPlus
	
def GlyphNumber(v):
	if v < 0:
		vstr = "N" + str(abs(v))  # negative number
	else:
		vstr = str(v)
	return vstr
	
# -----------------------------
# Main routine

BariyehWidth = 2700
outfile = "../../source/opentype/arithmetic.feax"
fout = open(outfile, 'w');

print("# This file was generated by the genArithmeticLookups.py script.", file=fout)

print("\n# Classes\n", file=fout)
GenClasses('x', dxMin, dxMax, pxMin, pxMax)
GenClasses('y', dyMin, dyMax, pyMin, pyMax)

print("\n@XMarkers = [@PxMarker @DxMarker pxNULL];", file=fout);
print("@YMarkers = [@PyMarker @DyMarker pyNULL];", file=fout);

print("\n# Arithmetic for X-axis\n", file=fout)
GenLookups_PosPlus('x', dxMin, dxMax, pxMin, pxMax)

print("\n# Arithmetic for Y-axis\n", file=fout)
GenLookups_PosPlus('y', dyMin, dyMax, pyMin, pyMax)

print("\n# Arithmetic callers\n", file=fout)

GenLookup_AddMarkers('x', dxMin, dxMax, pxMin, pxMax)
GenLookup_AddMarkers('y', dyMin, dyMax, pyMin, pyMax)

print("\n# Initialization\n", file=fout)

GenLookup_InitPos('x', dxMin, dxMax, pxMin, pxMax)
GenLookup_InitPos('y', dyMin, dyMax, pyMin, pyMax)

fout.close()

print("Written to '" + outfile + "'")
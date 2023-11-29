#!/usr/bin/python

# Generate FTML test data files

# To add a new character:
# - Define a short code for it and add the corresponding USV mapping in _char_name_to_usv().
#       Keep in mind that characters with varying finals (yeh, noon, qaf) need to be handled twice.
# - Add a code for it in the appropriate list in expand_sequences() or insert_diacritics().
# - Add the corresponding information in _group_name_format() or _diac_group_name_format().

# To use default output, run from the root directory of the project.

import collections
import codecs
import copy
import argparse
import os

def run():

    defPath = os.path.join( "tests", "FTML_XSL")

    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--output",default=r"tests/FTML_XSL",help="Where to write output files")  # assumes calling from the root
    parser.add_argument("-t","--text",action="store_true",help="Generate data as simple text file")
    parser.add_argument("-m","--mode",action="append",default=["all"],help="test modes to generate [all]")
    parser.add_argument("-f","--font",default=r"Awami Nastaliq",help="Name of font to use")
    parser.add_argument("-s","--scale",default=300,type=int,help="font scale [300]")

    args = parser.parse_args()
    
    modeArgs = []
    for i in range(len(args.mode)):
        if i == 0 and args.mode[i] == "all" and len(args.mode) > 1:
            pass
        else:
        	  modeArgs.append(args.mode[i])

    modes = []
    for m in modeArgs:
        if m == "all":
            if len(modeArgs) <= 1 or modeArgs[1] == "all":
		            modes.extend(["basicforms", "allbasechars", "basic_somediac", "allbasecharforms", "basic_alldiac"])
		            # "alldiac" and "allbase_somediac" currently aren't supported
            else:
		            pass  # ignore all
        else:
            modes.append(m)

    # Debugging:
    #modes = ["basicforms"]         # all contextual forms of the basic shapes (beh, jeem, seen, etc.)
    #modes = ["allbasechars"]       # some contextual forms of all letters - make sure nuqtas are generated
    #modes = ["basic_somediac"]     # same characters as basicforms, each with an upper and lower diac
    #modes = ["allbasecharforms"]   # all forms of all letters - HUGE file
    #modes = ["basic_alldiac"]      # same characters as basicforms, with every diac
    #modes = ["allbase_somediac"]   # not implemented
    #modes = ["alldiac"]            # not implemented???
    
    fontName = args.font
    fontScale = int(args.scale)
    #fontScale = "100"  # for waterfall file
    
    print(modes)

    for mode in modes:
        print("Mode: " + mode)
        dir = args.output
        dir = dir.replace( "tests/FTML_XSL", defPath)  # if it's there
        dir = dir.replace( "tests\\FTML_XSL", defPath)
        outputFilename = os.path.join(dir, "test_" + mode + (".txt" if args.text else ".xml"))

        # Debugging:
        #outputFilename = "testoutput.ftml"

        # Start with tuples of basic characters, organized by the first char. Each character has associated
        # # a list of triples. The second element of the triple indicates how the last sequence connects,
        # and the third element indicates the *key* - which character the sequence will be displayed with in the
        # final output.
        # E.g., (much simplified):
        # [('beh', [ (('beh',  'jeem'), 'both',   'jeem')
        #            (('beh',  'lam'),  'both',   'lam),
        #            (('beh',  'dal'),  'right',  'dal') ),
        #  ('jeem',[ (('jeem', 'jeem'), 'both',   'jeem'),
        #            (('jeem', 'lam'),  'both',   'lam'),
        #            (('jeem', 'dal'),  'right',  'dal') ) ]
        basicSeq = generate_basic_sequences(mode)
        print("basicSeq =", basicSeq)

        # Then either add additional sequences to handle non-basic characters (allbasecharforms), 
        # or substitute non-basic characters for some of the basic ones (allbasechars).
        (expandedSeq, expandLeft) = expand_sequences(mode, basicSeq)
        print("expandedSeq =", expandedSeq)
        
        seqWDiacritics = insert_diacritics(mode, expandedSeq)
        print("seqWDiacritics =", seqWDiacritics)
        
        groupedSeq = organize_sequences_by_group(mode, seqWDiacritics)
        print("groupedSeq =", groupedSeq)

        if not len(groupedSeq):
            continue

        if args.text:
            gen = Text(outputFilename)
        else:
            gen = FTML(outputFilename)
        output(gen, mode, fontName, fontScale, groupedSeq, expandLeft)
        print("")

    print("Done")

# end of run    


""" The return value is a list of tuples of the form (keyChar, sequences) where each sequence is a triple:
    1. the sequence of character codes
    2. 'both' to include both contexts, 'right' to include only the left context
    3. key char

    The key char is the character under which this sequence should be organize - usually the last char 
    in the sequence.
"""
def generate_basic_sequences(mode) :
    
    dualConnecting = ["beh", "jeem", "seen", "sad", "tah", "ain", "feh", "lam", "meem", "kaf",
        "hehDo", "hehGoal"]
    rightConnecting = ["alef", "dal", "reh", "qaf", "waw", "bariyeh", "chotiyeh", "noon", "tehMarbuta"]
    
    (dualSubs, rightSubs) = _generate_sub_sequences()
    
    # DEBUGGING:
    """
    dualConnecting = ["beh", "jeem"]
    rightConnecting = ["qaf", "noon"]
    dualSubs = []
    rightSubs = []
    """

    sequences = []
    for dualChar1 in dualConnecting :
        ###if dualChar1 != "beh" and dualChar1 != "jeem" : continue
        
        seconds = []
        for dualChar2 in dualConnecting :
            uniple = (dualChar1, dualChar2)
            seconds.append((uniple, "both", dualChar2))
            
        for dualList in dualSubs :
            dualListGroup = dualList[0]
            dualListChars = dualList[1:]
            if dualListChars[0] == "ANY" or dualListChars[0] == dualChar1 :
                subList = tuple([dualChar1] + list(dualListChars[1:]))
                seconds.append((subList, "both", dualListGroup))
                
        for rightChar in rightConnecting :
            uniple = (dualChar1, rightChar)
            seconds.append((uniple, "right", rightChar))
        
        for rightList in rightSubs :
            rightListGroup = rightList[0]
            rightListChars = rightList[1:]
            if rightListChars[0] == "ANY" or rightListChars[0] == dualChar1 :
                subList = tuple([dualChar1] + list(rightListChars[1:]))
                seconds.append((subList, "right", rightListGroup))
        
        sequences.append((dualChar1, seconds))
        
    # end for over dualConnecting
        
    return sequences
        
# end of generate_sequences

def _generate_sub_sequences() :
    
    dualSubs = []
    rightSubs = []
    
    dualSubs.append(("multi-beh", "ANY", "beh", "beh"))          # beh+beh
    dualSubs.append(("multi-beh", "ANY", "beh", "beh", "beh"))   # beh+beh+beh

    rightSubs.append(("beh+noon", "ANY", "beh", "noon"))         # beh+noon
    rightSubs.append(("beh+reh", "ANY", "beh", "reh"))           # beh+reh
    rightSubs.append(("beh+hehGoal", "ANY", "beh", "hehGoal"))   # beh+hehGoal
    
    # generate seen/sad + beh + ... sub-sequences
    for ss in ("seen", "sad") :
        for char3 in ("sad", "tah", "ain", "feh", "qaf", "beh") :
            # NB: strictly speaking, ss + beh + beh is only significant in the final position,
            # but it doesn't hurt to test both.
            dualSubs.append(("seen/sad+beh", ss, "beh", char3))
    
    # generate alternate meem sub-sequences
    for char1 in ("jeem", "seen", "sad", "tah", "ain", "beh", "feh", "meem", "hehGoal", "hehDo") :
        for char3 in ("alef", "dal") :
            rightSubs.append(("alt-meem", char1, "meem-alt", char3))
        for char3 in ("kaf", "lam") :
            dualSubs.append(("alt-meem", char1, "meem-alt", char3))
            
    # generate seen + seen + seen
    dualSubs.append(("multi-seen", "ANY", "seen", "seen", "seen"))
    
    return (dualSubs, rightSubs)

# end of generate_sub_sequences


def expand_sequences(mode, basicSequences) :

    if mode == "basicforms" :
        expand = {"kaf" : ["gaf"]}
        expandLeft = {}
        changeKey = False
        
    elif mode == "basic_somediac" or mode == "basic_alldiac" :
        expand = {"kaf" : ["gaf"],
            "beh" : ["teh"]  # because diacritics attach differently to upper and lower nuqtas
        }
        expandLeft = {}
        changeKey = False
        
    elif mode == "allbasecharforms" or mode == "allbasechars" :
        # Note: it is appropriate to add new characters to the beginning of the lists below, not at the end.
        # They are processed in reverse order.
        expand = {
            "alef"      :   ["alef3", "alef2", "alefWasla", "alefMadda"],
            "beh"       :   ["dotlessBeh", "teh3down", "tehRing", "beeh", "tteheh", "peh", "tteh", "theh", "teh"],
            "jeem"      :   ["hah4below", "hahTah2smd", "hahTah", "hah3dots", "hahHamza", "tcheheh",  "dyeh", "tcheh", "khah", "hah"],
            "seen"      :   ["seen4", "seenInvV", "seen3dots3dots", "seen3below", "seenTah2smd", "seen2dotsV", "seen4dots", "seenDotDot", "sheen"],
            "sad"       :   ["sad3dots", "dadDotBelow", "dad"],
            "tah"       :   ["zah"],
            "ain"       :   ["ain3dots", "ghain"],
            "feh"       :   ["dotlessFeh", "feh3dotsBelow", "feh3dotsAbove"],
            "qaf"       :   ["dotlessQaf"],
            "kaf"       :   ["graf", "keheh3dots", "kehehDot", "ng", "kaf2dots", "kafRing", "ngoeh", "gueh", "gaf"],
                                        # gafRing - not needed for Nastaliq
            "lam"       :   ["lamTah", "lam3dots", "lamSmallV", "lamBar"],
            "noon"      :   ["noon3dots", "noonSmallV", "noonRing", "rnoon", "noonDotBelow", "noonRetro", "noonGhunna"],
            "chotiyeh"  :   ["yeh4below", "yeh3", "yeh2", "alefMaksura", "arabicE", "yehSmallV", "yehHamza"],
            "bariyeh"   :   ["bariyeh3", "bariyeh2"],
            "hehGoal"   :   ["hehHamza", "arabicHeh"],
                
            "reh"       :   ["rehSmallVbelow", "reh2dotsV", "rehTah2smd", "rehRing", "rehHamza", "reh4dots", "reh2dots", "rehDotDot",
                                "rehDotBelow", "jeh", "rreh", "zain"],
            "dal"       :   ["dul", "dal4dots", "dalRing", "dal2dotsVTah", "dalDotTah", "ddal", "thal"],
                                        # dalDotBelow - not really needed for Nastaliq
            "waw"       :   ["waw3", "waw2", "waw2dots", "wawDot", "yu", "ve", "kirghizYu", "wawRing", "wawHamza"],
            "tehMarGoal" :  ["hehYeh", "tehMarbuta"]
        }

        expandLeft = {  # initial/medial forms of letters that have different finals
            "beh"       :   ["noon3dotsIM", "noonSmallVIM", "noonRingIM", "rnoonIM", "noonDotBelowIM", "noonRetroIM", "noonGhunnaIM", "noonIM",
                                "alefMaksuraIM", "arabicEIM", "yehSmallVIM", "yehHamzaIM", "chotiyehIM"],
            "feh"       :   ["dotlessQafIM", "qafIM"]
        }
        
        # Debugging:
        #expand = { "jeem" : ["khah", "hah"], "beh" : ["teh"], "qaf" : ["dotlessQaf"] }
        #expandLeft = { "beh" :   ["noon3dotsIM", "noonRingIM", "noonIM"] }

        changeKey = True
        
    elif mode == "alldiac" :
        expand = {}
        expandLeft = {}

    else:
        print("ERROR: Unexpected mode: " + mode)
        return []

    resultSeq = basicSequences

    if mode == "allbasechars" :
        for key, expandList in expand.items() :
            reverseList = _reverse_list(expandList)
            #if key in expandLeft.keys() :
            #    reverseList_left = expandLeft[key]
            #    print('reverseList_left =',reverseList_left)
            #    reverseList.extend(reverseList_left)
            #    print('reverseList = ', reverseList)
            
            resultSeq = _substitute_bases(resultSeq, key, reverseList, False)
        
        # There is currently an issue where, if you substitute a initial/medial-only form for the last item in the sequence,
        # you get the wrong final - e.g., you turn (lam, beh) into (lam, noonSmallV), which makes no sense, and isn't a 
        # final beh form as the test expects. This is fixed by a post-processing step at the end.
        for key, expandList in expandLeft.items() :
            reverseList = _reverse_list(expandList)
            resultSeq = _substitute_bases(resultSeq, key, reverseList, True)
            
    else :
        for key, value in expand.items() :
            for expandChar in value :
                resultSeq = _add_set_starting_with(resultSeq, key, expandChar, changeKey)
                
        for key, value in expandLeft.items() :
            for expandChar in value :
                # We use copy below instead of left because char of interest is the FIRST, which means
                # the fact that is is left connecting is irrelevant.
                resultSeq = _add_set_starting_with(resultSeq, key, expandChar, changeKey)
    
        #print("after _add_set_starting_with: ",resultSeq)
    
        for key, value in expand.items() :
            for expandChar in value :
                resultSeq = _expand_one_char(resultSeq, key, expandChar, "copy")
    
        for key, value in expandLeft.items() :
            for expandChar in value :
                # We use copy below instead of left because char of interest is the FIRST, which means
                # the fact that is is left connecting is irrelevant.
                resultSeq = _expand_one_char(resultSeq, key, expandChar, "copy")
     
    # Also return expandleft lists to use for some post-processing.
    return (resultSeq, expandLeft)
    
# end of expand_sequences


""" This is kind of subtle. It tries to figure out whether a newly generated sequence
    should be dual-, right-, or left-connecting.
    If the old one is right-connecting (eg, ending in alef), the new one is as well.
    Otherwise, if we are expanding left-only characters (noonIM), it is left-connecting.
    Otherwise, if we are expanding a dual-connecting character, we pass "copy" and leave it unchanged.
"""
def _is_dual(oldIsDual, setIsDual) :
    if oldIsDual == "right" :
        return "right"
    elif setIsDual == "left" :
        return "left"  # instead of "both"
    else :
        return oldIsDual

""" Find the sequence in *sequences* associated with *basicChar*.
    Expand the sequence to include *expandchar*.
"""
def _add_set_starting_with(sequences, basicChar, expandChar, changeKey) :
    #print("_add_set_starting_with", basicChar, expandChar)
    i = 0
    for (char1, charList) in sequences :
        if char1 == basicChar :
            newList = []
            for (charTuple, isDual, key) in charList :
                newKey = expandChar if (key == basicChar and changeKey) else key
                #newIsDual = _is_dual(isDual, "copy")
                newTuple = tuple([expandChar] + list(charTuple[1:]))
                newStuff = (newTuple, isDual, newKey)
                #print("adding", newStuff)
                newList.append(newStuff)
            sequences.insert(i+1, (expandChar, newList))
            break
        i = i + 1
    return sequences
    
# end of _add_set_starting_with

        
def _expand_one_char(sequences, basicChar, expandChar, setIsDual) :
    #print("exanding " + basicChar + " to " + expandChar + "; setIsDual: " + setIsDual )
    newStuff = []
    iChar1 = 0
    for (char1, charData) in sequences :
        #print("char1=",char1)
        
        iTuple = 0
        skip = 0
        for (charTuple, isDual, groupName) in charData :
            #print(charTuple)
            if skip > 0 :
                # This was a new sequence that was just inserted.
                skip = skip - 1
                #print("skipping charTuple:",charTuple)
            else :
                #print("maybe copying charTuple:", charTuple)
                newList = []
                foundOneToExpand = False
                iChar = 0
                for remChar in charTuple :
                    #if iChar == len(charTuple) - 1 and setIsDual == "left" :
                    #    # we only want to substitute left-connecting glyphs, and this is a final
                    #    newList.append(remChar)
                    if remChar == basicChar and iChar > 0 : # if iChar == 0, first char is redundant with char1 key
                        #print(iChar,basicChar," - expand this")
                        newList.append(expandChar)  # substitute expandChar, the similarly formed character
                        foundOneToExpand = True
                    else :
                        newList.append(remChar)
                    iChar = iChar + 1
            
                if foundOneToExpand :
                    #print("inserting ", newList)
                    newIsDual = _is_dual(isDual, setIsDual)
                    newGroup = expandChar if groupName == basicChar else groupName
                    charData.insert(iTuple + skip + 1, (tuple(newList), newIsDual, newGroup)) # insert after this one
                    skip = skip + 1
                    #print("skip=",skip)
            
            iTuple = iTuple + 1
                
        #charData.extend(newStuff)
        sequences[iChar1] = (char1, charData)
        
        #print("### sequences=", sequences)
        
        iChar1 = iChar1 + 1
        
    return sequences

# end of _expand_one_char


""" Substitute an "expand" form for the basic form of the key.
    For instance, one item might be (('jeem', 'lam'), 'both', 'lam').
    This might substitute (('jeem', 'lamBar'), 'both', 'lam').
"""
def _substitute_bases(sequences, key, expandList, imFlag) :
    
    subList = [key] + expandList
    maxC = len(subList)
    nextC = 0
    for (char1, charData) in sequences :
        #print("char1=", char1)
        iData = 0
        for (charTuple, isDual, groupName) in charData :
            charList = list(charTuple)
            charCnt = len(charList)
            newList = []
            for char in charList :
                if nextC >= maxC :
                    nextC = 0;
                if char == key :
                    newList.append(subList[nextC])
                    nextC = nextC + 1
                else :
                    newList.append(char)

            charData[iData] = (tuple(newList), isDual, groupName)
            
            iData = iData + 1
            
    return sequences
    
# end of _substitute_bases


def insert_diacritics(mode, sequences) :
    
    if mode == "basic_somediac" :
        diacList = [ "zabar", "zair" ]
        
    elif mode == "basic_alldiac" :
        diacList = ["zabar", "pesh", "zair", "dozabar", "dopesh", "dozair",
            "shadda", "jazm", "kharizabar", "kharizair", "ultapesh", "short-vowel"]
        
    else :
        diacList = []
        
    if len(diacList) == 0 :
        resultSeq = sequences
        
    else :
        resultDict = {}
        for diac in diacList :
            resultDict = _insert_diacritic(sequences, resultDict, diac)
           
        # convert dictionary to tuple of (key, list)
        resultSeq = []
        for (char1, charData) in resultDict.items() :
            resultSeq.append((char1, charData))
        
    return resultSeq
    
# end of insert_diacritics


def _insert_diacritic(sequences, seqWDiacritics, diacChar) :
    
    for (char1, charData) in sequences :
        if not char1 in seqWDiacritics: seqWDiacritics[char1] = []
        newCharData = seqWDiacritics[char1]
        for (charTuple, isDual, groupName) in charData:
            newCharList = []
            for char in charTuple :
                newCharList.append(char)
                newCharList.append(diacChar)
            newCharData.append((tuple(newCharList), isDual, groupName, diacChar))  # four elements now
           
        seqWDiacritics[char1] = newCharData
    
    return seqWDiacritics
    
# end of _insert_diacritic


# Sequences are generated based on what letter comes first, but for they most part, they are output by
# what comes last (except for special cases).
def organize_sequences_by_group(mode, expandedSeq) :

    resultSeq = {}
       
    for (char1, charData) in expandedSeq :
        for seq in charData :
            if mode == "basic_somediac" or mode == "basic_alldiac" :
                (charTuple, isDual, groupName, diacGroupName) = seq
                (diacSortVal, diacLabel) = _diac_group_name_format(diacGroupName)
                diacGroupNameExt = "&" + diacGroupName
            else :
                (charTuple, isDual, groupName) = seq
                diacSortVal = ""
                diacGroupNameExt = ""
            
            (sortVal, label, colFM_bogus, colIM_bogus) = _group_name_format(groupName)

            key = sortVal + diacSortVal + "_" + groupName + diacGroupNameExt
        
            if not key in resultSeq :
                resultSeq[key] = []
            
            #if charTuple[1] == "NONE" :
            #    fullTuple = (char1, charTuple[0])
            #else :
            #    fullTuple = tuple([char1] + list(charTuple))
            #resultSeq[key].append((fullTuple, isDual))
            
            resultSeq[key].append((charTuple, isDual))
    
    resultSeq = collections.OrderedDict(sorted(resultSeq.items()))  # sort
    
    return resultSeq

# end of organize_sequences_by_group


# The last char is something like noonSmallVIM which doesn't make sense as a final.
# Replace it with the basic char, ie, beh.
def _fix_last_char(lastChar, expandLeft) :
    newLast = lastChar
    for basicChar, imOnlyChars in expandLeft.items() :
        for imChar in imOnlyChars :
            if imChar == lastChar :
                newLast = basicChar
            
    return newLast

class FTML(object):
    def __init__(self, fname):
        self.f = codecs.open(fname, 'w', 'utf-8')

    def close(self):
        self.f.close()

    def write_header(self, mode, fontName, fontScale):
        if mode == "basicforms" :
            title = "Test of Awami Basic Base Character Set"
        elif mode == "allbasechars" :
            title = "Test of All Awami Base Characters"
        elif mode == "allbasecharforms" :
            title = "Test of Awami - All Forms of All Base Characters"
        elif mode == "basic_somediac" :
            title = "Test of Awami - Basic Forms with Diacritics"
        elif mode == "basic_alldiac" :
            title = "Test of Awami - Basic Forms with All Diacritics"
        elif mode == "all_diac" :
            title = "Test of Awami - All Diacritics"
        else :
            title = "Test of Awami Rendering (???)"
            
        self.f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        self.f.write('<?xml-stylesheet type="text/xsl" href="ftml.xsl"?>\n')
        self.f.write('<ftml version="1.0">\n')
        self.f.write('  <head>\n')
        self.f.write('    <columns comment="15%" label="20%" string="15%"/>\n')
        self.f.write('    <description>' + title + '</description>\n')
        self.f.write('    <fontscale>' + str(fontScale) + '</fontscale>\n')
        self.f.write('    <fontsrc>local(' + fontName + '), url(AwamiNastaliq-Regular.ttf)</fontsrc>\n')
        self.f.write('    <!--   <fontsrc>local(' + fontName + ' Medium), url(AwamiNastaliq-Medium.ttf)</fontsrc>   -->\n');
        self.f.write('    <!--   <fontsrc>local(' + fontName + ' SemiBold), url(AwamiNastaliq-SemiBold.ttf)</fontsrc>   -->\n');
        self.f.write('    <!--   <fontsrc>local(' + fontName + ' Bold), url(AwamiNastaliq-Bold.ttf)</fontsrc>   -->\n');
        self.f.write('    <!--   <fontsrc>local(' + fontName + ' ExtraBold), url(AwamiNastaliq-ExtraBold.ttf)</fontsrc>   -->\n');
        self.f.write('    <title>' + title + '</title>\n')
        self.f.write('    <styles><style feats=\' \' name="default"/></styles>\n')
        self.f.write('  </head>\n')

    def write_closing(self):
        self.f.write('</ftml>\n')

    def start_group(self, label):
        self.f.write('  <testgroup label="' + label + '">\n')

    def end_group(self):
        self.f.write('  </testgroup>\n')

    def write_one_sequence(self, seq, contextCharI, contextCharF, expandLeft) :
        
        seqLabel = ''
        seqUsvs = ''
        seqUsvsWoLast = ''
        plusSep = ''
        ###seqLabel = char1
        ###seqUsvs = '&#x' + _char_name_to_usv(char1) + ';'
        (moreChars, isDual) = seq
        for nextChar in moreChars :
            if nextChar != 'NONE' :
                seqUsvsWoLast = seqUsvs
                seqLabel = seqLabel + plusSep + _char_name_to_label(nextChar)
                seqUsvs = seqUsvs + '&#x' + _char_name_to_usv(nextChar) + ';'
                plusSep = ' + '
                lastChar = nextChar

        # Convert a sequence like (lam, noonSmallVI) back to (lam, beh) just for use in a final context.
        lastCharIM = lastChar
        lastChar = _fix_last_char(lastChar, expandLeft)
        finalSeqUsvs = seqUsvsWoLast + '&#x' + _char_name_to_usv(lastChar) + ';' 
        if lastChar != lastCharIM :
            #seqLabel = seqLabel + " / final " + _char_name_to_label(lastChar)  # when showing the basic final instead
            isDual = "left"  # create a blank gray cell
                
        #barSep = "  |  "
        
        #f.write('    <test label="' + seqLabel + '" rtl="True" class="default">\n')
        self.f.write('    <testgroup label="' + seqLabel + '">\n')  # second level testgroup
        
        mainStr = "<em>" + seqUsvs + "</em>"
        finalStr = "<em>" + finalSeqUsvs + "</em>"
        colCnt = 0
        if isDual == "left" :
            # no final forms - add blank cells
            self.f.write('      <test rtl="True" background="#cfcfcf"><string/></test>\n')
            self.f.write('      <test rtl="True" background="#cfcfcf"><string/></test>\n')
            colCnt = colCnt + 2
        if isDual == "right" or isDual == "both" :
            self.f.write('      <test rtl="True"><string>' + finalStr)  # IF
            #f.write('      <comment></comment>\n')
            self.f.write('</string></test>\n')
            self.f.write('      <test rtl="True"><string>' + contextCharI + finalStr + '</string></test>\n')   # MF
            colCnt = colCnt + 2
        if isDual == "left" or isDual == "both" :
            # Showing only the left connections is used for medial forms of qaf, yeh, and noon that
            # are "extra" forms of other basic characters.
            ##if isDual == "both" :
            ##    f.write(barSep)
            self.f.write('      <test rtl="True"><string>' + mainStr + contextCharF + '</string></test>\n')  # IM
            self.f.write('      <test rtl="True"><string>' + contextCharI + mainStr + contextCharF + '</string></test>\n')   # MM
            colCnt = colCnt + 2
            
        while colCnt < 4 :
            self.f.write('      <test rtl="True" background="#cfcfcf"><string/></test>\n')  # empty cell
            colCnt = colCnt + 1
            
        self.f.write('    </testgroup>\n')
    # end of write_one_sequence



class Text(FTML):

    def write_header(self, mode, fontscale):
        pass

    def write_closing(self):
        pass

    def start_group(self, label):
        pass

    def end_group(self):
        pass

    def write_one_sequence(self, seq, contextCharI, contextCharF) :
        cI = unichr(int(contextCharI[3:-1], 16))
        cF = unichr(int(contextCharF[3:-1], 16))
        (chars, dual) = seq
        s = u"".join(unichr(int(_char_name_to_usv(c), 16)) for c in chars if c != 'NONE')
        if dual == "right" or dual == "both":
            self.f.write(s+"\n")
            self.f.write(cI+s+"\n")
        if dual == "left" or dual == "both":
            self.f.write(s+cF+"\n")
            self.f.write(cI+s+cF+"\n")


def output(gen, mode, fontName, fontScale, sequences, expandLeft) :
    #import codecs

    contextCharI = "&#x0644;" # lam (arbitrary pre-context)
    #contextCharI = "&#x0639;" # ain (arbitrary pre-context)
    contextCharF = "&#x0641;" # feh (arbitrary post-context)
    gen.write_header(mode, fontName, fontScale)

    for key in sequences :
        (sortValBogus, groupName) = key.split('_')
        temp = groupName.split("&")
        if len(temp) == 2 :
            (baseGroupName, diacGroupName) = temp
        else :
            baseGroupName = groupName
            diacGroupName = ""
            
        (sortValBogus, label, colFM_bogus, colIM_bogus) = _group_name_format(baseGroupName)
        label = label + " sequences"
        if diacGroupName :
            (diacSortValBogus, diacLabel) = _diac_group_name_format(diacGroupName)
            label = label + " with " + diacLabel

        gen.start_group(label)
        
        keySeq = sequences[key]
        
        for seq in sequences[key] :
            gen.write_one_sequence(seq, contextCharI, contextCharF, expandLeft)
        
        gen.end_group()
            
    gen.write_closing()
    gen.close()

def _char_name_to_usv(charName) :
    charNameToUsv = {
        "alef"          :   '0627',
            "alefMadda" :   '0622',
            "alefWasla" :   '0671',
            "alef2"     :   '0773',
            "alef3"     :   '0774',
        "beh"           :   '0628',
            "teh"       :   '062A',
            "theh"      :   '062B',
            "tteh"      :   '0679',
            "peh"       :   '067E',
            "tteheh"    :   '067A',
            "beeh"      :   '067B',
            "tehRing"   :   '067C',
            "teh3down"  :   '067D',
            "dotlessBeh":   '066E',
        "jeem"          :   '062C',
            "hah"       :   '062D',
            "khah"      :   '062E',
            "tcheh"     :   '0686',
            "dyeh"      :   '0684',
            "tcheheh"   :   '0687',
            "hahHamza"  :   '0681',
            "hah3dots"  :   '0685',
            "hahTah"    :   '076E',
            "hahTah2smd":   '076F',
            "hah4below" :   '077C',
        "dal"           :   '062F',
            "thal"      :   '0630',
            "ddal"      :   '0688',
            "dalDotBelow":  '068A',
            "dalDotTah" :   '068B',
            "dal2dotsVTah": '0759',
            "dalRing"   :   '0689',
            "dal4dots"  :   '0690',
            "dul"       :   '068E',
        "reh"           :   '0631',
            "zain"      :   '0632',
            "rreh"      :   '0691',
            "jeh"       :   '0698',
            "rehDotBelow" : '0694',
            "rehDotDot" :   '0696',
            "reh2dots"  :   '0697',
            "reh4dots"  :   '0699',
            "rehHamza"  :   '076C',
            "rehRing"   :   '0693',
            "rehTah2smd" :  '0771',
            "reh2dotsV" :   '076B',
            "rehSmallVbelow" : '0695',
        "seen"          :   '0633',
            "sheen"     :   '0634',
            "seenDotDot":   '069A',
            "seen4dots" :   '075C',
            "seen2dotsV"  : '076D',
            "seenTah2smd" : '0770',
            "seen3below":   '069B',	
            "seen3dots3dots" : '069C',
            "seenInvV"  :   '077E',
            "seen4"     :   '077D',
        "sad"           :   '0635',
            "dad"       :   '0636',
            "dadDotBelow" : '06FB',
            "sad3dots"  :   '069E',
        "tah"           :   '0637',
            "zah"       :   '0638',
        "ain"           :   '0639',
            "ghain"     :   '063A',
            "ain3dots"  :   "06A0",
        "feh"           :   '0641',
            "feh3dotsAbove" :   '06A4',
            "feh3dotsBelow" :   '06A5',
            "dotlessFeh"    :   '06A1',
        "qaf"               :   '0642',     # Note: add two codes for each character!
            "qafIM"         :   '0642',
            "dotlessQaf"    :   '066F',
            "dotlessQafIM"  :	'066F',
        "lam"           :   '0644',
            "lamBar"    :   '076A',
            "lamSmallV" :   '06B5',
            "lam3dots"  :   '06B7',
            "lamTah"    :   '08C7',
        "meem"          :   '0645',
        "meem-alt"      :   '0645',
        "noon"              :   '0646',     # Note: add two codes for each character!
            "noonIM"        :   '0646',
            "noonGhunna"    :   '06BA',
            "noonGhunnaIM"  :   '06BA',
            "noonRetro"     :   '0768',
            "noonRetroIM"   :   '0768',
            "noonDotBelow"  :   '06B9',
            "noonDotBelowIM":   '06B9',
            "rnoon"         :   '06BB',
            "rnoonIM"       :   '06BB',
            "noonRing"      :   '06BC',
            "noonRingIM"    :   '06BC',
            "noonSmallV"    :   '0769',
            "noonSmallVIM"  :   '0769',
            "noon3dots"     :   '06BD',
            "noon3dotsIM"   :   '06BD',
        "waw"           :   '0648',
            "wawHamza"  :   '0624',
            "wawRing"   :   '06C4',
            "kirghizYu" :   '06C9',
            "ve"        :   '06CB',
            "yu"        :   '06C8',
            "wawDot"    :   '06CF',
            "waw2dots"  :   '06CA',
            "waw2"      :   '0778',
            "waw3"      :   '0779',
        "kaf"           :   '06A9',
            "gaf"       :   '06AF',
            "gueh"      :   '06B3',
            "ngoeh"     :   '06B1',
            "kafRing"   :   '06AB',
            "kaf2dots"  :   '077F',
            "ng"        :   '06AD',  # kaf w/ three dots
            "kehehDot"  :   '0762',
            "keheh3dots":   '0763',
            "gafRing"   :   '06B0',
            "graf"      :   '08C8',
        "hehDo"         :   '06BE',
        "hehGoal"       :   '06C1',
            "arabicHeh" :   '0647',
            "hehHamza"  :   '06C2',
        "tehMarGoal"    :   '06C3',
            "tehMarbuta":   '0629',
            "hehYeh"    :   '06C0',
        "chotiyeh"      :   '06CC',     # Note: add two codes for each character!
            "chotiyehIM":   '06CC',
            "yehHamza"  :   '0626',
            "yehHamzaIM":   '0626',
            "yehSmallV" :   '06CE',
            "yehSmallVIM" : '06CE',   
            "arabicE"   :   '06D0',
            "arabicEIM" :   '06D0',
            "alefMaksura" : '0649',
            "alefMaksuraIM":'0649',
            "yeh2"      :   '0775',
            "yeh3"      :   '0776',
            "yeh4below" :   '0777',
        "bariyeh"       :   '06D2',
            "bariyeh2"  :   '077A',
            "bariyeh3"  :   '077B',
            
        "zabar"         :   '064E',
        "pesh"          :   '064F',
        "zair"          :   '0650',
        "dozabar"       :   '064B',
        "dopesh"        :   '064C',
        "dozair"        :   '064D',
        "shadda"        :   '0651',
        "jazm"          :   '0652',
        "kharizabar"    :   '0670',
        "kharizair"     :   '0656',
        "ultapesh"      :   '0657',
        "short-vowel"   :   '08FF'
    }
            
    return charNameToUsv[charName]

# end of _char_name_to_usv


def _char_name_to_label(charName) :
    
    if charName[-3:] == "_IM" :
        label = charName[:-3]
    elif charName[-2:] == "IM" :
        label = charName[:-2]
    else :
        label = charName
        
    return label
                
# end of _char_name_to_label


def _reverse_list(aList) :
    newList = []
    for item in aList :
        newList.insert(0, item)
    return newList


def _group_name_format(charName) :
    # code : { sort-key, label, final/medial count, initial/medial count }
    #    2, 2 - standard dual-connected character
    #    2, 0 - standard right-connected character
    #    0, 2 - initial/medial form of a dual-connected character that has an different final (eg, yeh, noon, qaf)
    groupNameFormat = {
        "alef"          :   ('01',      'Alef form',        2, 0),
        "alefMadda"     :   ('01a',     'Alef madda form',  2, 0),
        "alefWasla"     :   ('01b',     'Alef wasla form',	2, 0),
        "alef2"         :   ('01c',     'Alef with 2',      2, 0),
        "alef3"         :   ('01d',     'Alef with 3',      2, 0),
            
        "beh"           :   ('02',      'Beh form',         2, 2),
        "teh"           :   ('02a',     'Teh form',         2, 2),
        "theh"          :   ('02b',     'Theh form',        2, 2),
        "tteh"          :   ('02c',     'Tteh form',        2, 2),
        "peh"           :   ('02d',     'Peh form',         2, 2),
        "tteheh"        :   ('02e',     'Tteheh form',      2, 2),
        "beeh"          :   ('02f',     'Beeh form',        2, 2),
        "tehRing"       :   ('02g',     'Teh with ring form',                   2, 2),
        "teh3down"      :   ('02h',     'Teh with 3 dots downward',             2, 2),
        "dotlessBeh"    :   ('02i',     'Dotless beh',                          2, 2),
        "noonIM"        :   ('02x0',    'Noon initial/medial form',             0, 2),
        "noonGhunnaIM"  :   ('02x1',    'Noon-ghunna form',                     0, 2),
        "noonRetroIM"   :   ('02x2',    'Noon-retro initial/medial form',       0, 2),
        "noonDotBelowIM":   ('02x3',    'Noon-dot-below form',                  0, 2),
        "rnoonIM"       :   ('02x4',    'Rnoon initial/medial form',            0, 2),
        "noonRingIM"    :   ('02x5',    'Noon-ring initial/medial form',        0, 2),
        "noonSmallVIM"  :   ('02x6',    'Noon-small-V initial/medial form',     0, 2),
        "noon3dotsIM"   :   ('02x7',    'Noon-with-3-dots initial/medial forms',0, 2),
        "chotiyehIM"    :   ('02y0',    'Chotiyeh initial/medial form',         0, 2),
        "yehHamzaIM"    :   ('02y1',    'Yeh-hamza initial/medial form',        0, 2),
        "yehSmallVIM"   :   ('02y2',    'Yeh with small V initial/medial form', 0, 2),
        "arabicEIM"     :   ('02y3',    'Arabic E initial/medial form',         0, 2),
        "alefMaksuraIM" :   ('02y4',    'Alef maksura initial/medial form',     0, 2),
        
        "jeem"          :   ('03',      'Jeem form',    2, 2),
        "hah"           :   ('03a',     'Hah form',     2, 2),
        "khah"          :   ('03b',     'Khah form',    2, 2),
        "tcheh"         :   ('03c',     'Tcheh form',   2, 2),
        "dyeh"          :   ('03d',     'Dyeh form',    2, 2),
        "tcheheh"       :   ('03e',     'Tcheheh form',                     2, 2),
        "hahHamza"      :   ('03f',     'Hah hamza form',                   2, 2),
        "hah3dots"      :   ('03g',     'Hah with 3 dots form',             2, 2),
        "hahTah"        :   ('03h',     'Hah with tah form',                2, 2),
        "hahTah2smd"    :   ('03i',     'Hah with tah and small dots form', 2, 2),
        "hah4below"     :   ('03j',     'Hah with 4 below',                 2, 2),
        
        "dal"           :   ('04',      'Dal form',     2, 0),
        "thal"          :   ('04a',     'Thal form',    2, 0),
        "ddal"          :   ('04b',     'Ddal',         2, 0),
        "dalDotTah"     :   ('04c',     'Dal with tah and dot below',         2, 0),
        "dal2dotsVTah"  :   ('04d',     'Dal with 2 dots vertically and tah', 2, 0),
        "dalRing"       :   ('04e',     'Dal with ring',        2, 0),
        "dal4dots"      :   ('04f',     'Dal with four dots',   2, 0),
        "dul"           :   ('04g',     'Dul',                  2, 0),
        "dalDotBelow"   :   ('04z',     'Dal with dot below',   2, 0),   # not needed for Nastaliq, but requested via email
            
        "reh"           :   ('05',      'Reh form',     2, 0),
        "zain"          :   ('05a',     'Zain form',    2, 0),
        "rreh"          :   ('05b',     'Rreh form',    2, 0),
        "rehDotBelow"   :   ('05c',     'Reh with dot below',               2, 0),
        "jeh"           :   ('05d',     'Jeh form',                         2, 0),
        "rehDotDot"     :   ('05e',     'Reh with dot above and below',     2, 0),
        "reh2dots"      :   ('05f',     'Reh with 2 dots above',            2, 0),
        "reh4dots"      :   ('05g',     'Reh with 4 dots above',            2, 0),
        "rehHamza"      :   ('05h',     'Reh with hamza',                   2, 0),
        "rehRing"       :   ('05i',     'Reh with ring',                    2, 0),
        "rehTah2smd"    :   ('05j',     'Reh with tah and two small dots',  2, 0),
        "reh2dotsV"     :   ('05k',     'Reh with two dots vertically',     2, 0),
        "rehSmallVbelow" :  ('05l',		'Reh with small V below',           2, 0),
        
        "seen"          :   ('06',      'Seen form',    2, 2),
        "sheen"         :   ('06a',     'Sheen form',   2, 2),
        "seenDotDot"    :   ('06b',     'Seen with dot above and below', 2, 2),
        "seen4dots"     :   ('06c',     'Seen with four dots',           2, 2),
        "seen2dotsV"    :   ('06d',     'Seen with two dots vertically',        2, 2),
        "seenTah2smd"   :   ('06e',     'Seen with tah and two small dots',     2, 2),
        "seen3below"    :   ('06f',     'Seen with three dots below',           2, 2),
        "seen3dots3dots":   ('06g',     'Seen with three lower and upper dots', 2, 2),
        "seenInvV"      :   ('06h',     'Seen with inverted V', 2, 2),
        "seen4"         :   ('06i',     'Seen with 4',          2, 2),
            
        "sad"           :   ('07',      'Sad form',           2, 2),
        "dad"           :   ('07a',     'Dad form',           2, 2),
        "dadDotBelow"   :   ('07b',     'Dad with dot below', 2, 2),
        "sad3dots"      :   ('07c',     'Sad with 3 dots',    2, 2),

        "tah"           :   ('08',      'Tah form',     2, 2),
        "zah"           :   ('08a',     'Zah form',     2, 2),

        "ain"           :   ('09',      'Ain form',                     2, 2),
        "ghain"         :   ('09a',     'Ghain form',                   2, 2),
        "ain3dots"      :   ('09b',     'Ain with three dots above',    2, 2),

        "feh"           :   ('10',      'Feh form',                         2, 2),
        "qafIM"         :   ('10a',     'Qaf initial/medial form',          0, 2),
        "feh3dotsAbove" :   ('10b',     'Feh with three dots above',        2, 2),
        "feh3dotsBelow" :   ('10c',     'Feh with three dots below',        2, 2),
        "dotlessFeh"    :   ('10d',     'Dotless feh',                      2, 2),
        "dotlessQafIM"  :   ('10e',     'Dotless qaf initial/medial form',	0, 2),
        "qaf"           :   ('11',      'Qaf form',         		2, 0),
        "dotlessQaf"    :   ('11a',     'Dotless qaf form',			2, 0),

        "lam"           :   ('12',      'Lam form',         		2, 2),
        "lamBar"        :   ('12a',     'Lam with bar',     		2, 2),
        "lamSmallV"     :   ('12b',     'Lam with small V', 		2, 2),
        "lam3dots"      :   ('12c',     'Lam with 3 dots',  		2, 2),
        "lamTah"        :   ('12d',     'Lam with small tah',		2, 2),

        "meem"          :   ('13',      'Meem form',        		2, 2),
        "alt-meem"      :   ('14',      'Alternate meem',   		2, 2),
        
        "noon"          :   ('15',      'Noon form',            2, 0),
        "noonGhunna"    :   ('15a',     'Noon-ghunna form',     2, 0),
        "noonRetro"     :   ('15b',     'Noon-retro form',      2, 0),
        "noonDotBelow"  :   ('15c',     'Noon-dot-below form',  2, 0),
        "rnoon"         :   ('15d',     'Rnoon form',           2, 0),
        "noonRing"      :   ('15e',     "Noon-ring",            2, 0),
        "noonSmallV"    :   ('15f',     "Noon-small-V form",    2, 0),
        "noon3dots"     :   ('15g',     "Noon with three dots", 2, 0),
        
        "waw"           :   ('16',      'Waw form',             2, 0),
        "wawHamza"      :   ('16a',     'Waw-hamza form',       2, 0),
        "wawRing"       :   ('16b',     'Waw-ring form',        2, 0),
        "kirghizYu"     :   ('16c',     'Kirghiz Yu form',      2, 0),
        "ve"            :   ('16d',     'Ve form',              2, 0),
        "yu"            :   ('16e',     'Yu form',              2, 0),
        "wawDot"        :   ('16f',     'Waw with dot form',    2, 0),
        "waw2dots"      :   ('16g',     'Waw with 2 dots',      2, 0),
        "waw2"          :   ('16h',     'Waw with 2',           2, 0),
        "waw3"          :   ('16i',     'Waw with 3',           2, 0),
        
        "kaf"           :   ('17',      'Kaf form',             2, 2),
        "gaf"           :   ('18',      'Gaf form',             2, 2),
        "gueh"          :   ('18a',     'Gueh form',            2, 2),
        "ngoeh"         :   ('18b',     'Ngoeh form',           2, 2),
        "kafRing"       :   ('18c',     'Kaf-ring form',        2, 2),
        "kaf2dots"      :   ('18d',     'Keheh with 2 dots',    2, 2),
        "ng"            :   ('18e',     'Ng (kaf w/ 3 dots)',   2, 2),
        "kehehDot"      :   ('18f',     'Keheh with dot',       2, 2),
        "keheh3dots"    :   ('18g',     'Keheh with 3 dots',    2, 2),
        "graf"          :   ('18h',     'Graf',                 2, 2),
        "gafRing"       :   ('18z',     'Gaf-ring form',        2, 2),  # not really needed for Nastaliq

        "hehDo"         :   ('19',      'Heh-Doachashmee form', 2, 2),
        
        "hehGoal"       :   ('20',      'Heh-Goal form',        2, 2),
        "arabicHeh"     :   ('20a',     'Arabic heh form',      2, 2),
        "hehHamza"      :   ('20b',     'Heh-hamza form',       2, 2),

        "tehMarGoal"    :   ('21',      'Teh-marbuta-goal form',2, 2),            
        "tehMarbuta"    :   ('21a',     'Teh-marbuta form',     2, 2),
        "hehYeh"        :   ('21b',     'Heh with yeh form',    2, 2),
       
        "chotiyeh"      :   ('22',      'Chotiyeh form',      2, 0),
        "yehHamza"      :   ('22a',     'Yeh-hamza form',     2, 0),
        "yehSmallV"     :   ('22b',     'Yeh-small-V form',   2, 0),
        "arabicE"       :   ('22c',     'Arabic E form',      2, 0),
        "alefMaksura"   :   ('22d',     'Alef maksura form',  2, 0),
        "yeh2"          :   ('22e',     'Yeh with 2',         2, 0),
        "yeh3"          :   ('22f',     'Yeh with 3',         2, 0),
        "yeh4below"     :   ('22g',     'Yeh with 4 below',   2, 0),

        "bariyeh"       :   ('23',      'Bariyeh form',       2, 0),
        "bariyeh2"      :   ('23a',     'Bariyeh with 2',     2, 0),
        "bariyeh3"      :   ('23b',     'Bariyeh with 3',     2, 0),
            
        "multi-beh"     :   ('24',      'Multiple Beh',       2, 2),
        "seen/sad+beh"  :   ('25',      'Seen/Sad + Beh',     2, 2),
        "beh+reh"       :   ('26',      'Beh + Reh',          2, 0),
        "beh+noon"      :   ('27',      'Beh + Noon',         2, 0),
        "beh+hehGoal"   :   ('28',      'Beh + Heh-Goal',     2, 0),
        "multi-seen"    :   ('29',      'Seen + seen + seen', 2, 0)
    }
            
    return groupNameFormat[charName]

# end of _group_name_format


def _diac_group_name_format(diacName) :
    groupNameFormat = {
        "zabar"         :   (':01',      "Zabar"),
        "pesh"          :   (':02',      "Pesh"),
        "zair"          :   (':03',      "Zair"),
        "dozabar"       :   (':04',      "Dozabar"),
        "dopesh"        :   (':05',      "Dopesh"),
        "dozair"        :   (':06',      "Dozair"),
        "shadda"        :   (':07',      "Shadda"),
        "jazm"          :   (':08',      "Sukun/Jazm"),
        "kharizabar"    :   (':09',      "Kharizabar"),
        "kharizair"     :   (':10',      "Kharizair"),
        "ultapesh"      :   (':11',      "Ultapesh"),
        "short-vowel"   :   (':12',      "Short-vowel mark")
    }
    return groupNameFormat[diacName]
    

# Top level

run()

# Generate FTML test data files

import collections
import codecs
import copy

def run():
    
    outputPath = "C:\\Awami-Git\\tests\\data\\FTML_XSL\\"
    
    #mode = "basicforms"         # all contextual forms of the basic shapes (beh, jeem, seen, etc.)
    #mode = "allbasechars"       # some contextual forms of all letters - make sure nuqtas are generated
    #mode = "allbasecharforms"   # all forms of all letters
    mode = "basic_somediac"     # same characters as basicforms, each with an upper and lower diac
    #mode = "basic_alldiac"      # same characters as basicforms, with every diac
    #mode = "allbase_somediac"
    #mode = "alldiac"  # not implemented???
    
    fontScale = "200"
    
    outputFilename = outputPath + "test_" + mode + ".xml"
 
    basicSeq = generate_basic_sequences(mode)
    print "basicSeq =", basicSeq
    
    expandedSeq = expand_sequences(mode, basicSeq)
    print "expandedSeq =", expandedSeq
    
    seqWDiacritics = insert_diacritics(mode, expandedSeq)
    print "seqWDiacritics =", seqWDiacritics
    
    groupedSeq = organize_sequences_by_group(mode, seqWDiacritics)
    print "groupedSeq =", groupedSeq
    
    output_ftml(mode, fontScale, outputFilename, groupedSeq)
    
    print ""
    print "Done"

# end of run    


def generate_basic_sequences(mode) :
    
    dualConnecting = ["beh", "jeem", "seen", "sad", "tah", "ain", "feh", "lam", "meem", "kaf",
        "hehDo", "hehGoal"]
    rightConnecting = ["alef", "dal", "reh", "qaf", "waw", "bariyeh", "chotiyeh", "noon", "tehMarbuta"]
    
    (dualSubs, rightSubs) = _generate_sub_sequences()
    
    # For debugging:
    """dualConnecting = ["sad"]
    rightConnecting = ["dal", "chotiyeh"]
    dualSubs = []
    rightSubs = []
    """
    
    sequences = []
    for dualChar1 in dualConnecting :
        ###if dualChar1 != "beh" and dualChar1 != "jeem" : continue
        
        seconds = []
        for dualChar2 in dualConnecting :
            uniple = (dualChar1, dualChar2)  # NONE is a kludge to force a tuple
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
            
    # TODO: add kinked kaf forms
    
    return (dualSubs, rightSubs)

# end of generate_sub_sequences


def expand_sequences(mode, basicSequences) :
    
    # Put the extra forms in the reverse order, since they always get added right after
    # the basic form.
    if mode == "basicforms" :
        expand = {"kaf" : ["gaf"]}
        expand_left = {}
        changeKey = False
        
    elif mode == "basic_somediac" or mode == "basic_alldiac" :
        expand = {"kaf" : ["gaf"],
            "beh" : ["teh"]  # because diacritics attach differently to upper and lower nuqtas
        }
        expand_left = {}
        changeKey = False
        
    elif mode == "allbasecharforms" or mode == "allbasechars" :
        expand = {
            "beh"       :   ["teh3down", "tehRing", "beeh", "tteheh", "peh", "tteh", "theh", "teh"],
            "jeem"      :   ["hahTah2smd", "hahTah", "hah3dots", "hahHamza", "tcheheh",  "dyeh", "tcheh", "khah", "hah"],
            "seen"      :   ["seen3dots3dots", "seenTah2smd", "seen2dotsV", "seen4dots", "seenDotDot", "sheen"],
            "sad"       :   ["dadDotBelow", "dad"],
            "tah"       :   ["zah"],
            "ain"       :   ["ghain"],
            "feh"       :   ["feh3dots"],
            "kaf"       :   ["kafRing", "ngoeh", "gueh", "gaf"],
                                        # gafRing - not needed for Nastaliq
            "lam"       :   ["lamSmallV", "lamBar"],
            "noon"      :   ["rnoon", "noonDotBelow", "noonRetro", "noonGhunna"],
            "chotiyeh"  :   ["arabicE", "yehHamza"],
            "hehGoal"   :   ["hehHamza", "arabicHeh"],
                
            "reh"       :   ["reh2dotsV", "rehTah2smd", "rehRing", "rehHamza", "reh4dots", "reh2dots", "rehDotDot", "rehDotBelow", "jeh", "rreh", "zain"],
            "dal"       :   ["dal4dots", "dalRing", "dal2dotsVTah", "dalDotTah", "ddal", "thal"],
                                        # dalDotBelow - not really needed for Nastaliq
            "waw"       :   ["wawRing", "wawHamza"],
            "tehMarGoal" :  ["hehYeh", "tehMarbuta"]
        }
        expand_left = {  # initial/medial forms of letters that have different finals
            "beh"       :   ["rnoonIM", "noonDotBelowIM", "noonRetroIM", "noonGhunnaIM", "noonIM", "arabicEIM", "yehHamzaIM", "chotiyehIM"],
            "feh"       :   ["qafIM"]
        }
        
        # Debugging:
        """expand = { "jeem" : ["khah", "hah"], "seen" : ["sheen"] }
        expand_left = { "beh" :   ["noonIM", "chotiyehIM"], }
        """
        
        changeKey = True
        
    elif mode == "alldiac" :
        expand = {}
        expand_left = {}

    resultSeq = basicSequences
    
    if mode == "allbasechars" :
        for key, expandList in expand.iteritems() :
            reverseList = _reverse_list(expandList)
            resultSeq = _substitute_bases(resultSeq, key, reverseList)
            
    else :
        for key, value in expand.iteritems() :
            for expandChar in value :
                resultSeq = _add_set_starting_with(resultSeq, key, expandChar, "copy", changeKey)
                
        for key, value in expand_left.iteritems() :
            for expandChar in value :
                resultSeq = _add_set_starting_with(resultSeq, key, expandChar, "left", changeKey)
    
        #print "after _add_set_starting_with: ",resultSeq
    
        for key, value in expand.iteritems() :
            for expandChar in value :
                resultSeq = _expand_one_char(resultSeq, key, expandChar, "copy")
    
        for key, value in expand_left.iteritems() :
            for expandChar in value :
                resultSeq = _expand_one_char(resultSeq, key, expandChar, "left")
     
    return resultSeq
    
# end of expand_sequences


def _is_dual(oldIsDual, setIsDual) :
    if oldIsDual == "right" :
        return "right"
    elif setIsDual == "left" :
        return "left"  # instead of "both"
    else :
        return oldIsDual


def _add_set_starting_with(sequences, basicChar, expandChar, setIsDual, changeKey) :
    print "_add_set_starting_with", basicChar, expandChar, setIsDual
    i = 0
    for (char1, charList) in sequences :
        if char1 == basicChar :
            newList = []
            for (charTuple, isDual, key) in charList :
                newKey = expandChar if (key == basicChar and changeKey) else key
                newIsDual = _is_dual(isDual, setIsDual)
                newTuple = tuple([expandChar] + list(charTuple[1:]))
                newStuff = (newTuple, newIsDual, newKey)
                print "adding",newStuff
                newList.append(newStuff)
            sequences.insert(i+1, (expandChar, newList))
            break
        i = i + 1
    return sequences
    
# end of _add_set_starting_with

        
def _expand_one_char(sequences, basicChar, expandChar, setIsDual) :
    #print "exanding " + basicChar +" to " + expandChar
    newStuff = []
    iChar1 = 0
    for (char1, charData) in sequences :
        #print "char1=",char1
        
        iTuple = 0
        skip = 0
        for (charTuple, isDual, groupName) in charData :
            #print charTuple
            if skip > 0 :
                # This was a new sequence that was just inserted.
                skip = skip - 1
                #print "skipping charTuple:",charTuple
            else :
                #print "maybe copying charTuple:", charTuple
                newList = []
                foundOneToExpand = False
                iChar = 0
                for remChar in charTuple :
                    if iChar == len(charTuple) - 1 and setIsDual == "left" :
                        # we only want to substitute left-connecting glyphs, and this is a final
                        newList.append(remChar)
                    elif remChar == basicChar and iChar > 0 : # if iChar == 0, first char is redundant with char1 key
                        #print iChar,basicChar," - expand this"
                        newList.append(expandChar)  # substitute expandChar, the similarly formed character
                        foundOneToExpand = True
                    else :
                        newList.append(remChar)
                    iChar = iChar + 1
            
                if foundOneToExpand :
                    #print "inserting ", newList
                    newIsDual = _is_dual(isDual, setIsDual)
                    newGroup = expandChar if groupName == basicChar else groupName
                    charData.insert(iTuple + skip + 1, (tuple(newList), newIsDual, newGroup)) # insert after this one
                    skip = skip + 1
                    #print "skip=",skip
            
            iTuple = iTuple + 1
                
        #charData.extend(newStuff)
        sequences[iChar1] = (char1, charData)
        
        #print "### sequences=",sequences
        
        iChar1 = iChar1 + 1
        
    return sequences

# end of _expand_one_char


# Substitute an "expand" form for the basic form.
def _substitute_bases(sequences, key, expandList) :
    
    subList = [key] + expandList
    maxC = len(subList)
    nextC = 0
    for (char1, charData) in sequences :
        #print "char1=",char1
        iData = 0
        for (charTuple, isDual, groupName) in charData :
            charList = list(charTuple)
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
        for (char1, charData) in resultDict.iteritems() :
            resultSeq.append((char1, charData))
        
    return resultSeq
    
# end of insert_diacritics


def _insert_diacritic(sequences, seqWDiacritics, diacChar) :
    
    for (char1, charData) in sequences :
        if not seqWDiacritics.has_key(char1) : seqWDiacritics[char1] = []
        newCharData = seqWDiacritics[char1]
        for (charTuple, isDual, groupName) in charData :
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
        
            if not resultSeq.has_key(key) :
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


def output_ftml(mode, fontScale, filename, sequences) :
    #import codecs

    f = codecs.open(filename, 'w', 'utf-8')
    write_xml_header(f, mode, fontScale)

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

        f.write('  <testgroup label="' + label + '">\n')
        
        keySeq = sequences[key]
        
        for seq in sequences[key] :
            write_one_sequence(f, seq)
        
        f.write('  </testgroup>\n')
            
    write_xml_closing(f)
    f.close()


def write_one_sequence(f, seq) :
    
    #contextCharI = "&#x0644;" # lam (arbitrary pre-context)
    contextCharI = "&#x0639;" # ain (arbitrary pre-context)
    contextCharF = "&#x0641;" # feh (arbitrary post-context)
    seqLabel = ''
    seqUsvs = ''
    plusSep = ''
    ###seqLabel = char1
    ###seqUsvs = '&#x' + _char_name_to_usv(char1) + ';'
    (moreChars, isDual) = seq
    for nextChar in moreChars :
        if nextChar != 'NONE' :
            seqLabel = seqLabel + plusSep + _char_name_to_label(nextChar)
            seqUsvs = seqUsvs + '&#x' + _char_name_to_usv(nextChar) + ';'
            plusSep = ' + '
            
    #barSep = "  |  "
    
    #f.write('    <test label="' + seqLabel + '" rtl="True" class="default">\n')
    f.write('    <testgroup label="' + seqLabel + '">\n')  # second level testgroup
    
    mainStr = "<em>" + seqUsvs + "</em>"
    colCnt = 0
    if isDual == "left" :
        # no final forms - add blank cells
        f.write('      <test rtl="True" background="#cfcfcf"><string/></test>\n')
        f.write('      <test rtl="True" background="#cfcfcf"><string/></test>\n')
        colCnt = colCnt + 2
    if isDual == "right" or isDual == "both" :
        f.write('      <test rtl="True"><string>' + mainStr)  # IF
        #f.write('      <comment></comment>\n')
        f.write('</string></test>\n')
        f.write('      <test rtl="True"><string>' + contextCharI + mainStr + '</string></test>\n')   # MF
        colCnt = colCnt + 2
    if isDual == "left" or isDual == "both" :
        # Showing only the left connections is used for medial forms of qaf, yeh, noon, etc. that
        # are "extra" forms of other basic characters.
        ##if isDual == "both" :
        ##    f.write(barSep)
        f.write('      <test rtl="True"><string>' + mainStr + contextCharF + '</string></test>\n')  # IM
        f.write('      <test rtl="True"><string>' + contextCharI + mainStr + contextCharF + '</string></test>\n')   # MM
        colCnt = colCnt + 2
        
    while colCnt < 4 :
        f.write('      <test rtl="True" background="#cfcfcf"><string/></test>\n')  # empty cell
        colCnt = colCnt + 1
        
    f.write('    </testgroup>\n')
    
def _char_name_to_usv(charName) :
    charNameToUsv = {
        "alef"          :   '0627',
        "beh"           :   '0628',
            "teh"       :   '062A',
            "theh"      :   '062B',
            "tteh"      :   '0679',
            "peh"       :   '067E',
            "tteheh"    :   '067A',
            "beeh"      :   '067B',
            "tehRing"   :   '067C',
            "teh3down"  :   '067D',
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
        "dal"           :   '062F',
            "thal"      :   '0630',
            "ddal"      :   '0688',
            "dalDotBelow":  '068A',
            "dalDotTah" :   '068B',
            "dal2dotsVTah": '0759',
            "dalRing"   :   '0689',
            "dal4dots"  :   '0690',
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
        "seen"          :   '0633',
            "sheen"     :   '0634',
            "seenDotDot":   '069A',
            "seen4dots" :   '075C',
            "seen2dotsV"  : '076D',
            "seenTah2smd" : '0770',
            "seen3dots3dots" : '069C',
        "sad"           :   '0635',
            "dad"       :   '0636',
            "dadDotBelow" : '06FB',
        "tah"           :   '0637',
            "zah"       :   '0638',
        "ain"           :   '0639',
            "ghain"     :   '063A',
        "feh"           :   '0641',
            "feh3dots"  :   '06A5',
        "qaf"           :   '0642',
            "qafIM"     :   '0642',
        "lam"           :   '0644',
            "lamBar"    :   '076A',
            "lamSmallV" :   '06B5',
        "meem"          :   '0645',
        "meem-alt"      :   '0645',
        "noon"          :   '0646',
            "noonIM"    :   '0646',
            "noonGhunna"    :   '06BA',
            "noonGhunnaIM"  :   '06BA',
            "noonRetro"     :   '0768',
            "noonRetroIM"   :   '0768',
            "noonDotBelow"  :   '06B9',
            "noonDotBelowIM":   '06B9',
            "rnoon"         :   '06BB',
            "rnoonIM"       :   '06BB',
        "waw"           :   '0648',
            "wawHamza"  :   '0624',
            "wawRing"   :   '06C4',
        "kaf"           :   '06A9',
            "gaf"       :   '06AF',
            "gueh"      :   '06B3',
            "ngoeh"     :   '06B1',
            "kafRing"   :   '06AB',
            "gafRing"   :   '06B0',
        "hehDo"         :   '06BE',
        "hehGoal"       :   '06C1',
            "arabicHeh" :   '0647',
            "hehHamza"  :   '06C2',
        "tehMarGoal"    :   '06C3',
            "tehMarbuta":   '0629',
            "hehYeh"    :   '06C0',
        "chotiyeh"      :   '06CC',
            "chotiyehIM":   '06CC',
            "yehHamza"  :   '0626',
            "yehHamzaIM":   '0626',
            "arabicE"   :   '06D0',
            "arabicEIM" :   '06D0',
        "bariyeh"       :   '06D2',
            
            
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
    groupNameFormat = {
        "alef"          :   ('01',      'Alef form',    2, 0),
            
        "beh"           :   ('02',      'Beh form',     2, 2),
        "teh"           :   ('02a',     'Teh form',     2, 2),
        "theh"          :   ('02b',     'Theh form',    2, 2),
        "tteh"          :   ('02c',     'Tteh form',    2, 2),
        "peh"           :   ('02d',     'Peh form',     2, 2),
        "tteheh"        :   ('02e',     'Tteheh form',  2, 2),
        "beeh"          :   ('02f',     'Beeh form',    2, 2),
        "tehRing"       :   ('02g',     'Teh with ring form',             2, 2),
        "teh3down"      :   ('02h',     "Teh with 3 dots downward",       2, 2),
        "noonIM"        :   ('02i0',     'Noon initial/medial form',       0, 2),
        "noonGhunnaIM"  :   ('02i1',    'Noon-ghunna form',               0, 2),
        "noonRetroIM"   :   ('02i2',    'Noon-retro initial/medial form', 0, 2),
        "noonDotBelowIM":   ('02i3',    'Noon-dot-below form',            0, 2),
        "rnoonIM"       :   ('02i4',    'Rnoon initial/medial form',      0, 2),
        "chotiyehIM"    :   ('02j0',    'Chotiyeh initial/medial form',   0, 2),
        "yehHamzaIM"    :   ('02j1',    'Yeh-hamza initial/medial form',  0, 2),
        "arabicEIM"     :   ('02j2',    'Arabic E initial/medial form',   0, 2),
        
        "jeem"          :   ('03',      'Jeem form',    2, 2),
        "hah"           :   ('03a',     'Hah form',     2, 2),
        "khah"          :   ('03b',     'Khah form',    2, 2),
        "tcheh"         :   ('03c',     'Tcheh form',   2, 2),
        "dyeh"          :   ('03d',     'Dyeh form',    2, 2),
        "tcheheh"       :   ('03e',     'Khah form',    2, 2),
        "hahHamza"      :   ('03f',     'Tcheh form',   2, 2),
        "hah3dots"      :   ('03g',     'Dyeh form',    2, 2),
        "hahTah"        :   ('03h',     'Tcheh form',   2, 2),
        "hahTah2smd"    :   ('03i',     'Dyeh form',    2, 2),
        
        "dal"           :   ('04',      'Dal form',     2, 0),
        "thal"          :   ('04a',     'Thal form',    2, 0),
        "ddal"          :   ('04b',     'Ddal',         2, 0),
        "dalDotTah"     :   ('04c',     'Dal with tah and dot below',   2, 0),
        "dal2dotsVTah"  :   ('04d',     'Dal with 2 dots vertically and tah', 2, 0),
        "dalRing"       :   ('04e',     'Dal with ring',        2, 0),
        "dal4dots"      :   ('04f',     'Dal with four dots',   2, 0),
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
        
        "seen"          :   ('06',      'Seen form',    2, 2),
        "sheen"         :   ('06a',     'Sheen form',   2, 2),
        "seenDotDot"    :   ('06b',     'Seen with dot above and below',     2, 2),
        "seen4dots"     :   ('06c',     'Seen with four dots',               2, 2),
        "seen2dotsV"    :   ('06d',     'Seen with two dots vertically',     2, 2),
        "seenTah2smd"   :   ('06e',     'Seen with tah and two small dots',  2, 2),
        "seen3dots3dots":   ('06f',     'Seen with three lower and upper dots', 2, 2),
            
        "sad"           :   ('07',      'Sad form',     2, 2),
        "dad"           :   ('07a',     'Dad form',     2, 2),
        "dadDotBelow"   :   ('07b',     'Dad with dot below', 2, 2),
        "tah"           :   ('08',      'Tah form',     2, 2),
        "zah"           :   ('08a',     'Zah form',     2, 2),
        "ain"           :   ('09',      'Ain form',     2, 2),
        "ghain"         :   ('09a',     'Ghain form',   2, 2),
        "feh"           :   ('10',      'Feh form',     2, 2),
        "qafIM"         :   ('10a',     'Qaf initial/medial form',      0, 2),
        "feh3dots"      :   ('10b',     'Feh with three dots below',    2, 2),
        "qaf"           :   ('11',      'Qaf form',     2, 0),
        "lam"           :   ('12',      'Lam form',     2, 2),
        "lamBar"        :   ('12a',     'Lam with bar',     2, 2),
        "lamSmallV"     :   ('12b',     'Lam with small V', 2, 2),
        "meem"          :   ('13',      'Meem form',        2, 2),
        "alt-meem"      :   ('14',      'Alternate meem',   2, 2),
        
        "noon"          :   ('15',      'Noon form',            2, 0),
        "noonGhunna"    :   ('15a',     'Noon-ghunna form',     2, 0),
        "noonRetro"     :   ('15b',     'Noon-retro form',      2, 0),
        "noonDotBelow"  :   ('15c',     'Noon-dot-below form',  2, 0),
        "rnoon"         :   ('15d',     'Rnoon form',           2, 0),
        
        "waw"           :   ('16',      'Waw form',             2, 0),
        "wawHamza"      :   ('16a',     'Waw-hamza form',       2, 0),
        "wawRing"       :   ('16b',     'Waw-ring form',        2, 0),
        
        "kaf"           :   ('17',      'Kaf form',         2, 2),
        "gaf"           :   ('18',      'Gaf form',         2, 2),
        "gueh"          :   ('18a',     'Gueh form',        2, 2),
        "ngoeh"         :   ('18b',     'Ngoeh form',       2, 2),
        "kafRing"       :   ('18c',     'Kaf-ring form',    2, 2),
        "gafRing"       :   ('18z',     'Gaf-ring form',    2, 2),  # not really needed for Nastaliq
        
        "hehDo"         :   ('19',      'Heh-Doachashmee form', 2, 2),
        
        "hehGoal"       :   ('20',      'Heh-Goal form',        2, 2),
        "arabicHeh"     :   ('20a',     'Arabic heh form',      2, 2),
        "hehHamza"      :   ('20b',     'Heh-hamza form',       2, 2),

        "tehMarGoal"    :   ('21',      'Teh-marbuta-goal form',2, 2),            
        "tehMarbuta"    :   ('21a',     'Teh-marbuta form',     2, 2),
        "hehYeh"        :   ('21b',     'Heh with yeh form',    2, 2),
       
        "chotiyeh"      :   ('22',      'Chotiyeh form',      2, 0),
        "yehHamza"      :   ('22a',     'Yeh-hamza form',     2, 0),
        "arabicE"       :   ('22b',     'Arabic E form',      2, 0),

        "bariyeh"       :   ('23',      'Bariyeh form',       2, 0),
            
        "multi-beh"     :   ('24',      'Multiple Beh',       2, 2),
        "seen/sad+beh"  :   ('25',      'Seen/Sad + Beh',     2, 2),
        "beh+reh"       :   ('26',      'Beh + Reh',          2, 0),
        "beh+noon"      :   ('27',      'Beh + Noon',         2, 0),
        "beh+hehGoal"   :   ('28',      'Beh + Heh-Goal',     2, 0)
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
    
# end of _diac_group_name_format


def write_xml_header(f, mode, fontScale) :
   
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
        
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<?xml-stylesheet type="text/xsl" href="ftml.xsl"?>\n')
    f.write('<ftml version="1.0">\n')
    f.write('  <head>\n')
    f.write('    <columns comment="15%" label="20%" string="15%"/>\n')
    f.write('    <description>' + title + '</description>\n')
    f.write('    <fontscale>' + fontScale + '</fontscale>\n')
    f.write('    <fontsrc>local(\'Awami Nastaliq Beta1\'), url(Awami_beta1.ttf)</fontsrc>\n')
    f.write('    <title>' + title + '</title>\n')
    f.write('    <styles><style feats=\' \' name="default"/></styles>\n')
    f.write('  </head>\n')

def write_xml_closing(f) :
    f.write('</ftml>\n')


# Top level

run()
#!/usr/bin/python
# Smith configuration file

#	This file is part of the Awami Nastaliq font
#	(http://software.sil.org/awami) and is
#	Copyright (c) 2014-2018 SIL International (http://www.sil.org/),
# with Reserved Font Names "Awami" and "SIL".
#
# This Font Software is licensed under the SIL Open Font License,
# Version 1.1.
#
#	You should have received a copy of the license along with this Font Software.
#	If this is not the case, go to (http://scripts.sil.org/OFL) for all the
#	details including an FAQ.


import glob

# set the default output folders
out="results"
DOCDIR = ["documentation", "web"]
OUTDIR="installers"
ZIPDIR="releases"
TESTDIR='tests'
# TESTSTRING=u'Hello World'
# TESTRESULTSDIR = 'results/tests'
# STANDARDS = 'reference'

# set package name
APPNAME='AwamiNastaliq-Dev'      #### AwamiNastaliq

# set the font family name
FAMILY='AwamiNastaliq'

COPYRIGHT='Copyright (c) 2014-2018, SIL International (http:/www.sil.org)'
LICENSE='OFL.txt'

DESC_SHORT = "Smart Unicode font for the Nastaliq script"
DESC_NAME = "Awami-Nastaliq"
DEBPKG = 'fonts-awami'

# Get version info from Regular UFO; must be first function call:
###getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')

VERSION='1.191'              # Now taken directly from the font
##TTF_VERSION="1.151"          # 

# override tex for pdfs
testCommand('pdfs', cmd="${CMPTXTRENDER} -t ${SRC[0]} -e ${shaper} --outputtype=json -r ${SRC[1]} | ${PDFSHAPED} -s 16 -l 2.0 -o ${TGT} -f ${SRC[1]}",
                    ext='.pdf', shapers=1, supports=['.txt', '.ftml', '.xml'], replace=True)

FONT_NAME = "Awami Nastaliq Dev"  #### Awami Nastaliq
FONT_FILENAME = "AwamiNastaliq-Dev"  #### AwamiNastaliq-Regular

font(target = process(FONT_FILENAME + '.ttf', name(FONT_NAME, lang='en-US', subfamily=('Regular')),
				# remove buggy tables:
				cmd('ttftable -d hdmx,VDMX,LTSH ${DEP} ${TGT}'),
				cmd('../tools/bin/octalap -m ${SRC} -o ${TGT} ${DEP}', "source/octabox.json"),
				# for removing psnames:
				########cmd('psfix -s ${DEP} ${TGT}'),
				# strip out bogus hints:
				cmd('ttfstriphints ${DEP} ${TGT}'),
				####cmd('${TTFAUTOHINT} -v -n -c  -D arab -W ${DEP} ${TGT}'),
				cmd('ttfsubset -s deva ${DEP} ${TGT}'),
				cmd('psfcompressgr ${DEP} ${TGT}'),
				cmd('typetuner -o ${TGT} add ${SRC} ${DEP}', "source/typetuner/feat_all.xml")
     		),
    source = "source/AwamiNastaliq-Regular.ufo",
    params = "--removeOverlap",
    graphite = gdl('awami.gdl', master = 'source/graphite/nastaliq_rules.gdl', params='-D -w3541 -w2504 -w4510',  ##### -c',
                    depends = glob.glob('*.gdh')),
    opentype = fea('source/simple.fea', no_make=1, no_test=True),
    ap = "AwamiNastaliqRegular_AP.xml",
    license = ofl('Awami','SIL'),
    copyright = COPYRIGHT,
    version = VERSION,
    extra_srcs = ['tools/bin/awami_makegdl', 'tools/bin/ffcopyglyphs.py', 'tools/bin/perllib/Font/TTF/Scripts/GDL.pm'], ## 'DoulosSIL-R.ttf'],
    #tests = tests,
    fret = fret(params = '-r -b'),  # -b = show octaboxes
    woff = woff('web/' + FONT_FILENAME + '.woff', params = '-v ' + VERSION + ' -m ../source/AwamiNastaliq-WOFF-metadata.xml'),
    )

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl -I ../tools/bin/perllib ../tools/bin/awami_makegdl'
    ctx.env['FFCOPYGLYPHS'] = '../tools/bin/ffcopyglyphs.py'
    ctx.env['PDFSHAPED'] = 'perl ../tools/bin/pdfshaped.pl'
    ctx.find_program('ttfautohint')

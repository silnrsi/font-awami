#!/usr/bin/python
# Smith configuration file

#	This file is part of the Awami Nastaliq font 
#	(http://software.sil.org/awami) and is 
#	Copyright (c) 2014-2017 SIL International (http://www.sil.org/),
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

# set the font name, version, licensing and description
APPNAME='AwamiNastaliq Dev'
VERSION='1.010'
TTF_VERSION="1.010"
COPYRIGHT='Copyright (c) 2014-2017, SIL International (http:/www.sil.org)'
LICENSE='OFL.txt'

DESC_SHORT = "Smart Unicode font for the Nastaliq script"
DESC_LONG = """
Awami Nastaliq is a Nastaliq-style Arabic script font supporting a wide variety 
of languages of Southwest Asia, including but not limited to Urdu. This font 
is aimed at minority language support. This makes it unique among Nastaliq fonts.

Awami means "of the people", "of the common population" or "public". 

The Awami Nastaliq font does not provide complete coverage of all the characters 
defined in Unicode for Arabic script. Because the font style is specifically 
intended for languages using the Nastaliq style of southwest Asia, the character 
set for this font is aimed at those languages.

This font makes use of state-of-the-art font technologies to support complex 
typographic issues. Font smarts have been implemented using  Graphite only. We have 
no current plans to support OpenType.

One font from this typeface family is included in this release:
     * Awami Nastaliq Regular

Font sources are published in the repository and an open workflow is used for building, testing and releasing.
"""
DESC_NAME = "Awami-Nastaliq"
DEBPKG = 'fonts-awami'

# override tex for pdfs
testCommand('pdfs', cmd="${CMPTXTRENDER} -t ${SRC[0]} -e ${shaper} --outputtype=json -r ${SRC[1]} | ${PDFSHAPED} -s 16 -l 2.0 -o ${TGT} -f ${SRC[1]}",
                    ext='.pdf', shapers=1, supports=['.txt', '.ftml', '.xml'], replace=True)

FONT_NAME = "Awami Nastaliq Dev"
FONT_FILENAME = "AwamiNastaliq-Dev"

font(target = process(FONT_FILENAME + '.ttf', name(FONT_NAME, lang='en-US', subfamily=('Regular')),
				# remove buggy tables:
				cmd('ttftable -d hdmx,VDMX,LTSH ${DEP} ${TGT}'),
				# for removing psnames:
				########cmd('psfix -s ${DEP} ${TGT}'),
				# strip out bogus hints:
				cmd('ttfstriphints ${DEP} ${TGT}'),
				cmd('ttfsubset -s deva ${DEP} ${TGT}'),
        cmd('psfcompressgr ${DEP} ${TGT}'),
        cmd('typetuner -o ${TGT} add ${SRC} ${DEP}', "source/typetuner/feat_all.xml")
     		),
    source = "source/AwamiNastaliqRegular.ttf",
    graphite = gdl('awami.gdl', master = 'source/nastaliq_rules.gdl', params='-D -w3541 -w2504 -w4510',  ##### -c',
                    depends = glob.glob('*.gdh')),
    opentype = fea('source/simple.fea', no_make=1, no_test=True),
    ap = "source/AwamiNastaliqRegular_AP.xml",
    license = ofl('Awami','SIL'),
    copyright = COPYRIGHT,
    version = TTF_VERSION,
    ###typetuner = "source/typetuner/feat_all.xml",
    extra_srcs = ['tools/bin/awami_makegdl', 'tools/bin/ffcopyglyphs.py', 'tools/bin/perllib/Font/TTF/Scripts/GDL.pm'], ## 'DoulosSIL-R.ttf'],
    #tests = tests,
    fret = fret(params = '-r'),  # -b = show octaboxes
    woff = woff('web/' + FONT_FILENAME + '.woff', params = '-v ' + VERSION + ' -m ../source/AwamiNastaliq-WOFF-metadata.xml'),
    )

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl -I ../tools/bin/perllib ../tools/bin/awami_makegdl'
    ctx.env['FFCOPYGLYPHS'] = '../tools/bin/ffcopyglyphs.py'
    ctx.env['PDFSHAPED'] = 'perl ../tools/bin/pdfshaped.pl'


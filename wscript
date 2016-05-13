#!/usr/bin/python
# this is a smith configuration file

import glob

# set the default output folders
out="results"
DOCDIR="documentation"
OUTDIR="installers"
ZIPDIR="releases"
TESTDIR='tests'
# TESTRESULTSDIR = 'results/tests'
# STANDARDS = 'reference'

# set the font name, version, licensing and description
APPNAME='Awami'
VERSION='0.50'
TTF_VERSION="0.500"
COPYRIGHT='Copyright (c) 2014-2016, SIL International (http:/www.sil.org)'
LICENSE='OFL.txt'

DESC_SHORT = "Smart Unicode font for the Nastaliq script"
DESC_LONG = """
We are currently working on a Nastaliq-style font which will be called 
Awami Nastaliq.

Awami means "of the people", "of the common population" or "public". It is 
intended to be a font that can be used by a wide variety of languages of
Pakistan, including but not limited to Urdu.

The font will not cover the full Unicode Arabic repertoire. It will only 
support characters known to be used by languages in areas of the world using 
the Nastaliq style of Arabic script.

This font will make use of state-of-the-art font technologies to support complex 
typographic issues. Font smarts will be implemented using  Graphite only. We have 
no current plans to support OpenType.

One font from this typeface family will be included in this release:
     * Awami Nastaliq Regular

Font sources are published in the repository and an open workflow is used for building, testing and releasing.
"""
DESC_NAME = "Awami-Nastaliq"
DEBPKG = 'fonts-awami'

tests = fonttest(extras = {
            'pdf' : tests({
                'pdfs' : cmd("${CMPTXTRENDER} -t ${SRC[1]} -e ${shaper} --outputtype=json -r ${SRC[0]} | ${PDFSHAPED} -s 16 -l 2.0 -o ${TGT} -f ${SRC[0]}")
            }, ext=".pdf")})

FONT_NAME = "Awami Nastaliq Alpha2"
FONT_FILENAME = "Awami_alpha2.ttf"

font(target = process(FONT_FILENAME, name(FONT_NAME, lang='en-US', subfamily=('Regular'))),
     #source = create('temp/Awami_full.sfd',
     #            cmd("${FFCOPYGLYPHS} -i ../DoulosSIL-R.ttf -r 21..7E -f ${SRC} ${TGT}", ['Awami Nastaliq Regular.ttf'])),
     source = "Awami Nastaliq Regular.ttf",
     graphite = gdl('awami.gdl', master = 'nastaliq_rules.gdl', params='-D',
                    depends = glob.glob('*.gdh')),
     ap = "Awami Nastaliq Regular_tmp.xml",
     license = ofl('Awami','SIL'),
     copyright = COPYRIGHT,
     version = TTF_VERSION,
     extra_srcs = ['bin/awami_makegdl', 'bin/FFcopyGlyphs.py', 'bin/perllib/Font/TTF/Scripts/GDL.pm'], ## 'DoulosSIL-R.ttf'],
     tests = tests,
     fret = fret(params = '-r')
    )

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl -I ../bin/perllib ../bin/awami_makegdl'
    ctx.env['FFCOPYGLYPHS'] = '../bin/FFcopyGlyphs.py'
    ctx.env['PDFSHAPED'] = 'perl ../bin/pdfshaped.pl'

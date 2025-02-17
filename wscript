#!/usr/bin/python
# Smith configuration file

#	This file is part of the Awami Nastaliq font
#	(https://software.sil.org/awami) and is
#	Copyright (c) 2014-2024 SIL Global (https://www.sil.org/),
# with Reserved Font Names "Awami" and "SIL".
#
# This Font Software is licensed under the SIL Open Font License,
# Version 1.1.
#
#	You should have received a copy of the license along with this Font Software.
#	If this is not the case, go to (https://openfontlicense.org/) for all the
#	details including an FAQ.


import glob

# set the default output folders
out="results"
DOCDIR = ["documentation", "web"]
OUTDIR="installers"
ZIPDIR="releases"
TESTDIR='tests'
genout = "generated/"
# TESTSTRING=u'Hello World'
# TESTRESULTSDIR = 'results/tests'
# STANDARDS = 'reference'

# set package name
APPNAME='AwamiNastaliq'      #### AwamiNastaliq-Dev

# set the font family name
FAMILY='AwamiNastaliq'


DESC_NAME = "Awami-Nastaliq"
DEBPKG = 'fonts-awami'

# Get version info from Regular UFO; must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Regular' + '.ufo')

# smith project-specific options:
#   -d          - debug: do not run ttfsubset
#   --autohint  - autohint the font (otherwise hints are stripped)
#   --noPSnames - remove psf names
#   --regOnly   - build just Regular weight
opts = preprocess_args({'opt' : '-d'}, {'opt': '--autohint'}, {'opt': '--noPSnames'}, {'opt': '--regOnly'}, {'opt': '--boldOnly'})

# override tex for pdfs
testCommand('pdfs', cmd="${CMPTXTRENDER} -t ${SRC[0]} -e ${shaper} --outputtype=json -r ${SRC[1]} | ${PDFSHAPED} -s 16 -l 2.0 -o ${TGT} -f ${SRC[1]}",
                    ext='.pdf', shapers=1, supports=['.txt', '.ftml', '.xml'], replace=True)

#FONT_NAME = "Awami Nastaliq Dev"     #### Awami Nastaliq
#FONT_FILENAME = "AwamiNastaliq-Dev"  #### AwamiNastaliq-Regular

ftmlTest('tests/FTML_XSL/ftml-smith.xsl')

cmds = [
    #name('${DS:FILENAME_BASE}', lang='en-US', subfamily = 'Regular'),
    # remove buggy tables:
    cmd('ttftable -d hdmx,VDMX,LTSH ${DEP} ${TGT}'),
    cmd('${OCTALAP} -m ${SRC} -o ${TGT} ${DEP}', "source/graphite/octabox_${DS:FILENAME_BASE}.json"),
]

if '--noPSnames' in opts:
    cmds.append(cmd('psfix -s ${DEP} ${TGT}'))

if '-d' not in opts:
    cmds.append(cmd('ttfsubset -s deva ${DEP} ${TGT}'))

if '--autohint' in opts:
    cmds.append(cmd('${TTFAUTOHINT} -v -n -c  -D arab -W ${DEP} ${TGT}'))
else:
    # strip out bogus hints:
    cmds.extend([
        cmd('ttfstriphints ${DEP} ${TGT}'),
        # and add Google-recommended gasp and prep
        cmd('gftools fix-nonhinting --no-backup -q ${DEP} ${TGT}')
    ])

cmds.extend([
    cmd('psfcompressgr -q ${DEP} ${TGT}'),
    cmd('typetuner -o ${TGT} add ${SRC} ${DEP}', "source/typetuner/feat_all.xml")
])

if '--regOnly' in opts:
    INST = ['Awami Nastaliq Regular']
elif '--boldOnly' in opts:
    INST = ['Awami Nastaliq Bold']
else:
    INST = None
    
dspace_file = 'source/awami.designspace'

# iterate over designspace
designspace(dspace_file,
    # -W option resets weights to 400 and 700, for RIBBI fonts - we don't want that.
    instanceparams='-l ' + genout + '${DS:FILENAME_BASE}_createintance.log',
    instances = INST,
    target = process('${DS:FILENAME_BASE}.ttf', *cmds),
    ap = '${DS:FILENAME_BASE}_AP.xml',  # genout?
    version=VERSION,  # Needed to ensure dev information on version string

    graphite = gdl(genout + '${DS:FILENAME_BASE}.gdl',
    		master = 'source/graphite/master_${DS:FILENAME_BASE}.gdl',
    		params='-D -w3541 -w2504 -w4510 -e gdlerr_${DS:FILENAME_BASE}.txt',  ##### -c',
        depends = glob.glob('*.gdh')),
    
    opentype = fea('source/simple.fea', no_make=1, no_test=True),
    #typetuner = typetuner("source/typetuner/feat_all.xml"),
    #classes = 'source/classes.xml',
    #script='arab',
    pdf=fret(params = '-r -b'),     # -b = show octaboxes
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
        cmd='psfwoffit -m ${SRC[1]} --woff ${TGT} --woff2 ${TGT}2 ${SRC[0]}'
        ),

    #woff=woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/${FAMILY}-WOFF-metadata.xml'),
    )

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl -I ../tools/bin/perllib ../tools/bin/awami_makegdl'
    ctx.env['FFCOPYGLYPHS'] = '../tools/bin/ffcopyglyphs.py'
    ctx.env['PDFSHAPED'] = 'perl ../tools/bin/pdfshaped.pl'
    ctx.find_program('ttfautohint')
    ctx.env['FRET'] = 'perl ../tools/bin/fret'
    ctx.find_program('octalap')

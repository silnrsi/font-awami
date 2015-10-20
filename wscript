#!/usr/bin/python

import glob

COPYRIGHT='Copyright 2015, SIL International. All rights reserved.'
APPNAME='Awami'
VERSION='0.1'

tests = fonttest(extras = {
            'pdf' : tests({
                'pdfs' : cmd("${CMPTXTRENDER} -t ${SRC[1]} -e ${shaper} --outputtype=json -r ${SRC[0]} | ${PDFSHAPED} -s 16 -l 2.0 -o ${TGT} -f ${SRC[0]}")
            }, ext=".pdf")})


font(target = 'Awami_test.ttf',
     source = create('temp/Awami_full.sfd',
                cmd("${FFCOPYGLYPHS} -i ../DoulosSIL-R.ttf -r 21..7E -f ${SRC} ${TGT}", ['Awami Nastaliq Regular.ttf'])),
     graphite = gdl('awami.gdl', master = 'nastaliq_rules.gdl', params='-D -c',
                    depends = glob.glob('*.gdh')),
     ap = "Awami Nastaliq Regular_tmp.xml",
     license = ofl(file='OFL.txt'),
     copyright = COPYRIGHT,
     extra_srcs = ['bin/awami_makegdl', 'bin/FFcopyGlyphs.py', 'bin/perllib/Font/TTF/Scripts/GDL.pm', 'DoulosSIL-R.ttf'],
     tests = tests
    )

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl -I ../bin/perllib ../bin/awami_makegdl'
    ctx.env['FFCOPYGLYPHS'] = '../bin/FFcopyGlyphs.py'
    ctx.env['PDFSHAPED'] = 'perl ../bin/pdfshaped.pl'

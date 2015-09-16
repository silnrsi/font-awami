import glob

font(target = 'Awami_test.ttf',
     source = create('temp/Awami_full.sfd',
                cmd("${FFCOPYGLYPHS} -i ../DoulosSIL-R.ttf -r 21..7E -f ${SRC} ${TGT}", ['Awami Nastaliq Regular.ttf'])),
     graphite = gdl('awami.gdl', master = 'nastaliq_rules.gdl', params='-D',
                    depends = glob.glob('*.gdh')),
     ap = "Awami Nastaliq Regular_tmp.xml",
     license = ofl("Awami")
    )

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl -I ../bin/perllib ../bin/awami_makegdl'
    ctx.env['FFCOPYGLYPHS'] = '../bin/FFcopyGlyphs.py'

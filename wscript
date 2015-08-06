font(target = 'Awami_test.ttf',
     source = 'Awami Nastaliq Regular.ttf',
     graphite = gdl('awami.gdl', master = 'nastaliq_rules.gdl', params='-D'),
     ap = "Awami Nastaliq Regular_tmp.xml",
    )

def configure(ctx) :
    ctx.env['MAKE_GDL'] = 'perl -I ../bin/perllib ../bin/awami_makegdl'

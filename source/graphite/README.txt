source/graphite/README.txt
==================

This file describes the Graphite source files included with the Awami Nastaliq
font family. This information should be distributed along with the Awami Nastaliq
fonts and any derivative works.

These files are part of Awami Nastaliq font family (https://software.sil.org/awami/) 
and are Copyright (c) 2014-2025, SIL Global (https://www.sil.org/),
with Reserved Font Names "Awami" and "SIL".

This Font Software is licensed under the SIL Open Font License, Version 1.1.

You should have received a copy of the license along with this Font Software.
If this is not the case, go to (https://openfontlicense.org/) for all the
details including an FAQ.

nastaliq_rules.gdl      Master GDL file; includes all the others

cp1252.gdl         Rules for Roman characters within codepage 1252

latin_awami.gdh	Graphite classes for Latin characters

nastaliq_classes.gdh	Graphite classes for Awami beyond the basic ones

nastaliq_cntxlClasses.gdh	Graphite classes for initial, medial, and final forms

nastaliq_complexShapes.gdh	This file contains a single class of glyphs that need extra octabox 
										metrics to handle their complex (concave) shape.
										This allows collision fixing to be adequately smart.
nastaliq_positioning.gdh	Graphite positioning rules for Awami Nastaliq

nastaliq_separateNuqtas.gdh	Graphite rules to separate base forms from nuqtas (keeping the nuqtas in the glyph stream)

nastaliq_shaping.gdh	Graphite substitution rules for Awami Nastaliq

octabox.json	Used in wscript. See octalap.md in documentation folder
---
title: Awami Nastaliq Developer Documentation
fontversion: 3.200
---

# Naming Conventions

## Class names

Identifiers starting with ‘c’ generally indicate a class. Those starting with ‘cs’ are classes used for substitution, and the elements of the class must match its corresponding class.

## Glyph names

The names of glyphs in the UFO are of the form: \<script\>\<Base\>\<Seq-position\>.\<interface\>\_\<other\>

- The \<script\> is usually “abs”, except when we are using Urdu character names, in which case it is “nlq” (eg, nlqChotiyeh). The script is omitted for glyphs that don’t represent characters, such as those that are only intended for attachment or to be used in compositions.
- The \<Base\> is the character name, such as “Jeem” or “Seen.” (Note the use of “Keheh” and “Kaf” mentioned below.)
- \<Seq-position\> is “Ini”, “Med”, “Fin”, or missing for isolate forms.
- \<interface\> indicates the interface the glyph uses, as described above.
- \<other\> indicates an alternate form, as described above.

The corresponding GDL names are of the form: g\<Base\>\<Seq-position\>\<Interface\>\_\<other\>.

For instance:

- absMeemIni.jm  => gMeemIniJm
- absSeenMed.bere => gSeenMedBeRe
- absKehehMed.benn_base => gKafMedBeNn_base
- nlqBariyehFin => gBariyehFin

Note that we use “Keheh” in the UFO, since these are generally what the Unicode names use, but “Kaf” for the corresponding Graphite glyph names. Why? Because I first learned the name as “kaf” and that’s what I got used to :-) but our team policy is to use Unicode names for our glyph names wherever feasible.

There is a special form of the **makegdl** script called **awami_makegdl** that generates these glyph names. The awami_makegdl script sets a variable called `awami_names` to true. There is also a special form of **gdl.pm** Perl file that tests this variable and does special transformations that are Awami-specific. [ABS-1306]

--------

<< Previous: [Alternating Beh Teeth](dev04_behteeth.md) | [Introduction and Index](dev01_intro.md) | Next: [Passes and Processing](dev06_passes.md) >>

<!-- PRODUCT SITE ONLY
[font id='awami' face='AwamiNastaliq-Regular' size='150%' rtl=1]
[font id='awamiL' face='AwamiNastaliq-Regular' size='150%' ltr=1]
-->

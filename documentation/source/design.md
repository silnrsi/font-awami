---
title: Awami Nastaliq - Design
fontversion: 3.000
---

Nastaliq style Arabic is one of the most complex forms of writing in the world, and standard font technologies are not quite up to the challenge of handling its sloping, calligraphic form. For this reason, SIL's smart-font technology, [Graphite](http://graphite.sil.org), has been extended with some special capabilities to address the particular challenges of this beautiful but complicated form of writing.

The sloping nature of Nastaliq creates a great challenge: glyph collisions. A straightforward, naive layout of base glyphs, nuqtas, and diacritics will inevitably result in a rendering where the glyphs collide, forming ugly and even unreadable text. Fixing these collisions is exacerbated by the large number of glyphs and the complex positioning created by the sloping baseline.

Workarounds to current font technologies have been used to create Urdu-specific fonts, but these approaches do not scale well when multiple languages and a variety of diacritics are needed. For this reason, SIL International has developed Awami Nastaliq, specifically intended to support lesser-known languages of South Asia (using an extended version of Graphite). While there are several fonts that support Urdu, this is the first Nastaliq-style font that supports a wide variety of lesser-known languages. 

Awami Nastaliq is a Nastaliq-style Arabic script font supporting a wide variety of languages of South Asia, including but not limited to Urdu. Lesser-known languages often require more vowel diacritics than Urdu. They may use a different set of base characters and diacritics, and the base characters often include more nuqtas to represent sounds that are not present in Urdu or standard Arabic. This font includes all the vowel diacritics and base characters (that we are aware of) required for languages using the Nastaliq style of Arabic script.

Five fonts from this typeface family are included in this release:
      
- Awami Nastaliq Regular
- Awami Nastaliq Medium
- Awami Nastaliq SemiBold
- Awami Nastaliq Bold
- Awami Nastaliq ExtraBold

More detailed design information is available from [What is Special About Awami Nastaliq](http://software.sil.org/awami/what-is-special/)? 

## Type Samples

Type samples showing some of the inventory of glyphs can be found here: 
[Awami Nastaliq Type Sample](sample.md).

Examples of some text is shown below. 

![Lateef Sample - Seven weights](assets/images/AwamiWeights.png){.fullsize}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/lateef/wp-content/uploads/sites/30/2022/06/AwamiWeights.png -->
<figcaption>Awami Nastaliq Sample - Five weights</figcaption>


![Awami Nastaliq Sample - Genesis 11](assets/images/AwamiUrduGen11.png){.fullsize}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2021/01/AwamiUrduGen11.png -->
<figcaption>Awami Nastaliq Sample - Genesis 11</figcaption>

## Character Set

For a complete list of characters included in Awami Nastaliq, see [Character Set Support](charset.md).

## Rendering the Allah ligature

In certain types of literature, the name *Allah* and words related to this name are given unique rendering. For a list of the rendering rules, see [Rendering the Allah ligature](allah.md).

## Automatic collision-fixing

To solve the problem of collisions, we have enhanced Graphite with an automatic collision-fixing capability. The Graphite engine makes use of a simplified form of the rendered glyphs to detect collisions, shift nuqtas and diacritics, and add kerning to create nicely laid-out text. Besides fixing collisions, the shape-based kerning mechanism can also create diagonal overlaps in the sloping text, as Nastaliq is traditionally written. 

## Vowel diacritical marks

Few Nastaliq style fonts handle vowel marks well. This is acceptable for Urdu, but not for other languages, such as Saraiki and Marwari, that make more extensive use of vowel marks. Awami Nastaliq provides good support for the vowel marks often used by other languages.

## User-selectable Font Features

Alternate glyphs that are available through features are demonstrated in the [Features](features.md) document. 

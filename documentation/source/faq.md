---
title: Awami Nastaliq - Frequently Asked Questions
fontversion: 3.400
---

Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](https://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [The SIL Open Font License (OFL-FAQ)](https://openfontlicense.org/ofl-faq/)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.

A generic FAQ for all of our Arabic scripts fonts can be found here: [Arabic Fonts - FAQ](https://software.sil.org/arabicfonts/support/faq/). FAQ's specific to Scheherazade New are found below.

### Problems with Bold weights

#### *Why does my application not show the Bold weight in font menus and dialogs?*

Some applications will list all the weights but leave out Bold. To access the Bold you need to choose Regular and turn on Bold using the application's UI controls such as a "B" button.

#### *Why do I sometimes get a fake Bold?*

If you choose a weight other than Regular (such as ExtraLight), then use application controls to turn on Bold, some applications will make a "fake" Bold rather than use one of the real ones in the font (Medium, SemiBold, Bold, ExtraBold). This is because only Regular has an associated Bold counterpart. This is a technical limitation with some apps and OSes. If you are using some other weight than Regular for text and want to make a word or phrase stand out you will need to select the text and apply one of the heavier weights manually. 

### *What is so special about Awami Nastaliq?*

This is the very first Nastaliq-style font with support for a wide range of languages, made possible by a flexible technology. This is the only freely-available font to provide an authentic Nastaliq style with kerned calligraphic segments. 

This font is designed to work with the [Graphite](https://graphite.sil.org) advanced font technology. To take advantage of the advanced typographic capabilities of this font, you must be using applications that provide an adequate level of support for Graphite. These advanced capabilities provide access to the variant character forms used in some languages. See [Font features](features.md) and [What is Special About Awami Nastaliq? ](https://software.sil.org/awami/what-is-special/)

### *What does Awami mean?*

Awami is an Urdu word meaning “of the people”, “of the common population” or “public”. Awami Nastaliq is an Arabic script font specifically intended for a wide variety of languages using the Nastaliq style of South Asia.

### *What characters are included with this release?*

See [Character set support](charset.md) for the full listing.

### *I notice that Awami Nastaliq is missing a number of characters that I would like. Will you add these?*

It is impossible for us to add every glyph that every person desires, but we do place a high priority on adding complete coverage of all the characters defined in Unicode for languages that use the Nastaliq style of Arabic script (excluding the Arabic Presentation Forms blocks, which are not recommended for normal use). You can send us your requests, but please understand that we are unlikely to add symbols where the user base is very small, unless they have been accepted into Unicode.

### *Why isn't this font shaping properly in Microsoft Word or in InDesign?*

We have only implemented this font using the Graphite technology. You *must* be using applications which support Graphite in order to get the shaping. Please see the [Resources](resources.md) page.

### *Why have you only implemented this font in Graphite?*

(1) Graphite's basic positioning mechanisms are more powerful than OpenType's; but more importantly (2) Nastaliq makes extensive use of Graphite's automatic collision avoidance; and also (3) Graphite has more powerful development tools. 

Should OpenType engines gain the necessary collision avoidance support, then we would probably add OpenType support to Awami Nastaliq.

### *Awami Nastaliq does not have proper spacing or collision avoidance in XeTeX. How can I get the promised collision avoidance?*

There is a special new parameter in XeTeX to support the new Graphite collision avoidance. See [Resources](resources.md) for help in getting that working.


### *Why isn't Awami Nastaliq working in XeLaTeX?*

Awami Nastaliq is a Graphite font. For OpenType fonts the font declaration would be:
```
\newfontfamily\fontnast[Script=Arabic]{Jameel Noori Nastaleeq}
```

However, because this is a Graphite font, you need a different declaration:
```
\newfontfamily\urdufont[Renderer=Graphite]{Awami Nastaliq}
```

It would also be useful to add `\XeTeXinterwordspaceshaping=1` to your file. Thus, you might have:
```
\XeTeXinterwordspaceshaping=1
\newfontfamily\urdufont[Renderer=Graphite]{Awami Nastaliq}
```

### *Why doesn't Awami Nastaliq use AGL (Adobe Glyph List) names? I cannot copy and paste from a pdf using Awami Nastaliq into another document. There is a lot of gibberish.*

In order to dynamically position the dots above and below the corresponding base forms, Awami Nastaliq separates the patterns of dots into their own nuqta glyphs. These nuqta glyphs have no possible AGL name because they do not correspond to any Unicode character. Therefore it is never going to be possible to extract a corresponding Unicode text stream from a sequence of Awami Nastaliq glyph names.

This does not mean it is impossible to copy and paste from a PDF. High quality PDF creation software will include the Unicode character text stream within the document, which makes copy and paste work regardless of the glyph names used by the font.


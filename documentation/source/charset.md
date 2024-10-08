---
title: Awami Nastaliq - Character Set Support
fontversion: 3.300
---

The Awami Nastaliq font does not provide complete coverage of all the characters defined in Unicode for Arabic script. Because the font style is specifically intended for languages using the Nastaliq style of Arabic script, the character set for this font is aimed at supporting those languages.

[Arabic (U+0600..U+06FF)](https://www.unicode.org/charts/PDF/U0600.pdf) was added to Unicode 1.0. [Arabic Supplement (U+0750..U+077F)](https://www.unicode.org/charts/PDF/U0750.pdf) was added to Unicode 4.1, [Arabic Extended-A (U+08A0..U+08FF)](https://www.unicode.org/charts/PDF/U08A0.pdf) was added to Unicode 6.1, [Arabic Extended-B (U+0870..U+089F)](https://www.unicode.org/charts/PDF/U0870.pdf) was added to Unicode 14.0, and [Arabic Extended-C (U+10EC0..U+10EFF)](https://www.unicode.org/charts/PDF/U10EC0.pdf) was added to Unicode 15.0. There are still some Arabic script characters being added to Unicode, so it is possible that not all languages using the Arabic script are fully represented in Unicode. 

## Supported characters

The following character ranges are supported by this font:

Unicode block | Awami Nastaliq support
------------- | ---------------
Arabic 	| ✓ except for 0605..0608, 0616..061C, 061D..061E, 063B..0640, 065C..065D, 0676..0678, 067F..0680, 0682, 068C..068D, 068F, 0692, 069C..069D, 069F, 06A2..06A3, 06A6..06A8, 06AA, 06AC, 06AE, 06B2, 06B4, 06B6, 06B8, 06BF, 06D1, 06D6..06DB, 06DE..06DF, 06E2..06E9, 06EB..06EC, 06EE..06EF, 06FA, 06FC..06FF
Arabic Supplement | ✓ except for 0750..0758, 075B, 075D..0761, 0764..0767
Arabic Extended-A | ✓ only includes 08C7, 08C8, 08F7, 08FF
Arabic Extended-B | ✗ 
Arabic Extended-C | ✓ only includes 10ED0 (a provisional codepoint in the Unicode pipeline)
Arabic Presentation Forms-A | ✓ only includes FD3E..FD3F, FD40..FD45, FD47..FD49, FD4D, FD90..FD91 (provisional codepoints in the Unicode pipeline), FDCF, FDF2, FDFA..FDFE
Arabic Presentation Forms-B | ✓ only includes FBC6..FBC7 (provisional codepoints in the Unicode pipeline)
Codepage 1252 (Western)¹ | ✓

A selection of characters from the General Punctuation block, such as various-sized spaces, are also supported; a utility such as <a href="https://scripts.sil.org/ViewGlyph_home">SIL ViewGlyph</a> can be used to examine the exact repertoire of this font. 

¹Inclusion of basic Latin repertoire is provided as a convenience, e.g., for use in menus or for displaying markup in text files; these fonts are not intended for extensive Latin script use.


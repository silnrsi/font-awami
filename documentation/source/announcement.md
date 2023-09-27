---
title: Awami Nastaliq - Announcement
fontversion: 3.200
---

This is a maintenance release of Awami Nastaliq.

### Changes

#### Improved
- Fixed bug in dot removal for YEH followed by COMBINING Hamza
- Fixed some minor kerning/collision/spacing bugs
- Changed shape of mark on 06C7 (Arabic U) to look like a comma instead of a pesh
- Created bold forms of the honorifics
- Changed PUA codepoint U+E003 to U+FD47 ARABIC LIGATURE ALAYHI AS-SALAAM

#### New
- Added six characters:
	- U+06A0 ARABIC LETTER AIN WITH THREE DOTS ABOVE ??? ABS-2702
	- U+06AD ARABIC LETTER N
  - U+06BD ARABIC LETTER NOON WITH THREE DOTS ABOVE
  - U+0762 ARABIC LETTER KEHEH WITH DOT ABOVE
  - U+FDCF ARABIC LIGATURE SALAAMUHU ALAYNAA
  - U+10ED0 ARABIC BIBLICAL END OF VERSE (this character is not officially in Unicode, it is in the pipeline for Unicode 16.0)

Both desktop and web fonts are provided in a single, all-platforms package on the [Download Page](https://software.sil.org/awami/download/).

### Known issues

- U+10ED0 ARABIC BIBLICAL END OF VERSE is not officially in Unicode. The codepoint *could* still change.
- U+E003 was a PUA codepoint. We have reencoded it to the proper codepoint at U+FD47 ARABIC LIGATURE ALAYHI AS-SALAAM. If the PUA codepoint U+E003 was used, it should be replaced by U+FD47.



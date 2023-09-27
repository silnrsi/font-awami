---
title: Awami Nastaliq Developer Documentation
fontversion: 3.200
---

# The Glyph Set

As is typical with Arabic script, each character can be thought of as belonging to a class of characters with a similar base shape. For instance, jeem, hah, khah, and tcheh form a class, seen and sheen form a class, etc. In Awami (and most Nastaliq fonts) this is more important than normal because the rendering process involves separating the nuqtas from the base characters, laying out the bases, and positioning the nuqtas appropriately. This happens for all forms except the isolates.

This decomposition approach has two advantages. Since roughly 50 glyphs are needed for every dual-connecting base form, this allows characters in the same class to share all these glyphs, which greatly reduces the number of glyphs required. It also allows nuqtas to be adjusted separately in order to avoid collisions.

For the rest of this discussion, we will simply use the primary character to represent glyphs of the entire class. So “beh” is assumed to include teh, theh, peh, initial/medial noon and yeh, and similar characters. “Seen” includes sheen and variants. “Jeem” includes hah, khah, tcheh, dyeh, etc.

--------

[Introduction and Index](dev01_intro.md) | Next: [Glyph Interfaces and Suffixes](dev03_interfaces.md) >>


<!-- PRODUCT SITE ONLY
[font id='awami' face='AwamiNastaliq-Regular' size='150%' rtl=1]
[font id='awamiL' face='AwamiNastaliq-Regular' size='150%' ltr=1]
-->

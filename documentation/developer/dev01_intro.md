---
title: Awami Nastaliq Developer Documentation
fontversion: 3.200
---

# Intro

The Awami Nastaliq font is designed to support the Nastaliq style of Arabic script for a wide variety of languages, particularly those used in Pakistan, that require the Nastaliq style. This sloping, calligraphic style has a variety of complexities that make rendering especially challenging. The sloping baseline in particular makes it difficult to predict and fix collisions, since there is no way to know the vertical position of any glyph before run-time when the full context of the glyph is known. Therefore Awami makes extensive use of Graphite’s automatic collision fixing algorithm both for adjustment of nuqta and diacritic positioning and for kerning.

Supporting a wide variety of languages in the Nastaliq style is particularly difficult using OpenType, and for this reason, Awami is implemented only using Graphite.  

Arabic is always written in a cursive style and Nastaliq is no exception. So every rendering operation involves either an isolate or a sequence of connected characters ending with a final form. Rendering an isolate is fairly trivial; the complications arise from constructing the contextual sequences.

A phenomenon that shows up in various ways in Nastaliq rendering is the necessity for backwards logic. The forms at the end of a sequence of characters influence the preceding characters more than the other way around. For this reason Nastaliq shaping must be run backwards, starting with the last character in a contextual chain. On the other hand, there are aspects of positioning that must happen in a forward direction.

*Assumptions:* This documentation assumes familiarity with Arabic script, behavior, and character names. It also assumes knowledge of Graphite, GDL, and Graphite's collision avoidance mechanism.


### Contents
- [The Glyph Set](dev02_glyphset.md) &#x2013; Overview of how the glyphs are organized
- [Glyph Interfaces and Suffixes](dev03_interfaces.md) &#x2013; How the glyphs connect
	- [Interface Graphics](dev03a_interfaceimages.md)  &#x2013; Graphical images for the main interfaces
- [Alternating Beh Teeth](dev04_behteeth.md) &#x2013; Special forms needed for sequences of beh, teh, theh, peh, noon, and yeh
- [Naming Conventions](dev05_namingconv.md) &#x2013; Classes and glyphs
- [Passes and Processing](dev06_passes.md) &#x2013; Summary of what each pass performs
- [Collision Fixing](dev07_collision.md)
- [Kerning and Overlaps](dev08_kerning.md)
- [Alternate Height Kafs and Gafs](dev09_altkafs.md)
- [Short Finals](dev10_shortfinals.md)
- [Testing](dev11_testing.md)

<!-- PRODUCT SITE ONLY
[font id='awami' face='AwamiNastaliq-Regular' size='150%' rtl=1]
[font id='awamiL' face='AwamiNastaliq-Regular' size='150%' ltr=1]
-->

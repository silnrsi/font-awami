---
title: Awami Preview B - Font Features
fontversion: 0.900
---

Awami is a TrueType font with smart font capabilities added using the OpenType font technology. The font includes a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The chart below enumerates the details of these features. Whether these features are available to users will depend on the application being used. For applications that do not make use of the OpenType Character Variants, you can now download fonts customized with the variant glyphs you choose. Read this document, visit [TypeTuner Web](https://typetunerweb.languagetechnology.org/ttw/fonts2go.cgi), then choose the variants and download your font. **This version of the font does not yet contain support for TypeTuner.**

See [Using Font Features](https://software.sil.org/fonts/features/). Although that page is not targeted at Arabic script support, it does provide a comprehensive list of applications that make full use of both the OpenType and Graphite font technologies.

See also [Arabic Fonts — Application Support](https://software.sil.org/arabicfonts/support/application-support/). It provides a fairly comprehensive list of applications that make full use of the [Graphite](https://graphite.sil.org) font technology.

This page uses web fonts (WOFF) to demonstrate font features. However, it will only display correctly in Mozilla Firefox. For a more concise example of how to use Awami as a web font see *AwamiNastaliq-webfont-example.html* in the font package web folder. 

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Complete feature list

### Language system tags

<span class='affects'>Affects: U+0623, U+0624, U+0626, U+0654, U+0655, U+0675, U+0681, U+06B5, U+06C2, U+06D3, U+076C</span>

Unfortunately, the UI needed to access the language-specific behavior is not yet present in many applications. LibreOffice supports language-specific behavior for Kashmiri and Malay. Some Harfbuzz-based apps, e.g., XeTeX, can access language-specific behavior. 

#### Kashmiri, Malay

Language | hamza | 0674 | Feature setting
:--      | ----: | ----: | :---
default | <span dir="rtl" class='awami-R normal' >&#x0623;&#x0020;&#x0624;&#x0020;&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020;&#x0628;&#x0654;&#x0020;&#x0628;&#x0655;&#x0020;&#x0675;&#x0020;&#x0681;&#x0020;&#x0681;&#x0681;&#x0681;&#x0020;&#x06C2;&#x0020;&#x06C2;&#x06C2;&#x06C2;&#x0020;&#x06D3;&#x0020;&#x076C;</span> |<span dir="rtl" class='awami-R normal'>&#x0627;&#x0674;</span> |
Kashmiri | <span dir="rtl" class='awami-R normal' lang='ks' style="color:red">&#x0623;&#x0020;&#x0624;&#x0020;&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020;&#x0628;&#x0654;&#x0020;&#x0628;&#x0655;&#x0020;&#x0675;&#x0020;&#x0681;&#x0020;&#x0681;&#x0681;&#x0681;&#x0020;&#x06C2;&#x0020;&#x06C2;&#x06C2;&#x06C2;&#x0020;&#x06D3;&#x0020;&#x076C;</span> |<span dir="rtl" class='awami-R normal' lang='ks'>&#x0627;&#x0674;</span> | `lang='ks'`
Malay | <span dir="rtl" class='awami-R normal' lang='ms' style="color:red">&#x0623;&#x0020;&#x0624;&#x0020;&#x0626;&#x0020;&#x0626;&#x0626;&#x0626;&#x0020;&#x0628;&#x0654;&#x0020;&#x0628;&#x0655;&#x0020;&#x0675;&#x0020;&#x0681;&#x0020;&#x0681;&#x0681;&#x0681;&#x0020;&#x06C2;&#x0020;&#x06C2;&#x06C2;&#x06C2;&#x0020;&#x06D3;&#x0020;&#x076C;</span> |<span dir="rtl" class='awami-R normal' lang='ms' style="color:red">&#x0627;&#x0674;</span> | `lang='ms'`

### Character variants

There are some character shape differences in different languages which use the Arabic script. These can be accessed by using OpenType character variants.  

Unless otherwise indicated, the first feature in a table is the default.

#### Lam-V alternate 

<span class='affects'>Affects: U+06B5</span>

Feature | Sample | Feature setting
---- | ------: | :----
V over bowl | <span dir="rtl" class='awami-R normal'><font color="red">&#x6B5;</font> &#x6B5;&#x628;&#x6B5;&#x628;<font color="red">&#x6B5;</font></span>| `cv43=0`
V over stem | <span dir="rtl" class='awami-R normal' style='font-feature-settings: "cv43" 1'><font color="red">&#x6B5;</font> &#x6B5;&#x628;&#x6B5;&#x628;<font color="red">&#x6B5;</font></span>| `cv43=1`

#### Arabic-style hamza 

<span class='affects'>Affects: U+0623, U+0624, U+0626, U+0654, U+0655, U+0675, U+0681, U+06C2, U+06D3, U+076C </span>

Feature | Sample | Feature setting
---- | ---------------: | :----
Urdu style | <span dir="rtl" class='awami-R normal'>ء أ ؤ بؤ إ ۂ بۂ ۓ بۓ ٵ ݬ بݬ ځ بځ بځب بٔ بٕ</span>| `cv55=0`
Arabic style | <span dir="rtl" class='awami-R normal' style='font-feature-settings: "cv55" 1'>ء أ ؤ بؤ إ ۂ بۂ ۓ بۓ ٵ ݬ بݬ ځ بځ بځب بٔ بٕ</span>| `cv55=1`

#### High-hamza alternate

<span class='affects'>Affects: U+0674 </span>

Feature | Sample | Feature setting
---- | ---------------: | :----
Urdu style | <span dir="rtl" class='awami-R normal'>&#x0674;</span>| `cv56=0`
Malay style | <span dir="rtl" class='awami-R normal' style='font-feature-settings: "cv56" 1'>&#x0674;</span>| `cv56=1`


#### Full-stop alternate 

<span class='affects'>Affects: U+06D4</span>

Feature | Sample | Feature setting
---- | ------: | :---- 
Dash | <span dir="rtl" class='awami-R normal'>&#x62c;&#x62c;&#x62c;<font color="red">&#x6d4;</font></span>| `cv85=0`
Dot | <span dir="rtl" class='awami-R normal' style='font-feature-settings: "cv85" 1'>&#x62c;&#x62c;&#x62c;<font color="red">&#x6d4;</font></span>| `cv85=1`

#### Arabic- or Latin-style punctuation 

<span class='affects'>Affects: U+0021, U+0022, U+0027, U+0028, U+0029, U+002A, U+002B, U+002D, U+002F, U+003A, U+003C, U+003D, U+003E, U+005B, U+005C, U+005D, U+007B, U+007C, U+007D, U+00AB, U+00AD, U+00B1, U+00B7, U+00BB, U+00D7, U+2004, U+2010, U+2011, U+2012, U+2013, U+2014, U+2015, U+2018, U+2019, U+201A, U+201C, U+201D, U+201E, U+2022, U+2025, U+2026, U+2027, U+2030, U+2039, U+203A, U+2212, U+2219</span>

Default uses Arabic-style punctuation for right-to-left segments and Latin-style for left-to-right segments

Feature | Sample | Feature setting
---- | ---------------: | :---- 
Default | <span dir="rtl" class='awami-R normal'>! " ' ( ) * + - / :  [ \ ] { } « ­ ± · » ×   ‐ ‑ ‒ – — ― ‘ ’ ‚ “ ” „ • ‥ … ‧ ‰ ‹ › − ∙ </span>| `cv86=0`
Arabic | <span dir="rtl" class='awami-R normal' style='font-feature-settings: "cv86" 1'>! " ' ( ) * + - / :  [ \ ] { } « ­ ± · » ×   ‐ ‑ ‒ – — ― ‘ ’ ‚ “ ” „ • ‥ … ‧ ‰ ‹ › − ∙ </span> | `cv86=1`
Latin | <span dir="rtl" class='awami-R normal' style='font-feature-settings: "cv86" 2'>! " ' ( ) * + - / :  [ \ ] { } « ­ ± · » ×   ‐ ‑ ‒ – — ― ‘ ’ ‚ “ ” „ • ‥ … ‧ ‰ ‹ › − ∙ </span>| `cv86=2`

## End of Ayah and Subtending marks

*This is not technically a feature, but we find it useful to demonstrate the use of these characters.*

These Arabic characters are intended to enclose or hold one or more digits. 

Firefox allows you to use U+06DD followed by the digits and proper rendering occurs. However, surrounding the sequence with U+202D and U+202C seems to give the most reliable results in different browsers, and so this font requires those characters in order to display properly.

Specific technical details of how to use them are discussed in the [Arabic fonts FAQ -- Subtending marks](https://software.sil.org/arabicfonts/support/faq#Ayah).

Character | Sample  
------------- | ---------------: 
U+06DD ARABIC END OF AYAH<br>(U+202D U+06DD U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x6DD;&#x6F1;&#x6F2;&#x6F3;&#x202C; &#x202D;&#x6DD;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x6DD;&#x6F1;&#x202C;</span>
U+0600 ARABIC NUMBER SIGN<br>(U+202D U+0600 U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x600;&#x6F1;&#x6F2;&#x6F3;&#x202C; &#x202D;&#x600;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x600;&#x6F1;&#x202C;</span>
U+0601 ARABIC SIGN SANAH (year)<br>(U+202D U+0601 U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x601;&#x6F1;&#x6F9;&#x6F3;&#x6F2;&#x202C;</span>
U+0602 ARABIC FOOTNOTE MARKER<br>(U+202D U+0602 U+06F1 U+06F2 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x602;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x602;&#x6F1;&#x202C;</span>
U+0603 ARABIC SIGN SAFHA (page)<br>(U+202D U+0603 U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x603;&#x6F1;&#x6F2;&#x6F3;&#x202C; &#x202D;&#x603;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x603;&#x6F1;&#x202C;</span>
U+0604 ARABIC SIGN SAMVAT (Samvat era dates in Urdu)<br>(U+202D U+0604 U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x604;&#x6F1;&#x6F2;&#x6F3;&#x6F4;&#x202C; &#x202D;&#x604;&#x6F1;&#x6F2;&#x6F3;&#x202C; &#x202D;&#x604;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x604;&#x6F1;&#x202C; </span>



## Paragraph of text

This sentence comes from the [Saraiki UDHR](https://www.unicode.org/udhr/d/udhr_skr.txt). 

Sample  | Feature setting
---------------: | :---- 
<span dir="rtl" class='awami-R normal'> &#x627;&#x642;&#x648;&#x627;&#x645;&#x20;&#x645;&#x62a;&#x62d;&#x62f;&#x6c1;&#x20;&#x646;&#x6d2;&#x20;&#x6c1;&#x631;&#x20;&#x6a9;&#x6c1;&#x6cc;&#x6ba;&#x20;&#x62f;&#x6d2;&#x20;&#x62d;&#x642;&#x648;&#x642;&#x20;&#x62f;&#x6cc;&#x20;&#x62d;&#x641;&#x627;&#x638;&#x62a;&#x20;&#x62a;&#x6d2;&#x20;&#x648;&#x62f;&#x6be;&#x627;&#x631;&#x6d2;&#x20;&#x62f;&#x627;&#x20;&#x62c;&#x6be;&#x646;&#x688;&#x627;&#x20;&#x627;&#x686;&#x627;&#x631;&#x20;&#x6a9;&#x6be;&#x6bb;&#x20;&#x62f;&#x627;&#x20;&#x627;&#x631;&#x627;&#x62f;&#x6c1;&#x20;&#x6a9;&#x6cc;&#x62a;&#x627;&#x20;&#x6c1;&#x648;&#x6d2;&#x6d4;&#x20;&#x627;&#x6cc;&#x6c1;&#x648;&#x20;&#x684;<font color="red">&#x626;</font>&#x6d2;&#x20;&#x648;&#x20;&#x62d;&#x634;&#x6cc;&#x627;&#x646;&#x6c1;&#x20;&#x6a9;&#x645;&#x627;&#x6ba;&#x20;&#x62f;&#x6cc;&#x20;&#x635;&#x648;&#x631;&#x62a;&#x20;&#x648;&#x686;&#x20;&#x638;&#x627;&#x6c1;&#x631;&#x20;&#x62a;&#x6be;<font color="red">&#x626;</font>&#x6cc;&#x20;&#x6c1;&#x6d2;</span>|`cv55=0`
<span dir="rtl" class='awami-R normal' style='font-feature-settings: "cv55" 1'>  &#x627;&#x642;&#x648;&#x627;&#x645;&#x20;&#x645;&#x62a;&#x62d;&#x62f;&#x6c1;&#x20;&#x646;&#x6d2;&#x20;&#x6c1;&#x631;&#x20;&#x6a9;&#x6c1;&#x6cc;&#x6ba;&#x20;&#x62f;&#x6d2;&#x20;&#x62d;&#x642;&#x648;&#x642;&#x20;&#x62f;&#x6cc;&#x20;&#x62d;&#x641;&#x627;&#x638;&#x62a;&#x20;&#x62a;&#x6d2;&#x20;&#x648;&#x62f;&#x6be;&#x627;&#x631;&#x6d2;&#x20;&#x62f;&#x627;&#x20;&#x62c;&#x6be;&#x646;&#x688;&#x627;&#x20;&#x627;&#x686;&#x627;&#x631;&#x20;&#x6a9;&#x6be;&#x6bb;&#x20;&#x62f;&#x627;&#x20;&#x627;&#x631;&#x627;&#x62f;&#x6c1;&#x20;&#x6a9;&#x6cc;&#x62a;&#x627;&#x20;&#x6c1;&#x648;&#x6d2;&#x6d4;&#x20;&#x627;&#x6cc;&#x6c1;&#x648;&#x20;&#x684;<font color="red">&#x626;</font>&#x6d2;&#x20;&#x648;&#x20;&#x62d;&#x634;&#x6cc;&#x627;&#x646;&#x6c1;&#x20;&#x6a9;&#x645;&#x627;&#x6ba;&#x20;&#x62f;&#x6cc;&#x20;&#x635;&#x648;&#x631;&#x62a;&#x20;&#x648;&#x686;&#x20;&#x638;&#x627;&#x6c1;&#x631;&#x20;&#x62a;&#x6be;<font color="red">&#x626;</font>&#x6cc;&#x20;&#x6c1;&#x6d2;</span>|`cv55=1`


<!-- PRODUCT SITE ONLY
[font id='awami' face='AwamiPreviewB-Regular' bold='AwamiPreviewB-Bold' size='150%' lineheight='200%' rtl=1]
[font id='awamiL' face='AwamiPreviewB-Regular' bold='AwamiPreviewB-Bold' size='100%' ltr=1]
[font id='awamipar' face='AwamiPreviewB-Regular' bold='AwamiPreviewB-Bold' size='150%' lineheight='200%' rtl=1]

-->



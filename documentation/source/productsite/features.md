

<font color="red">Note:</font> |
:------------ | -
**This page will only display properly in Mozilla Firefox. Also, Graphite must be enabled. See the [instructions on how to enable Graphite in Firefox](http://scripts.sil.org/cms/scripts/page.php?site_id=projects&amp;item_id=graphite_firefox#cf8a0574).** |


Awami Nastaliq is a TrueType font with smart font capabilities added using the [Graphite](http://graphite.sil.org) font technology. The font includes a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The chart below enumerates the details of these features. Whether these features are available to users will depend on the application being used.

See [Using Font Features](https://software.sil.org/fonts/features/). Although that page is not targeted at Arabic script support, it does provide a comprehensive list of applications that make full use of both the OpenType and Graphite font technologies.

See also [Arabic Fonts — Application Support](http://software.sil.org/arabicfonts/support/application-support/). It provides a fairly comprehensive list of applications that make full use of the [Graphite](http://graphite.sil.org) font technology.

This page uses web fonts (WOFF) to demonstrate font features. However, it will only display correctly in Mozilla Firefox. For a more concise example of how to use Awami Nastaliq as a web font see *AwamiNastaliq-webfont-example.html* in the font package web folder. 

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## End of Ayah (U+06DD), subtending marks (U+0600..U+0605)

These Arabic characters are intended to enclose or hold one or more digits. 

Specific technical details of how to use them are discussed in the [Arabic fonts FAQ -- Subtending marks](http://software.sil.org/arabicfonts/support/faq#Ayah).

## Customizing with TypeTuner

For applications that do not make use of Graphite features or the OpenType Character Variants, you can now download fonts customized with the variant glyphs you choose. Read this document, visit [TypeTuner Web](http://scripts.sil.org/ttw/fonts2go.cgi), then choose the variants and download your font.

### Character variants

There are some character shape differences in different languages which use the Arabic script. These can be accessed by using Graphite features.  

Unless otherwise indicated, the first feature in a table is the default.

#### Hook on medial heh-goal

<span class='affects'>Affects: U+06C1, U+06C2</span>

Feature | Sample | Feature setting
---- | ------: | :----
True| <span dir="rtl" class='awami-R normal'>&#x628;<font color="red">&#x6C1;</font>&#x628; &#x628;<font color="red">&#x6C2;</font>&#x628;</span>| `hehk=1`
False | <span dir="rtl" class='awami-hehk-0-R normal'>&#x628;<font color="red">&#x6C1;</font>&#x628; &#x628;<font color="red">&#x6C2;</font>&#x628;</span>| `hehk=0`

#### Initial heh doachashmee

<span class='affects'>Affects: U+06BE</span>

Feature | Sample | Feature setting
---- | ------: | :----
Heart shape | <span dir="rtl" class='awami-R normal'><font color="red">&#x6BE;</font>&#x627;</span> | `hedo=0`
Round | <span dir="rtl" class='awami-hedo-1-R normal'><font color="red">&#x6BE;</font>&#x627;</span>| `hedo=1`

#### Lam with V 

<span class='affects'>Affects: U+06B5</span>

Feature | Sample | Feature setting
---- | ------: | :----
V over stem | <span dir="rtl" class='awami-R normal'><font color="red">&#x6B5;</font> &#x6B5;&#x628;&#x6B5;&#x628;<font color="red">&#x6B5;</font></span>| `lamv=0`
V over bowl | <span dir="rtl" class='awami-lamv-1-R normal'><font color="red">&#x6B5;</font> &#x6B5;&#x628;&#x6B5;&#x628;<font color="red">&#x6B5;</font></span>| `lamv=1`

#### Full Stop 

<span class='affects'>Affects: U+06D4</span>

Feature | Sample | Feature setting
---- | ------: | :---- 
Dash | <span dir="rtl" class='awami-R normal'>&#x62c;&#x62c;&#x62c;<font color="red">&#x6d4;</font></span>| `cv85=0`
Dot | <span dir="rtl" class='awami-cv85-1-R normal'>&#x62c;&#x62c;&#x62c;<font color="red">&#x6d4;</font></span>| `cv85=1`

#### Punctuation 

<span class='affects'>Affects: U+0021, U+0022, U+0027, U+0028, U+0029, U+002A, U+002B, U+002D, U+002F, U+003A, U+003C, U+003D, U+003E, U+005B, U+005C, U+005D, U+007B, U+007C, U+007D, U+00AB, U+00AD, U+00B1, U+00B7, U+00BB, U+00D7, U+2004, U+2010, U+2011, U+2012, U+2013, U+2014, U+2015, U+2018, U+2019, U+201A, U+201C, U+201D, U+201E, U+2022, U+2025, U+2026, U+2027, U+2030, U+2039, U+203A, U+2212, U+2219</span>

Default uses Arabic-style punctuation for right-to-left segments and Latin-style for left-to-right segments

Feature | Sample | Feature setting
---- | ---------------: | :---- 
Default | <span dir="rtl" class='awami-R normal'>! " ' ( ) * + - / :  [ \ ] { } « ­ ± · » ×   ‐ ‑ ‒ – — ― ‘ ’ ‚ “ ” „ • ‥ … ‧ ‰ ‹ › − ∙ </span>| `punc=0`
Arabic | <span dir="rtl" class='awami-punc-1-R normal'>! " ' ( ) * + - / :  [ \ ] { } « ­ ± · » ×   ‐ ‑ ‒ – — ― ‘ ’ ‚ “ ” „ • ‥ … ‧ ‰ ‹ › − ∙ </font></span> | `punc=1`
Latin | <span dir="rtl" class='awami-punc-2-R normal'>! " ' ( ) * + - / :  [ \ ] { } « ­ ± · » ×   ‐ ‑ ‒ – — ― ‘ ’ ‚ “ ” „ • ‥ … ‧ ‰ ‹ › − ∙ </font></span>| `punc=2`

#### Sukun/jazm 

<span class='affects'>Affects: U+0652</span>

Feature | Sample | Feature setting
---- | ------: | :---- 
Open down | <span dir="rtl" class='awami-cv78-1-R normal'>&#x628;&#x652; &#x25cc;&#x652;</span>| `cv78=1`
Open left | <span dir="rtl" class='awami-cv78-2-R normal'>&#x628;&#x652; &#x25cc;&#x652;</font></span>| `cv78=2`

#### Hamza 

<span class='affects'>Affects: U+0654, U+0655, U+0623, U+0624, U+0626, U+0675, U+076C, U+0681, U+06C2, U+06D3</span>

Feature | Sample | Feature setting
---- | ---------------: | :----
Urdu style | <span dir="rtl" class='awami-R normal'>ء أ ؤ بؤ إ ۂ بۂ ۓ بۓ ٵ ݬ بݬ ځ بځ بځب بٔ بٕ</span>| `hamz=0`
Arabic style | <span dir="rtl" class='awami-hamz-1-R normal'>ء أ ؤ بؤ إ ۂ بۂ ۓ بۓ ٵ ݬ بݬ ځ بځ بځب بٔ بٕ</font></span>| `hamz=1`

#### Word spacing 

Feature | Sample | Feature setting
---- | ---------------: | :----
Extra tight | <span dir="rtl" class='awami-wdsp-0-R normal'>   کیوں جو انسانی حقوق کنوں</span>| `wdsp=0`
Tight | <span dir="rtl" class='awami-wdsp-1-R normal'>   کیوں جو انسانی حقوق کنوں</span>| `wdsp=1`
Medium (default) | <span dir="rtl" class='awami-R normal'>   کیوں جو انسانی حقوق کنوں</span>| `wdsp=2`
Wide| <span dir="rtl" class='awami-wdsp-3-R normal'>   کیوں جو انسانی حقوق کنوں</span>| `wdsp=3`
Extra wide| <span dir="rtl" class='awami-wdsp-4-R normal'>   کیوں جو انسانی حقوق کنوں</span>| `wdsp=4`

#### Short forms 

<span class='affects'>Affects: kafs &amp; gafs: U+06A9, U+06AF, U+0643, U+06B1, U+06B3, U+06AB, U+06B0; finals: U+06CC, U+0633, U+0642, U+0644, U+0645, U+0646, U+06B5, U+06D0, U+0626, U+06CE, U+06BA, U+06BB, U+06B9, U+0768, U+0769</span>

Feature | Sample | Feature setting
---- | ---------------: | :----
None | <span dir="rtl" class='awamipar-shrt-0-R normal'>&#x62F;&#x6CC;&#x6A9;&#x6BE;&#x62A;&#x6CC; &#x6A9;&#x646;&#x633;&#x644;&#x679;&#x646;&#x679;&#x633; &#x646;&#x6AF;&#x6BE;&#x646;&#x6D2; &#x62A;&#x6A9;&#x645;&#x6CC;&#x644;</span>| `shrt=0`
Kafs and gafs | <span dir="rtl" class='awamipar-shrt-1-R normal'>&#x62F;&#x6CC;<font color="red">&#x6A9;</font>&#x6BE;&#x62A;&#x6CC; <font color="red">&#x6A9;</font>&#x646;&#x633;&#x644;&#x679;&#x646;&#x679;&#x633; &#x646;<font color="red">&#x6AF;</font>&#x6BE;&#x646;&#x6D2; &#x62A;<font color="red">&#x6A9;</font>&#x645;&#x6CC;&#x644;</font></span>| `shrt=1`
Finals | <span dir="rtl" class='awamipar-shrt-2-R normal'>&#x62F;&#x6CC;&#x6A9;&#x6BE;&#x62A;<font color="red">&#x6CC;</font> &#x6A9;&#x646;&#x633;&#x644;&#x679;&#x646;&#x679;<font color="red">&#x633;</font> &#x646;&#x6AF;&#x6BE;&#x646;&#x6D2; &#x62A;&#x6A9;&#x645;&#x6CC;<font color="red">&#x644;</font></span>| `shrt=2`
All (default)| <span dir="rtl" class='awamipar-shrt-3-R normal'>&#x62F;&#x6CC;<font color="red">&#x6A9;</font>&#x6BE;&#x62A;<font color="red">&#x6CC;</font> <font color="red">&#x6A9;</font>&#x646;&#x633;&#x644;&#x679;&#x646;&#x679;<font color="red">&#x633;</font> &#x646;<font color="red">&#x6AF;</font>&#x6BE;&#x646;&#x6D2; &#x62A;<font color="red">&#x6A9;</font>&#x645;&#x6CC;<font color="red">&#x644;</font></span>| `shrt=3`

#### Collision avoidance

Feature | Sample | Feature setting
---- | ---------------: | :---- 
Off | <span dir="rtl" class='awami-agca-0-R normal'><font color="red">&#x67e;&#x6cc;</font>&#x679;&#x6cc; <font color="red">&#x627;&#x614;&#x628;&#x650;&#x6cc;</font>&#x62c;<font color="red">&#x6cc;&#x644;</font> &#x62a;&#x62d;<font color="red">&#x631;</font>&#x650;<font color="red">&#x6cc;</font>&#x62c;</span> | `agca=0`
Kern-only | <span dir="rtl" class='awami-agca-1-R normal'><font color="red">&#x67e;&#x6cc;</font>&#x679;&#x6cc; <font color="red">&#x627;&#x614;&#x628;&#x650;&#x6cc;</font>&#x62c;<font color="red">&#x6cc;&#x644;</font> &#x62a;&#x62d;<font color="red">&#x631;</font>&#x650;<font color="red">&#x6cc;</font>&#x62c;</span> | `agca=1`
Not implemented | | `agca=2`
On (default) | <span dir="rtl" class='awami-agca-3-R normal'><font color="red">&#x67e;&#x6cc;</font>&#x679;&#x6cc; <font color="red">&#x627;&#x614;&#x628;&#x650;&#x6cc;</font>&#x62c;<font color="red">&#x6cc;&#x644;</font> &#x62a;&#x62d;<font color="red">&#x631;</font>&#x650;<font color="red">&#x6cc;</font>&#x62c;</span> | `agca=3`

## End of Ayah and Subtending marks

*This is not technically a feature, but we find it useful to demonstrate the use of these characters.*

Firefox allows you to use U+06DD followed by the digits and proper rendering occurs. However, surrounding the sequence with U+202D and U+202C seems to give the most reliable results in different browsers, and so this font requires those characters in order to display properly.

Character | Sample  
------------- | ---------------: 
U+06DD ARABIC END OF AYAH<br>(U+202D U+06DD U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x6DD;&#x6F1;&#x6F2;&#x6F3;&#x202C; &#x202D;&#x6DD;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x6DD;&#x6F1;&#x202C;</span>
U+0600 ARABIC NUMBER SIGN<br>(U+202D U+0600 U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x600;&#x6F1;&#x6F2;&#x6F3;&#x202C; &#x202D;&#x600;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x600;&#x6F1;&#x202C;</span>
U+0601 ARABIC SIGN SANAH (year)<br>(U+202D U+0601 U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x601;&#x6F1;&#x6F9;&#x6F3;&#x6F2;&#x202C;</span>
U+0602 ARABIC FOOTNOTE MARKER<br>(U+202D U+0602 U+06F1 U+06F2 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x602;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x602;&#x6F1;&#x202C;</span>
U+0603 ARABIC SIGN SAFHA (page)<br>(U+202D U+0603 U+06F1 U+06F2 U+06F3 U+202C)| <span dir="rtl" class='awami-R normal'>&#x202D;&#x603;&#x6F1;&#x6F2;&#x6F3;&#x202C; &#x202D;&#x603;&#x6F1;&#x6F2;&#x202C; &#x202D;&#x603;&#x6F1;&#x202C;</span>



## Paragraph of text

This sentence comes from the [Saraiki UDHR](http://unicode.org/udhr/d/udhr_skr.txt). 

Sample  | Feature setting
---------------: | :---- 
<span dir="rtl" class='awamipar-R normal'> &#x627;&#x642;&#x648;&#x627;&#x645;&#x20;&#x645;&#x62a;&#x62d;&#x62f;&#x6c1;&#x20;&#x646;&#x6d2;&#x20;&#x6c1;&#x631;&#x20;&#x6a9;<font color="red">&#x6c1;</font>&#x6cc;&#x6ba;&#x20;&#x62f;&#x6d2;&#x20;&#x62d;&#x642;&#x648;&#x642;&#x20;&#x62f;&#x6cc;&#x20;&#x62d;&#x641;&#x627;&#x638;&#x62a;&#x20;&#x62a;&#x6d2;&#x20;&#x648;&#x62f;<font color="red">&#x6be;</font>&#x627;&#x631;&#x6d2;&#x20;&#x62f;&#x627;&#x20;&#x62c;&#x6be;&#x646;&#x688;&#x627;&#x20;&#x627;&#x686;&#x627;&#x631;&#x20;&#x6a9;&#x6be;<font color="red">&#x6bb;</font>&#x20;&#x62f;&#x627;&#x20;&#x627;&#x631;&#x627;&#x62f;&#x6c1;&#x20;&#x6a9;&#x6cc;&#x62a;&#x627;&#x20;&#x6c1;&#x648;&#x6d2;&#x6d4;&#x20;&#x627;&#x6cc;<font color="red">&#x6c1;</font>&#x648;&#x20;&#x684;<font color="red">&#x626;</font>&#x6d2;&#x20;&#x648;&#x20;&#x62d;&#x634;&#x6cc;&#x627;&#x646;&#x6c1;&#x20;&#x6a9;&#x645;&#x627;&#x6ba;&#x20;&#x62f;&#x6cc;&#x20;&#x635;&#x648;&#x631;&#x62a;&#x20;&#x648;&#x686;&#x20;&#x638;&#x627;&#x6c1;&#x631;&#x20;&#x62a;&#x6be;<font color="red">&#x626;</font>&#x6cc;&#x20;&#x6c1;&#x6d2;</span>|`hehk=1, hedo=0, hamz=0, shrt=3`
<span dir="rtl" class='awamipar-R normal' style='font-feature-settings: "hehk" 0, "hedo" 1, "hamz" 1, "shrt" 2'> &#x627;&#x642;&#x648;&#x627;&#x645;&#x20;&#x645;&#x62a;&#x62d;&#x62f;&#x6c1;&#x20;&#x646;&#x6d2;&#x20;&#x6c1;&#x631;&#x20;&#x6a9;<font color="red">&#x6c1;</font>&#x6cc;&#x6ba;&#x20;&#x62f;&#x6d2;&#x20;&#x62d;&#x642;&#x648;&#x642;&#x20;&#x62f;&#x6cc;&#x20;&#x62d;&#x641;&#x627;&#x638;&#x62a;&#x20;&#x62a;&#x6d2;&#x20;&#x648;&#x62f;<font color="red">&#x6be;</font>&#x627;&#x631;&#x6d2;&#x20;&#x62f;&#x627;&#x20;&#x62c;&#x6be;&#x646;&#x688;&#x627;&#x20;&#x627;&#x686;&#x627;&#x631;&#x20;&#x6a9;&#x6be;<font color="red">&#x6bb;</font>&#x20;&#x62f;&#x627;&#x20;&#x627;&#x631;&#x627;&#x62f;&#x6c1;&#x20;&#x6a9;&#x6cc;&#x62a;&#x627;&#x20;&#x6c1;&#x648;&#x6d2;&#x6d4;&#x20;&#x627;&#x6cc;<font color="red">&#x6c1;</font>&#x648;&#x20;&#x684;<font color="red">&#x626;</font>&#x6d2;&#x20;&#x648;&#x20;&#x62d;&#x634;&#x6cc;&#x627;&#x646;&#x6c1;&#x20;&#x6a9;&#x645;&#x627;&#x6ba;&#x20;&#x62f;&#x6cc;&#x20;&#x635;&#x648;&#x631;&#x62a;&#x20;&#x648;&#x686;&#x20;&#x638;&#x627;&#x6c1;&#x631;&#x20;&#x62a;&#x6be;<font color="red">&#x626;</font>&#x6cc;&#x20;&#x6c1;&#x6d2;</span>|`hehk=0, hedo=1, hamz=1, shrt=2`


[font id='awamipar' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1]
[font id='awami' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1]
[font id='awamiL' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='100%' ltr=1]



[font id='awamipar-hehk-0' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='hehk 0']
[font id='awamipar-hedo-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='hedo 1']
[font id='awamipar-lamv-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='lamv 1']
[font id='awamipar-cv85-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='cv85 1']
[font id='awamipar-punc-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='punc 1']
[font id='awamipar-punc-2' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='punc 2']
[font id='awamipar-cv78-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='cv78 1']
[font id='awamipar-cv78-2' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='cv78 2']
[font id='awamipar-hamz-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='hamz 1']
[font id='awamipar-wdsp-0' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='wdsp 0']
[font id='awamipar-wdsp-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='wdsp 1']
[font id='awamipar-wdsp-3' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='wdsp 3']
[font id='awamipar-wdsp-4' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='wdsp 4']
[font id='awamipar-shrt-0' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='shrt 0']
[font id='awamipar-shrt-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='shrt 1']
[font id='awamipar-shrt-2' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='shrt 2']
[font id='awamipar-shrt-3' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='shrt 3']
[font id='awamipar-agca-0' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='agca 0']
[font id='awamipar-agca-1' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='agca 1']
[font id='awamipar-agca-3' face='AwamiNastaliq-Regular' bold='AwamiNastaliq-Bold' size='150%' lineheight='200%' rtl=1 feats='agca 3']

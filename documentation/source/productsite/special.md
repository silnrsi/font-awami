
The Awami Nastaliq font was developed to support a wide variety of languages that are written using the Nastaliq style of Arabic script. Since at least the year 2000, SIL’s Writing Systems Technology team has received requests for a publication-quality Nastaliq font that is fully customizable and extensible, enabling support for minority languages. While there are a handful of Nastaliq-style fonts that support the Urdu language adequately, until recently there have been no fonts that handle the range of characters and diacritics needed for approximately twenty-five other languages of Pakistan, spoken by over 120 million people, as well as other languages in neighboring countries. The Awami Nastaliq font meets a long-standing need in this part of the world.

The complexity of the sloping, calligraphic style makes the development of a truly flexible font quite challenging, and so Awami Nastaliq makes use of specially-designed mechanisms built into SIL’s Graphite font technology. For this reason, Awami Nastaliq requires applications that provide Graphite support. Such applications include the [Firefox web browser](https://www.mozilla.org/firefox), the [LibreOffice suite](https://www.libreoffice.org/), [XeTeX/XeLaTeX](https://www.tug.org/texlive/), and linguistic software such as [FieldWorks](https://software.sil.org/fieldworks/), [Paratext](https://paratext.org/), [PTXprint](https://software.sil.org/ptxprint/), and [Bloom](http://bloomlibrary.org/).

The following are some characteristics of Awami’s smart font rendering.

## Special character support

Awami Nastaliq supports all the special characters known to be used by languages of Pakistan. Below we give examples of some of those characters and how they can appear with missing or incomplete support in other fonts. (The problems -- shown below in red -- are demonstrated using Awami, but they all show rendering failures actually encountered with other popular fonts.) For instance, where the character is completely missing from the font, the software may substitute a glyph from another Arabic font. In other cases, an isolate form is used with no contextual shaping.

![Seen with four dots - U+075C](assets/images/MissingLetters2_Palula_red.png){width=30%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/MissingLetters2_Palula_red.png -->
[caption]<em>Seen with four dots - U+075C (used in Shina and Palula)</em>[/caption]

![Rnoon - U+06BB (used in Saraiki and Palula)](assets/images/MissingLetters1_Saraiki_red.png){width=30%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/08/MissingLetters1_Saraiki_red.png -->
[caption]<em>Rnoon - U+06BB (used in Saraiki and Palula)</em>[/caption]

![Seen with three dots above and below - U+069C (used in Palula - notice that the yeh with sideways noon ghunna mark is also incorrect in one example.)](assets/images/MissingLetters5_Palula_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/08/MissingLetters5_Palula_red.png -->
[caption]<em>Seen with three dots above and below - U+069C (used in Palula - notice that the yeh with sideways noon ghunna mark is also incorrect in one example.)</em>[/caption]

![Yeh with small V above - U+06CE (used in Balochi)](assets/images/MissingLetters3_Balochi_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/MissingLetters3_Balochi_red.png -->
[caption]<em>Yeh with small V above - U+06CE (used in Balochi)</em>[/caption]

![Hah with small tah and two dots below - U+076F (used in Khowar)](assets/images/MissingLetters6_Khowar_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2019/06/MissingLetters6_Khowar_red.png -->
[caption]<em>Hah with small tah and two dots below - U+076F (used in Khowar)</em>[/caption]

![Seen with small tah and two dots below - U+0770 (used in Khowar)](assets/images/MissingLetters4_Khowar_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2019/06/MissingLetters4_Khowar_red.png -->
[caption]<em>Seen with small tah and two dots below - U+0770 (used in Khowar)</em>[/caption]

## Diacritic support

The highly calligraphic and sloping style of Nastaliq makes proper handling of diacritics especially tricky. Some languages require a wider variety and more frequently occurring diacritics than Urdu, so providing support for them has always been a challenge.

Awami Nastaliq includes support for a wide variety of diacritics in combination with all the special characters available in the font. The images below demonstrate how Awami’s special glyph positioning mechanism allows the diacritics to be shifted to avoid collisions that might otherwise occur.

![Diacritic support](assets/images/DiacCollisions1_Marwari_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/DiacCollisions1_Marwari_red.png -->

![Diacritic support](assets/images/DiacCollisions2_Marwari_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/DiacCollisions2_Marwari_red.png -->

![Diacritic support](assets/images/DiacCollisions3_Brahui_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/DiacCollisions3_Brahui_red.png -->

![Diacritic support](assets/images/DiacCollisions4_Balochi_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/DiacCollisions4_Balochi_red.png -->



## Correct spacing

Graphite’s smart shape-based kerning mechanism is used to both avoid collisions between calligraphic sequences and to provide the correct spacing between words.

![Correct spacing](assets/images/Spacing1_Shina_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Spacing1_Shina_red.png -->

![Correct spacing](assets/images/Spacing2_Palula_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Spacing2_Palula_red.png -->

![Correct spacing](assets/images/Spacing3_Balochi_red.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Spacing3_Balochi_red.png -->


## Diagonal cluster fitting

One of the distinctives of the written Nastaliq style is that the left side of diagonally-sloping clusters can be tucked underneath the right side of others in order to give the page a more even texture. This is quite difficult to accomplish with most computer fonts, because the overlap has to be anticipated and the text adjusted ahead of time. The Awami Nastaliq font, however, uses Graphite’s on-the-fly smart positioning to make these adjustments happen without pre-programming.  

The images below show some segments and word sequences with the distinctive cluster fitting and compares them with the same sequences without the fitting (in red).

The following examples show cluster fitting within a single word.

![Diagonal cluster fitting](assets/images/Fitting1Word1_Balochi.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Fitting1Word1_Balochi.png -->

![Diagonal cluster fitting](assets/images/Fitting1Word2_Palula.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Fitting1Word2_Palula.png -->

![Diagonal cluster fitting](assets/images/Fitting1Word3_Balochi.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Fitting1Word3_Balochi.png -->

Cluster fitting also occurs between words.

![Cluster fitting also occurs between words](assets/images/Fitting2Words1_Balochi.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Fitting2Words1_Balochi.png -->

![Cluster fitting also occurs between words](assets/images/Fitting2Words2_Balochi.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Fitting2Words2_Balochi.png -->

![Cluster fitting also occurs between words](assets/images/Fitting2Words3_Palula.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Fitting2Words3_Palula.png -->

## Variable word spacing

Communities that use Nastaliq-style script can have varying preferences about how tight or loose word spacing should be. Highly literate communities often prefer minimal word spacing, but language groups new to literacy find that wider spaces enhance readability for inexperienced readers.

For this reason, Awami Nastaliq allows the user to choose among five levels of word spacing, depending on the needs of the expected readership. The image below demonstrates the five levels of word spacing.

![Variable word spacing](assets/images/WordSpacing.png){width=28%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/WordSpacing.png -->

## Alternate letter forms

Awami Nastaliq provides alternate forms of the letters shown below. These alternates can be selected within LibreOffice by modifying the font name or in Firefox using CSS - see [Features Demo](features) for a description of how to use these features.

![Medial heh goal (with or without hook)](assets/images/Feature_hehk_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_hehk_color.png -->
[caption]<em>Medial heh goal (with or without hook)</em>[/caption]

![Initial heh doachashmee (round or heart-shaped)](assets/images/Feature_hedo_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_hedo_color.png -->
[caption]<em>Initial heh doachashmee (round or heart-shaped)</em>[/caption]

![Lam with V (V located over stem or bowl on isolate and final forms)](assets/images/Feature_lamv_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_lamv_color.png -->
[caption]<em>Lam with V (V located over stem or bowl on isolate and final forms)</em>[/caption]

![Full stop (dash-like or dot-like)](assets/images/Feature_cv85_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_cv85_color.png -->
[caption]<em>Full stop (dash-like or dot-like)</em>[/caption]

![Sukun/jazm (open down or open left)](assets/images/Feature_cv78_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_cv78_color.png -->
[caption]<em>Sukun/jazm (open down or open left)</em>[/caption]

![Hamza (Urdu- or Arabic-style)](assets/images/Feature_hamz_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_hamz_color.png -->
[caption]<em>Hamza (Urdu- or Arabic-style)</em>[/caption]

![Small nuqtas - Larger nuqtas enhance readability, but can cause problems with glyph collisions. It is possible to use smaller glyphs on initial, medial, and final forms.](assets/images/Feature_snuq_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_snuq_color.png -->
[caption]<em>Small nuqtas - Larger nuqtas enhance readability, but can cause problems with glyph collisions. It is possible to use smaller glyphs on initial, medial, and final forms.</em>[/caption]


## Short forms

The diagonal nature of the Nastaliq style causes some of the letter sequences to get quite tall, which can result in collisions with the previous line of text. Awami includes a feature to use shorter forms of some of the letters to help avoid this problem. Letters that can be shortened include kafs and gafs (at or near the beginning of the sequence) and final forms of noon, seen, chotiyeh, lam, meem, and qaf.

![Kafs and gafs](assets/images/Feature_shrt1_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_shrt1_color.png -->
[caption]<em>Kafs and gafs</em>[/caption]

![Finals - noon, seen, chotiyeh, lam, meem, qaf](assets/images/Feature_shrt2_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_shrt2_color.png -->
[caption]<em>Finals - noon, seen, chotiyeh, lam, meem, qaf</em>[/caption]

![Both](assets/images/Feature_shrt3_color.png){width=22%}
<!-- PRODUCT SITE IMAGE SRC https://software.sil.org/awami/wp-content/uploads/sites/33/2017/07/Feature_shrt3_color.png -->
[caption]<em>Both</em>[/caption]


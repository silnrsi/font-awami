
The SIL Arabic script fonts are encoded according to Unicode, so your application must support Unicode text in order to access letters other than the standard ANSI characters. Most applications now provide basic Unicode support. You will, however, need some way of entering Unicode text into your document.

Arabic script is a complex and difficult script, and this complexity is compounded by the fact that Arabic script is used for [many different languages](https://scriptsource.org/scr/Arab) and cultures with variations in acceptable calligraphic style. From a computer perspective at least, the technologies used to implement Arabic script are not yet fully mature. The result is that while a given font might work for one set of languages on a given software platform, the same font might not work for other languages or on other platforms. This means that it is very difficult to give an accurate answer to the question of software requirements. 

## Requirements

This font is supported by all major operating systems (macOS, Windows, Linux-based, iOS, and Android), however the extent of that support depends on the individual OS and application.

## Installation

Install the font by decompressing the .zip archive and installing the font using the standard font installation process for .ttf (TrueType/OpenType) fonts for your platform. For additional tips see the help page on [Font installation](https://software.sil.org/fonts/installation).

## Keyboarding and character set support

## Keyboarding and character set support

This font package does not include keyboards or other software for entering text. To type the symbols in this font, use the keyboarding systems provided in your OS or use a separate utility. [Keyman](https://keyman.com/) is a cross-platform keyboarding system.

Various other means may be available for different operating-system platforms to create additional input methods. Some suggestions are listed here: [Keyboard Systems Overview](https://scriptsource.org/entry/ytr8g8n6sw).

See [Character set support](charset) for details of the Unicode characters supported by this font.

### Keyman keyboards

[Keyman](https://keyman.com/) provides quite a few keyboards for languages which use the Nastaliq style of Arabic script. Go to [Keyman.com](https://keyman.com/). Click on **Keyboards** and then type the language for which you wish to select a keyboard. It will offer you keyboard packages if any are available for that language.

### Installing an Urdu keyboard

#### On Windows 10/11:
- Open the Language control panel.
- Click on **Add a language**.
- Choose "Urdu (Pakistan)" and click **OK**.
- Activate the keyboard using the Taskbar control or language bar.

#### To see a visual layout for the keyboard:

On Windows 10/11: see [Use the On-Screen Keyboard (OSK) to type](https://support.microsoft.com/en-us/windows/use-the-on-screen-keyboard-osk-to-type-ecbb5e08-5b4e-d8c8-f794-81dbf896267a#ID0EBBD=Windows_11).


## Rendering and application support

The Awami Nastaliq font requires software enabled with the very latest [Graphite](https://graphite.sil.org/) engine (version 1.3.4+) in order to render correctly. The font does not support OpenType rendering. **It will not work with standard software such as Microsoft Office**. 

Currently, the only software that can render Awami Nastaliq are the [Firefox web browser](https://www.mozilla.org/firefox), the [LibreOffice suite](https://www.libreoffice.org/), [XeTeX/XeLaTeX](https://www.tug.org/texlive/), and linguistic software such as [FieldWorks](https://software.sil.org/fieldworks/), [Paratext](https://paratext.org/), [PTXprint](https://software.sil.org/ptxprint/), and [Bloom](http://bloomlibrary.org/).

If a developer wishes to add support for Graphite, the Graphite engine is available [here](https://github.com/silnrsi/graphite/releases/).

Here are links for downloading appropriate versions:

### Firefox

You will need a [recent version of Firefox](https://www.mozilla.org/en-US/firefox/new/?scene=2&amp;f=85) - version 46 or later.

Due to security concerns, Graphite has sometimes been disabled in Firefox by default, so you might need to enable it. Follow these [instructions for enabling Graphite in Firefox](https://graphite.sil.org/graphite_firefox).

### LibreOffice

We recommend [LibreOffice 5.3+](https://www.libreoffice.org/) which supports version 1.3.8 of the Graphite engine.

Version 5.2 fixed the bug that was in version 5.1.

Version 5.1 supports Awami, but it has a bug where certain characters (eg, the small tah) would be displayed in an incorrect position.


### XeTeX

The TeXLive 2017 version of XeTeX contains a fix for Harfbuzz which was causing combining marks to clash at the end of words when followed by a Latin character.

TeXLive is available from [https://www.tug.org/texlive/](https://www.tug.org/texlive/).

#### Full Collision Avoidance

To use the full collision avoidance (both intra- and inter- word) of Awami in XeTeX (required version 0.99995 or newer) a macro parameter needs to be set. 

Explanations of this parameter are at:

[http://tug.org/pipermail/xetex/2016-February/026398.html](http://tug.org/pipermail/xetex/2016-February/026398.html)
[http://tug.org/pipermail/xetex/2016-February/026401.html](http://tug.org/pipermail/xetex/2016-February/026401.html)
[http://tug.org/pipermail/xetex/2016-February/026402.html](http://tug.org/pipermail/xetex/2016-February/026402.html)
[http://tug.org/pipermail/xetex/2016-February/026403.html](http://tug.org/pipermail/xetex/2016-February/026403.html)
[http://tug.org/pipermail/xetex/2016-February/026474.html](http://tug.org/pipermail/xetex/2016-February/026474.html)

This parameter should be set in a .tex file. The file could look something like:

```
%% Cross-space contextualization

% No cross-space contextualization.
% This is how XeTeX behaves by default.
% Most projects will use this setting.
% \XeTeXinterwordspaceshaping = 0

% Some cross-space contextualization.
% Spaces between words are adjusted,
% but the rendering of individual words is not affected by the spaces.
% \XeTeXinterwordspaceshaping = 1

% Full cross-space contextualization.
% Spaces between words are adjusted,
% and the rendering of individual words is affected by the spaces.
% \XeTeXinterwordspaceshaping = 2
```

You must uncomment the appropriate command! For Awami Nastaliq, you will likely want to uncomment the last line (`\XeTeXinterwordspaceshaping = 2`). That allows the full support for collision avoidance.  

The above text (all comments and commented out statements) will give the same behaviour as before this feature was added to XeTeX, so existing users do not see any unexpected changes.

#### Bidi Support

XeTeX in [TeXLive 2017+](https://www.tug.org/texlive/) uses the latest version of Harfbuzz (1.4.6+) which fixes a bug in bidirectional data.

## Web fonts

Web font versions of this font (in WOFF and WOFF2 formats) are available in the `web` folder. These can be copied to a web server and used as fonts on web pages. A very basic HTML/CSS demo page is also included. For more information on the options and techniques available for using these fonts on web pages see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

## Text conversion

One common type of data conversion is from Roman script to Arabic script. Cross-script conversion is often very language specific. TECkit is one program that can be used for character encoding conversion. TECkit allows users to write their own custom conversion mappings. The TECkit package is available for download from SIL’s [TECkit](https://software.sil.org/teckit/) Web site. The [SIL Converters](https://software.sil.org/silconverters/) software will be an important tool in data conversion.

One page that may prove helpful is: [Roman Script to Arabic Script Conversion](https://software.sil.org/arabicfonts/rs-to-as-conversion/).

Other suggestions are listed here: [Introduction to Text Conversion and Transliteration](https://scriptsource.org/entry/xlzd6n5aqt).

See also: [Arabic Fonts -- Resources](https://software.sil.org/arabicfonts/resources/).

## Advanced features

See [Font features](features) for further information.

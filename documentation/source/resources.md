---
title: Awami Preview B - Resources
fontversion: 0.900
---

The SIL Arabic script fonts are encoded according to Unicode, so your application must support Unicode text in order to access letters other than the standard ANSI characters. Most applications now provide basic Unicode support. You will, however, need some way of entering Unicode text into your document.

Arabic script is a complex and difficult script, and this complexity is compounded by the fact that Arabic script is used for [many different languages](https://writingsystems.info/scrlang/scripts/arab/) and cultures with variations in acceptable calligraphic style. From a computer perspective at least, the technologies used to implement Arabic script are not yet fully mature. The result is that while a given font might work for one set of languages on a given software platform, the same font might not work for other languages or on other platforms. This means that it is very difficult to give an accurate answer to the question of software requirements. 

## Requirements

This font is supported by all major operating systems (macOS, Windows, Linux-based, iOS, and Android), however the extent of that support depends on the individual OS and application.

## Installation

Install the font by decompressing the .zip archive and installing the font using the standard font installation process for .ttf (TrueType/OpenType) fonts for your platform. For additional tips see the help page on [Font installation](https://software.sil.org/fonts/installation).

## Keyboarding and character set support

This font package does not include keyboards or other software for entering text. To type the symbols in this font, use the keyboarding systems provided in your OS or use a separate utility. [Keyman](https://keyman.com/) is a cross-platform keyboarding system.

Various other means may be available for different operating-system platforms to create additional input methods. Some suggestions are listed here: [Keyboard Systems Overview](https://writingsystems.info/topics/input/keyboards-and-tools/).

See [Character set support](charset.md) for details of the Unicode characters supported by this font.

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

This version of the font is using the Opentype rendering rather than SIL's smart-font technology, [Graphite](https://graphite.sil.org). **However, it still does not work well with some software such as Microsoft Office**. 

## Web fonts

Web font versions of this font (in WOFF and WOFF2 formats) are available in the `web` folder. These can be copied to a web server and used as fonts on web pages. A very basic HTML/CSS demo page is also included. For more information on the options and techniques available for using these fonts on web pages see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

## Text conversion

One common type of data conversion is from Roman script to Arabic script. Cross-script conversion is often very language specific. TECkit is one program that can be used for character encoding conversion. TECkit allows users to write their own custom conversion mappings. The TECkit package is available for download from SIL’s [TECkit](https://software.sil.org/teckit/) Web site. The [SIL Converters](https://software.sil.org/silconverters/) software will be an important tool in data conversion.

One page that may prove helpful is: [Roman Script to Arabic Script Conversion](https://software.sil.org/arabicfonts/rs-to-as-conversion/).

Other suggestions are listed here: [Encoding Conversion](http://writingsystems.info/topics/encoding/encoding-conversion/).

See also: [Arabic Fonts -- Resources](https://software.sil.org/arabicfonts/resources/).

## Advanced features

See [Font features](features.md) for further information.

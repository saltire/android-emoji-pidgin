# Android emoji theme for Pidgin/Adium

A smiley theme for Pidgin and Adium using the Android emoji symbols,
taken from the Noto font at https://github.com/googlei18n/noto-emoji
and resized to 25px width.

This theme contains 1075 symbols, up to Unicode 8.0.

![Android emoji theme for Pidgin](./preview.png?raw=true)


## Installation

Copy the `android-emoji-theme` folder to
`~/.purple/smileys` on Linux, or `%APPDATA%/Roaming/.purple/smileys` on Windows.
For Adium on Mac, copy and rename the folder to
`~/Library/Application\ Support/Adium\ 2.0/Emoticons/android-emoji-theme.AdiumEmoticonSet`.

You can then select the theme from Pidgin's Preferences menu, under Themes.


## Info on emojis in Unicode

A list of symbols can be found in `emoji-unicode8.txt`.
This was scraped from charts found here: http://www.unicode.org/emoji/charts/index.html

An ordered list is in `emoji-ordered.txt`, scraped from:
http://www.unicode.org/emoji/charts/emoji-ordering.html

More data can be found here: http://www.unicode.org/Public/emoji/

Some information, from here: http://www.unicode.org/reports/tr51/

- 722 characters from Japanese carriers (3 of which are spaces, leaving 719)
- 126 common additions in Unicode 6.0 and 6.1
- 247 flags supported in Unicode 6.0, in addition to the 10 already available
- 190 standard additions (most, but not all, are new to Unicode 7.0 or 8.0)
- 1282 total emoji in Unicode 8.0.

There are also 5 skin tone modifiers, which as of Unicode 8.0 can be combined with 64 symbols,
yielding another 320 possible emoji.
These don't seem to be supported by Noto yet, but at some point I may add them to the theme.

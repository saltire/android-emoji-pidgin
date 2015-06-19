# Android Emoji theme for Pidgin

A smiley theme for Pidgin using the Android emoji symbols,
taken from the Noto font at https://github.com/googlei18n/noto-emoji
and resized to 25px width.

This theme contains 860 symbols, up to Unicode 6.1.


## Installation

Copy the `android-emoji-theme` folder to
`~/.purple/smileys` on Linux or Mac, or `%APPDATA%/Roaming/.purple/smileys` on Windows.

You can then select the theme from Pidgin's Preferences menu, under Themes.


## Info on emojis in Unicode

A list of symbols can be found in `emoji-unicode8.txt`.
This was scraped from charts found here: http://www.unicode.org/emoji/charts/index.html

Some information, from here: http://www.unicode.org/reports/tr51/

- Level 1 Emoji
  - 722 characters from Japanese carriers (3 of which are spaces, leaving 719)
  - 126 common additions in Unicode 6.0 and 6.1
  - 845 total
- Level 2 Emoji
  - 247 flags supported in Unicode 6.0, in addition to the 10 available in level 1
  - 148 standard additions (most, but not all, are new to Unicode 7.0)
  - 41 new symbols in Unicode 8.0 (including 5 skin-tone modifiers)
  - 436 total

1281 total emoji in Unicode 8.0.

133 symbols are subject to skin-tone modifiers, yielding another 665 possible symbols.
At some point I may add these to the theme.

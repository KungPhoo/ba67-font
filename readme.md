# BA67-Font
## About
The BA67 font is a merge of the original CBM
fonts, characters from [Char8.js](https://www.masswerk.at/char8/),
and lots of hand-drawn emojis. It should support
all existing Unicode characters (as of 2025-08).

## Build
In order to create the font, uncomment the line
`// BDFExport bdf; bdf.writeBDF(pData, "C:\\Temp\\ba67.bdf", 8, 16);`
in chardef.cpp and run a debug build on Windows.
It will create the file `C:\Temp\ba67.bdf'.

Next, open [FontForge](https://https://fontforge.org),
and install `Autotrace` as specified in their manual.
Now, create a new font, then select menu `File/Import`
and check the flag `Import as background`.

Next, select all characters `Ctrl+A` and start the
menu item `Element\Autotrace`.

Finally, export it with `File/Generate Fonts...`.

### Script
Use this script with fontforge's own python
version.
```
import fontforge

font = fontforge.font()

# Import all bitmaps into background
font.importBitmaps("./BA67.bdf", True)

# Read a preference
print(fontforge.getPrefs("PreferPotrace"))

# Change a preference
fontforge.setPrefs("PreferPotrace", True)

# Auto-trace each glyph
for g in font.glyphs():
    print(g.glyphname)
    g.autoTrace()

# Save as TTF
font.generate("./BA67.ttf")
font.generate("./BA67.woff2")
```


## License
to be set, yet. Will be as liberate as possible.



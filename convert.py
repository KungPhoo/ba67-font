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
    # the glyphname is U+xxx
    g.unicode = int(g.glyphname[2:], 16)
    g.autoTrace()

# Save as TTF
font.generate("./BA67.ttf")
font.generate("./BA67.woff2")


##########################################
# Now the square font

font = fontforge.font()

# Import all bitmaps into background
font.importBitmaps("./BA67-square.bdf", True)

# Read a preference
print(fontforge.getPrefs("PreferPotrace"))

# Change a preference
fontforge.setPrefs("PreferPotrace", True)

# Auto-trace each glyph
for g in font.glyphs():
    print(g.glyphname)
    # the glyphname is U+xxx
    g.unicode = int(g.glyphname[2:], 16)
    g.autoTrace()

# Save as TTF
font.generate("./BA67-square.ttf")
font.generate("./BA67-square.woff2")


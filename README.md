# CopyKerningTo-Glyphs
This script helps you copy exception kerning or single kernings from one glyph to another.
 

How it works

The script opens a window.

You type in lines like this:
baseglyph = targetglyph
n = eng
o = oe

<img width="454" height="284" alt="WindowViewGlyphs" src="https://github.com/user-attachments/assets/d970ee41-5ff1-4825-85b4-3207b4cdd04c" />

When you click Copy, the script looks through all kerning pairs in all masters and duplicates any kerning attached to the baseglyph onto the targetglyph.

Works for both left and right kerning.


# MenuTitle: Copy Kerning to
# -*- coding: utf-8 -*-
from GlyphsApp import *
from vanilla import *

class CopyKerningToWindow(object):
    def __init__(self):
        self.w = Window((400, 200), "Copy Kerning to")
        self.w.instructions = TextBox((15, 10, -15, 20), "Add lines like baseglyph = targetglyph")
        self.w.glyphPairs = TextEditor((15, 35, -15, 110))
        self.w.copyButton = Button((-110, -40, 90, 30), "Copy", callback=self.copyKerning)
        self.w.open()

    def getGlyphNameFromID(self, font, glyphID):
        for glyph in font.glyphs:
            if glyph.id == glyphID:
                return glyph.name
        return None

    def copyKerning(self, sender):
        font = Glyphs.font
        if not font:
            Message("No font open", "Please open a font in Glyphs.")
            self.w.close()
            return
        
        lines = self.w.glyphPairs.get().splitlines()
        pairs = []
        for line in lines:
            if '=' in line:
                base, target = [s.strip() for s in line.split('=', 1)]
                if base and target:
                    pairs.append((base, target))
        if not pairs:
            Message("No pairs", "Please enter at least one pair in the format baseglyph=targetglyph.")
            self.w.close()
            return
        
        successfulPairs = 0
        for base, target in pairs:
            if not font.glyphs[base]:
                print(f"Base glyph '{base}' not found.")
                continue
            if not font.glyphs[target]:
                print(f"Target glyph '{target}' not found.")
                continue
            for master in font.masters:
                kerning = font.kerning[master.id]
                for leftKey, rightDict in list(kerning.items()):
                    for rightKey, value in list(rightDict.items()):
                        leftName = leftKey if leftKey.startswith('@') else self.getGlyphNameFromID(font, leftKey)
                        rightName = rightKey if rightKey.startswith('@') else self.getGlyphNameFromID(font, rightKey)
                        if leftName == base:
                            try:
                                font.setKerningForPair(master.id, target, rightName, value)
                                successfulPairs += 1
                            except Exception as e:
                                print(f"Error copying {base} to {target} (left): {e}")
                        elif rightName == base:
                            try:
                                font.setKerningForPair(master.id, leftName, target, value)
                                successfulPairs += 1
                            except Exception as e:
                                print(f"Error copying {base} to {target} (right): {e}")
        if successfulPairs > 0:
            Message("Kerning copied!", f"Successfully copied {successfulPairs} kerning pairs.")
        else:
            Message("No kerning found", "No kerning pairs found for the specified glyphs.")
        self.w.close()

CopyKerningToWindow() 
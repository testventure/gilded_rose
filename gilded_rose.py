# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                if item.sell_in < 0:
                    quality_change = 2
                else:
                    quality_change = 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    quality_change = -item.quality
                elif item.sell_in < 6:
                    quality_change = 3
                elif item.sell_in < 11:
                    quality_change = 2
                else:
                    quality_change = 1
            else:
                if item.sell_in < 0:
                    quality_change = -2
                else:
                    quality_change = -1
                if "conjured" in item.name.lower():
                    quality_change = 2 * quality_change
            # Legendary items are above the 50 quality threshold
            if item.quality <= 50:
                item.quality = limit(item.quality + quality_change)
            item.sell_in -= 1

def limit(num, minimum=0, maximum=50):
  return max(min(num, maximum), minimum)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Legendary(Item):
    pass

class Common(Item):
    pass

class Conjured(Item):
    pass

class BackstagePass(Item):
    pass
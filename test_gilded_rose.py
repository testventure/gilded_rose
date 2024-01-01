# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_regular_item_sell_in(self):
        items = [Item("belt", sell_in=5, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)

    def test_aged_brie_sell_in(self):
        items = [Item("Aged Brie", sell_in=5, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)

    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)

    def test_backstage_pass_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 14)

    def test_regular_item_quality(self):
        items = [Item("belt", sell_in=5, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)

    def test_regular_item_quality_below_0_sell_in(self):
        items = [Item("belt", sell_in=-1, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 3)

    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", sell_in=5, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)

    def test_aged_brie_quality_at_50(self):
        items = [Item("Aged Brie", sell_in=4, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_aged_brie_below_0_sell_in(self):
        items = [Item("Aged Brie", sell_in=-2, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 7)

    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)

    def test_backstage_pass_quality_normal(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_pass_quality_medium(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_pass_quality_high(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_pass_quality_at_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_backstage_pass_sell_in_below_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_quality_cannot_be_negative(self):
        items = [Item("belt", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item_quality_drop(self):
        items = [Item("conjured belt", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)

    def test_conjured_item_quality_drop_past_sell_in(self):
        items = [Item("conjured belt", sell_in=-1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)
        

        
if __name__ == '__main__':
    unittest.main()

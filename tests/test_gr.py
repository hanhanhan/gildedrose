import pytest

from ..gildedrose import *

sulfuras = "Sulfuras, Hand of Ragnaros"
brie = "Aged Brie"
dexterity = "+5 Dexterity Vest"
passes = "Backstage passes to a TAFKAL80ETC concert"
conjured = "Conjured Mana Cake"

parameters = (
    'name', 'sell_in', 'quality', 'next_expected_sell_in',
    'next_expected_quality', 'case')

cases = [
    # Sulfuras
    (sulfuras, 1, 87, 1, 87, "Never decreases in quality before sell in"),
    (sulfuras, -1, 87, -1, 87, "Never decreases in quality after sell in"),
    # Aged Brie
    (brie, 2, 0, 1, 1, "Increases by 1 in quality before sell in date"),
    (brie, 5, 50, 4, 50, "Max quality is 50."),
    (brie, 0, 5, -1, 7, "Quality increases by 2 after sell in date - undocumented behavior in kata."),
    # +5 Dexterity Vest
    (dexterity, 10, 12, 9, 11, "Typical quality degradation before sell in date"),
    (dexterity, 10, 0, 9, 0, "Typical quality degradation before sell in date"),
    (dexterity, 0, 10, -1, 8, "Typical quality degradation after sell in date"),
    (dexterity, -1, 0, -2, 0, "Quality is never negative"),
    # Passes
    (passes, 0, 50, -1, 0, "Quality drops to 0 after the concert"),
    (passes, 11, 30, 10, 31,
     "Quality increases by 1 when there are more than 10 days sell in"),
    (passes, 10, 49, 9, 50, "Quality is never more than 50"),
    (passes, 10, 30, 9, 32, "Quality increases by 2 when there are 10 days or less"),
    (passes, 5, 30, 4, 33, "Quality increases by 3 when there are 5 days or less"),
    (passes, 5, 50, 4, 50, "Quality is never more than 50"),
    (passes, 4, 48, 3, 50, "Quality is never more than 50"),
    # Conjured - New item to add
    (conjured, 10, 12, 9, 10, "Degrades in quality 2x normal rate before sell in"),
    (conjured, 0, 12, -1, 8, "Degrades in quality 2x normal rate after sell in"),
    (conjured, 0, 0, -1, 0, "Quality is never negative"),
]


@pytest.mark.parametrize(parameters, cases)
def test_item(name, sell_in, quality, next_expected_sell_in, next_expected_quality, case):
    GildedItemByName = name_to_class.get(name, GildedItem)
    item = GildedItemByName(name=name, sell_in=sell_in, quality=quality)

    gilded = GildedRose([item])
    gilded.update_quality()

    assert item.sell_in == next_expected_sell_in, case
    assert item.quality == next_expected_quality, case


"""
Original exercise test fixtures
Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
Item(name="Aged Brie", sell_in=2, quality=0),
Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
Item(name="Backstage passes to a TAFKAL80ETC concert",
        sell_in=15, quality=20),
Item(name="Backstage passes to a TAFKAL80ETC concert",
        sell_in=10, quality=49),
Item(name="Backstage passes to a TAFKAL80ETC concert",
        sell_in=5, quality=49),
Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
"""

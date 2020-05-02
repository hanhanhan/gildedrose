from .updaters import *


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = name_to_class.get(item.name, item_update)
            next_quality, next_sell_in = updater(item.quality, item.sell_in)
            item.quality = next_quality
            item.sell_in = next_sell_in


class Item:
    """We're not allowed to touch this code!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __str__(self):
        return f"{self.name}, Sell in: {self.sell_in}, Quality: {self.quality}"


# Easy to forget map
name_to_class = {
    "Aged Brie": brie_update,
    "Sulfuras, Hand of Ragnaros": sulfuras_update,
    "Conjured Mana Cake": conjured_update,
    "Backstage passes to a TAFKAL80ETC concert": backstage_update,
}

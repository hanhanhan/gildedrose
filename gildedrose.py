class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            item.sell_in = item.sell_in - 1

            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.quality < 50 and item.sell_in < 0:
                    item.quality = item.quality + 1
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":

                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 5:
                    item.quality = item.quality + 3
                elif item.sell_in < 10:
                    item.quality = item.quality + 2
                else:
                    item.quality = item.quality + 1

                item.quality = min(item.quality, 50)
                continue

            # "Conjured" items degrade in Quality twice as fast as normal items
            if item.name == "Conjured Mana Cake" and item.quality > 0:
                item.quality = item.quality - 1
            if item.name == "Conjured Mana Cake" and item.sell_in < 0:
                if item.quality > 0:
                    item.quality = item.quality - 1

            if item.quality > 0:
                item.quality = item.quality - 1

            if item.sell_in < 0:
                if item.quality > 0:
                    item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __str__(self):
        return f"{self.name}, Sell in: {self.sell_in}, Quality: {self.quality}"

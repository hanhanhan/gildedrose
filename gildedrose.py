class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    """We're not allowed to touch this code!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __str__(self):
        return f"{self.name}, Sell in: {self.sell_in}, Quality: {self.quality}"


class GildedItem(Item):
    """
    - All items have a SellIn value which denotes the number of days we have to sell the item
    - All items have a Quality value which denotes how valuable the item is
    - At the end of each day our system lowers both values for every item


    -The Quality of an item is never more than 50
    -The Quality of an item is never negative
    -Once the sell by date has passed, Quality degrades twice as fast
    """

    def _decrement_sell_in(self):
        """A day passes by."""
        self.sell_in = self.sell_in - 1

    def _update_quality(self):
        """How the quality changes when a day passes."""
        if self.quality > 0:
            self.quality = self.quality - 1

        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1

    def update_quality(self):
        """A day passes. 
        Change the quality and sell_in together.
        """
        self._decrement_sell_in()
        self._update_quality()


# Initialize objects to hold classes/mappings for Item creation based on name.
all_items = []
name_to_class = {}


def register_item(cls):
    """Keep track of all Gilded Rose specialty items for lookup by name."""
    all_items.append(cls)
    name_to_class.update({cls.name: cls for cls in all_items})


@register_item
class BrieItem(GildedItem):
    """Aged Brie" actually increases in Quality the older it gets"""

    name = "Aged Brie"

    def _update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        if self.quality < 50 and self.sell_in < 0:
            self.quality = self.quality + 1


@register_item
class SulfurasItem(GildedItem):
    """Quality is 80 and it never alters

    Should we add checking to make sure it's instantiated with quality 80?
    What is supposed to happen to its sell-in?
    """

    name = "Sulfuras, Hand of Ragnaros"

    def _decrement_sell_in(self):
        return

    def _update_quality(self):
        return


@register_item
class BackstageItem(GildedItem):
    """Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert
    """

    name = "Backstage passes to a TAFKAL80ETC concert"

    def _update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality = self.quality + 3
        elif self.sell_in < 10:
            self.quality = self.quality + 2
        else:
            self.quality = self.quality + 1

        self.quality = min(self.quality, 50)


@register_item
class ConjuredItem(GildedItem):
    name = "Conjured Mana Cake"

    def _update_quality(self):
        """Conjured mana cake's quality decays at twice the rate of GildedItem.
        """
        super()._update_quality()
        super()._update_quality()

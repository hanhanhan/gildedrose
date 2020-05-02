
def item_update(quality, sell_in):
    """
    - All items have a SellIn value which denotes the number of days we have to sell the item
    - All items have a Quality value which denotes how valuable the item is
    - At the end of each day our system lowers both values for every item


    -The Quality of an item is never more than 50
    -The Quality of an item is never negative
    -Once the sell by date has passed, Quality degrades twice as fast
    """

    """A day passes by."""
    next_sell_in = sell_in - 1

    if next_sell_in >= 0:
        next_quality = max(quality - 1, 0)
    else:
        next_quality = max(quality - 2, 0)

    return (next_quality, next_sell_in)


def brie_update(quality, sell_in):
    """Aged Brie" actually increases in Quality the older it gets"""
    next_sell_in = sell_in - 1

    if next_sell_in > 0:
        next_quality = min(50, quality + 1)
    else:  # sell_in < 0:
        next_quality = min(50, quality + 2)

    return (next_quality, next_sell_in)


def sulfuras_update(quality, sell_in):
    """Quality is 80 and it never alters

    Just return 80 or whatever value is there?
    What is supposed to happen to its sell-in?
    """

    return (quality, sell_in)


def backstage_update(quality, sell_in):
    """Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert
    """
    next_sell_in = sell_in - 1

    if next_sell_in < 0:
        next_quality = 0
    elif next_sell_in < 5:
        next_quality = min(quality + 3, 50)
    elif next_sell_in < 10:
        next_quality = min(quality + 2, 50)
    else:
        next_quality = min(quality + 1, 50)

    return (next_quality, next_sell_in)


def conjured_update(quality, sell_in):
    """Conjured mana cake's quality decays at twice the rate of GildedItem.
    """
    n_quality, _ = item_update(quality, sell_in)
    next_quality, next_sell_in = item_update(n_quality, sell_in)

    return (next_quality, next_sell_in)

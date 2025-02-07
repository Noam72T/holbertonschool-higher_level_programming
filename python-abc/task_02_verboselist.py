#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
<<<<<<< HEAD
=======
        # Add the item using the built-in list functionality.
>>>>>>> 893ca82ba51ec69194097d3b65b49e61291bb859
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
<<<<<<< HEAD
=======
        # Convert the iterable to a list so we can count the items.
>>>>>>> 893ca82ba51ec69194097d3b65b49e61291bb859
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
<<<<<<< HEAD
=======
        # Print the notification before removing the item.
>>>>>>> 893ca82ba51ec69194097d3b65b49e61291bb859
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
<<<<<<< HEAD
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
=======
        # Retrieve the item that will be removed.
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
>>>>>>> 893ca82ba51ec69194097d3b65b49e61291bb859

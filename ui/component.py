from config import settings

# Define generic table size
size = settings.TABLE_SIZE

# Draw line border
# Sample: +----------------------+
def line_border():
    line_border = "+"

    for i in range (0, size-2):
        line_border += "-"
    line_border += "+"

    return str(line_border)

# Draw and place table line
# Sample: | student              |
def table_line(entity):
    item_line = "| "
    item_line += str(entity).upper()

    for i in range (0, (size-3)-len(str(entity))):
        item_line += " "
    item_line += "|"

    return item_line

# Draw and place item line
# Sample: | + name               |
def item_line(attribute):
    item_line = "| + "
    item_line += str(attribute).capitalize()

    for i in range (0, (size-5)-len(str(attribute))):
        item_line += " "
    item_line += "|"

    return item_line

# Draw and place item line
# Sample: | + name               |
def relation_line(relation):
    item_line = "| "
    item_line += str(relation).capitalize()

    for i in range (0, (size-3)-len(str(relation))):
        item_line += " "
    item_line += "|"

    return item_line
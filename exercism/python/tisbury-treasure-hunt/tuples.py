"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    


    return record[1]
    
# print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """



    return tuple(coordinate)

# print(convert_coordinate("2A"))    


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """



    coor_1 = tuple(azara_record[1])
    # print(coor_1)
    coor_2 = rui_record[1]
    # print(coor_2)
    return coor_1 == coor_2

# print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
# print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """



    if compare_records(azara_record, rui_record) == 1: #используя предыдщую функцию, чтоб не преобразовывать опять по срезам. Хотела написать True - выдает ошибку
        result = azara_record + rui_record #делаем конкатенацию кортежей
        return result
    else:
        return("not a match")
    

# print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
# print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
    ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')
    ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')
        
    report = ""
    for record in combined_record_group:
        treasure = record[0]
        coord_treasure = record[1]
        location = record[2]
        coord_location = record[3]
        quadrant = record[4]
        # print(f"record: {record}")
        cleaned_record = (treasure, location, coord_location, quadrant)
        # print(f"cleaned_record: {cleaned_record}")
        report += f"{cleaned_record} \n"
    return report
    

    # result_1 = combined_record_group[0][0] + combined_record_group[1][0] + combined_record_group[2][0]
    # result_2 = combined_record_group[0][2:]+ combined_record_group[1][2:] + combined_record_group[2][2:]
    # print(result_1, result_2)
    # report = result_1 + result_2 
    # return report


print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))    
def map_to_25_grid(row):
    mapping = {
        (False, 'inside', 'high'): 'F',
        (False, 'inside', 'low'): 'O',
        (False, 'inside', 'middle'): 'J',
        (False, 'middle', 'high'): 'E',
        (False, 'middle', 'low'): 'N',
        (False, 'middle', 'middle'): 'I',
        (False, 'outside', 'high'): 'D',
        (False, 'outside', 'low'): 'M',
        (False, 'outside', 'middle'): 'H',
        (True, 'inside', 'high'): 'C',
        (True, 'inside', 'low'): 'P',
        (True, 'inside', 'middle'): 'K',
        (True, 'middle', 'high'): 'B',
        (True, 'middle', 'low'): 'Q',
        # (True, 'middle', 'middle'): 'Unknown', ## impossible
        (True, 'outside', 'high'): 'A',
        (True, 'outside', 'low'): 'L',
        (True, 'outside', 'middle'): 'G',
    }
    return mapping.get((row['is_obvious_off_zone'], row['horizontal_ending'], row['vertical_ending']), 'Unknown')

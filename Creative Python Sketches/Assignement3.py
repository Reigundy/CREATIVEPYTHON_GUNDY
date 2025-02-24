import os, random, time, math

WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.005

NUM_COLUMNS = 20
COLUMN_WIDTH = 3

COLUMN_CHAR = '0'
EMPTY_CHAR = ' '

GAP_SIZE = (WIDTH - COLUMN_WIDTH) // (NUM_COLUMNS + 1)
BETWEEN_TWIST_LENGTH_MIN = 0
BETWEEN_TWIST_LENGTH_MAX = 50
TWIST_LENGTH = 50

# The sine step increment makes the twist animation smooth:
SINE_STEP_INC = (math.pi / 2) / TWIST_LENGTH

# Start with the outermost columns instead
left_index = 1
right_index = NUM_COLUMNS

try:
    while True:
        # Draw the straight columns across the terminal:
        columns = [EMPTY_CHAR] * WIDTH
        for i in range(1, NUM_COLUMNS + 1):
            for j in range(COLUMN_WIDTH):
                columns[(i * GAP_SIZE) + j] = COLUMN_CHAR

        # Print a few lines of the straight columns:
        rows_between_twist = random.randint(BETWEEN_TWIST_LENGTH_MIN, BETWEEN_TWIST_LENGTH_MAX)
        for _ in range(rows_between_twist):
            print(''.join(columns))
            time.sleep(DELAY)

        # Calculate base positions for the two twist columns:
        left_base = left_index * GAP_SIZE
        right_base = right_index * GAP_SIZE
        # Calculate the maximum offset: I want the columns to move inward
        # without overlapping. The available distance is the gap between the columns  minus the column width.
        distance = right_base - left_base - COLUMN_WIDTH
        max_offset = distance // 2 if distance > 0 else 0

        # Twist Animation
        # Which column is twisting.
        for sine_step in range(TWIST_LENGTH):
            columns = [EMPTY_CHAR] * WIDTH
            offset = int(math.sin(sine_step * SINE_STEP_INC) * max_offset)
            # For the left twisting column, shift right by offset:
            left_pos = left_base + offset
            # For the right twisting column, shift left by offset:
            right_pos = right_base - offset

            # Draw the twisted left column:
            for j in range(COLUMN_WIDTH):
                if 0 <= left_pos + j < WIDTH:
                    columns[left_pos + j] = COLUMN_CHAR

            # Draw the twisted right column:
            for j in range(COLUMN_WIDTH):
                if 0 <= right_pos + j < WIDTH:
                    columns[right_pos + j] = COLUMN_CHAR

            # Draw the remaining (untwisted) columns:
            for i in range(1, NUM_COLUMNS + 1):
                if i == left_index or i == right_index:
                    continue
                base_pos = i * GAP_SIZE
                for j in range(COLUMN_WIDTH):
                    if 0 <= base_pos + j < WIDTH:
                        columns[base_pos + j] = COLUMN_CHAR

            print(''.join(columns))
            time.sleep(DELAY)

        # After the twist, move the twist pair inward.
        left_index += 1
        right_index -= 1
        # If they've crossed columns, then they reset back to the outermost columns.
        if left_index >= right_index:
            left_index = 1
            right_index = NUM_COLUMNS

except KeyboardInterrupt:
    print('Twists, by Al Sweigart al@inventwithpython.com 2024')
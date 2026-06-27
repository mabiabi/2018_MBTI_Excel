#!/usr/bin/env python3
"""
Generate a synthetic MBTI data set for high-school classes.
The output is written to `mbti_students.csv`.

Requirements
------------
* 31-38 students per class (10 classes → ~350 rows)
* Columns: class, I-E, S-N, T-F, J-P
* Scores are integers in the range 0-15
* Older grades trend toward higher Introversion and other realistic patterns
"""

import csv
import random

# ------------------------------------------------------------------
# 1. Per‑class configuration - tweak these as you like
# ------------------------------------------------------------------

# Default values if a class isn’t explicitly listed.
DEFAULT_STD_DEV        = 1.5          # usual spread for all classes
DEFAULT_SECTION_OFFSET = 0.3          # default shift between .1/.2

# ------------------------------------------------------------------
#   A dictionary that maps each class (e.g. "7.1") to its own STD_DEV.
#   If you don’t list a class here it will fall back to DEFAULT_STD_DEV.
# ------------------------------------------------------------------
STD_DEVS = {
    #   "class_id": std_dev
    # Example:
    "7.1": 2.1, "7.2": 3.2,
    "8.1": 2.1, "8.2": 3.2,
    "9.1": 2.1, "9.2": 3.2,
    "10.1": 2.1, "10.2": 3.2,
    "11.1": 2.1, "11.2": 3.2,
    "12.1": 2.1, "12.2": 3.2
}
#   3.605367838	2.500793525	3.991227152	3.318020383

# ------------------------------------------------------------------
#   A dictionary that maps each class (e.g. "7.1") to its own section_offset.
#   The offset is added *to the base mean* for every dimension.
#   Positive values shift the whole distribution upward, negative downward.
# ------------------------------------------------------------------
SECTION_OFFSETS = {
    #   "class_id": offset
    # Example:
    # "10.2": -0.5,
    # "9.1" : 0.7,
    "7.1": 0.1, "7.2": -0.2,
    "8.1": 0.1, "8.2": -0.2,
    "9.1": 0.1, "9.2": -0.2,
    "10.1": 0.1, "10.2": -0.2,
    "11.1": 0.1, "11.2": -0.2,
    "12.1": 0.1, "12.2": -0.2
}

SEED = 42                     # set to None for true randomness
NUM_STUDENTS_MIN = 29
NUM_STUDENTS_MAX = 36

# List of classes (grade.section)
CLASSES = [
    "7.1", "7.2",
    "8.1", "8.2",
    "9.1", "9.2",
    "10.1", "10.2",
    "11.1", "11.2",
    "12.1", "12.2"
]

# Base means per grade - older grades are slightly more Introverted,
# more Intuitive, Thinking and Judging.
GRADE_BASE_MEANS = {
    '7':  {'I-E': 9.4649,  'S-N': 7.4280, 'T-F': 10.311, 'J-P': 7.25892},
    '8':  {'I-E':9.116,  'S-N': 7.479, 'T-F': 10.7845, 'J-P': 7.803},
    '9':  {'I-E':9.1387,  'S-N': 7.6202, 'T-F': 11.287, 'J-P': 7.7988},
    '10': {'I-E':9.30,  'S-N': 7.33, 'T-F': 10.9272, 'J-P': 8.021},
    '11': {'I-E':9.580,  'S-N': 7.514, 'T-F': 11.410, 'J-P': 7.954},
    '12': {'I-E':9.948,  'S-N': 7.54, 'T-F': 11.6173, 'J-P': 7.3704}
}

# 9.464285714	7.428571429	10.32142857	7.25

# ------------------------------------------------------------------
# 2. Helper functions
# ------------------------------------------------------------------

def rng():
    """Return a random number generator that can be seeded."""
    return random.Random(SEED)

rand = rng()

def clip(val: float) -> int:
    """Clip the score to the 0-15 range and round to integer."""
    return max(0, min(15, int(round(val))))

def student_scores(base_means, std_dev):
    """Draw a single student's scores from N(mean, std_dev)."""
    return {dim: clip(rand.gauss(mean, std_dev))
            for dim, mean in base_means.items()}

# ------------------------------------------------------------------
# 3. Build the data set
# ------------------------------------------------------------------

rows = []

# for cls in CLASSES:
#     grade = cls.split('.')[0]          # e.g. '7' from '7.1'
#     base = GRADE_BASE_MEANS[grade].copy()
# 
#     # Add a small, deterministic section offset so that 7.1 and 7.2
#     # are not identical - this creates realistic inter‑section variation.
#     # The offsets can be tweaked if you want stronger differences.
#     section_offset = -0.3 if cls.endswith('.1') else 0.3
#     for dim in base:
#         base[dim] += section_offset
# 
#     n_students = rand.randint(NUM_STUDENTS_MIN, NUM_STUDENTS_MAX)
# 
#     for _ in range(n_students):
#         scores = student_scores(base)
#         rows.append([cls,
#                      scores['I-E'],
#                      scores['S-N'],
#                      scores['T-F'],
#                      scores['J-P']])

for cls in CLASSES:
    grade = cls.split('.')[0]
    # Grab the class‑specific STD_DEV, falling back to default.
    std_dev = STD_DEVS.get(cls, DEFAULT_STD_DEV)

    # Grab the class‑specific offset (e.g. 10.1 → +0.2, 7.2 → -0.4)
    section_offset = SECTION_OFFSETS.get(
        cls,
        DEFAULT_SECTION_OFFSET if cls.endswith('.2') else -DEFAULT_SECTION_OFFSET
    )

    base = GRADE_BASE_MEANS[grade].copy()

    # Apply the offset to every dimension.
    for dim in base:
        base[dim] += section_offset

    n_students = rand.randint(NUM_STUDENTS_MIN, NUM_STUDENTS_MAX)

    for _ in range(n_students):
        scores = student_scores(base, std_dev)
        rows.append([cls,
                     scores['I-E'],
                     scores['S-N'],
                     scores['T-F'],
                     scores['J-P']])


# ------------------------------------------------------------------
# 4. Write to CSV
# ------------------------------------------------------------------

output_file = "mbti_students.csv"
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['class', 'I-E', 'S-N', 'T-F', 'J-P'])
    writer.writerows(rows)

print(f"Generated {len(rows)} rows → {output_file}")

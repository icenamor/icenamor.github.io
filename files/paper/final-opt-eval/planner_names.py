TEAM_ID_TO_PLANNER_NAME = {
    1  : "fs-blind",
    2  : "DecStar",
    3  : "Symple-1",
    4  : "freelunch-madagascar",
    5  : "MSP",
    6  : "mercury2014",
    7  : "Saarplan",
    8  : "OLCFF",
    9  : "Complementary1",
    10 : "Symple-2",
    # 11 : "", # withdrawn
    # 12 : "", # withdrawn
    13 : "maplan-1",
    14 : "MERWIN",
    15 : "Cerberus",
    16 : "Cerberus-gl",
    17 : "maplan-2",
    18 : "IBaCoP-2018",
    # 19 : "", # recreated repository under different name
    20 : "LAPKT-DUAL-BFWS",
    21 : "Metis1",
    22 : "Metis2",
    23 : "Delfi1",
    24 : "Delfi2",
    # 25 : "", # recreated repository under different name
    26 : "FDMS1",
    27 : "FDMS2",
    # 28 : "", # submitted under different name
    # 29 : "", # withdrawn
    30 : "LAPKT-POLYNOMIAL-BFWS",
    31 : "LAPKT-DFS+",
    32 : "Complementary2",
    33 : "alien",
    34 : "freelunch-doubly-relaxed",
    35 : "IBaCoP2-2018",
    36 : "fs-sim",
    # 37 : "", # submitted under different name
    # 38 : "", # recreated repository under different name
    # 39 : "", # recreated repository under different name
    40 : "Planning-PDBs",
    # 41 : "", # submitted in canceled multi-core track
    # 42 : "", # withdrawn
    43 : "Fast Downward Remix",
    44 : "Scorpion",
    45 : "Fast Downward Stone Soup 2018",
    # 46 : "", # submitted in canceled multi-core track
    47 : "LAPKT-BFWS-Preference",
}

PLANNER_NAME_TO_TEAM_ID = {v : k for k, v in TEAM_ID_TO_PLANNER_NAME.items()}

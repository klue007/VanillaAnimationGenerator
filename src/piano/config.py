

PIANO_CONFIG= {

    "MARKER_TAG": "keyboard_console",

    "MIDI_PATH" : "",
    "BLOCK_PATH" : "",
    "DATAPACK_NAME" : "",
    "DATAPACK_VERSION" : 94,

    "DISPLAYER_KILL_AREA" : "dx=-22,dy=25,dz=162",
    "DISPLAYER_BLOCK" : "ochre_froglight",
    "DISPLAYER_COUNT_RIGHT" : 5,
    "DISPLAYER_COUNT_LEFT" : 5,
    "DISPLAYER_PEAK_HEIGHT" : 10.0,
    "DISPLAYER_MAX_MOVING_TICK" : 40,
    "DISPLAYER_SUMMON_CMD" : "summon item_display ~ ~ ~ {{item:{{id:\"{displayer_block}\"}},transformation:{{left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],scale:[1.0f,1.0f,1.0f],translation:[0.0f,0.0f,0.0f]}},Tags:[\"piano_displayer\",\"piano_displayer_{id}\"],Glowing:1b,brightness:{{sky:15,block:15}}}}",

    "TICK_RATE" : 32,
    "ALLOW_DURATIONS" : [0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 4.00],
    "SOUND_NAMESPACE" : "piano",
    "BASE_VOLUME" : 1.0,
    "MIN_VOLUME" : 0.20,

    "BLOCK_SPLITS" : 3200,

    "PLAYSOUND_TPL" : (
        "execute "
        "positioned ~100 ~-20 ~-20 as @a[dx=-180,dy=100,dz=197] at @s "
        "run playsound {sound} master @s ~ ~ ~ {vol} 1"
    ),

    "SCOREBOARD_TPL" : (
        "scoreboard players set @s "
        "note_{note_num} {tick_len}"
    ),

    "MOTION_Y" : 1.0,
    "MOTION_Y_RANDOM" : 1.5,
    "PAINTING_BASE_POS" : [7, -19, -51],

    "NOTE_DUR_EXTRA_MS": 0,

    "NOTE_POS" : {
        22: [0.0, 3.0, 4.0],
        25: [0.0, 3.0, 9.0],
        27: [0.0, 3.0, 13.0],
        30: [0.0, 3.0, 19.0],
        32: [0.0, 3.0, 22.0],
        34: [0.0, 3.0, 25.0],
        37: [0.0, 3.0, 31.0],
        39: [0.0, 3.0, 34.0],
        42: [0.0, 3.0, 40.0],
        44: [0.0, 3.0, 43.0],
        46: [0.0, 3.0, 46.0],
        49: [0.0, 3.0, 52.0],
        51: [0.0, 3.0, 55.0],
        54: [0.0, 3.0, 61.0],
        56: [0.0, 3.0, 64.0],
        58: [0.0, 3.0, 67.0],
        61: [0.0, 3.0, 73.0],
        63: [0.0, 3.0, 76.0],
        66: [0.0, 3.0, 82.0],
        68: [0.0, 3.0, 85.0],
        70: [0.0, 3.0, 88.0],
        73: [0.0, 3.0, 94.0],
        75: [0.0, 3.0, 97.0],
        78: [0.0, 3.0, 103.0],
        80: [0.0, 3.0, 106.0],
        82: [0.0, 3.0, 109.0],
        85: [0.0, 3.0, 115.0],
        87: [0.0, 3.0, 118.0],
        90: [0.0, 3.0, 124.0],
        92: [0.0, 3.0, 127.0],
        94: [0.0, 3.0, 130.0],
        97: [0.0, 3.0, 136.0],
        99: [0.0, 3.0, 139.0],
        102: [0.0, 3.0, 145.0],
        104: [0.0, 3.0, 148.0],
        106: [0.0, 3.0, 151.0],
        21: [0.0, 2.0, 2.5],
        23: [0.0, 2.0, 5.5],
        24: [0.0, 2.0, 8.5],
        26: [0.0, 2.0, 11.5],
        28: [0.0, 2.0, 14.5],
        29: [0.0, 2.0, 17.5],
        31: [0.0, 2.0, 20.5],
        33: [0.0, 2.0, 23.5],
        35: [0.0, 2.0, 26.5],
        36: [0.0, 2.0, 29.5],
        38: [0.0, 2.0, 32.5],
        40: [0.0, 2.0, 35.5],
        41: [0.0, 2.0, 38.5],
        43: [0.0, 2.0, 41.5],
        45: [0.0, 2.0, 44.5],
        47: [0.0, 2.0, 47.5],
        48: [0.0, 2.0, 50.5],
        50: [0.0, 2.0, 53.5],
        52: [0.0, 2.0, 56.5],
        53: [0.0, 2.0, 59.5],
        55: [0.0, 2.0, 62.5],
        57: [0.0, 2.0, 65.5],
        59: [0.0, 2.0, 68.5],
        60: [0.0, 2.0, 71.5],
        62: [0.0, 2.0, 74.5],
        64: [0.0, 2.0, 77.5],
        65: [0.0, 2.0, 80.5],
        67: [0.0, 2.0, 83.5],
        69: [0.0, 2.0, 86.5],
        71: [0.0, 2.0, 89.5],
        72: [0.0, 2.0, 92.5],
        74: [0.0, 2.0, 95.5],
        76: [0.0, 2.0, 98.5],
        77: [0.0, 2.0, 101.5],
        79: [0.0, 2.0, 104.5],
        81: [0.0, 2.0, 107.5],
        83: [0.0, 2.0, 110.5],
        84: [0.0, 2.0, 113.5],
        86: [0.0, 2.0, 116.5],
        88: [0.0, 2.0, 119.5],
        89: [0.0, 2.0, 122.5],
        91: [0.0, 2.0, 125.5],
        93: [0.0, 2.0, 128.5],
        95: [0.0, 2.0, 131.5],
        96: [0.0, 2.0, 134.5],
        98: [0.0, 2.0, 137.5],
        100: [0.0, 2.0, 140.5],
        101: [0.0, 2.0, 143.5],
        103: [0.0, 2.0, 146.5],
        105: [0.0, 2.0, 149.5],
        107: [0.0, 2.0, 152.5],
        108: [0.0, 2.0, 155.5]
    },

    "BLOCK_PAINTING": 1,
    "DISPLAYER": 1,
    "DISPLAYER_VORTEX": 11,
    "VORTEX_POOL": 1,

    "DELAY_MS": 0,
}

PIANO_MINI_CONFIG= {

    "MARKER_TAG": "keyboard_mini_console",

    "MIDI_PATH" : "",
    "BLOCK_PATH" : "",
    "DATAPACK_NAME" : "",
    "DATAPACK_VERSION" : 94,

    "DISPLAYER_KILL_AREA" : "dx=2,dy=2,dz=5",
    "DISPLAYER_BLOCK" : "ochre_froglight",
    "DISPLAYER_COUNT_RIGHT" : 5,
    "DISPLAYER_COUNT_LEFT" : 5,
    "DISPLAYER_PEAK_HEIGHT" : 0.1,
    "DISPLAYER_MAX_MOVING_TICK" : 40,
    "DISPLAYER_SUMMON_CMD" : "summon item_display ~ ~1 ~ {{item:{{id:\"{displayer_block}\"}},transformation:{{left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],scale:[0.03f,0.03f,0.03f],translation:[0.0f,0.0f,0.0f]}},Tags:[\"piano_displayer\",\"piano_displayer_{id}\"],Glowing:1b,brightness:{{sky:15,block:15}}}}",

    "TICK_RATE" : 32,
    "ALLOW_DURATIONS" : [0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 4.00],
    "SOUND_NAMESPACE" : "piano",
    "BASE_VOLUME" : 1.0,
    "MIN_VOLUME" : 0.20,

    "BLOCK_SPLITS" : 3200,

    "PLAYSOUND_TPL" : (
        "execute "
        "at @s "
        "run playsound {sound} master @a ~ ~ ~2 {vol} 1"
    ),

    "SCOREBOARD_TPL" : (
        "scoreboard players set @s "
        "note_{note_num} {tick_len}"
    ),

    "MOTION_Y" : 1.0,
    "MOTION_Y_RANDOM" : 1.5,
    "PAINTING_BASE_POS" : [7, -19, -51],

    "NOTE_DUR_EXTRA_MS": 600,

    "NOTE_POS" : {
        22: [0.550, 1.14, 0.125],
        25: [0.550, 1.14, 0.275],
        27: [0.550, 1.14, 0.350],
        30: [0.550, 1.14, 0.500],
        32: [0.550, 1.14, 0.575],
        34: [0.550, 1.14, 0.650],
        37: [0.550, 1.14, 0.800],
        39: [0.550, 1.14, 0.875],
        42: [0.550, 1.14, 1.025],
        44: [0.550, 1.14, 1.100],
        46: [0.550, 1.14, 1.175],
        49: [0.550, 1.14, 1.325],
        51: [0.550, 1.14, 1.400],
        54: [0.550, 1.14, 1.550],
        56: [0.550, 1.14, 1.625],
        58: [0.550, 1.14, 1.700],
        61: [0.550, 1.14, 1.850],
        63: [0.550, 1.14, 1.925],
        66: [0.550, 1.14, 2.075],
        68: [0.550, 1.14, 2.150],
        70: [0.550, 1.14, 2.225],
        73: [0.550, 1.14, 2.375],
        75: [0.550, 1.14, 2.450],
        78: [0.550, 1.14, 2.600],
        80: [0.550, 1.14, 2.675],
        82: [0.550, 1.14, 2.750],
        85: [0.550, 1.14, 2.900],
        87: [0.550, 1.14, 2.975],
        90: [0.550, 1.14, 3.125],
        92: [0.550, 1.14, 3.200],
        94: [0.550, 1.14, 3.275],
        97: [0.550, 1.14, 3.425],
        99: [0.550, 1.14, 3.500],
        102: [0.550, 1.14, 3.650],
        104: [0.550, 1.14, 3.725],
        106: [0.550, 1.14, 3.800],
        21: [0.550, 1.1, 0.0875],
        23: [0.550, 1.1, 0.1625],
        24: [0.550, 1.1, 0.2375],
        26: [0.550, 1.1, 0.3125],
        28: [0.550, 1.1, 0.3875],
        29: [0.550, 1.1, 0.4625],
        31: [0.550, 1.1, 0.5375],
        33: [0.550, 1.1, 0.6125],
        35: [0.550, 1.1, 0.6875],
        36: [0.550, 1.1, 0.7625],
        38: [0.550, 1.1, 0.8375],
        40: [0.550, 1.1, 0.9125],
        41: [0.550, 1.1, 0.9875],
        43: [0.550, 1.1, 1.0625],
        45: [0.550, 1.1, 1.1375],
        47: [0.550, 1.1, 1.2125],
        48: [0.550, 1.1, 1.2875],
        50: [0.550, 1.1, 1.3625],
        52: [0.550, 1.1, 1.4375],
        53: [0.550, 1.1, 1.5125],
        55: [0.550, 1.1, 1.5875],
        57: [0.550, 1.1, 1.6625],
        59: [0.550, 1.1, 1.7375],
        60: [0.550, 1.1, 1.8125],
        62: [0.550, 1.1, 1.8875],
        64: [0.550, 1.1, 1.9625],
        65: [0.550, 1.1, 2.0375],
        67: [0.550, 1.1, 2.1125],
        69: [0.550, 1.1, 2.1875],
        71: [0.550, 1.1, 2.2625],
        72: [0.550, 1.1, 2.3375],
        74: [0.550, 1.1, 2.4125],
        76: [0.550, 1.1, 2.4875],
        77: [0.550, 1.1, 2.5625],
        79: [0.550, 1.1, 2.6375],
        81: [0.550, 1.1, 2.7125],
        83: [0.550, 1.1, 2.7875],
        84: [0.550, 1.1, 2.8625],
        86: [0.550, 1.1, 2.9375],
        88: [0.550, 1.1, 3.0125],
        89: [0.550, 1.1, 3.0875],
        91: [0.550, 1.1, 3.1625],
        93: [0.550, 1.1, 3.2375],
        95: [0.550, 1.1, 3.3125],
        96: [0.550, 1.1, 3.3875],
        98: [0.550, 1.1, 3.4625],
        100: [0.550, 1.1, 3.5375],
        101: [0.550, 1.1, 3.6125],
        103: [0.550, 1.1, 3.6875],
        105: [0.550, 1.1, 3.7625],
        107: [0.550, 1.1, 3.8375],
        108: [0.550, 1.1, 3.9125],
    },

    "BLOCK_PAINTING": 11,
    "DISPLAYER": 1,
    "DISPLAYER_VORTEX": 11,
    "VORTEX_POOL": 1,

    "DELAY_MS": 3000,
}

PIANO_VORTEX_CONFIG= {

    "MARKER_TAG": "keyboard_mini_console",

    "MIDI_PATH" : "",
    "BLOCK_PATH" : "",
    "DATAPACK_NAME" : "",
    "DATAPACK_VERSION" : 94,

    "DISPLAYER_KILL_AREA" : "distance=..16",
    "DISPLAYER_BLOCK" : "ochre_froglight",
    "DISPLAYER_COUNT_RIGHT" : 5,
    "DISPLAYER_COUNT_LEFT" : 5,
    "DISPLAYER_PEAK_HEIGHT" : 1.25,
    "DISPLAYER_MAX_MOVING_TICK" : 40,
    "DISPLAYER_SUMMON_CMD" : "summon item_display ~ ~1 ~ {{item:{{id:\"{displayer_block}\"}},transformation:{{left_rotation:[0.0f,0.0f,0.0f,1.0f],right_rotation:[0.0f,0.0f,0.0f,1.0f],scale:[0.5f,0.5f,0.5f],translation:[0.0f,0.0f,0.0f]}},Tags:[\"piano_displayer\",\"piano_displayer_{id}\"],Glowing:1b,brightness:{{sky:15,block:15}}}}",

    "TICK_RATE" : 32,
    "ALLOW_DURATIONS" : [0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 4.00],
    "SOUND_NAMESPACE" : "piano",
    "BASE_VOLUME" : 1.0,
    "MIN_VOLUME" : 0.20,

    "BLOCK_SPLITS" : 3200,

    "PLAYSOUND_TPL" : (
        "execute "
        "at @s as @a[distance=..45] at @s "
        "run playsound {sound} master @s ~ ~ ~ {vol} 1"
    ),

    "SCOREBOARD_TPL" : (
        "scoreboard players set @s "
        "note_{note_num} {tick_len}"
    ),

    "MOTION_Y" : 1.0,
    "MOTION_Y_RANDOM" : 1.5,
    "PAINTING_BASE_POS" : [7, -19, -51],

    "NOTE_DUR_EXTRA_MS": 600,

    "NOTE_POS" : {
       21: [5.08421, 0, -11.41932],
       22: [5.67488, 0.399, -11.13758],
       23: [6.25000, 0, -10.82532],
       24: [7.34732, 0, -10.11271],
       25: [7.86650, 0.399, -9.71432],
       26: [8.36413, 0, -9.28931],
       27: [8.83883, 0.399, -8.83883],
       28: [9.28931, 0, -8.36413],
       29: [10.11271, 0, -7.34732],
       30: [10.48338, 0.399, -6.80799],
       31: [10.82532, 0, -6.25000],
       32: [11.13758, 0.399, -5.67488],
       33: [11.41932, 0, -5.08421],
       34: [11.66976, 0.399, -4.47960],
       35: [11.88821, 0, -3.86271],
       36: [12.22685, 0, -2.59890],
       37: [12.34610, 0.399, -1.95543],
       38: [12.43152, 0, -1.30661],
       39: [12.48287, 0.399, -0.65420],
       40: [12.50000, 0, 0.00000],
       41: [12.43152, 0, 1.30661],
       42: [12.34610, 0.399, 1.95543],
       43: [12.22685, 0, 2.59890],
       44: [12.07407, 0.399, 3.23524],
       45: [11.88821, 0, 3.86271],
       46: [11.66976, 0.399, 4.47960],
       47: [11.41932, 0, 5.08421],
       48: [10.82532, 0, 6.25000],
       49: [10.48338, 0.399, 6.80799],
       50: [10.11271, 0, 7.34732],
       51: [9.71432, 0.399, 7.86650],
       52: [9.28931, 0, 8.36413],
       53: [8.36413, 0, 9.28931],
       54: [7.86650, 0.399, 9.71432],
       55: [7.34732, 0, 10.11271],
       56: [6.80799, 0.399, 10.48338],
       57: [6.25000, 0, 10.82532],
       58: [5.67488, 0.399, 11.13758],
       59: [5.08421, 0, 11.41932],
       60: [3.86271, 0, 11.88821],
       61: [3.23524, 0.399, 12.07407],
       62: [2.59890, 0, 12.22685],
       63: [1.95543, 0.399, 12.34610],
       64: [1.30661, 0, 12.43152],
       65: [0.00000, 0, 12.50000],
       66: [-0.65420, 0.399, 12.48287],
       67: [-1.30661, 0, 12.43152],
       68: [-1.95543, 0.399, 12.34610],
       69: [-2.59890, 0, 12.22685],
       70: [-3.23524, 0.399, 12.07407],
       71: [-3.86271, 0, 11.88821],
       72: [-5.08421, 0, 11.41932],
       73: [-5.67488, 0.399, 11.13758],
       74: [-6.25000, 0, 10.82532],
       75: [-6.80799, 0.399, 10.48338],
       76: [-7.34732, 0, 10.11271],
       77: [-8.36413, 0, 9.28931],
       78: [-8.83883, 0.399, 8.83883],
       79: [-9.28931, 0, 8.36413],
       80: [-9.71432, 0.399, 7.86650],
       81: [-10.11271, 0, 7.34732],
       82: [-10.48338, 0.399, 6.80799],
       83: [-10.82532, 0, 6.25000],
       84: [-11.41932, 0, 5.08421],
       85: [-11.66976, 0.399, 4.47960],
       86: [-11.88821, 0, 3.86271],
       87: [-12.07407, 0.399, 3.23524],
       88: [-12.22685, 0, 2.59890],
       89: [-12.43152, 0, 1.30661],
       90: [-12.48287, 0.399, 0.65420],
       91: [-12.50000, 0, 0.00000],
       92: [-12.48287, 0.399, -0.65420],
       93: [-12.43152, 0, -1.30661],
       94: [-12.34610, 0.399, -1.95543],
       95: [-12.22685, 0, -2.59890],
       96: [-11.88821, 0, -3.86271],
       97: [-11.66976, 0.399, -4.47960],
       98: [-11.41932, 0, -5.08421],
       99: [-11.13758, 0.399, -5.67488],
       100: [-10.82532, 0, -6.25000],
       101: [-10.11271, 0, -7.34732],
       102: [-9.71432, 0.399, -7.86650],
       103: [-9.28931, 0, -8.36413],
       104: [-8.83883, 0.399, -8.83883],
       105: [-8.36413, 0, -9.28931],
       106: [-7.86650, 0.399, -9.71432],
       107: [-7.34732, 0, -10.11271],
       108: [-6.25000, 0, -10.82532],
    },

    "BLOCK_PAINTING": 11,
    "DISPLAYER": 1,
    "DISPLAYER_VORTEX": 1,
    "VORTEX_POOL": 1,

    "DELAY_MS": 1000,
}

class PianoConfigPresets():

    def __init__(self):
        self.piano = PIANO_CONFIG
        self.piano_mini = PIANO_MINI_CONFIG
        self.piano_vortex = PIANO_VORTEX_CONFIG


class PianoConfig():
    def __init__(self, preset: dict):
        self.marker_tag = preset["MARKER_TAG"]
        self.displayer_kill_area = preset["DISPLAYER_KILL_AREA"]
        self.displayer_block = preset["DISPLAYER_BLOCK"]
        self.displayer_count_right = preset["DISPLAYER_COUNT_RIGHT"]
        self.displayer_count_left = preset["DISPLAYER_COUNT_LEFT"]
        self.displayer_peak_height = preset["DISPLAYER_PEAK_HEIGHT"]
        self.displayer_max_moving_tick = preset["DISPLAYER_MAX_MOVING_TICK"]
        self.displayer_summon_cmd = preset["DISPLAYER_SUMMON_CMD"]
        self.tick_rate = preset["TICK_RATE"]
        self.allow_durations = preset["ALLOW_DURATIONS"]
        self.sound_namespace = preset["SOUND_NAMESPACE"]
        self.base_volume = preset["BASE_VOLUME"]
        self.min_volume = preset["MIN_VOLUME"]
        self.block_splits = preset["BLOCK_SPLITS"]
        self.playsound_tpl = preset["PLAYSOUND_TPL"]
        self.scoreboard_tpl = preset["SCOREBOARD_TPL"]
        self.motion_y = preset["MOTION_Y"]
        self.motion_y_random = preset["MOTION_Y_RANDOM"]
        self.note_dur_extra_ms = preset["NOTE_DUR_EXTRA_MS"]
        self.note_pos = preset["NOTE_POS"]
        self.block_painting = preset["BLOCK_PAINTING"]
        self.displayer = preset["DISPLAYER"]
        self.displayer_vortex = preset["DISPLAYER_VORTEX"]
        self.vortex_pool = preset["VORTEX_POOL"]
        self.delay_ms = preset["DELAY_MS"]
        self.painting_base_pos = preset["PAINTING_BASE_POS"]
        self.midi_path = preset["MIDI_PATH"]
        self.block_path = preset["BLOCK_PATH"]
        self.datapack_name = preset["DATAPACK_NAME"]
        self.datapack_version = preset["DATAPACK_VERSION"]




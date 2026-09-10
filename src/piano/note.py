
import mido
from mido import MidiFile
from src.piano.config import PianoConfig

class Note:
    """
    A class that records note information.
    """

    def __init__(self, midi_number: int, start_second: float, velocity: float, duration_second: float, track: int, config: PianoConfig):
        self.midi_number = midi_number
        self.start_second = start_second + config.delay_ms / 1000
        self.velocity = velocity
        self.duration_second = duration_second + config.note_dur_extra_ms / 1000
        self.track = track
        self.get_ingame(config)

    def get_ingame(self, config: PianoConfig):
        self.mc_tick = round(self.start_second * config.tick_rate)
        self.error_time = abs(self.mc_tick / config.tick_rate - self.start_second)

        self.ingame_duration = min(config.allow_durations, key=lambda x: abs(x - self.duration_second * config.tick_rate / 20))
        self.sound_id = f"{config.sound_namespace}:{self.midi_number}_{self.ingame_duration:.2f}"
        self.volume = config.base_volume * (self.velocity / 127.0)
        self.volume = round(self.volume,3)
        self.volume = max(self.volume,config.min_volume)


def midi_parse(midi_file: MidiFile, config: PianoConfig) -> list[Note]:
    """
    Read and translate MIDI information.

    Args:
        midi_file : (MidiFile)
    """

    ticks_per_beat = midi_file.ticks_per_beat
    tempo = mido.midifiles.midifiles.DEFAULT_TEMPO

    all_events = []  # (absolute_tick, message)

    # Collect information and calculate the absolute tick
    track_num = 0
    for track in midi_file.tracks:
        absolute_tick = 0
        track_num += 1
        for message in track:
            absolute_tick += message.time
            all_events.append((absolute_tick, message, track_num))

    all_events.sort(key=lambda x: x[0])

    note_on_cache = dict()   # note : (midi_absolute_tick, velocity)

    # Record the absolute tick and duration
    current_midi_abs = 0
    current_seconds = 0.0

    # output list
    output_note_list = []

    for midi_absolute_tick, msg, track in all_events:

        delta_sec = mido.tick2second(midi_absolute_tick - current_midi_abs, ticks_per_beat, tempo)
        current_seconds += delta_sec
        current_midi_abs = midi_absolute_tick

        if msg.is_meta:
            if msg.type == "set_tempo":
                tempo = msg.tempo
            continue

        note = getattr(msg, "note", 0)
        vel = getattr(msg, "velocity", 0)

        if note == 0:
            continue

        if msg.type == "note_on" and vel > 0:
            note_on_cache[note] = (current_seconds, vel)

        elif (msg.type == "note_off") or (msg.type == "note_on" and vel == 0):
            if note in note_on_cache:
                start_sec, start_vel = note_on_cache.pop(note)
                dur_sec = current_seconds - start_sec
                output_note_list.append(Note(note, start_sec, start_vel, dur_sec, track, config))

    output_note_list.sort(key=lambda x: x.midi_number)
    return output_note_list
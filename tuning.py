#!/usr/bin/env python
"""A library for dealing with many tuning systems including just intonation."""
import sympy
import playback


class EqualTemperament:
    """
    Process any equal temperament, not just 12TET, given a step size in cents.

    The equal temperament need not be octave repeating.
    """

    def __init__(self, step_size):

        print("Equal temperament system initialized.")
        self.step_size = step_size

    def set_tonic_frequency(self, frequency):
        """Set tonic frequency."""
        self.frequency = frequency


class JustIntonation:
    """Process just intonation of any prime limit."""

    def __init__(self, limit):

        print("Just intonation system initialized.")
        self.limit = limit
        self.primes = list(sympy.sieve.primerange(1, self.limit))

    def set_tonic_frequency(self, frequency):
        """Set tonic frequency."""
        self.frequency = frequency


class ArbitraryTuning:
    """Process any arbitrary tuning given a list of ratios."""

    def __init__(self, ratios):

        print("Arbitrary tuning system initialized.")
        self.ratios = ratios

    def set_tonic_frequency(self, frequency):
        """Set tonic frequency."""
        self.frequency = frequency


class Stream:
    """Output audio."""

    def __init__(self):

        print("Stream created.")
        self.intervals = []
        self.frequency = None

    def set_intervals(self, intervals):
        """Set intervals."""
        self.intervals = intervals

    def play(self):
        """Play."""
        # below line will be removed.
        self.frequency = 220.0
        print("Playing starting frequency: " + str(self.frequency) + " hz.")
        playback.play(playback.sine_wave(self.frequency, 4096), 1000)
        frequencies = [self.frequency]
        for interval in self.intervals:
            self.frequency *= interval
            print("Playing a " + str(interval)
                  + " to: " + str(self.frequency) + " hz.")
            playback.play(playback.sine_wave(self.frequency, 4096), 1000)
            frequencies.append(self.frequency)
        return frequencies


def comma_pump(frequency):
    """Comma pump."""
    print("Demonstrating the syntonic comma. Starting at "
          + str(frequency) + " hz.")
    intervals = [3/2, 3/4, 3/2, 3/4, 4/5]
    stream = Stream()
    stream.set_intervals(intervals)
    notes = stream.play()
    print("Playing starting note: " + str(frequency)
          + " hz, again for comparison.")
    playback.play(playback.sine_wave(frequency, 4096), 1000)
    print("Hear the difference?")
    return notes


def main():
    """Main."""
    """
    alpha_scale = pd.read_csv(os.path.join("tunings", "equal temperaments",
                                           "alpha.csv"))
    beta_scale = pd.read_csv(os.path.join("tunings", "equal temperaments",
                                          "beta.csv"))
    gamma_scale = pd.read_csv(os.path.join("tunings", "equal temperaments",
                                           "gamma.csv"))
    """
    # syntonic_comma = 1.0125
    comma_pump(220.0)


if __name__ == "__main__":

    main()

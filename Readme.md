<h1>Bach in a Box</h1>

<h2>This is a Python program designed to generate music in a baroque style, use counterpoint, and to handle calculations related to just intonation.</h2>

<h3>It makes extensive use of:</h3>

- [Music21](http://web.mit.edu/music21/ "Music21")

- [PyQt5](https://pypi.org/project/PyQt5/ "PyQt5")

Before running for the first time, run build.bat on Windows. --- not needed yet

If the program doesn't run at all on Linux, run dos2unix on it. This SHOULD rectify the issue. The dos2unix package is easy to get for Arch-based distrobutions in the AUR.

License only applies to work done by me and excludes small portions like the following. They are licensed under their respective licenses (GNU, MIT, etc.):

- Art of Fugue example midi converted from a score by Pikabolt5 [here](https://musescore.com/pikabolt5/the-art-of-fugue-contrapunctus-i "Art of Fugue") licensed under [Creative Commons Zero](https://creativecommons.org/publicdomain/zero/1.0/ "Creative Commons Zero").

- Logo in docs folder made from a public domain painting of Bach and a image by Svengraph [here](https://commons.wikimedia.org/wiki/File:Svengraph_Box.png "Box image") licensed under [Creative Commons Attribution 3.0 Unported](https://creativecommons.org/licenses/by/3.0/deed.en "Creative Commons Attribution 3.0 Unported")

<h3>Planned Features:</h3>

- UI in PyQt5

- Use of scipy and numpy for mathematical calculations

- SuperCollider audio output through osc4py3(Documented here: https://osc4py3.readthedocs.io/en/latest/) or oscpy(Source here: https://github.com/kivy/oscpy)

- 100% cross-platform

- Less unneeded code and better performance

Resources:

[Xen Wiki](https://en.xen.wiki/)

[Counterpoint](https://en.wikipedia.org/wiki/Counterpoint)

Species of Counterpoint

1. Note against note;
2. Two notes against one;
3. Four notes against one;
4. Notes offset against each other (as suspensions);
5. All the first four species together, as "florid" counterpoint.

Considerations for all Species

The following rules apply to melodic writing in each species, for each part:

1. The final must be approached by step. If the final is approached from below, then the leading tone must be raised in a minor key (Dorian, Hypodorian, Aeolian, Hypoaeolian), but not in Phrygian or Hypophrygian mode. Thus, in the Dorian mode on D, a C♯ is necessary at the cadence.[11]
2. Permitted melodic intervals are the perfect fourth, fifth, and octave, as well as the major and minor second, major and minor third, and ascending minor sixth. The ascending minor sixth must be immediately followed by motion downwards.
3. If writing two skips in the same direction—something that must be only rarely done—the second must be smaller than the first, and the interval between the first and the third note may not be dissonant. The three notes should be from the same triad; if this is impossible, they should not outline more than one octave. In general, do not write more than two skips in the same direction.
4. If writing a skip in one direction, it is best to proceed after the skip with motion in the other direction.
5. The interval of a tritone in three notes should be avoided (for example, an ascending melodic motion F–A–B♮)[12] as is the interval of a seventh in three notes.
6. There must be a climax or high point in the line countering the cantus firmus. This usually occurs somewhere in the middle of exercise and must occur on a strong beat.
7. An outlining of a seventh is avoided within a single line moving in the same direction.

And, in all species, the following rules govern the combination of the parts:

1. The counterpoint must begin and end on a perfect consonance.
2. Contrary motion should dominate.
3. Perfect consonances must be approached by oblique or contrary motion.
4. Imperfect consonances may be approached by any type of motion.
5. The interval of a tenth should not be exceeded between two adjacent parts unless by necessity.
6. Build from the bass, upward.

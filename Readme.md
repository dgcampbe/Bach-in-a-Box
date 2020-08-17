# Bach-in-a-Box
## A Python program to generate music and tuning systems.
### Dependencies
Requires:
* Python 3
	* [Music21](https://web.mit.edu/music21/)
	* [PyQt5](https://pypi.org/project/PyQt5/)
	* [Mido](https://pypi.org/project/mido/)

### Licensing:
* Code licensed under [GNU Affero GPL v3](https://www.gnu.org/licenses/agpl-3.0.html)
* Art of Fugue example midi converted from a score by Pikabolt5 [here](https://musescore.com/pikabolt5/the-art-of-fugue-contrapunctus-i) licensed under [Creative Commons Zero](https://creativecommons.org/publicdomain/zero/1.0/).
* Logo in docs folder made from a public domain painting of Bach and a image by Svengraph [here](https://commons.wikimedia.org/wiki/File:Svengraph_Box.png) licensed under [Creative Commons Attribution 3.0 Unported](https://creativecommons.org/licenses/by/3.0/deed.en)

### Current Features:
* Generates random midi files
* Converts midi files to dectalk (inspired by 7coil/midi-to-dectalk)

### Planned Features:
* UI in PyQt5
* Use of scipy and numpy for mathematical calculations
* SuperCollider audio output through [python-supercollider](https://github.com/ideoforms/python-supercollider)
* 100% cross-platform
* Less unneeded code and better performance

Resources:
* [Xen Wiki](https://en.xen.wiki/)
* [Counterpoint](https://en.wikipedia.org/wiki/Counterpoint)
* [Maqam](https://www.youtube.com/watch?v=IwS8LfGlCTk)
* [Counterpoint](https://en.wikipedia.org/wiki/Counterpoint)
* [Canon](https://www.youtube.com/watch?v=OiG_5HcuJnc)
	1. Pick key and number of measures to lead
	2. First note in leader is the tonic
	3. Make catchy theme to lead
	4. Copy lead to second voice, transposed by octave
	5. Harmonize the leader to the copied lead
	6. Thirds, fifths, and sixths are harmonious
	7. Fourths are dissonant
	8. No parallel fifths, avoid unison
	9. Rinse and Repeat

Jokes
* The Well Justified Clavier
* Nobody expects the Spanish Intonation

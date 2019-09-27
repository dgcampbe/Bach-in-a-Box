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

<h3>Here are some basic reading</h3>

- https://en.wikipedia.org/wiki/Five-limit_tuning

- More sources coming. To be honest, I don't know everything about this either. I am learning through experience. :P

<h3>Planned Features:</h3>

- UI in PyQt5

- Use of scipy and numpy for mathematical calculations

- SuperCollider audio output through osc4py3(Documented here: https://osc4py3.readthedocs.io/en/latest/) or oscpy(Source here: https://github.com/kivy/oscpy)

- 100% cross-platform

- Less unneeded code and better performance
from __future__ import unicode_literals
import re

VOWELS = 'aoeui'

specialsyllables_en = """\
tottered 2
chummed 1
peeped 1
moustaches 2
shamefully 3
messieurs 2
satiated 4
sailmaker 4
sheered 1
disinterred 3
propitiatory 6
bepatched 2
particularized 5
caressed 2
trespassed 2
sepulchre 3
flapped 1
hemispheres 3
pencilled 2
motioned 2
poleman 2
slandered 2
sombre 2
etc 4
sidespring 2
mimes 1
effaces 2
mr 2
mrs 2
ms 1
dr 2
st 1
sr 2
jr 2
truckle 2
foamed 1
fringed 2
clattered 2
capered 2
mangroves 2
suavely 2
reclined 2
brutes 1
effaced 2
quivered 2
h'm 1
veriest 3
sententiously 4
deafened 2
manoeuvred 3
unstained 2
gaped 1
stammered 2
shivered 2
discoloured 3
gravesend 2
60 2
lb 1
unexpressed 3
greyish 2
unostentatious 5
"""

fallback_cache = {}
_fallback_subsyl = ["cial", "tia", "cius", "cious", "gui", "ion", "iou",
                    "sia$", ".ely$"]
_fallback_addsyl = ["ia", "riet", "dien", "iu", "io", "ii",
                    "[aeiouy]bl$", "mbl$",
                    "[aeiou]{3}",
                    "^mc", "ism$",
                    "(.)(?!\\1)([aeiouy])\\2l$",
                    "[^l]llien",
                    "^coad.", "^coag.", "^coal.", "^coax.",
                    "(.)(?!\\1)[gq]ua(.)(?!\\2)[aeiou]",
                    "dnt$"]
fallback_subsyl = [re.compile(a) for a in _fallback_subsyl]
fallback_addsyl = [re.compile(a) for a in _fallback_addsyl]


def _normalize_word(word):
    return word.strip().lower()


# Read syllable overrides and populate cache with them
for line in specialsyllables_en.splitlines():
    line = line.strip()
    if line:
        toks = line.split()
        assert len(toks) == 2
        fallback_cache[_normalize_word(toks[0])] = int(toks[1])


def countsyllables_en(word):
    if not word:
        return 0

    # Remove final silent 'e'
    if word[-1] == "e":
        word = word[:-1]

    # Check for a cached syllable count
    if word in fallback_cache:
        return fallback_cache[word]

    # Count vowel groups
    result = 0
    prev_was_vowel = False
    for char in word:
        is_vowel = char in VOWELS or char == 'y'
        if is_vowel and not prev_was_vowel:
            result += 1
        prev_was_vowel = is_vowel

    # Add & subtract syllables
    for r in fallback_addsyl:
        if r.search(word):
            result += 1
    for r in fallback_subsyl:
        if r.search(word):
            result -= 1

    # Cache the syllable count
    fallback_cache[word] = result

    return result


LANGDATA = dict(
        syllables=countsyllables_en
)

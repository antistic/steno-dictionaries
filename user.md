# User

My user dictionary.

**Requires:**
 - [plover-markdown-dictionary](https://github.com/antistic/plover-markdown-dictionary)

**Table of contents:**
- [Punctuation](#punctuation)
- [Keyboard Control](#keyboard-control)
  - [Keys](#keys)
  - [Plover](#plover)
  - [i3 (window manager)](#i3-window-manager)
  - [Other Programs](#other-programs)
  - [Dictionary Control](#dictionary-control)
  - [Plover Plugins](#plover-plugins)
- [Changes](#changes)
  - [Dropped syllables](#dropped-syllables)
  - [Compacted (still steno order)](#compacted-still-steno-order)
  - [Folding](#folding)
  - [Orthography fixes](#orthography-fixes)
  - [Different emphasis](#different-emphasis)
  - [Different word boundaries](#different-word-boundaries)
  - [Different way of writing word parts](#different-way-of-writing-word-parts)
  - [Accidentally adding a prefix to a brief.](#accidentally-adding-a-prefix-to-a-brief)
  - [Alternative by spelling](#alternative-by-spelling)
  - [Alternative by pronunciation](#alternative-by-pronunciation)
  - [Star](#star)
  - [Swaps/shuffles](#swapsshuffles)
  - [Overwrites](#overwrites)
  - [Prefer lowercase to not have `*` and uppercase to have `*` (if available)](#prefer-lowercase-to-not-have--and-uppercase-to-have--if-available)
  - [Prefer prefix/suffix to be under `*`.](#prefer-prefixsuffix-to-be-under-)
  - [Prefer -Z for plurals if there are conflicts](#prefer--z-for-plurals-if-there-are-conflicts)
  - [KP\* for ex- (and KP if it is free)](#kp-for-ex--and-kp-if-it-is-free)
  - [SPW for int-](#spw-for-int-)
  - [OEU for -y](#oeu-for--y)
  - [-FR for -M](#-fr-for--m)
  - [Other](#other)
- [Phrasing](#phrasing)
- [New](#new)
  - [Days of the week](#days-of-the-week)
  - [Months](#months)
  - [Symbols](#symbols)
  - [Names](#names)
  - [Abbreviations](#abbreviations)
  - [Other](#other-1)

## Punctuation

Change the opening and closing punctuation in prose. (Use the [symbol dictionary](./symbols.py) for other uses).

```yaml
PR-PB: {~|(^} # () PR-N for parenthesis. Originally PREPB.
PR*PB: {^})
PWR-S: {~|\\{^} # {} BR-S for brace. Originally TPR-BGT for FRench BracKT, but I don't call it that.
PWR*S: {^~|\\}}
PWR-T: {~|[^} # [] BR-T for bracket. Exists.
PWR*T: {^~|]} # exists
KW-GS: '{~|"^}' # exists
KW*GS: '{^~|"}' # use * like for the brackets. Overwrites "QSing"
KW-FP: '{~|"^}' # shape based brief, a merging of Emily symbols and the original Plover KW-GS brief
KW*FP: '{^~|"}' # as above, but for closing brackets
SKW-T: "{'^}" # exists
SKW*T: "{^'}" # exists
```

## Modes etc.

```yaml
"#*": {*}
KHR-R: "{}{^}" # "{^ ^}{#backspace}" # resets prefixes/space, good for form inputs
KPA: {-|}
KPA*: {^}{-|}
KPA*S: {MODE:CAPS}
KPA*T: {MODE:TITLE}
HRO*ER: {>}
HRO*ERS: {MODE:LOWER}
TK-FPS: {*!}
AFPS: {*?}
TK-LG: {PLOVER:LOOKUP}
PHR*UP: {PLOVER:LOOKUP}
S*GS: {PLOVER:SUGGESTIONS}
TKHR*RS: {*($c)}
R*EFT: {MODE:RESET}
STPH*S: {MODE:SET_SPACE:_}
TPR*S: {MODE:SET_SPACE:-}
R-R: {^~|\\n^}{MODE:RESET}
```

[elkowar/plover\_retro\_everything](https://github.com/elkowar/plover_retro_everything),
which lets you retroactively format the last stroke with any mode. Repeat to
apply to more strokes.

```yaml
HRO*ERD: =retro_everything:{MODE:LOWER},{MODE:RESET} # lowered
HR*D: =retro_everything:{MODE:LOWER},{MODE:RESET} # l'ed (lower)
*UPD: =retro_everything:{MODE:CAPS},{MODE:RESET} # upped
KPA*D: =retro_everything:{MODE:TITLE},{MODE:RESET} # capped
TKPA*D: =retro_everything:{MODE:CAMEL},{MODE:RESET} # capped (delete space)
STPH*D: =retro_everything:{MODE:SNAKE},{MODE:RESET} # sn'ed (snake)
SKWR*D: =retro_everything:{MODE:CAPS}{MODE:SET_SPACE:_},{MODE:RESET} # caps snake
TK*D: =retro_everything:{MODE:SET_SPACE:},{MODE:RESET} # d'ed (delete space)
```

## Keyboard Control

Usually I'll use the [symbol](./symbols.py) or [modifier](./modifiers_stack.py) dictionaries. These definitions are for things I use often enough that I'd prefer a special brief for them.

### Keys

```yaml
STPH-GS: "{#Right}" # no attach, useful for getting out of brackets
T*B: "{#Tab}{^~|^}"
ST*B: "{#shift(Tab)}{^~|}"
TA*B: "{#Tab}{^~|}"
```

### i3 (window manager)

```yaml
KHR-Z: "{#super(w)}" # close window
KHR*Z: "{#control(w)}" # close tab
PR-F: "{#super(braceleft)}" # previous workspace
TPH-GT: "{#super(braceright)}" # next workspace
STPWH-B: "{#super(j)}" # move to window
STPWH-G: "{#super(l)}"
STPWH-P: "{#super(k)}"
STPWH-R: "{#super(h)}"
STPWH*B: "{#super(shift(j))}" # move window
STPWH*G: "{#super(shift(l))}"
STPWH*P: "{#super(shift(k))}"
STPWH*R: "{#super(shift(h))}"
WOEUPB: "{^}{#super}{^}" # win key
T-RPL: "{^}{#super(Return)}{^}" # open terminal
SKR-FP: "{#super(minus)}{^}" # open scratchpad
SKR*FP: "{#super(shift(minus))}{^}" # move to scratchpad
```

### Other Programs

```yaml
T*RPL: "{#control(apostrophe)}" # open terminal in VSCode
```

### Dictionary Control

Requires [plover-dictionary-commands](https://pypi.org/project/plover-dict-commands/)

```yaml
TKR*L: {PLOVER:TOGGLE_DICT:-dictionaries/british_english.md,-dictionaries/personal_style.md}{MODE:RESET} # drill
TPH*L: {PLOVER:TOGGLE_DICT:+dictionaries/british_english.md,+dictionaries/personal_style.md}{MODE:LOWER} # normal (overwrites non-Hodgkin's lymphoma, use TPHA*UPB/H*L)
PR*RP: {PLOVER:TOGGLE_DICT:+dictionaries/british_english.md,-dictionaries/personal_style.md}{MODE:RESET} # proper
R*LD: {PLOVER:SET_CONFIG} # reloads the dictionaries
```

### Other Plover Plugins

[sashac/plover\_retro\_stroke](https://github.com/sachac/plover_retro_stroke),
which lets you retroactively format the last stroke as raw steno. Repeat to
apply to more strokes.

```yaml
STPH-RBGS: =retro_stroke:/,`,` # shape based
STPH*RBGS: =retro_stroke:/
```

[antistic/plover\_cards](https://github.com/antistic/plover_cards), which holds
my Anki related tools. These strokes let you add the last N words as a new Anki
card.

```yaml
K*RD: {PLOVER:ANKI_ADD_CARD}
K*RDZ: "{#}"
K*RDZ/34: {PLOVER:ANKI_ADD_CARD:2}
K*RDZ/4: {PLOVER:ANKI_ADD_CARD:3}
```


## Changes

Dictionary changes and additions that mostly fit within Plover theory.

There's an attempt to categorise these, but it's rough and probably some could fit into
several different categories.


### Dropped syllables

```yaml
SKWREPBD: agenda # A/SKWREPBD/TKA
SUPLGS: assumption # SUPGS, A/SUPLGS
THRAOET: athlete # overwrites throat (use THROET)
TROS/TEU: atrocity # A/TROS/TEU
TAFPLT: attachment # TAPLT, A/TAFPLT
AUT/PHEU: autonomy
A*F/KAD: avocado
AF/KAD: avocado
AZ/PWAOEU/SKWRAPB: Azerbaijan # no ER
TKEUPBLG: digital # TK*EUL, TKEUPBLG/TAL
PHA*EUL: email # mail + *
THAOUS: enthuse # overwrites 'use it' (use TAOUS). makes consistent with THAOUS/KWRAFT: enthusiast. SPWAOUZ
TPO: info # fo. overwrites "to", a misstroke
SRAOEUT: invite # overwrites vit (use SR*EUT)
HR*ET/SKWREU: lethargy
PHOTS/REL: mozzarella
PWHRAOEUPBLGD: obliged
HREUFRP/KWRAPB: Olympian # like HREUFRP/EUBG: Olympic.
TPOPB/TEUBG: phonetic # TPOEPB/TEUBG, TPOPB/ET/EUBG
PHREUT/SA*EUGS: politicization
PHREUT/SAEUGS: politicization
KWA*RPBT: quarantine # KWARPBT: quadrant
SKRAO*EUB: subscribe
```

### Compacted (still steno order)

```yaml
PWAOUFS: abusive
PWHOELD: behold
PWHOLD: behold
KHROERB: closure # KHRO*ERS
KHRAO*UD: conclude # KHRUD: included, KHRAOUD: collude
TK*EBT: debit
STKPARPBLG: disparage
TKWALT: duality # TKAOULT
KPO*EPBT: exponent
SPOEPBT: exponent
TPAFL: facile
TPAFL/TAEUT: facilitate
TPAERL: farewell
TPAERL: farewell
TPAOEFBL: feasible
TP*EUFG: fixing # like PH*EUFG: mixing
PHRAL: morale # overwrites moral (use PHORL). PHO*ERL
PERPBLG: percentage # there's PWERPBLG, which might be a misstroke
PRERBT: prescient
SPREURT: separator
SPEUFRPB: spinach # spinch
SPHEUFS: submissive
THAERPT: therapist # therapy + T. TH*EUFT, THA*EURPS
TPHULT: tumult
TUPLT: tumult
WAOEUFT: wisest
```

### Folding

Folding in a syllable to fit

Ending -G, -S, -D, -Z

```yaml
AL/HRAOEUD: allied # al lied
KOB/WEBS: cobwebs # could be webs
TKEPLTD: demented # departmented
TKEUS/EPB/TPRAPB/KHAOEUFD: disenfranchised
TKAOUP/KATS: duplicates
TEFRP/TAOURS: temperatures
KPAPBLG/RAEUTS: exaggerates
TPHRUBGT/WAEUTD: fluctuated
UPB/TKULT/RAEUTD: unadulterated
HAOUPLD/TEUS: humidities
RE/PAOELD: repealed
HAOUPLD/TEUZ: humidities
HREPL/O*PBS: lemons
HREPL/PBS: lemons
HREUB/RAEUGT: liberating
HAOUPLD/TEUS: humidities
HAOUPLD/TEUZ: humidities
PHAOEUG/RAPBTS: migrants
PHAOEU/TKPWRAPBTS: migrants
PA*PBG/-G: panicking
PAR/HAOEUFD: paralyzed
ST*EUPL/-G: stimming
ST*EUPLG: stimming
TEFRP/TAOURS: temperatures
UPD: upped
```

-TD for -ded

```yaml
SPWEPBTD: intended
EUPB/SRAEUTD: invaded
```

Tuck in HR for -ly

```yaml
STKHREPBL: accidentally
SHRERBL: essentially
HREFPBL: eventually
TKPWROELS: grossly
TPHAD/SRERLT: inadvertently
STPHAPBLT: instantly # the version without -T exists
HROPGS: optionally
HRORPBLG: originally
THREURD: thirdly
HRUPLT: ultimately
HROPLGS: optionally # OPGS: option (OPLGS: optional defined here)
```

Tuck in -L for -ly

```yaml
AURBLGD: awkwardly
AURBLG: awkwardly # without D is more comfortable
PHAEUFPL: maturely
RE/PAOELTD: repeatedly
SPREULT: separately
SKEUPBLGT: succinctly
SKEUPBLG: succinctly # without T is more comfortable
SPRAOEULG: surprisingly
THEURLD: thirdly
PRAOEUFLT: privately
WAOERLD: weirdly
```

Tuck in -R for -er, -or

```yaml
STAERT: starter
HRAORS: looser
SKWRAOURPB: junior
OE/PREFR: oppressor # OE/PRES/O*R
OE/PREFRS: oppressors
STRAOERPL: streamer
PAEUPB/KEURL: painkiller # PAEUPB/KEURLS: painkillers
A/SRERPBG: avenger
```

Tuck in E for -y

```yaml
HOEB: hobby
OERPBLG: originally
```

Other

```yaml
TPAEURPLGS: affirmation # fold in A-
TPAEURPL: affirm # overwrites fairly (use TPAEURL)
TAEFRPT: attempt # fold in A-
TAEPLT: attempt # fold in A-
SPHROEURT: exploiter
SRAOEPBG: vegan
TKPWRAEUFLT: grateful # TKPWRA*EUFL
OPLGS: optional # OPGS: option
SPRAOEUGS: surprising # SPRAOEUS: surprise + G (without final -S exists)
TAEPLT: attempt
SABG/TPAOEUFD: sacrificed # overwrites 'sack fived'. SARBG/TPAOEUFD
RAELTS: realities # like RAEL: real
RAELT: reality # like RAEL: real
TKEURBGS: dictionary # overwrites dirks (use TKEURBGZ)
SKAOEL: conceal
KHRAEUFR: clarify # KHRAEUR/TPEU
```

### Orthography fixes

Nearly works but the spelling is wrong.

```yaml
A/KUFPL: accustom # A/KUFPLD: accustomed exists
KWR-D/HROG: idealogue
KWR-D/OLG: ideology
KPHRO*EUT/TEUF: exploitative
KPHROEUT/TEUF: exploitative
SPHROEUT/TEUF: exploitative
```

### Different emphasis

```yaml
SKOPBD: second # SEBGD
SWERL: several # SEFRL
```

### Different word boundaries

```yaml
A/ROE: arrow # AR/ROE
A/HREUS: Alice # AL/EUS, A*LS
A/SET: asset # AS/SET
A/SETS: assets
A/TEUBG: attic # AT/TEUBG
TKEUS/APL/PWEUG/WA*EUT: disambiguate
TKEUS/APL/PWEUG/WAEUT: disambiguate
TKEUZ/AEUPL/PWEUG/WA*EUT: disambiguate
PHORT/*EUGS: mortician # PHOR/TEUGS
TPHEG/AEUGS: negation # TPHE/TKPWAEUGS
PE/REUL: peril # PER/EUL
SPEBG/TAEURT: spectator # from SPEBG/TAEUT. like SPEBGT/AEURT
SRULT/AOUR: vulture
STOEUPB/TKPWRAEF: stenography # STPHOG/TPEU
HREUFRP/EUBG: Olympic # overwrites limpic. HREUPL/PEUBG
PWREUT/A*PB: Britain # PWREU/TAPB
```

### Different way of writing word parts

```yaml
KHRARS/SA: Clarissa # KHRARS/KWRA
A/ROE/PHA/THAERP: aromatherapy # prefer THAERP for therapy
PHUPB/TREU: monetary # PHUPB: money. PHOPB/TREU
PHUPB/KAE: monkey # phonetic. PHOPB/KAE
KAU/HREUGS: coalition # KOE/HREUGS
KAU/HERPBT: coherent # KO/HERPBT, KAU/HAOERPBT
TRAPBZ/SEPBD: transcend # TRA*PBS/SEPBD, TRAPBZ/EPBD
SROL/KA*PBG: volcanic # SROL/KAPBG
TRAPBZ/PAEURPBS: transparency # like TRAPBS/PAEURPBT
TRAPBZ/PARPBS: transparency # like TRAPBZ/PAEURPBS
THAOUS/ST-BG: enthusiastic # makes consistent with THAOUS/KWRAFT: enthusiast
AUR/TKPWAPL/SKWREU: origami # ^i instead of PHEU. AUR/TKPWAPL/PHEU
AUR/THOE: ortho # ORT/THO
AUR/THO: ortho
SPR/STEUGS: superstition # SAOUP/STEUGS
HUBG/*L/PWER/REU: huckleberry # REU instead of KWREU
```

Vowel changes
```yaml
PHAOUFP: mature # PHAEUFP. Like PHAOURT: maturity
```

### Accidentally adding a prefix to a brief.

```yaml
AL/TKPWR*EUFPL: algorithm
A/PHAEUFPLT: amazement
EUPB/TWAOUF: intuitive
```

### Alternative by spelling

```yaml
TKOEFPS: DevOps # TKOPS (it has both an E and O in it)
KOUS/KOUS: couscous # KAOUS/KAOUS
KAFLT: castle # KAFL
PWHR*EU: bleu # PWHR*U
KREUFLT: crystal # KREUFL, no T
TKAEURPBLG: danger # TKAEUPBLG, no R
TKAOEFPBLT: decently # TKAOEPBLT, no F
TKAOEFPBT: decent # TKAOEPBT, no F
TPHRAPBT: transplant # THRAPBT, no P
PREFRPBL: preferential # PREFRL, PRERPBL
PROERP: proper # PROER, PRORP
STAURPBT: restaurant # STRAUPBT
PRAERP: prepare # PRAEP, no R
RAOEFPBLT: recently # RAOEFPBLT, no F
RAOEFPBT: recent # RAOEPBT, no F
TAURPBT: restaurant # TRAUPBT
PHOEURBG: motorcycle # PHOEUBG, no R
PHAOUFPL: museum # PHAOUPL, no F
TPOURPL: forum # TPAURPL
PHED/KWROERBG: mediocre # PHAOED/KWROERBG
TKO*ET: doth # TKA*UT, TKO*T: do the
HRO*UT: layout # HRO*EUT
```

### Alternative by pronunciation

```yaml
TKUFPB: dozen # TKOZ, TKOFPB
TKPWOL: goal # TKPWAOL
KAOEU/PWORB: kibosh # KEUB/ORB
SULT: subtle # SUBLT
SULT/HREU: subtly
PRAED: parade # PRAD: parade, PRAEUD: prayed
AOEUS/KWROE: "{iso^}" # AOEUS/KWRO
AOEU/SHA: Aisha # AOEU/AOERB/SHA
AOEURB/SHA: Aisha # AOEURB/SHA
SKWREUT/PHAEUT: legitimate # verb version. SKWREUT/PHAT
SKWREPB/WEUPBL: genuinely # SKWREPB/WAOEUPBL
```

### Star

No star version.

```yaml
TPHEUFT: antagonist
KALT: cattle
KRUF: constructive
TP-RB: efficiency
TERPBL: eternal
SKWRERPB: German
OURSZ: ourselves
AO*URP/KWRAPB: European # AO*URP/KWRA*PB
AO*URP/KWRAPBS: Europeans # AO*URP/KWRA*PBS
SPOF: responsive
SKAEUD: cascade
REF/KABL: revocable
```

With star versions.

```yaml
HR*RD: already
HR*EFPBT: eleventh # HREFPBT
PEUBGS/*EL: pixel # PEUBGS/EL
HAFRP/*ER: hamper
```

### Swaps/shuffles

Swapping, shuffling entries because I didn't like what was there before.

```yaml
KHRAEURT: calculator # overwrites clarity (use KHRAERT), fold in E
KHRAERT: clarity # overwrites calculator (use KHRAEURT), like KHRAEUT: calculate
KEFRBT: conservative
KEFRB: conserve # overwrites conservative
KRAO*EBG: critique # overwrites pancreatic. like TAO*EBG: technique
KRA*EBG: pancreatic
SPWROUBGS: introduction # TROUBGS. overwrites obstruction
PWRUBGS: obstruction # SPWRUBGS exists, but gets in the way of the whole SPW: int thing
SKWRERPBLT: generality # follows SKWRERPBL: general
SKWRERPBL: general # overwrites generally (use SKWHRERPBL). I didn't like how -R made it -ly
SKWREPBLT: gentle # without * since general was moved
OBGS: ox # overwrites objection (use OPBLGS)
R*EF: rev
REF: ref
SPREUTS: separates # overwrites spritz (use SPREUTZ, defined here)
SPREUTZ: spritz
STPHEUFL: sniffle # swap sniffle and snivel so that *F: V, -F: F
STPH*EUFL: snivel # swap sniffle and snivel so that *F: V, -F: F-8
SAOURP: super # overwrites supper (use SURP)
SURP: supper # overwrites syrup (use SEURP)
HRAOURBL: usually # HR + usual
AOURBL: usual # overwrites usually
HRA*S: last # overwrites las (use HRAZ)
SREUPL: vim
SR*EUPL: victim
```

### Overwrites

Overwrites without having an entry for what was there before.

```yaml
HA/HA: haha # ha-ha
HA/HA/HA: hahaha # ha-ha-ha
KR*EPBT: century # Century (use KPA/KR*EPBT)
TAEUPBD: contained # overwrites tained, which probably isn't a word?
```

### Prefer lowercase to not have `*` and uppercase to have `*` (if available)

```yaml
KOEL/PHABG: colemak # new
KO*EL/PHABG: Colemak
KO*FPB: conf # overwrites Conf (use KPA/KO*FPB)
TKPWRAOEU: gui
TKPWRAO*EU: GUI
PABG/PHAPB: pacman # used for arch linux package management
PABG/PHA*PB: Pacman
WERPB: western
W*ERPB: Western
UFB: usb
"*UFB": USB
```

### Prefer prefix/suffix to be under `*`.

```yaml
TKEUBGS: diction
TK*EUBGS: "{diction^}"
PHEUD: mid # PHEUD/PHEUD, overwrites mid^
PH*EUD: "{mid^}" # exists
```

### Prefer -Z for plurals if there are conflicts

```yaml
TKPWAOEUS: guise
TKPWAOEUZ: guys
```

### KP\* for ex- (and KP if it is free)

(It's kind of plover, but not consistently)

```yaml
KP*EPT: except
KP*EPGS: exception
KPA*EUPBG: exchange # KPAEUPBG
KPHRAEUPL: exclaim # SKHRAEUPL
KPHRAO*UD: exclude # KPHRAOUD
KPHRAO*UGS: exclusion
KPHR*UGS: exclusion
KPHRUGS: exclusion
KPHRAOUGS: exclusion # SKHRAOUGS
KPAO*UT: execute # SKAOUT
KPAPBD: expand
KPA*UFT: exhaust # KPAUFT
KPA*PBD: expand # EBGS/PAPBD
KP*EPBS: expense # SPEPBS
KP*ERPLT: experiment
KPERPLT: experiment # SPERPLT
KPHRA*EUPB: explain # SPHRAEUPB
KPHRAPBGS: explanation
KPHRA*PBGS: explanation # explanation
KPHR*EUFT: explicit # EBGS/PHREUFT
KPHREUFLT: explicitly
KPHR*EUFLT: explicitly # EBGS/PHREUFLT
KPHROEUT: exploit
KPHRO*EURT: exploiter
KPHROEURT: exploiter
KPHRO*EUT: exploit # SPHROEUT
KPHRO*R: explore
KPHROR: explore # SPHROR
KP*EPBL: exponential
KPEPBL: exponential
KPO*RT: export
KPO*ERB: exposure
KPOERB: exposure
KPR*ES: express # express
KP*ERPBL: external # KPERPBL
```

### SPW for int-

(It's kind of plover, but not consistently)

```yaml
SPWREPBGS: intervention # TWEPBGS
SPWAOUT: intuit # TWAOUT
SPWAOUGS: intuition # TWAOUGS
SPWAOUF: intuitive # TWAOUF
SPWAOUFT: intuitive # TWAOUFT
SPWAOUFL: intuitively # TWAOUFLT
SPWRAOUS: introduce
```

### OEU for -y

(It's kind of plover, but not consistently)

```yaml
HO*EULT: healthy # there's HOEUFLT, but I think the F is a misstroke?
POEUT: pity
THROEUFT: thrifty
TROEUT: treaty
```

### -FR for -M

```yaml
KWRAFRL: yaml
TREFRBL: tremble
STUFRBL: stumble
KAFRL: camel
```

### Other

```yaml
TKA*EGS: accommodation # like TKA*ET: accommodate
TKAEGS: accommodation # no * since it's free
ARB/TREU: arbitrary # ARB/TRAER
-RPBT: "aren't" # other side R
A*ERG: argh # like HA*E: ah. A*RG
AUDZ: audience # AUPBS
PWHR*UT: Bluetooth # bluth. short u like PWHRU: blue
A/TPHEPL/TPHE: anemone
KHAO*S: chaos # KHAOS: choose, KAOS: consists
KHAOT/EUBG: chaotic # like the new KHAO*S
SKHRAEUGS: circulation # overwrites acceleration (use SHRERGS)
KPHAOUBGS: communication # KPHAOUPBGS, no n like KPHAOUBGT: communicate
TPHUPL/K-L: numerical
TPHUPL/K*L: numerical
SAEPB: sane # SAEUPB
SKRAOURBT: excruciate
ROEUR/TPHOUS: erroneous
TKPWO*FP: gotcha
HOEPL/SEBGS/WAELT: homosexuality
SKRAOURBGT: excruciating
KPRAOURBGT: excruciating
SPHROEFS: explosive
SPR/SRAOEUFG: supervising
SPWEGT: integrity
R-FPL: respectful
R-FL: relatively
K-FG: config
PROUPBZ: pronouns # PROUPBS: pronounce
KPWEPBT: indent # SPWEPBT: intent
OERPBT: orient # overwrites interior (use SPWAOER)
SKEF: consecutive
KR-RT: contractor # like KR-T: contract. overwrites ^ (use symbols dictionary SKWH-RPG)
SPAPBGS: expansion
SKWA: schwa # SKHA, SKWHA
KWEPBL: conventional # SREPBL
KO*ERP: copper # KO*RP
STKAOEUF: decisive # STKAOEUFS
TK-PBGS: definition # define + shun
TK-FGS: definition # def + shun
EFL: eventually # like UFL: unfortunately
TKPW-PLT: government # TKPWOPLT, TKPW-FT
H*EPL: helm # HEL/*PL
HOEFPL: hopeful # HOEFL, no P
AO*EULD: idle # overwrites "Island"
KWRA*EU: i.e. # AOEU/KWRAOE. Like KWRO*EU: i.e.,
EUPL/PHREUBGS: implication # EUPL/PHREUBGS/-S: implications exists, so why not this?
TPHERBL: incredible # TPHRERBL: incredibly
TPH-RBT: inefficient # TPH: in + TP-RBT: efficient
STPHAOEUR: inspire
SPWERPBLT: internment
EUPBT/PRERT: interpreter # EUPBT/PRET/*ER
HRAPT: laptop
HR-PBLG: logic # L-J
PHAOULT: mutual
OURP: occupier # like OUPG: occupying, OUPD: occupied
OUP: occupy # overwrites up (use UP). Like OUPG: occupying, OUPD: occupied
R-F: relative # overwrites rf (use R*F in programming.md)
R-FR: review
STPH*EUF: sensitive # like STPH*EUFT: sensitivity
SWAUPBS: "someone's" # someones + A, like AE: '
SWAE/HRAPBS: surveillance
SEUFRP/TPHEU: symphony # overwrites 'simple any' (use {*?} or TK-LS), which is much less common according to Google Ngram Viewer. SEUFRP/TPH*EU
S-BG: sync
S-BG/TPHOUS: synchronous
THAUBG: thank you # like THABG: thank, THAUPBG: thank you
THR*EPBT: threaten # THREFPB, THREPBT: talent
"*UPLT": ultimately # misstroke for *ULT, because UPLT is ultimate
"*UPBS": understood # UPBS: understand, URPBD: understand, *URPBD: understood
AUPGD: upgrade # AUP: up^, like AOUPT: output. UPGD
SRAE: via # SRAOEU: vie
```

## Phrasing

- +O: go / going / goes + to

Doesn't work for "gone"
```yaml
TKPWOG: going to # overwrites going (use going)
TKPWO: go to # overwrites go (use TKPW)
TKPWOS: goes to # exists
```

- Different definitions
```yaml
WUF: one of # WUFPB
WUFT: one of the # WUFPBT
STKPWAOS: as good as # like SPHUFPS: as much as (STKPWAOZ exists)
```

- SPH some

```yaml
SPHOER: some other
SPH-F: some of
SPH-FT: some of the
SPHEPL: some people
```

- Other
```yaml
KAOEUF: kind of # KAOEUFPBD
KAOEUFS: kinds of
TAOEUF: type of
TAOEUFS: types of # overwrites typhus (use TAO*EUFS)
```

## New

### Days of the week

```yaml
PHO*PB: Mon # PHOPB: mon
TAOU: Tue
TAO*U: Tue # * for consistency
W*ED: Wed # WED: wed
THAOU: Thu
THAO*U: Thu # * for consistency
TPR*EU: Fri # exists
SA*ET: Sat # SAT: sat, SA*T: SAT
S*UPB: Sun # SUPB: sun
```

### Months

```yaml
SKWRA*PB: Jan # exists
TP*EB: Feb # swapped Feb and Feb so the abbreviation has the *
TPEB: February
PHA*R: Mar # overwrites March (use PHA*FRPB)
PR*EUL: Apr
PHA*EU: May # exists
SKWRUPB: Jun # overwrites June (use SKWRAOUPB)
SKWR*UPB: Jun # * consistency
SKWR*UL: Jul
A*UG: Aug
S*EPT: Sept
O*BGT: Oct
TPHO*F: Nov
TK*ES: Dec # short E
TKAO*ES: Dec # overwrites "December"
```

### Symbols

```yaml
H-RT: ♥ # heart
SPH-L: :) # smile
SPH*L: :( # unsmile
```

### Names

```yaml
TKAO*EU/TKAO*EU: Di # overwrites di. TKAOEU: die, TKAO*EU: dye, TKEU: did I, TK*EU: di^
TKPWERG/KWROE: Gergo
TKPWERG/KWRO: Gergo
KEP/HRER: Kepler
KW-PLG: qmk
KW*PLG: QMK
TAOEUP/KWREU/TAOEUP: Typey Type
TPHET/TPAOEU: netlify
TPH*ET/TPAOEU: Netlify
```

### Abbreviations

```yaml
A*PLT: atm
PW-S: bc # like PWAUS: because, but without vowels
PW*D: bday
PW*T: btw
TKPWRATS: congrats
TKW: dw
"*EFP": esp
"*EPS": esp
H-R: HR
"*EUBGD": idk
PH-L: {^}ml
KWRU: EU
P-P/ORG: {^.org}
P-P/P-PBG: {^.png}
AO*EURBG: iirc
AOEURBG: iirc
"*EURBG": ikr
O*EUPL: imo
OFBS: obvs
O*PLG: omg
P-LS: pls
PRO*EB: prob # PROB: probable, PRO*B: problem, PROEB: probe
-RPB: rn
TKPW-P: GP
SOZ: soz
S*RS: srs
A*UR: AUR
S*RLS: srsly
SWEFR: SWERF
TPW-F: tbf
TPWH: tbh
TEFR: TERF
K*G: kg # overwrites kilogram (use K-G)
K*GS: kgs # overwrites kilograms (use K-GS)
KWR*UR: ur
SPR-PB: VPN
SR-S: vs # overwrites "haves" (use SR-Z)
W-FT: wtf
KWR*/TPHOE: y\'know
```

### Other

```yaml
S-FD: ssd
A/KUFRD: accursed
AG/TPHOE/TOLG: agnotology
PWAFL/EUFBG: basilisk # overwrites baffliffic
PWA/SEUL/EUFBG: basilisk # overwrites basiliffic (if using british_english.md)
KAR/SER/A*L: carceral
KAR/SERL: carceral
KARS/RAL: carceral
AO*ET/*ER: aether
A/HA/HA: ahaha
KHAOER/HRAOED: cheerlead # KHAOER/HRAOERD: cheerleader
KHO*BG: choc # KHOBG: chock
SKWRAOU/SREU: juvie
S*EUS/SKWREPBD/*ER: cisgender
KAUPB/TEPL: contemn
S*EUS/SKWRERPBD: cisgender
PHAOEFPB: meson
AB/SAEUL: abseil
S*EUS: cis # overwrites cyst (use KREUFT)
KHROEZ: cloze # overwrites close (use KHROES)
KO*PL: {com^} # overwrites comp (use KOFRP)
KROEPB/SRAOEURS: coronavirus
KO*EFD: covid
AOEU/TKPWEPB: eigen
PHOUT: {^mouth}
KOEFD: covid
KR*UFT: cruft # KRUFT: crust
TKOBGS/AEUFT/EUBG: doxastic
TKOBGS/AFT/KHREU: doxastically
AOED: Eid # overwrites he'd (use HAOED)overwrites crust (use KR*US)
EFBL: evitable # TPHEFBL: inevitable
EBGS/EUF: EXIF
HA/REUS/SA: harissa
HA/REUS/SKWRA: harissa
HARS/SA: harissa
HARS/SKWRA: harissa
EUPBS/TA*: {insta^}
EUPBS/TA: insta
EUPBT/KWRO/SEPGS: interoception
EUPBT/SKWRO/SEPGS: interoception
SPWROEPGS: interoception
EUPBT/KWROE/SEPGS: interoception # otherwise does interro
SKWRAEPBG: janky
SKWRA*PBG/KWREU: janky
SKWRAPB/KEU: janky
KAO*EF: kiev # KAOE/*EF: Kiev
TP*EPB/STOEUPB: phenrsteno
S*EBGS/ED: sex ed
STAPB: stan # overwrites Stan (use STA*PB)
```

Compound

```yaml
TPHRARB/KA*RD: flashcard
KAOE/KAP: keycap
KAOE/KAPS: keycaps
KAOE/KAPZ: keycaps
SKAOEU/TKAO*EUF: skydive # overwrites sky derive
SKAOEU/TKAO*EUFR: skydiver
SPAOED/PWHR-G: speedbuilding
WORBG/SPA*EUS: workspace
```

Moves existing entries

```yaml
KORPB/SKWRE: Corne # overwrites coryne^ (use KOR/REUPB)
KOR/REUPB: "{coryne^}"
PHEUFBG: misc # overwrites miscellaneous
PH*EUFBG: miscellaneous
POEUL: poly # overwrites poly^
PO*EUL: "{poly^}"
KWRE: ye # overwrites yes (use KWRES)
KWRES: yes # overwrites yes, sir (did not redefine since I don't use it)
```

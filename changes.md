# Changes

Various changes I have made to my dictionary.

Requires:
  - [plover-markdown-dictionary](https://github.com/antistic/plover-markdown-dictionary)

Table of contents:
- [Punctuation](#punctuation)
- [Briefs](#briefs)
- [Alternatives / Misspellings](#alternatives--misspellings)
  - [Prefixes](#prefixes)
  - [Word Boundaries](#word-boundaries)
  - [Unstar](#unstar)
  - [Swaps/shuffles](#swapsshuffles)
- [Overrides](#overrides)
- [Rules](#rules)
- [Phrasing](#phrasing)
- [New](#new)
  - [Abbreviations](#abbreviations)
  - [Symbols](#symbols)
  - [Names](#names)
  - [Other](#other)
- [Added by Plover](#added-by-plover)

## Punctuation

Change the opening and closing punctuation in prose. (Use the symbol dictionary for other uses).

TODO:  figure out how to carry punctuation

```yaml
PR-PB: {~|(^} # () PR-N for parenthesis. Originally PREPB.
PR*PB: {^})
PWR-S: {~|\\{^} # {} BR-S for brace. Originally TPR-BGT for FRench BracKT, but I don't call it that.
PWR*S: {^\\}}
PWR-T: [{^} # [] BR-T for bracket. Exists.
PWR*T: {^}] # exists
KW-GS: '{~|"^}' # exists
KW*GS: '{^~|"}' # use * like for the brackets. Overwrites "QSing"
SKW-T: "{'^}" # exists
SKW*T: "{^'}" # exists
```

## Briefs

Shorter entries where none already exist.

```yaml
TKA*EGS: accommodation # like TKA*ET: accommodate
TKAEGS: accommodation # no * since it's free
A/KUFPL: accustom # A/KUFPLD: accustomed exists
TPAEURPLGS: affirmation
TPAEURPL: affirm # overwrites fairly (use TPAEURL)
SKWREPBD: agenda # A/SKWREPBD/TKA
TROS/TEU: atrocity # A/TROS/TEU
TAEFRPT: attempt # fold in A-
TAEPLT: attempt # fold in A-
AUT/PHEU: autonomy
A*F/KAD: avocado
AF/KAD: avocado
PWHOELD: behold
PWHOLD: behold
PWHR*UT: Bluetooth
KHAO*S: chaos # KHAOS: choose, KAOS: consists
SKAOEL: conceal
K-FG: config
K-FG/-BL: configurable
SKEF: consecutive
TK*EBT: debit
TKEURBGS: dictionary # overrides dirks (use TKEURBGZ)
PHA*EUL: email # mail + *
KPHRO*EURT: exploiter
KPHROEURT: exploiter
SPHROEURT: exploiter
KPO*EPBT: exponent
SPOEPBT: exponent
TPAFL: facile
TPAFL/TAEUT: facilitate
TPAERL: farewell
TPAOEFBL: feasible
TP*EUFG: fixing # like PH*EUFG: mixing
TKPWRAEUFLT: grateful
H*EPL: helm # HEL/*PL
KWR-D/HROG: idealogue
KWR-D/OLG: ideology
AO*EULD: idle # overwrites "Island"
KWRA*EU: i.e. # AOEU/KWRAOE. Like KWRO*EU: i.e.,
TPHERBL: incredible
TPH-RBT: inefficient
TPO: info # fo. overwrites "to", a misstroke
STPHAOEUR: inspire
SPWERPBLT: internment
SRAOEUT: invite # overwrites vit (use SR*EUT)
SKWRAOURPB: junior
HRAPT: laptop
HR*ET/SKWREU: lethargy
HR-PBLG: logic # L-J
HRAORS: looser # fold in -R
PHAOULT: mutual
OURP: occupier # like OUPG: occupying, OUPD: occupied
OUP: occupy # overwrites up (use UP). Like OUPG: occupying, OUPD: occupied
HREUFRP/KWRAPB: Olympian # like HREUFRP/EUBG: Olympic (in alternatives)
OE/PREFR: oppressor # OE/PRES/O*R
OE/PREFRS: oppressors
HROPLGS: optionally # OPGS: option, like OPLGS: optional (defined here)
OPLGS: optional # OPGS: option
PHREUT/SA*EUGS: politicization
PHREUT/SAEUGS: politicization
PRERBT: prescient
KWA*RPBT: quarantine # KWARPBT: quadrant
R-F: relative # overwrites rf (use R*F in programming.md)
R-FR: review
STPH*EUF: sensitive # like STPH*EUFT: sensitivity
SPREUTS: separates # overwrites spritz (use SPREUTZ, defined here)
SPREURT: separator
SWAUPBS: "someone's" # someones + A, like AE: '
SPEUFRPB: spinach # spinch
SPREUTZ: spritz
STAERT: starter
SKRAO*EUB: subscribe
STKPARPBLG: disparage
SWAE/HRAPBS: surveillance
S-BG: sync
S-BG/TPHOUS: synchronous
TR-FRPL/TEUF: transformative
TPHULT: tumult
TUPLT: tumult
SRAOEPBG: vegan
SRAE: via # SRAOEU: vie
```

## Alternatives / Misspellings

```yaml
A/HREUS: Alice # AL/EUS, A*LS
ARB/TREU: arbitrary # ARB/TRAER
KAO*EUF: archive # KRAO*EUF
-RPBT: "aren't" # other side R
A/ROE/PHA/THAERP: aromatherapy # prefer THAERP for therapy
SUPLGS: assumption # SUPGS, A/SUPLGS
TAFPLT: attachment # TAPLT, A/TAFPLT
AUDZ: audience
AZ/PWAOEU/SKWRAPB: Azerbaijan # no ER
PWHR*EU: bleu # PWHR*U
KAFLT: castle # KAFL, no T
KHAOT/EUBG: chaotic # like the new KHAO*S
SKHRAEUGS: circulation # overrides acceleration (use SHRERGS)
KHRAEUFR: clarify # KHRAEUR/TPEU
KHRAEFR: clarify # KHRAR/TPEU
KHRARS/SA: Clarissa # KHRARS/KWRA
KHROERB: closure
KAU/HREUGS: coalition # KOE/HREUGS
KAU/HERPBT: coherent # KO/HERPBT, KAU/HAOERPBT
KPHAOUBGS: communication # KPHAOUPBGS
KWEPBL: conventional # SREPBL
KO*ERP: copper # KO*RP
KOUS/KOUS: couscous # by spelling. KAOUS/KAOUS
KREUFLT: crystal # KREUFL, no T
TKAEURPBLG: danger # TKAEUPBLG, no R
TKAET/PWA*EUS: database # overwrites data-base
TKAOEFPBLT: decently # TKAOEPBLT, no F
TKAOEFPBT: decent # TKAOEPBT, no F
STKAOEUF: decisive # STKAOEUFS
TK-PBGS: definition # define + shun
TK-FGS: definition # def + shun
TKOEFPS: DevOps # TKOPS
TKEUPBLG: digital
TKO*ET: doth # TKA*UT
TKUFPB: dozen # TKOZ, TKOFPB
TKWALT: duality # TKAOULT
HR*EFPBT: eleventh # HREFPBT
THAOUS: enthuse # overwrites 'use it' (use TAOUS). makes consistent with THAOUS/KWRAFT: enthusiast. SPWAOUZ
THAOUS/ST-BG: enthusiastic # makes consistent with THAOUS/KWRAFT: enthusiast
AO*URP/KWRAPB: European # AO*URP/KWRA*PB
AO*URP/KWRAPBS: Europeans # AO*URP/KWRA*PBS
EFL: eventually # like UFL: unfortunately
TPOURPL: forum # by spelling. TPAURPL
TKPWOL: goal # TKPWAOL
TKPW-PLT: government
HOEFPL: hopeful # HOEFL, no P
HUBG/*L/PWER/REU: huckleberry # REU instead of KWREU
EUPL/PHREUBGS: implication
EUPBT/PRERT: interpreter # EUPBT/PRET/*ER
AOEUS/KWROE: "{iso^}" # phonetic. AOEUS/KWRO
KAOEU/PWORB: kibosh # KEUB/ORB
HRO*UT: layout # HRO*EUT
SKWROERT: majority # SKWRORPLT
PHED/KWROERBG: mediocre # PHAOED/KWROERBG
PHUPB/TREU: monetary # PHUPB: money. PHOPB/TREU
PHUPB/KAE: monkey # phonetic. PHOPB/KAE
PHRAL: morale # overwrites moral (use PHORL). PHO*ERL
PHAOUFPL: museum # PHAOUPL, no F
HREUFRP/EUBG: Olympic # overwrites limpic. HREUPL/PEUBG
AUR/TKPWAPL/SKWREU: origami # ^i instead of PHEU. AUR/TKPWAPL/PHEU
PRAED: parade # PRAD: parade, PRAEUD: prayed
PERPBLG: percentage # there's PWERPBLG, which might be a misstroke
TPOPB/TEUBG: phonetic # TPOEPB/TEUBG, TPOPB/ET/EUBG
PEUBGS/*EL: pixel # PEUBGS/EL
PREFRPBL: preferential # PREFRL, PRERPBL
PRAERP: prepare # PRAEP, no R
PROERP: proper # PROER, PRORP
RAELTS: realities # like RAEL: real
RAELT: reality # like RAEL: real
RAOEFPBLT: recently # RAOEFPBLT, no F
RAOEFPBT: recent # RAOEPBT, no F
STAURPBT: restaurant # STRAUPBT
TAURPBT: restaurant # TRAUPBT
SABG/TPAOEUFD: sacrificed # overwrites 'sack fived'. SARBG/TPAOEUFD
SKOPBD: second # SEBGD
SWERL: several # SEFRL
STOEUPB/TKPWRAEF: stenography
SULT: subtle # SUBLT
SPR/STEUGS: superstition # SAOUP/STEUGS
SPRAOEUGS: surprising # SPRAOEUS: surprise + G (without final -S exists)
SEUFRP/TPHEU: symphony # overwrites 'simple any' (use {*?} or TK-LS), which is much less common according to Google Ngram Viewer. SEUFRP/TPH*EU
THAUBG: thank you # like THABG: thank, THAUPBG: thank you
THAERPT: therapist # therapy + T. TH*EUFT, THA*EURPS
THR*EPBT: threaten # THREFPB, THREPBT: talent
TRAPBZ/SEPBD: transcend # TRA*PBS/SEPBD, TRAPBZ/EPBD
TRAPBZ/PAEURPBS: transparency # like TRAPBZ/PAEURPBT
TRAPBZ/PARPBS: transparency # like TRAPBZ/PARPBS
TPHRAPBT: transplant # THRAPBT, no P
"*UPLT": ultimately # misstroke for *ULT, because UPLT is ultimate
"*UPBS": understood # UPBS: understand, URPBD: understand, *URPBD: understood
AUPGD: upgrade # AUP: up^, like AOUPT: output. UPGD
SROL/KA*PBG: volcanic # SROL/KAPBG
```

### Prefixes

Accidentally adding a prefix to a brief.

```yaml
AL/TKPWR*EUFPL: algorithm
A/PHAEUFPLT: amazement
EUPB/TWAOUF: intuitive
```

### Word Boundaries

Different word boundaries.

```yaml
A/ROE: arrow # AR/ROE
A/SET: asset # AS/SET
A/SETS: assets
A/TEUBG: attic # AT/TEUBG
PHORT/*EUGS: mortician # PHOR/TEUGS
TPHEG/AEUGS: negation # TPHE/TKPWAEUGS
PE/REUL: peril # PER/EUL
SPEBG/TAEURT: spectator # from SPEBG/TAEUT. like SPEBGT/AEURT
SRULT/AOUR: vulture
```

### Unstar

It has a `*` but the non `*` version is free.

```yaml
TPHEUFT: antagonist
KALT: cattle
KRUF: constructive
TP-RB: efficiency
TERPBL: eternal
SKWRERPB: German
OURSZ: ourselves
SPOF: responsive
SKAEUD: cascade
```

### Swaps/shuffles

```yaml
KHRAEURT: calculator # overwrites clarity (use KHRAERT), fold in E
KHRAERT: clarity # overwrites calculator (use KHRAEURT), like KHRAEUT: calculate
KEFRBT: conservative
KEFRB: conserve # overwrites conservative
SKWRERPBLT: generality # follows SKWRERPBL: general
SKWRERPBL: general # overwrites generally (use SKWHRERPBL). I didn't like how -R made it -ly
SKWREPBLT: gentle # without * since general was moved
OBGS: ox # overwrites objection (use OPBLGS)
STPHEUFL: sniffle # swap sniffle and snivel so that *F: V, -F: F
STPH*EUFL: snivel # swap sniffle and snivel so that *F: V, -F: F-8
HRAOURBL: usually # HR + usual
AOURBL: usual # overwrites usually
SAOURP: super # overwrites supper (use SURP)
SURP: supper # overwrites syrup (use SEURP)
```

## Overrides

```yaml
HA/HA: haha # ha-ha
HA/HA/HA: hahaha # ha-ha-ha
KR*EPBT: century # Century
```

## Rules

Ending -G, -S, -D, -Z (not automatic for multi-stroke words, may have orthography errors)

```yaml
AL/HRAOEUD: allied
PWEUS/KEUTS: biscuits
KOB/WEBS: cobwebs
TKEPLTD: demented
TKEUS/EPB/TPRAPB/KHAOEUFD: disenfranchised
TKAOUP/KATS: duplicates
KPAPBLG/RAEUTS: exaggerates
TPHRUBGT/WAEUTD: fluctuated
HAOUPLD/TEUS: humidities
HAOUPLD/TEUZ: humidities
HREPL/O*PBS: lemons
HREPL/PBS: lemons
PHAOEUG/RAPBTS: migrants
PHAOEU/TKPWRAPBTS: migrants
PA*PBG/-G: panicking
PAR/HAOEUFD: paralyzed
ST*EUPL/-G: stimming
ST*EUPLG: stimming
TEFRP/TAOURS: temperatures
```

-TD for -ded

```yaml
SPWEPBTD: intended
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
WAOERLD: weirdly
```

Tuck in E for -y

```yaml
HOEB: hobby
OERPBLG: originally
```

Tuck in -R for -er/-or

```yaml
STRAOERPL: streamer
```

Prefer lowercase to not have `*` and uppercase to have `*`

```yaml
KOEL/PHABG: colemak # new
KO*EL/PHABG: Colemak
TKPWRAOEU: gui
TKPWRAO*EU: GUI
PABG/PHAPB: pacman # used for arch linux package management
PABG/PHA*PB: Pacman
WERPB: western
W*ERPB: Western
UFB: usb
"*UFB": USB
```

Prefer prefix/suffix to be under `*`.

```yaml
TKEUBGS: diction
TK*EUBGS: "{diction^}"
PHEUD: mid # PHEUD/PHEUD, overwrites mid^
PH*EUD: "{mid^}" # exists
```

Prefer -Z for plurals if there are conflicts

```yaml
TKPWAOEUS: guise
TKPWAOEUZ: guys
```

KP\* for ex- (and KP if it is free)

```yaml
KPA*EUPBG: exchange # KPAEUPBG
KPHRAEUPL: exclaim # SKHRAEUPL
KPHRAO*UD: exclude # KPHRAOUD
KPHRAO*UGS: exclusion
KPHR*UGS: exclusion
KPHRUGS: exclusion
KPHRAOUGS: exclusion # SKHRAOUGS
KPAO*UT: execute # SKAOUT
KPAPBD: expand
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
KPHRO*EUT: exploit # SPHROEUT
KPHROR: explore # SPHROR
KPHRO*R: explore
KP*EPBL: exponential
KPEPBL: exponential
KP*ERPBL: external # KPERPBL
KPO*RT: export
KPO*ERB: exposure
KPOERB: exposure
KPR*ES: express # express
```

SPW for int-

```yaml
SPWREPBGS: intervention # TWEPBGS
SPWROEUBGS: introduction # TROUBGS
SPWAOUT: intuit # TWAOUT
SPWAOUGS: intuition # TWAOUGS
SPWAOUF: intuitive # TWAOUF
SPWAOUFT: intuitive # TWAOUFT
SPWAOUFL: intuitively # TWAOUFLT
```

/\*ER for words with -er

```yaml
HAFRP/*ER: hamper
```

OEU for -y

```yaml
HO*EULT: healthy # there's HOEUFLT, but I think the F is a misstroke?
POEUT: pity
THROEUFT: thrifty
TROEUT: treaty
```

## Phrasing


- +O: go / going / goes + to

Doesn't work for "gone"
```yaml
TKPWOG: going to # overwrites going (use going)
TKPWO: go to # overwrites go (use TKPW)
TKPWOS: goes to # exists
```

## New

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
AO*EURBG: iirc
AOEURBG: iirc
"*EURBG": ikr
O*EUPL: imo
OFBS: obvs
O*PLG: omg
P-LS: pls
PRO*EB: prob # PROB: probable, PRO*B: problem, PROEB: probe
-RPB: rn
SOZ: soz
S*RS: srs
S*RLS: srsly
TPW-F: tbf
TPWH: tbh
KWR*UR: ur
SPR-PB: VPN
SR-S: vs # overrides "haves" (use SR-Z)
W-FT: wtf
KWR*/TPHOE: y\'know
```

Days of the week

```yaml
PH*OPB: Mon # PHOPB: mon
TAOU: Tue
TAO*U: Tue # * for consistency
W*ED: Wed # WED: wed
THAOU: Thu
THAO*U: Thu # * for consistency
TPR*EU: Fri # exists
SA*ET: Sat # SAT: sat, SA*T: SAT
S*UPB: Sun # SUPB: sun
```

Months

```yaml
SKWRA*PB: Jan # exists
TP*EB: Feb # swapped Feb and Feb so the abbreviation has the *
TPEB: February
PHA*R: Mar # overwrites March (use PHA*FRPB)
PR*EUL: Apr
PHA*EU: May # it's the same
SKWRUPB: Jun # overwrites June (use SKWRAOUPB)
SKWR*UPB: Jun # * consistency
SKWRUL: Jul
SKWRU*L: Jul # * consistency
A*UG: Aug
S*EPT: Sept
"*OBGT": Oct
TPH*OF: Nov
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
TKAO*EU/TKAO*EU: Di # overrides di. TKAOEU: die, TKAO*EU: dye, TKEU: did I, TK*EU: di^
TKPWERG/KWROE: Gergo
TKPWERG/KWRO: Gergo
KEP/HRER: Kepler
KW-PLG: qmk
KW*PLG: QMK
TAOEUP/KWREU/TAOEUP: Typey Type
```

### Other

```yaml
A/KUFRD: accursed
PWAFL/EUFBG: basilisk # overwrites baffliffic
PWA/SEUL/EUFBG: basilisk # overwrites basiliffic (if using british_english.md)
KAR/SER/A*L: carceral
KAR/SERL: carceral
KARS/RAL: carceral
KHO*BG: choc # KHOBG: chock
S*EUS: cis # overwrites cyst (use KREUFT)
S*EUS/SKWRERPBD: cisgender
S*EUS/SKWREPBD/*ER: cisgender
KHROEZ: cloze # overwrites close (use KHROES)
KO*PL: {com^} # overrides comp (use KOFRP)
KROEPB/SRAOEURS: coronavirus
KOEFD: covid
KR*UFT: cruft #
AOED: Eid # overwrites he'd (use HAOED)overwrites crust (use KR*US)
EFBL: evitable # TPHEFBL: inevitable
EBGS/EUF: EXIF
HA/REUS/SA: harissa
HA/REUS/SKWRA: harissa
HARS/SA: harissa
HARS/SKWRA: harissa
EUPBS/TA: insta
EUPBS/TA*: {insta^}
EUPBT/KWROE/SEPGS: interoception # otherwise does interro
EUPBT/KWRO/SEPGS: interoception
EUPBT/SKWRO/SEPGS: interoception
SPWROEPGS: interoception
KAO*EF: kiev # KAOE/*EF: Kiev
AUR/THOE: ortho
AUR/THO: ortho
STAPB: stan # overwrites Stan (use STA*PB)
```

Compound

```yaml
TPHRARB/KA*RD: flashcard
SKAOEU/TKAO*EUF: skydive # overwrites sky derive
SKAOEU/TKAO*EUFR: skydiver
SPAOED/PWHR-G: speedbuilding
WORBG/SPA*EUS: workspace
```

Moves existing entries

```yaml
KORPB/SKWRE: Corne # overwrites coryne^ (use KOR/REUPB)
KOR/REUPB: "{coryne^}"
PHEUFBG: misc # overrides miscellaneous
PH*EUFBG: miscellaneous
POEUL: poly # overrides poly^
PO*EUL: "{poly^}"
KWRE: ye # overrides yes (use KWRES)
KWRES: yes # overrides yes, sir (did not redefine since I don't use it)
```

## Added by Plover

```yaml
KAOE/KAP: keycap
UPD: upped
```

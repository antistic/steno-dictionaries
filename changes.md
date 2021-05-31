# Changes

- [Punctuation](#punctuation)
- [Briefs](#briefs)
- [Alternatives / Misspellings](#alternatives--misspellings)
  - [Swaps/shuffles](#swapsshuffles)
- [Overrides](#overrides)
- [Rules](#rules)
- [New](#new)
  - [Abbreviations](#abbreviations)
    - [Days of the week](#days-of-the-week)
    - [Months](#months)
  - [Symbols](#symbols)
  - [Words](#words)
  - [Names](#names)

## Punctuation

Change the opening and closing brackets in prose. (Use the symbol dictionary for other uses).

```yaml
PR-PB: ({^} # () PR-N for parenthesis. Originally PREPB.
PR*PB: {^})
PWR-S: {{^} # {} BR-S for brace. Originally TPR-BGT for FRench BracKT, but I don't call it that.
PWR*S: {^}}
PWR-T: [{^} # [] BR-T for bracket. Exists, here for completeness.
PWR*T: {^}]
```

## Briefs

Shorter entries where none already exist.

```yaml
TROS/TEU: atrocity  # A/TROS/TEU
OUP: occupy  # overwrites up (use UP). Like OUPG: occupying, OUPD: occupied
OURP: occupier  # like OUPG: occupying, OUPD: occupied
A/KUFPL: accustom  # A/KUFPLD: accustomed exists
TKA*EGS: accommodation  # fits with TKA*ET: accommodate
TKAEGS: accommodation  # without the * since it's free
SKWREPBD: agenda  # A/SKWREPBD/TKA
KHAO*S: chaos  # KHAOS: choose, KAOS: consists
PHA*EUL: email  # mail + *
H*EPL: helm  # HEL/*PL
SRAOEUT: invite  # overwrites vit (use SR*EUT)
AO*EULD: idle  # overwrites "Island"
KWRA*EU: i.e. # AOEU/KWRAOE. Like KWRO*EU: i.e.,
TPO: info  # fo. overwrites "to", a misstroke
HR-PBLG: logic  # L-J
SPEUFRPB: spinach  # spinch
STAERT: starter
TPAFL: facile
SRAE: via  # SRAOEU: vie
HRAPT: laptop
KWA*RPBT: quarantine  # KWARPBT: quadrant
SRAOEPBG: vegan
SKWRAOURPB: junior
S-BG: sync
S-BG/TPHOUS: synchronous
SWAE/HRAPBS: surveillance
```

## Alternatives / Misspellings

```yaml
ARB/TREU: arbitrary  # ARB/TRAER
TKO*ET: doth  # TKA*UT
KREUFLT: crystal  # KREUFL
SABG/TPAOEUFD: sacrificed  # overwrites 'sack fived'. SARBG/TPAOEUFD
A/ROE/PHA/THAERP: aromatherapy  # prefer THAERP for therapy
AZ/PWAOEU/SKWRAPB: Azerbaijan  # without ER
KOUS/KOUS: couscous  # by spelling. KAOUS/KAOUS
AOEUS/KWROE: {iso^} # phonetic. AOEUS/KWRO
KO*ERP: copper  # KO*RP
PHRAL: morale # overwrites moral (use PHORL). PHO*ERL
SKOPBD: second  # SEBGD
SKWROERT: majority  # SKWRORPLT
TKUFPB: dozen # TKOZ, TKOFPB
STAURPBT: restaurant  # STRAUPBT
TAURPBT: restaurant  # TRAUPBT
TKPWOL: goal  # TKPWAOL
THAERPT: therapist  # therapy + T. TH*EUFT, THA*EURPS
PHUPB/TREU: monetary  # PHUPB: money. PHOPB/TREU
PHUPB/KAE: monkey  # phonetic. PHOPB/KAE
AUR/TKPWAPL/SKWREU: origami  # ^i instead of PHEU. AUR/TKPWAPL/PHEU
PEUBGS/*EL: pixel  # PEUBGS/EL
RAOEFPBT: recent  # RAOEPBT, without the F
RAOEFPBLT: recently  # RAOEFPBLT, without the F
TKAOEFPBT: decent # TKAOEPBT, without the F
TKAOEFPBLT: decently  # TKAOEPBLT, without the F
SPEBG/TAEURT: spectator  # from SPEBG/TAEUT. like SPEBGT/AEURT
SPRAOEUGS: surprising  # SPRAOEUS: surprise + G (without final -S exists)
"*UPLT": ultimately  # misstroke for *ULT, because UPLT is ultimate
SEUFRP/TPHEU: symphony  # overwrites 'simple any' (use {*?} or TK-LS), which is much less common according to Google Ngram Viewer. SEUFRP/TPH*EU
AUPGD: upgrade  # AUP: up^, like AOUPT: output. UPGD
```

Accidentally adding a prefix to a brief.

```yaml
A/PHAEUFPLT: amazement
AL/TKPWR*EUFPL: algorithm
```

Different word boundaries.

```yaml
A/ROE: arrow
A/SET: asset
A/TEUBG: attic
A/SETS: assets
PE/REUL: peril  # PER/EUL
```

It has a `*` but the non `*` version is free.

```yaml
TPHEUFT: antagonist
TP-RB: efficiency
OURSZ: ourselves
TERPBL: eternal
```


### Swaps/shuffles

Between prefix/suffix and whole word. Prefer prefix/suffix to be under `*`.

```yaml
TKEUBGS: diction
TK*EUBGS: {diction^}
PHEUD: mid  # PHEUD/PHEUD, overwrites mid^
PH*EUD: {mid^} # exists
```

```yaml
KEFRB: conserve  # overwrites conservative
KEFRBT: conservative
OBGS: ox  # overwrites objection (use OPBLGS)
AOURBL: usual  # overwrites usually
HRAOURBL: usually  # HR + usual
SKWRERPBL: general  # overwrites generally (use SKWHRERPBL). I didn't like how -R made it -ly
SKWRERPBLT: generality  # follows SKWRERPBL: general
```

## Overrides

```yaml
HA/HA: haha  # ha-ha
HA/HA/HA: hahaha  # ha-ha-ha
```

## Rules

Ending -G, -S, -D, -Z (not automatic for multi-stroke words, may have orthography errors)

```yaml
AL/HRAOEUD: allied
TKAOUP/KATS: duplicates
TPHRUBGT/WAEUTD: fluctuated
ST*EUPL/-G: stimming
ST*EUPLG: stimming
PA*PBG/-G: panicking
```

Tuck in HR for -ly

```yaml
STKHREPBL: accidentally
SHRERBL: essentially
HREFPBL: eventually
TKPWROELS: grossly
TPHAD/SRERLT: inadvertently
STPHAPBLT: instantly  # the version without -T exists
HROPGS: optionally
HRORPBLG: originally
THREURD: thirdly
HRUPLT: ultimately
```

Tuck in -L for -ly

```yaml
AURBLGD: awkwardly
AURBLG: awkwardly  # without D is more comfortable
PHAEUFPL: maturely
RE/PAOELTD: repeatedly
SPREULT: separately
SPRAOEULG: surprisingly
THEURLD: thirdly
```

Tuck in E for -y

```yaml
HOEB: hobby
OERPBLG: originally
```

Prefer lowercase to not have `*` and uppercase to have `*`

```yaml
TKPWRAOEU: gui
TKPWRAO*EU: GUI
PABG/PHAPB: pacman  # used for arch linux package management
PABG/PHA*PB: Pacman
WERPB: western
W*ERPB: Western
```

Prefer -Z for plurals if there are conflicts

```yaml
TKPWAOEUS: guise
TKPWAOEUZ: guys
```

KP* for ex-

```yaml
KP*ERPBL: external
```

/*ER for words with -er

```yaml
HAFRP/*ER: hamper
```

OEU for -y

```yaml
HO*EULT: healthy  # there's HOEUFLT, but I think the F is a misstroke?
POEUT: pity
THROEUFT: thrifty
TROEUT: treaty
```

## New

### Abbreviations

```yaml
A*PLT: atm
PW-S: bc
PW*D: bday
PW*T: btw
KPHOEUPB: c\'mon
TKPWRATS: congrats
TKW: dw
"*EFP": esp
"*EPS": esp
"*EUBGD": idk
AO*EURBG: iirc
AOEURBG: iirc
"*EURBG": ikr
O*EUPL: imo
OFBS: obvs
O*PLG: omg
P-LS: pls
-RPB: rn
SOZ: soz
S*RS: srs
S*RLS: srsly
TPWH: tbh
KWR*UR: ur
SR-S: vs  # overrides "haves" (use SR-Z)
W-FT: wtf
KWR*/TPHOE: y\'know
```

#### Days of the week

```yaml
PH*OPB: Mon  # PHOPB: mon
TAOU: Tue
TAO*U: Tue  # * for consistency
W*ED: Wed  # WED: wed
THAOU: Thu
THAO*U: Thu  # * for consistency
TPR*EU: Fri  # exists
SA*ET: Sat  # SAT: sat, SA*T: SAT
S*UPB: Sun  # SUPB: sun
```

#### Months

```yaml
SKWRA*PB: Jan  # exists
TP*EB: Feb  # swapped Feb and Feb so the abbreviation has the *
TPEB: February
PHA*R: Mar  # overwrites March (use PHA*FRPB)
PR*EUL: Apr
PHA*EU: May  # it's the same
SKWRUPB: Jun  # overwrites June (use SKWRAOUPB)
SKWR*UPB: Jun  # * consistency
SKWRUL: Jul
SKWRU*L: Jul  # * consistency
A*UG: Aug
S*EPT: Sept
"*OBGT": Oct
TPH*OF: Nov
TK*ES: Dec  # short E
TKAO*ES: Dec  # overwrites "December"
```

### Symbols

```yaml
H-RT: ♥ # heart
SPH-L: :) # smile
SPH*L: :( # unsmile
```

### Words

```yaml
PWAFL/EUFBG: basilisk  # overwrites baffliffic
PWA/SEUL/EUFBG: basilisk  # overwrites basiliffic (if using british_english.md)
A/KUFRD: accursed
KAR/SER/A*L: carceral
KAR/SERL: carceral
KARS/RAL: carceral
KHO*BG: choc  # KHOBG: chock
KROEPB/SRAOEURS: coronavirus
KOEFD: covid
KR*UFT: cruft  # overwrites crust (use KR*US)
EBGS/EUF: EXIF
HA/REUS/SA: harissa
HA/REUS/SKWRA: harissa
HARS/SA: harissa
HARS/SKWRA: harissa
KAO*EF: kiev  # KAOE/*EF: Kiev
PHOTS/ER/REL/LA: mozzerella
PHOTS/REL: mozzerella
STAPB: stan  # overwrites Stan (use STA*PB)
```

### Names

```yaml
A/HREUS: Alice  # AL/EUS, A*LS
TKAO*E: Di  # TKAOEU: die, TKAO*EU: dye, TKEU: did I, TK*EU: di^
TKPWERG/KWROE: Gergo
TKPWERG/KWRO: Gergo
KAEUT/KWREU: Katy  # KAET/KWREU
TAOEUP/KWREU/TAOEUP: Typey Type
KEP/HRER: Kepler
```

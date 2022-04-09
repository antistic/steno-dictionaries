# User

My user dictionary.

↖️ Check out the ☰menu in the top left in GitHub for a table of contents

## Requires

- [plover\_markdown\_dictionary](https://github.com/antistic/plover_markdown_dictionary)

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

## Plover control

```yaml
PHR*UP: {PLOVER:LOOKUP}
TK-LG: {PLOVER:LOOKUP}
S*GS: {PLOVER:SUGGESTIONS}
SK*GS: "{PLOVER:SUGGESTIONS}{#Super(w)}"
```

## Spacing and Mode control

Spacing

```yaml
TK-FPS: {*!}
AFPS: {*?}
"#*": {*}
KHR-R: "{}{^}" # "{^ ^}{#backspace}" # resets prefixes/space, good for form inputs
```

Modes

|     | KPA               | HROER               |
| --- | ----------------- | ------------------- |
| \*  | Next word capital | Next word lowercase |
| \*S | All Caps mode     | Lowercase mode      |
| \*T | Title mode        | -                   |
| \*D | Retro title case  | Retro lowercase     |

- HR\*D retro lowercase
- UP\*D retro caps

```yaml
KPA: {-|}
HRO*ER: {>}
KPA*: {^}{-|}
KPA*S: {MODE:CAPS}
HRO*ERS: {MODE:LOWER}
TPR*S: {MODE:SET_SPACE:-}
STPH*S: {MODE:SET_SPACE:_}
KPA*T: {MODE:TITLE}
```

[elkowar/plover\_retro\_everything](https://github.com/elkowar/plover_retro_everything),

which lets you retroactively format the last stroke with any mode. Repeat to
apply to more strokes.

```yaml
TKPA*D: =retro_everything:{MODE:CAMEL},{MODE:RESET} # capped (delete space)
*UPD: =retro_everything:{MODE:CAPS},{MODE:RESET} # upped
SKWR*D: =retro_everything:{MODE:CAPS}{MODE:SET_SPACE:_},{MODE:RESET} # caps snake
HR*D: =retro_everything:{MODE:LOWER},{MODE:RESET} # l'ed (lower)
HRO*ERD: =retro_everything:{MODE:LOWER},{MODE:RESET} # lowered
TK*D: =retro_everything:{MODE:SET_SPACE:},{MODE:RESET} # d'ed (delete space)
STPH*D: =retro_everything:{MODE:SNAKE},{MODE:RESET} # sn'ed (snake)
KPA*D: =retro_everything:{MODE:TITLE},{MODE:RESET} # capped
```

Other

```yaml
TKHR*RS: {*($c)} # retro format currency
R*EFT: {MODE:RESET}
R-R: {^~|\\n^}{MODE:RESET}
```

## Keyboard Control

Usually I'll use the [symbol](./symbols.py) or [modifier](./modifiers_stack.py) dictionaries. These definitions are for things I use often enough that I'd prefer a special brief for them.

### Keys

```yaml
KHR*R: "{#control(a)}{#backspace}"
STPH-GS: "{#Right}" # no attach, useful for getting out of brackets
```

### Copy and paste

One-handed copy and paste so I can use the mouse at the same time.

Uses `STK` as a starter, and done by shape.

```yaml
STKW: "{#control(c)}"
STKWR: "{#control(x)}"
STKR: "{#control(v)}"
STKR*: "{^ ^}{#control(v)}"
STKHR: "{#control(shift(v))}"
```

### i3 (window manager)

```yaml
KHR-Z: "{#super(w)}" # close window
KHR*Z: "{#control(w)}" # close tab
PR-F: "{#super(braceleft)}" # previous workspace
TPH-GT: "{#super(braceright)}" # next workspace
WOEUPB: "{^}{#super}{^}" # win key (like WOEUPBD window, but without the D)
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
TKR*L: {PLOVER:TOGGLE_DICT:-dictionaries/uk/uk.md,-dictionaries/personal_style.md}{MODE:RESET} # drill
TPH*L: {PLOVER:TOGGLE_DICT:+dictionaries/uk/uk.md,+dictionaries/personal_style.md}{MODE:LOWER} # normal (overwrites non-Hodgkin's lymphoma, use TPHA*UPB/H*L)
PR*RP: {PLOVER:TOGGLE_DICT:+dictionaries/uk/uk.md,-dictionaries/personal_style.md}{MODE:RESET} # proper
R*LD: {PLOVER:SET_CONFIG} # reloads the dictionaries
```

### Other Plover Plugins

[sashac/plover\_retro\_stroke](https://github.com/sachac/plover_retro_stroke),
which lets you retroactively format the last stroke as raw steno. Repeat to
apply to more strokes.

```yaml
STPH*RBGS: =retro_stroke:/,`{MODE:CAPS},{MODE:RESET}` # shape based
STPH-RBGS: =retro_stroke:/,{MODE:CAPS},{MODE:RESET}
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

### Skeletal briefs

```yaml
"*RL": rely # R-L: really, -RL: recall
ST*S: status # ST*TS
```

### Dropped syllables

```yaml
SKWREPBD: agenda # A/SKWREPBD/TKA
TP*EURBL: artificial # TPHR*EURBL
SUPLGS: assumption # SUPGS, A/SUPLGS
STROPB/PHER: astronomer # A/STROPB/PHER
THRAOET: athlete # overwrites throat (use THROET)
TROS/TEU: atrocity # A/TROS/TEU
TAFPLT: attachment # TAPLT, A/TAFPLT
A*UT/TEUFT: authenticity # A*UT/*EPB/TEUFT
AUT/PHEU: autonomy
A*F/KAD: avocado
AF/KAD: avocado
AZ/PWAOEU/SKWRAPB: Azerbaijan # no ER
PWOUPBT: bounty # PWOEUPBT: buoyant
KWEPBGS/HREU: conventionally
TKEUPBLG: digital # TK*EUL, TKEUPBLG/TAL
EL/SAFL/TKOR: El Salvador # EL/SAL/TKOR
PHA*EUL: email # mail + *
THAOUS: enthuse # overwrites 'use it' (use TAOUS). makes consistent with THAOUS/KWRAFT: enthusiast. SPWAOUZ
H*UR: hurry # HUR/KWREU
TPO: info # fo. overwrites "to", a misstroke
SRAOEUT: invite # overwrites vit (use SR*EUT)
SKWREUT: legit # HREPBLGT
HR*ET/SKWREU: lethargy
PHAPB/TP*EFT: manifesto # PHAPB/TPEFT: manifest
PHOTS/REL: mozzarella
PWHRAOEUPBLGD: obliged
HREUFRP/KWRAPB: Olympian # like HREUFRP/EUBG: Olympic.
TPOPB/TEUBG: phonetic # TPOEPB/TEUBG, TPOPB/ET/EUBG
PHREUT/SA*EUGS: politicization
PHREUT/SAEUGS: politicization
PREF/HRAPBS: prevalence # misstroke
PREF/HREPBS: prevalence # pref lens. PREFLS
KWA*RPBT: quarantine # KWARPBT: quadrant
SKRAO*EUB: subscribe
```

### Compacted (still steno order)

```yaml
PWAOUFS: abusive
KPEBL: accessible # like KPES: access
AFPL: actual
AERL: aerial # AEURL: arial
A/TROFT: atrocity # A/TROS/TEU
A*UFPL: autism # AUFPL: awesome
PWHOELD: behold
PWHOLD: behold
KREUFPLS: Christmas
KHROERB: closure # KHRO*ERS
KO*ERGS: coercion # overwrites categories (use KOERGS)
KPARPB: comparison
KHRAO*UD: conclude # KHRUD: included, KHRAOUD: collude
KWAEU: convey
KWAE: convey # like SWAE: survey
KAO*P: co-op
KURPBS: currency
TKHRAOEUPB: deadline # overwrites midline (use PHRAOEUPB)
TK*EBT: debit
TKPHOPBS/PWHREU: demonstrably
STKERPB: discern
STKPARPBLG: disparage
TKWALT: duality # TKAOULT
ELG/-BLT: eligiblity # like ELG/-BL: eligible
EPL/PWEFL: embezzle # embevel
AOEPLT: emit
KPHAEUPBG: exchange # overwrites change (use KHAEUPBG)
KPO*EPBT: exponent
SPOEPBT: exponent
TPAFL: facile
TPAFL/TAEUT: facilitate
TPAERL: farewell
TPAERL: farewell
TPAOEFBL: feasible
TP*EUFG: fixing # like PH*EUFG: mixing
EUPL/PAOUPBT: impunity # EUPL/PAOUPB/TEU
EUPB/KAPB/TKEFPBT: incandescent
KEPB/KWRAPB: Kenyan # KEPB/KWRA/*PB
HRORPL: lorem ipsum # HROR/EPL/EUP/SUPL
PHO*ELD: modal # overwrites model (use PHOELD)
PHRAL: morale # overwrites moral (use PHORL). PHO*ERL
OE/PWHREUFPB: oblivion
PWHREUFS: oblivious
PERPBLG: percentage # there's PWERPBLG, which might be a misstroke
PRO*L: petrol
TPHROFL: philosophical
PRERBT: prescient
PROUPB: pronoun # PRO/TPHOUPB
RARLS: regardless # RARLD
RE/PREFS: repressive
SPREURT: separator
SEFRPBT: servant
SHROEFT: slowest
STPHARBT: snapshot # STPHAP/SHOT
SPRUPL: spectrum # SPREPL
SPEUFRPB: spinach # spinch
SPHEUFS: submissive
SPWORPBT: subordinate
SAUB/STARBT: substantiate
SPREURBL: superficial
THAERPT: therapist # therapy + T. TH*EUFT, THA*EURPS
TPHULT: tumult
TUPLT: tumult
WAOEUFT: wisest
```

### Folding and inversion

#### Ending -G, -S, -D, -Z

```yaml
TK*EUT/*ERS: dithers
PUGD: pudding # pugged
EBGS/TEPB/WAEUGT: extenuating
ES/KHRAEUGT: escalating
RE/TAEUPBD: retained
OP/RAEUTS: operates
TKEUPL/PHATS: diplomats # dim mats
PAOEPBL/AOEUFG: penalizing
AOEU/KOPBS: icons # eye cons. AOEU/KOPB: icon
EURBGZ: irks # overwrites {^-I} (non-Plover)
PWAOE/KOPBS: beacons # bee cons. PWAOE/KOPB: beacon
TKEUZ/TREGS: distressing
TKEUS/TREGS: distressing
SAOEUD/HRAOEUPBD: sidelined # SAOEUD/HRAOEUPB: sideline
KPEFD: accessed
KOEFRD: coerced # overwrites coffered (use KOEFR/-D)
TKPWRAEZ: agrees # like TKPWRAE: agree. overwrites grease (use TKPWRAOES)
ES/KHRAEUTD: escalated # es calculated
AL/HRAOEUD: allied # al lied
AL/HRAOEUZ: allies # alalize. AL/HRAOEUS exists
KOB/WEBS: cobwebs # could be webs
TKEPLTD: demented # departmented
TKEUS/EPB/TPRAPB/KHAOEUFD: disenfranchised
TKAOUP/KATS: duplicates
KPAPBLG/RAEUTS: exaggerates
TPHRUBGT/WAEUTD: fluctuated
HAOUPLD/TEUS: humidities
HAOUPLD/TEUS: humidities
HAOUPLD/TEUZ: humidities
HAOUPLD/TEUZ: humidities
HREPL/O*PBS: lemons
HREPL/PBS: lemons
HREUB/RAEUGT: liberating
PHAOEUG/RAPBTS: migrants
PHAOEU/TKPWRAPBTS: migrants
PA*PBG/-G: panicking
PAR/HAOEUFD: paralyzed
RE/PAOELD: repealed
ST*EUPL/-G: stimming
ST*EUPLG: stimming
TEFRP/TAOURS: temperatures
TEFRP/TAOURS: temperatures
UPB/TKULT/RAEUTD: unadulterated
UPD: upped
```

#### -TD for -ded

```yaml
TKULT/RA*EUTD: adulterated # with star because "adult rated" could be a thing
AG/SRAEUTD: aggravated
TKAOEUTD: decided
TKE/PHOET/SRAEUTD: demotivated
AOE/HREUPL/TPHAEUTD: eliminated
EBGS/KHRAOUTD: excluded
EBGS/TEPBTD: extended
SPWEPBTD: intended
EUPB/SRAEUTD: invaded
P-PB/AEUTD: opinionated
PROEUFTD: provided
RAO*EUPBTD: reminded
SKHRAOUTD: secluded
```

#### Tuck in HR for -ly

```yaml
STKHREPBL: accidentally
HRAFPL: actually # like AFPL: actual
HRALGS: additionally
SHRERBL: essentially
HREFPBL: eventually
TPHR-PBL: financially
TKPWROELS: grossly
TPHAD/SRERLT: inadvertently
STPHAPBLT: instantly # the version without -T exists
TPHROL: normally
KWHRAEULGS: occasionally
KWHRAEUGS: occasionally # KWAEULGS: occasional
HROPGS: optionally
HROPLGS: optionally # OPGS: option (OPLGS: optional defined here)
HRORPBLG: originally
THREURD: thirdly
HRUPLT: ultimately
```

#### Tuck in -L for -ly

```yaml
AURBLGD: awkwardly
AURBLG: awkwardly # without D is more comfortable
PWHRUPBLT: bluntly
KHRAB/TEUFL: collaboratively # KHRAB/TEUF: collaborative
STKPRALT: desperately
TPEUFRLT: firstly
TP*EURLS: firstly
HAEPL: happily
HROULD: loudly
PHAEUFPL: maturely
TPHAOEULT: nightly
PRAOEUFLT: privately
RE/PAOELTD: repeatedly
SPREULT: separately
SWAOERL: severely
SOUPBLD: soundly
SPHREFBG: specifically
STELD: steadily
SKEUPBLGT: succinctly
SKEUPBLG: succinctly # without T is more comfortable
SPRAOEULG: surprisingly
SPRAOEUFLG: surprisingly # SPRAOEULG also exists
THEURLD: thirdly
WAOERLD: weirdly
```

#### Tuck in -L for -le

```yaml
KALT: cattle
KRAEULD: cradle
K*ULD: cuddle
TPRAFL: frazzle
TPHAOLD: noodle
REF/KABL: revocable
STA*RLT: startle
TA*LT: tattle
THROLT: throttle
```

#### Tuck in -R for -er, -or

```yaml
A/KAOUPL/HRAEURT: accumulator
A/KAOUPL/HRAEURT: accumulator # A/KAOUPL/HRAEUT: accumulate
A/SRERPBG: avenger
KHRURT: clutter
KHRAB/RAEURT: collaborator # collab rarity. KHRAB/RAEUT: collaborate
KRURBGT: constructor
KAUPB/SAOURPL: consumer # KAOURPL
TA*EURPB: container  # * because ^itarian
KAORBG: cooker
SKWRAOURPB: junior
HRAURPBD: launder
HRAORS: looser
PHURT: mutter
OE/PREFR: oppressor # OE/PRES/O*R
OE/PREFRS: oppressors
PAEUPB/KEURL: painkiller # PAEUPB/KEURLS: painkillers
PRAOUFR: previewer
STAERT: starter
STRAOERPL: streamer
SWARG: swagger
```

#### Tuck in E for -y

```yaml
KAERBL: casually
HOEB: hobby
OERPBLG: originally
PAERBL: partially # overwrites partial (use PARBL)
```

#### F for S

```yaml
KHROEFL: closely
```

#### Other

```yaml
TPAEURPLGS: affirmation # fold in A-
TPAEURPL: affirm # overwrites fairly (use TPAEURL)
TAEPLT: attempt
TAEFRPT: attempt # fold in A-
TAEPLT: attempt # fold in A-
KAEF: cafe
KRERPBT: century # overwrites center (use STR)
KHRAEUFR: clarify # KHRAEUR/TPEU
SKAOEL: conceal
KAUPB/SPEURT: conspirator # conspirit
SKRAEUPB: constrain
SKRUBGT: construct # KRUBGT
TKEURBGS: dictionary # overwrites dirks (use TKEURBGZ)
TKWAOEUFS: divisive
SPHROEURT: exploiter
TPAOEFRL: fearful # TPAOER/-FL
TPORLT: formality
TKPWRAEUFLT: grateful # TKPWRA*EUFL
HORP: hopper # overwrites who were (use WHORP)
HO*ELT: hotel
HOELT: hotel
KWAEULGS: occasional # overwrites occasionally (use KWHRAEUGS or KWHRAEULGS)
OPLGS: optional # OPGS: option
PRE/KAEURT: precarity # PRE/KAEUR/TEU
RAELTS: realities # like RAEL: real
RAELT: reality # like RAEL: real
SABG/TPAOEUFD: sacrificed # overwrites 'sack fived'. SARBG/TPAOEUFD
SKWEFRT: sequester
SKEPLT: skeptical # squishing SKEPT/K-L. SKEPT: concept
SPRAOEUGS: surprising # SPRAOEUS: surprise + G (without final -S exists)
SRAOEPBG: vegan
```

### Orthography fixes

Nearly works but the spelling is wrong.

```yaml
A/KUFPL: accustom # A/KUFPLD: accustomed exists
KPHRO*EUT/TEUF: exploitative
KPHROEUT/TEUF: exploitative
SPHROEUT/TEUF: exploitative
KWR-D/HROG: idealogue
KWR-D/OLG: ideology
PHAR/KWROPB/AO*ET: marionnette
PET/HR*EPBT: petulent # pettulent
RE/KOFR/KWREU: recovery # recoverry. ROFR/KWREU
UPB/SERPB/TEU: uncertainty
```

### Boundary errors

```yaml
PWAEUS/SAL/REU: base salary # basalry
```

### Different emphasis

```yaml
SKOPBD: second # SEBGD
SWERL: several # SEFRL
```

### Different word boundaries

```yaml
A/HREUS: Alice # AL/EUS, A*LS
A/TPHEBG/TKOET: anecdote # APB/EBG/TKOET
A/TPHEBG/TKOET: anecdote # APB/EBG/TKOET
A/ROE: arrow # AR/ROE
A/SET: asset # AS/SET
A/SETS: assets
A/TEUBG: attic # AT/TEUBG
A/SRAPBT/TKPWARD: avant-garde
PWREUT/A*PB: Britain # PWREU/TAPB
KAUPB/SPEURT/O*R: conspirator # KAUPB/SPEUR/TOR
TKPHOPBS/STRA/PWHREU: demonstrably # TKEPL/STRAB/HREU
TKEUS/APL/PWEUG/WA*EUT: disambiguate
TKEUS/APL/PWEUG/WAEUT: disambiguate
TKEUZ/AEUPL/PWEUG/WA*EUT: disambiguate
PHORT/*EUGS: mortician # PHOR/TEUGS
TPHEG/AEUGS: negation # TPHE/TKPWAEUGS
OBGT/A*L: octal # also OBG/TAL
HREUFRP/EUBG: Olympic # overwrites limpic. HREUPL/PEUBG
PE/REUL: peril # PER/EUL
REUBG/TEU: rickety # REUBGT/KWREU
SKED/HREUPBG: scheduling # SKED/-G
SPEBG/TAEURT: spectator # from SPEBG/TAEUT. like SPEBGT/AEURT
STOEUPB/TKPWRAEF: stenography # STPHOG/TPEU
SRULT/AOUR: vulture
```

### Different way of writing word parts

```yaml
TKPHEUPB/STRAF: administrative # TKPHEUPB/STREUF
AFRP/TPAOEU: amplify # AFRP/TPEU
APBGS/TEU: angsty # APBGS/KWREU
A/ROE/PHA/THAERP: aromatherapy # prefer THAERP for therapy
ATS/TPAOERBG: atmospheric # ATS/STPAOERBG
ATS/TPERBG: atmospheric # ATS/STPAOERBG
AUPL/TEUBG: automatic # AUPL/EUBG
PWA/ROPB: baron # PWAR/ROPB
KHRARS/SA: Clarissa # KHRARS/KWRA
KAU/HREUGS: coalition # KOE/HREUGS
KAU/HERPBS: coherence # KO/HERPBS
KAU/HERPBT: coherent # KO/HERPBT, KAU/HAOERPBT
TKE/SAO*EFD: deceived # overwrites dereceived, TKE/SAOEFD: deceased, also TKAOE/SAOEFD and STKAOEFD
TKEUZ/POEUPBTD: disappointed
TKEUZ/PWURS: disburse
TKEUZ/SERPB: discern # overwrites discertain
TKEUZ/PHREUPB: discipline
TKEUZ/KRAOET: discreet
TKEUZ/KRAET: discrete
TKEUZ/KREGS/REU: discretionary
TKEUZ/TKEUFL: dismissal # TKEUS/PHEUFL
TKEUZ/PARPBLG: disparage
TKEUZ/PARPBLG/-G: disparaging
TKEUZ/PRAT: disparate
TKEUZ/PEPBS: dispense
TKEUZ/RUPT: disrupt
TKEUZ/RUPGS: disruption
TKEUZ/PAEUT: dissipate
TKEUZ/PAEUTD: dissipated
TKEUZ/TEUPBGT: distinct
TKEUZ/TRAUT: distraught
TKEUZ/TURBD: disturbed
THAOUS/ST-BG: enthusiastic # makes consistent with THAOUS/KWRAFT: enthusiast
HER/TEUPBLG: heritage # her to the best of my knowledge. HER/TAPBLG
HUBG/*L/PWER/REU: huckleberry # REU instead of KWREU
PH*ERT/PHREUS: metropolis # like PH*ERT: metro^. PHERT/PHREUS: metropolis
PH*ERT/POL: metropolitan # like PH*ERT: metro^. PHERT/POL: metropolitan
PH*ERT/POL/TAPB: metropolitan # like PH*ERT: metro^. PHERT/POL/TAPB
PHEUZ/KRAOEPBT: miscreant # PHEUS/KRAOEPBT
PHEUZ/KRAPBT: miscreant # PHEUS/KRAPBT
PHEUZ/HAPS: mishaps
PHUPB/TREU: monetary # PHUPB: money. PHOPB/TREU
PHUPB/KAE: monkey # phonetic. PHOPB/KAE
AUR/TKPWAPL/SKWREU: origami # ^i instead of PHEU. AUR/TKPWAPL/PHEU
AUR/THO: ortho
AUR/THOE: ortho # ORT/THO
SPHO*EUD: social media # SPHAO*ED. Make it more like PHO*EUD: media
STAOUD/KWRO*E: studio # STAOUD/KWROE. KWRO*E: ^io
SPR/TPEURBL: superficial # superofficial. SAOUP/TPEURBL
SPR/STEUGS: superstition # SAOUP/STEUGS
S-PL/ABG: systematic # system ack. Like PRO*B/ABG: problematic
TEFRP/KHAOUR: temperature # TEFRP/TAOUR and TEFRP/KHUR exist
TERPB/REU: ternary # TERPB/AER
TRAPBZ/SEPBD: transcend # TRA*PBS/SEPBD, TRAPBZ/EPBD
TRAPBZ/PAEURPBS: transparency # like TRAPBS/PAEURPBT
TRAPBZ/PARPBS: transparency # like TRAPBZ/PAEURPBS
AUPLD: upload # UPLD. like AUP: up^, AUPTD: update
SRAFRP/AOEUR: vampire # SRA*PL/AOEUR
SROL/KA*PBG: volcanic # SROL/KAPBG
WAUL/PAEURP: wallpaper # WAUL/PAEUP
```

Vowel changes

```yaml
PHAOUFP: mature # PHAEUFP. Like PHAOURT: maturity
```

### Accidentally adding a prefix to a brief.

```yaml
ABG/TKPHEUBG: academic
AD/HAO*EFS: adhesive
AL/TKPWR*EUFPL: algorithm
A/PHAEUFPLT: amazement
A/R*EUT/PHET/EUBG: arithmetic
TKE/STROEUR: destroyer
AOE/HREUPL/TPHAEUGT: eliminating
AOE/TPHABGT: enact
EUPB/TWAOUF: intuitive
```

### Alternative by spelling

```yaml
STKHREPBL: accidentally
PWHR*EU: bleu # PWHR*U
KAFLT: castle # KAFL
KOUS/KOUS: couscous # KAOUS/KAOUS
KREUFLT: crystal # KREUFL, no T
TKAEURPBLG: danger # TKAEUPBLG, no R
TKAOEFPBLT: decently # TKAOEPBLT, no F
TKAOEFPBT: decent # TKAOEPBT, no F
TKOEFPS: DevOps # TKOPS (it has both an E and O in it)
TKO*ET: doth # TKA*UT, TKO*T: do the
SHRERBL: essentially
HREFPBL: eventually
TPOURPL: forum # TPAURPL
TKPWROELS: grossly
TPHAD/SRERLT: inadvertently
STPHAPBLT: instantly # the version without -T exists
HRO*UT: layout # HRO*EUT
PHED/KWROERBG: mediocre # PHAOED/KWROERBG
PHOEURBG: motorHRAFPL: actually # like AFPL: actual
PHAOUFPL: museum # PHAOUPL, no F
TPHROL: normally
HROPGS: optionally
HROPLGS: optionally # OPGS: option (OPLGS: optional defined here)cycle # PHOEUBG, no R
HRORPBLG: originally
PREFRPBL: preferential # PREFRL, PRERPBL
PRAERP: prepare # PRAEP, no R
PROERP: proper # PROER, PRORP
RAOEFPBLT: recently # RAOEFPBLT, no F
RAOEFPBT: recent # RAOEPBT, no F
STAURPBT: restaurant # STRAUPBT
TAURPBT: restaurant # TRAUPBT
SHAEL: shale # SHAEUL
THREURD: thirdly
TPHRAPBT: transplant # THRAPBT, no P
HRUPLT: ultimately
```

### Alternative by pronunciation

```yaml
HAEUFPD: ADHD # HA*ED
AOEU/SHA: Aisha # AOEU/AOERB/SHA
AOEURB/SHA: Aisha # AOEURB/SHA
A/RAOEU: awry
A/REU: awry
PWE/SERBG: berserk
KERB: curb
TKUFPB: dozen # TKOZ, TKOFPB
KPEFRP/TPAOEUD: exemplified # KPEFRP/TPEUD
KPEFRP/TPAOEU: exemplify # KPEFRP/TPEU
EBGS/TERBL: existential # EBGS/TEPBL
SKWREPB/WEUPBL: genuinely # SKWREPB/WAOEUPBL
TKPWOL: goal # TKPWAOL
AOEUS/KWROE: "{iso^}" # AOEUS/KWRO
KAOEU/PWORB: kibosh # KEUB/ORB
SKWREUT/PHAEUT: legitimate # verb version. SKWREUT/PHAT
PHAR/KWROPB/ET: marionnette
TPHAO*EUF: naive # TPHAOEF, TPHAOEU/AOEF
PRAED: parade # PRAD: parade, PRAEUD: prayed
SHED/HREUPBG: scheduling # shedling
SULT: subtle # SUBLT
SULT/HREU: subtly
S*EPB/*EUT: zenith # SAO*EPB/*EUT
```

### Star

#### No star version.

```yaml
TPHEUFT: antagonist
PWAOELT: beetle
SKAEUD: cascade
KRUF: constructive
TP-RB: efficiency
TERPBL: eternal
AO*URP/KWRAPB: European # AO*URP/KWRA*PB
AO*URP/KWRAPBS: Europeans # AO*URP/KWRA*PBS
EBGS/TROEFRT: extrovert # EBGS/TROEFRT
TPRAZ/-L/-D: frazzled
TPRAZ/-LD: frazzled
TPRAZ/-L: frazzled
SKWRERPB: German
HUPB: hun # overwrites hundred (use HUPBD)
HRERB: leisure
TPHAOELT: neatly
-PBT: "{^n't}" # overwrites ' (use symbols/AE)
OURSZ: ourselves
PEFR: perf
SPOF: responsive
```

#### With star versions.

```yaml
HR*RD: already
TKA*FL: dazzle
HR*EFPBT: eleventh # HREFPBT
HAFRP/*ER: hamper
HED/KWART/*ER: headquarter # HED/KWART/ER
PEUBGS/*EL: pixel # PEUBGS/EL
```

### Swaps/shuffles

Swapping, shuffling entries because I didn't like what was there before.

```yaml
A*EPL/-S: apples # overwrites amps (use AFRPS)
A*EPLS: apples # overwrites amps (use AFRPS)
KHRAEURT: calculator # overwrites clarity (use KHRAERT), fold in E
KHRAERT: clarity # overwrites calculator (use KHRAEURT), like KHRAEUT: calculate
KHRAO*UD: collude
KHRAO*UGS: collusion
KHRAOUD: conclude
KHRAOUGS: conclusion
KEFRBT: conservative
KEFRB: conserve # overwrites conservative
KRAO*EBG: critique # overwrites pancreatic. like TAO*EBG: technique
SKWRERPBLT: generality # follows SKWRERPBL: general
SKWRERPBL: general # overwrites generally (use SKWHRERPBL). I didn't like how -R made it -ly
SKWREPBLT: gentle # without * since general was moved
HERD: herd # overwrites heard (use HAERD)
STPHEUFT: insist # overwrites "snift" (use STPHEUFT/STPHEUFT)
SPWROUBGS: introduction # TROUBGS. overwrites obstruction
HRA*S: last # overwrites las (use HRAZ)
HREURLT/-S: literals # overwrites liters (use HRAOERTS)
PHOELD: model
PHOLD: mold
OEU: oi # overwrites / (use symbols dictionary)
OBGS: ox # overwrites objection (use OPBLGS)
KRA*EBG: pancreatic
REF: ref
R*EF: rev
S*EFL: {^self}
SEFL: self
SPREUTS: separates # overwrites spritz (use SPREUTZ, defined here)
STPHEUFL: sniffle # swap sniffle and snivel so that *F: V, -F: F
STPHEUFT/STPHEUFT: snift
STPH*EUFL: snivel # swap sniffle and snivel so that *F: V, -F: F-8
SPREUTZ: spritz
SAOURP: super # overwrites supper (use SURP)
SURP: supper # overwrites syrup (use SEURP)
HRAOURBL: usually # HR + usual
AOURBL: usual # overwrites usually
SR*EUPL: victim
SREUPL: vim
KWRUP: yup # overwrites up^, use AUP
```

### Closed and open forms

With and without spaces

```yaml
PWEURT/SWAOET: bittersweet # PWEUT/*ER/SWAOET: bittersweet
PWHROBG/KHA*EUPB: blockchain
STOER/TERL: storyteller # story teller. STOER/TEL/*ER exists. STOER/TELG: storytelling is also closed
TAOEUPL/STA*FRP: timestamp # with asterisk to keep TAOEUPL/STAFRP: time stamp
```

### Different punctuation

```yaml
PWHRA/PWHRA: blah blah
PWHRA/PWHRA/PWHRA: blah blah blah
HA/HA: haha # ha-ha
HA/HA/HA: hahaha # ha-ha-ha
H*E/H*E: heh heh # heh-heh
POP/SKWRUP: popup # pop-up (use POP/SKWR*UP)
SAOEUPB/SKWRUP: signup # overwrites sign-up (use SAOEUPB/SKWR*UP)
```

### Different capitalisation

```yaml
TORL: editorial # overwrites Editorial
HRAPBG: lang # overwrites Lang
```

### Overwrites

Overwrites without having an entry for what was there before.

```yaml
TAEUPBD: contained # overwrites tained, which probably isn't a word? #400
PHA/SKWROPBG: mahjong # mah jongg. Different spelling. Merriam Webster says mah-jongg, but Wikipedia says mahjong, which is also the spelling I'm more familiar with
PHEFRPB/TKAOEUZ: merchandise # merchandis (possible typo? #400)
```

#### Undo misstrokes

```yaml
PWAR/TKPWAPB/-G: bargaining # bagaaining (#400)
STRAORD/HREU: straightforwardly # extraordinarily (use KPRAORD/HREU)
TOED/AS: today as # today's (use TOED/AES)
HU/U: uh you # huh-uh (use H*U/H-B/HU)
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
PAUZ: paws # overwrites pause (use PAUS)
```

### KP\* for ex- (and KP if it is free)

(It's kind of plover, but not consistently)

```yaml
KP*EL: excel # EBGS/EL
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
KPA*UFT: exhaust # KPAUFT
KPAPBD: expand
KPA*PBD: expand # EBGS/PAPBD
KP*EPBS: expense # SPEPBS
KP*ERPLT: experiment
KPERPLT: experiment # SPERPLT
KPHRA*EUPB: explain # SPHRAEUPB
KPHRAPBGS: explanation
KPHRA*PBGS: explanation # EBGS/PHRAPBGS
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
SPWRAOUD: introduced # TROUD
SPWRAOUFD: introduced # TROUD
SPWRAOUS: introduce # TROU
SPWAOUGS: intuition # TWAOUGS
SPWAOUFL: intuitively # TWAOUFLT
SPWAOUF: intuitive # TWAOUF
SPWAOUFT: intuitive # TWAOUFT
SPWAOUT: intuit # TWAOUT
```

### STPH for ins-

```yaml
STPHEUFPBT: insistent
STPHAOEUR: inspire
STPHEUL: instill
STPHRUBGT: instruct
STPHREBGS: insurrection
RE/STPHAEUT: reinstate
```

### OEU for -y

(Though not exclusively)

```yaml
PWOEUR: bury
STKOEUFR: discovery # like SKOEUFR and STKOEFR
TKOEUT: duty
KPOEUR: expiry # KPAOEUR: expire
TKPWOEULT: guilty
HO*EULT: healthy # there's HOEUFLT, but I think the F is a misstroke?
POEUT: pity
THROEUFT: thrifty
TROEUT: treaty
```

### -FR for -M

```yaml
TPHAFRL: animal
A/SUFRPGS: assumption
SUFRPGS: assumption
PWUFRBL: bumble
KAFRL: camel
KOFRP/SEUT: composite # comp sit
TKAOEU/TPHAFRBG: dynamic
EFRP/SAOEUFD: emphasized
EFRP/TEUBG: emphatic
EFRP/KHREU: emphatically
EPB/SEFRBL: ensemble
EPB/SOFRBL: ensemble
TKPWAFRBL: gamble
TKPWRUFRBL: grumble
SKWRUFRBL: jumble
TPHEUFRBL: nimble
RAFRBL: ramble
RE/SEFRBL: resemble
SKRAFRBL: scramble
STUFRBL: stumble
TREFRBL: tremble
TRAOEUFRP: triumph
KWRAFRL: yaml
```

### SWR for -Z

```yaml
SWR*EUPBG: zinc
```

### SKWR for suffix

```yaml
SKWROEFR: {^over}
```

### Other

```yaml
TKA*EGS: accommodation # like TKA*ET: accommodate
TKAEGS: accommodation # no * since it's free
AL/HRAOEUZ: allies
A/TPHEPL/TPHE: anemone
ARB/TREU: arbitrary # ARB/TRAER
-RPBT: "aren't" # other side R
A*ERG: argh # like HA*E: ah. A*RG
AUDZ: audience # AUPBS
PWHR*UT: Bluetooth # bluth. short u like PWHRU: blue
PWR-R: brr
KHAO*S: chaos # KHAOS: choose, KAOS: consists
KHAO*T/EUBG: chaotic # like the new KHAO*S
KHAOT/EUBG: chaotic # like the new KHAO*S
SKHRAEUGS: circulation # overwrites acceleration (use SHRERGS)
KPHAOUBGS: communication # KPHAOUPBGS, no n like KPHAOUBGT: communicate
K-FG: config
SKEF: consecutive
KR-RT: contractor # like KR-T: contract. overwrites ^ (use symbols dictionary SKWH-RPG)
KWEPBL: conventional # SREPBL
KO*ERP: copper # KO*RP
STKAOEUF: decisive # STKAOEUFS
TK-PBGS: definition # define + shun
TK-FGS: definition # def + shun
ROEUR/TPHOUS: erroneous
EFL: eventually # like UFL: unfortunately
SKRAOURBT: excruciate
KPRAOURBGT: excruciating
SKRAOURBGT: excruciating
SPAPBGS: expansion
SPHROEFS: explosive
TKPWO*FP: gotcha
TKPW-PLT: government # TKPWOPLT, TKPW-FT
H*EPL: helm # HEL/*PL
HOEPL/SEBGS/WAELT: homosexuality
HOEFPL: hopeful # HOEFL, no P
AO*EULD: idle # overwrites "Island"
KWRA*EU: i.e. # AOEU/KWRAOE. Like KWRO*EU: i.e.,
EUPL/PHREUBGS: implication # EUPL/PHREUBGS/-S: implications exists, so why not this?
TPHERBL: incredible # TPHRERBL: incredibly
KPWEPBT: indent # SPWEPBT: intent
TPH-RBT: inefficient # TPH: in + TP-RBT: efficient
SPWEGT: integrity
SPWERPBLT: internment
EUPBT/PRERT: interpreter # EUPBT/PRET/*ER
KAO*EUF: kinda # like KAOEUF: kind of
HRAPT: laptop
HR-PBLG: logic # L-J
PHAOULT: mutual
TPHUPL/K*L: numerical
TPHUPL/K-L: numerical
OURP: occupier # like OUPG: occupying, OUPD: occupied
OUP: occupy # overwrites up (use UP). Like OUPG: occupying, OUPD: occupied
OERPBT: orient # overwrites interior (use SPWAOER)
PROUPBZ: pronouns # PROUPBS: pronounce
R-FL: relatively
R-F: relative # overwrites rf (use R*F in programming.md)
R-FPL: respectful
R-FR: review
SAEPB: sane # SAEUPB
SKWA: schwa # SKHA, SKWHA
STPH*EUF: sensitive # like STPH*EUFT: sensitivity
SWAUPBS: "someone's" # someones + A, like AE: '
SPR/SRAOEUFG: supervising
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

- \+O: go / going / goes + to

Doesn't work for "gone"

```yaml
TKPWOG: going to # overwrites going (use going)
TKPWO: go to # overwrites go (use TKPW)
TKPWOS: goes to # exists
TKPWOBG: going to be
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

- Part of

```yaml
PAFRT: part of # overwrites "part of the"
PA*FRT: part of the
PAFRTS: parts of
PA*FRTS: parts of the
```

- Other

```yaml
SKPAF: and a half # TPHAF was used for nav/naff
TPHOEPLT: at the moment
TKWOER: "don't worry"
TPRAOEUPLT: from time to time # TPREUPLT
KWR-G: I guess
KAOEUF: kind of # KAOEUFPBD
KAOEUFS: kinds of
PHOEF: most of
WUPBD: on one hand
ORPB: other than
OUFT: out of the # overwrites oust (use O*UFT)
STPA*RS: so far as
SPH*D: some day
SPH-PL: some people
SOFPS: so much as
THA*EBGT: that is correct
TOUPBDZ: to understand # TOPBDZ
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
H-RT: ♥  # heart
H*RT: 💛 # because everyone has a signature heart colour, right?
SPH-L: :) # smile
SPH*L: :( # unsmile
```

### Names

```yaml
SHAPB/TEL: Chantelle
TKAO*EU/TKAO*EU: Di # overwrites di. TKAOEU: die, TKAO*EU: dye, TKEU: did I, TK*EU: di^
TKPWERG/KWROE: Gergo
TKPWERG/KWRO: Gergo
EUPL/SKWREPB: Imogen
KA/REPB: Karen # overwrites "karen"
KEP/HRER: Kepler
KW-PLG: qmk
KW*PLG: QMK
TAOEUP/KWREU/TAOEUP: Typey Type
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
AB/SAEUL: abseil
A/KUFRD: accursed
AO*ET/*ER: aether
AG/TPHOE/TOLG: agnotology
A/HA/HA: ahaha
PWAP: bap
PWAFL/EUFBG: basilisk # overwrites baffliffic
PWA/SEUL/EUFBG: basilisk # overwrites basiliffic (if using british_english.md)
PWEU/PWEUPL/PWAP: bibimbap
PWOE/PWA: boba
KAR/SER/A*L: carceral
KAR/SERL: carceral
KARS/RAL: carceral
KHAOER/HRAOED: cheerlead # KHAOER/HRAOERD: cheerleader
KHO*BG: choc # KHOBG: chock
S*EUS/SKWREPBD/*ER: cisgender
S*EUS/SKWRERPBD: cisgender
S*EUS: cis # overwrites cyst (use KREUFT)
KHROEZ: cloze # overwrites close (use KHROES)
KAUPB/TEPL: contemn
KROEPB/SRAOEURS: coronavirus
KOS/PHRAEU: cosplay
KO*EFD: covid
KOEFD: covid
KR*UFT: cruft # KRUFT: crust
TKOBGS/AEUFT/EUBG: doxastic
TKOBGS/AFT/KHREU: doxastically
TK-R: Dr.{-|} # overwrites "--" (use symbols dictionary SKWHAOPLS)
AOED: Eid # overwrites he'd (use HAOED)
AOEU/TKPWEPB: eigen
EFBL: evitable # TPHEFBL: inevitable
EBGS/EUF: EXIF
TPARB: fash
TPAOEF/TKOPL: fiefdom
TKPWRA*EFZ: greaves # overwrites Gram negatives. AE since conflict with grieves
HA/REUS/SA: harissa
HA/REUS/SKWRA: harissa
HARS/SA: harissa
HARS/SKWRA: harissa
EUPB/EF/-BLT: ineffability # like EUPB/EF/-BL: ineffable
EUPBS/TA: insta
EUPBT/KWRO/SEPGS: interoception
EUPBT/SKWRO/SEPGS: interoception
SPWROEPGS: interoception
EUPBT/KWROE/SEPGS: interoception # otherwise does interro
SKWRAEPBG: janky
SKWRA*PBG/KWREU: janky
SKWRAPB/KEU: janky
SKWRAOU/SREU: juvie
KE/PWAB: kebab # KA/PWOB: kabob
KAO*EF: kiev # KAOE/*EF: Kiev
PHAOEFPB: meson
TP*EPB/STOEUPB: phenrsteno
TPERPB/STOEUPB: phenrsteno
S*EBGS/ED: sex ed
S*EUPL: sim
SPHOL: smol
SPR*EUT: SPRiT
S-FD: ssd
STAPB: stan # overwrites Stan (use STA*PB)
STOEUPB/TPH*EUPL: stenonym # overwrites steno nipple
TA/TKA*: tada
THOT: thot
TO*T: tot # overwrites to the (use TOT)
TREFL: trestle
AO*UPB: uni
SRABGS: vax
SRABGS/-D: vaxxed
SRAGD: vaxxed
```

#### Prefixes

```yaml
KO*PL: {com^} # overwrites comp (use KOFRP)
EUPBS/TA*: {insta^}
A*UPB: {on-^}
PRO*: {pro-^}
A*UP: {up-^}
```

#### Suffixes

```yaml
AEURPBT: {^ariat}
A/THOPB: {^athon}
PWO*BGS: {^box}
PHOPBG/*ER/-G: {^mongering} # fixes ^mongerring
T*EU: {^ty}
T*EU: {^ty}
```

#### Compound

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

#### Moves existing entries

```yaml
KORPB/SKWRE: Corne # overwrites coryne^ (use KOR/REUPB)
KOR/REUPB: "{coryne^}"
HART: hart # overwrites heart
HAERT: heart
PH*EUFBG: miscellaneous
PHEUFBG: misc # overwrites miscellaneous
PO*EUL: "{poly^}"
POEUL: poly # overwrites poly^
KWRE: ye # overwrites yes (use KWRES)
KWRES: yes # overwrites yes, sir (did not redefine since I don't use it)
```

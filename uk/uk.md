# UK

This covers some differences that aren't covered by the script.

I try to reference the [Wikipedia page](https://en.wikipedia.org/wiki/American_and_British_English_spelling_differences) for the differences, but sometimes I choose whatever spellings I'm used to, and sometimes I want to be able to use either.

### Requires

- [plover\_markdown\_dictionary](https://github.com/antistic/plover_markdown_dictionary)

## Table of contents

- [Spelling](#spelling)
  - [-e words](#-e-words)
  - [-ce (nouns), -se (verbs)](#-ce-nouns--se-verbs)
  - [Suffixes](#suffixes)
  - [Other](#other)
- [Pronunciation Differences](#pronunciation-differences)
- [Regional words](#regional-words)
  - [URLs](#urls)
  - [Places](#places)
    - [Place suffixes](#place-suffixes)
  - [Currency](#currency)
  - [Other](#other-1)

## Spelling

### -e words

Can generally handled by Plover's `SKWRE: {^e}`. For example, `PRAPL/SKWRE:
programme`.

```yaml
TOPB/SKWRE: tonne
TPHAOURPB/SKWRE: neurone
```

### -ce (nouns), -se (verbs)

following the `SREUS: advice`, `SREUZ: advise` pattern that is already in the dictionary

```yaml
PRABGS: practice # exists
PRABGZ: practise
HR-PBZ: license
HR-PBS: licence #  overwrites license
```

### Suffixes

```yaml
AOEUBL: {^isable}
SA*EUGS: {^isation}
AOEUZ: {^ise}
AO*EUFD: {^ised}
AO*EUFG: {^ising}
```

### Other

```yaml
AEUPBLG/-G: ageing
A*PL/AOUL: ampoule
APB/HROG: analogue # overrides analog (use APB/HRO*G)
ART/SKWREU/TPABGT: artifact
PWE/HAOF: behoove # behove is PWE/HAO*F
PWREPBT: brent
PWR*EPBT: Brent
SKEL/-D: cancelled
SKELD: cancelled
STR*: centre
KWAL/-G: equalling
KWALG: equalling
SKWRA*EUL: gaol
KERB: kerb # overrides curb (use KURB)
HRAEUB/KWROUS: laborious
HRAEURB/KWROUS: laborious
HRAOEUB/*EL/OUS: libellous
HRAOEUB/EL/OUS: libellous
HRAO*EUBL/HROUS: libellous
HRAO*EUBL/OUS: libellous
HRAOEUBL/HROUS: libelous
HRAOEUBG/-BL: likeable
PHAT/*T: matt
PHAOERT: metre # overrides meter (use PHAOET/*ER)
TPHAOEF/TAEU: naivete # US spelling
KWARLD: quarrelled
RAEUT/-BL: rateable
RAOEUD/-BL: rideable
SAF/REU: savory # still have the other options for "savoury"
STPHAL/-G: signalling
STPHALG: signalling
SAOEUZ/-BL: sizeable
TAOEUR: tyre
UPB/SHAEUBG/-BL: unshakeable
WHEUFBG/KWREU: whisky # overrides whiskey (use WHEUFBG/KWRAOE)
WAOL/KWREU: woolly
KWROG/HURT: yoghurt
```

## Pronunciation Differences

The words exist in the dictionary, but I say them differently

```yaml
PWAOET/KWRA: beta
PWA/SEUL: basil
PWAEFL: basil # PWAFL: baffle
SHED/AOUL: schedule # shed/^ule. already exists under `SHED/KWRAOUL`, `SKED/AOUL`
TPHAT/TOE: tomato
TPHAT/TOES: tomatoes
RAOURT: router
```

## Regional words

### URLs

```yaml
PAOUPBG: {^.uk} # folded
P-P/AOUBG: {^.uk}
P-P/UBG: {^.uk}
KOUBG: {^.co.uk}
KROUBG: {^.co.uk}
```

### Places

```yaml
PWEBGS/HREU: Bexley
PWREUPB: Britain
PWREUBGS/STOPB: Brixton
PWREUBGS/TOPB: Brixton
KHRAP/HA*PL: Clapham
TPEUPBS/PWRE: Finsbury
HAFRP/SHEUR: Hampshire
HAOEUD/PARBG: Hyde Park # HAO*EUD/PA*RBG
TKPW*B: GB
HAEUFRG: Havering
HOL/PWORPB: Holborn
HRAPB/KAFRT: Lancaster
TOT/TPHAPL: Tottenham
WAP/-G: Wapping
WAPG: Wapping
```

#### Place suffixes

```yaml
PWRE: {^bury} # PW*UR/KWREU exists
KAFRT: {^caster}
PHOUT: {^mouth}
```

### Currency

```yaml
P*PBDZ: {*(£c)}
```

### Other

```yaml
ARS: arse
PER/TPHEUBG/TEU: pernickety
OE/PWER/SKWRAOEPB: aubergine
PWA*EUPL: BAME
PWAO*EB: BBC
PWAOEB: beeb
PWOPBLG: bodge
PWREBGS/EUT: Brexit
KHUF: chuff
KORPBLG/AO*ET: courgette
KOR/SKWRET: courgette
KRAEUL: CrossRail
KR*F: CV
KWRU: EU
KWROEUR/SREUGS: Eurovision
TPAF: faff
HAOFR: hoover # overwrites Hoover (use HAO*FR)
TPHOB/HREU: knobbly
HREUD/*L: Lidl
PHOPB/SO*: Monzo
-FRP: MP
TPHAF: naff
TPHAPB/TKOES: "Nando's"
TPH*S: NHS
PRAPL/PWHRAEURT: perambulator
PER/APL/PWHRAEURT: perambulator # PER/APL/PWHRAEUT/O*R
PRAEPL: pram # PRAPL: program
PEUPBLG/PHAS: pyjamas
PEU/SKWRA/PHAS: pyjamas
SAEUPBS/PWREUS: "Sainsbury's"
SAEUPBS/PWRAOES: Sainsbury\'s
SEFP: sesh
SOEF: sofa
TEL/HREU: telly
THREL: telly
TEFBG/SKWRO: Tesco
TES/KOE: Tesco
TES/KOES: "Tesco's"
TEUT/PWEUT: titbit
```

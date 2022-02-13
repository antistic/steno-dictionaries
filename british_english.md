# British English

### Requires

- [plover_markdown_dictionary](https://github.com/antistic/plover_markdown_dictionary)

Table of contents:
- [Spelling Changes](#spelling-changes)
- [Pronunciation Changes](#pronunciation-changes)
- [URLs](#urls)
- [Briefs](#briefs)
- [Regional words](#regional-words)
- [Places](#places)
- [Currency](#currency)


## Spelling Changes

The second yaml block is overriding briefs not defined in Plover.

-ce (nouns) -> -se (verbs)

following the SREUS: advice, SREUZ: advise pattern that is already in the dictionary

```yaml
PRABGS: practice # exists
PRABGZ: practise
HR-PBZ: license
HR-PBS: licence #  overwrites license
```

-or -> -our

```yaml
THOR: authorise
EPB/TKEFR: endeavour
EPB/TKEFRS: endeavours
TPAEUFR: favour
TPAUFR: favour
TPAEUFRT: favourite
HO*RPB: honour
HRAEUB: labour
HRAEURB: labour
```

-er -> -re

```yaml
KAL/PW*ER: calibre
KAL/PW-R: calibre
STR*: centre # keeping STR: center for programming
```

-ize -> -ise

```yaml
AOEUZ: {^ise}
THORZ: authorise
KREUT/SAOEUZ: criticise
EFPL/SAOEUFD: emphasised
ORG: organise
RAELGS: realisation
RAELZ: realise
RAEFLD: realised
THRAELZ: realise that
R*EZ: recognise
REZ: recognise
```

-zation -> -sation
```yaml
PHREUT/SAEUGS: politicisation
```

-ization -> -isation

```yaml
SA*EUGS: {^isation}
ORGS: organisation
```

```yaml
PHREUT/SA*EUGS: politicisation
```

-ling -> -lling
```yaml
PHO*ELD/-G: modelling
```


## Pronunciation Changes

```yaml
PWAOET/KWRA: beta
PWA/SEUL: basil
PWAEFL: basil # PWAFL: baffle
SHED/AOUL: schedule # shed/^ule. already exists under `SHED/KWRAOUL`, `SKED/AOUL`
TPHAT/TOE: tomato
TPHAT/TOES: tomatoes
```

## URLs

```yaml
PAOUPBG: {^.uk} # folded
P-P/AOUBG: {^.uk}
P-P/UBG: {^.uk}
KOUBG: {^.co.uk}
```

## Briefs

Briefs for words that are more common in British English than American.

```yaml
H*UR: hurry
SW*EUFP: sandwich
```

## Regional words

```yaml
ARS: arse
OE/PWER/SKWRAOEPB: aubergine
PWA*EUPL: BAME
PWAO*EB: BBC
PWAOEB: beeb
PWOPBLG: bodge
PWREBGS/EUT: Brexit
KHUF: chuff
KR*F: CV
KWRU: EU
KWROEUR/SREUGS: Eurovision
HAOFR: hoover # overwrites Hoover (use HAO*FR)
TPHOB/HREU: knobbly
-FRP: MP
TPH*S: NHS
PER/APL/PWHRAEURT: perambulator
PRAEPL: pram # PRAPL: program
SEFP: sesh
SOEF: sofa
TEL/HREU: telly
THREL: telly
AOUPB: uni
```

## Places

```yaml
PWEBGS/HREU: Bexley
PWREUBGS/STOPB: Brixton
PWREUBGS/TOPB: Brixton
SAEUPBS/PWRAOES: Sainsbury\'s
```

## Currency

```yaml
P*PBDZ: {*(£c)}
```

## Added by Plover

```yaml
TOPB: tonne
TOPBS: tonnes
SOERBL/AOEUZ: socialise
```

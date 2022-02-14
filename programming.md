# Programming

Requires:

- [plover\_markdown\_dictionary](https://github.com/antistic/plover_markdown_dictionary)

Other useful dictionaries:

- Find symbols at [symbols.py](./symbols.py), which is my fork of
  [Emily's Symbols](https://github.com/EPLHREU/emily-symbols).
- If you use vim, the attachment [fingerspelling dictionary](./fingerspelling.json)
  ([script](./scripts/fingerspelling.py)) may be useful.

Theory:

- File extensions are `P-P` followed by the letters in the extension, and are lowercase.
- Names have the lowercase variant (usually a command name) without a `*` and the brand name with a `*`. This is opposite to what's in the default Plover dictionary.

## Table of Contents

- - [General / Misc](#general--misc)
    - [Commands/Keys](#commandskeys)
    - [Words](#words)
  - [Command Line](#command-line)
  - [DevOps](#devops)
  - [Haskell](#haskell)
  - [HTML & CSS](#html--css)
  - [Git](#git)
  - [JavaScript, JSON, web dev](#javascript-json-web-dev)
  - [Markdown](#markdown)
  - [Lua](#lua)
  - [PHP](#php)
  - [Python](#python)
  - [SQL](#sql)
- [Vim](#vim)
  - [WordPress](#wordpress)
  - [Yaml](#yaml)

## General / Misc

### Commands/Keys

```yaml
KPA: {-|} # exists as {}{-|}, which inserts a space with prefix strokes (e.g. a^)
KPA*: {^}{-|} # exists
KA*EPL: {MODE:CAMEL} # as suggested in the wiki
STPH*BG: {MODE:LOWER}{MODE:SNAKE} # as suggested in the wiki
R*EFT: {MODE:RESET} # as suggested in the wiki
SK-P: "{#Escape}{MODE:RESET}" # eSKaPe, with reset. good for vim
S-P: {^ ^}{MODE:RESET} # exists without reset. good for special modes on a single word
P-P: {^.^}{>} # add lowercase to next word since I'm usually using this for domain names and file extensions
```

### Words

```yaml
APB/SEU: ansi
OEUP: api
OEUP/OEUP: API
AERG: arg # A*RG is argh
RAE: array # A/RAEU
AFBG: asc
PWAOL: bool # exists
PW-PBT: btn
PWOERT/TP*S: btrfs
PW*UF: buf
KRAO*EL: ceil
KHR*EU: cli
KHR*EU/KHR*EU: CLI
KPH-D: cmd
K-PLD: cmd
K-FG: config # exists as KAUPB/TP*EUG
KO*PBS: const
KRO*L: ctrl
TK*EFBG: desc
TK*EF/*EL: devel
TKEUFT: dist
KHOE: echo # overwrites Cho (use KHO or KHO*E)
EFPL: efm
"*EFPB": env
SRAOEURPB: environ
EFBG: esc
ETS: etc # overwrites "et cetera" (use EGTS)
TPAOEUL/PA*ET: filepath # using AE since you may still want TPAOEUL/PA*T: file path
TPA*UPBG: func # exists
TKPWAOE: gui
TKPWAO*E: GUI
HAO*EPTS: HTTPS
EUPBG: inc # overwrites Inc. (use AO*EPBG)
SPWEPBLG: integer
"*EUPBT": int # exists
SPW*: int # exists
HR-FP: lsp
PH*BG: mk
TPHAF: nav
TPHA*F: nav # overwrites 1/2 (use HA*F)
TPHAUPL: num # TPHUPL is taken by number
PA*RPL: param # PRA*PL
P-P/P-FD: {^}.pdf
P-FD: pdf
P*ERPL/HR*EUPBG: permalink # perm link
RA*E: re
R*EZ: res
RUPB/TAO*EUPL: runtime
STK-BG: sdk
S*EP: sep
S-RBG: src # exists
SHR*: ssl
ST*D: std # overwrites standard deviation (use STAO*EFD)
ST*R: str # STR: center, ST-R: sister. STR*: centre by my British dictionary, so ST*R is what's left
S-FG: svg
TA*EL: tel
T-FRP: tmp
TO/TKO*: todo
TUPL: tuple
P-P/T-GT: {^}{>}.txt
WEUD: uid
AO*ULT: util # AOULT: utility, AOU/TEUL: util
SR*EBG: vec
SR-S/KO*ED: VSCode
```

Things you might expect if using the above briefs

```yaml
K-FG/RAEUGS: configuration # probably better to use TKPWRAEUGS
KHOED: echoed # overwrites choad
```

## Command Line

- Prefixed with `{>}` for lowercase.
- When possible, tries to use `*` for consistency.
- Doesn't use left attach since you might use the commands somewhere other than the start (e.g. when piping)

```yaml
KR-D: {>}cd # KR*D: CD. Overwrites considered (use K-RD)
KPHOD: {>}chmod # exists (without {>})
KHOEPB: {>}chown # exists (wihout {>})
KR-P: {>}cp # exists. KR*P is used for fingerspelling
TKPWREP: {>}grep # exists (without {>})
HR*S: {>}ls # exists
PH-BG/TKEUR: {>}mkdir # exists (without {>})
PH*BGD: {>}mkdir # M*KDir
PH*F: {>}mv # exists as '{>}{^mv}'
PAS/W*D: {>}passwd
PW-D: {>}pwd # exists (without {>})
R*F: {>}rf # overwrites 'reticular formation'
R-PL/TKEUR: {>}rmdir
R*PLD: {>}rmdir # R*MDir. Overwrites {&.r}
R*PL: {>}rm # * for consistency
R-PL: {>}rm # overwrites 'rm'
SKR*P: {>}scp # * for consistency with most else
SKR-P: {>}scp # no * for consistency with cp
S*ED: {>}sed
P-P/SH: {^.sh}
SH*: {>}ssh # overwrites '{>}{&s}{&h}'
SOUD: {>}sudo # SAOU/TKAOU
SOUD/ETD: {>}sudoedit
SAOU/TKAOU/ETD: {>}sudoedit
```

```yaml
K-LT: {^ctl}
TKAEPL/O*PB: daemon
TKPHO*PB: daemon
HR*F: lf
HREUB/TPH*PT: libinput
R*G: rg
S*RB: zsh
```

## DevOps

```yaml
A*US/A*US: Amazon Web Services
ARPB: arn
A*US: aws
A*US/KHREU: aws-cli # A*US/KHR*EU: AWS CLI
KREUBGD: CI/CD
TKOERBG: docker
TKO*RBG: docker
TKPO*ES: docker-compose
TKOERBG/TPAOEUL: dockerfile
TKO*RBG/TPAOEUL: dockerfile
TKOT/TPAOEUL: dotfile
TKOT/TPAOEULS: dotfiles
TKOT/TPAOEULZ: dotfiles
EBGS/K-LT: eksctl
"*EF": env
H*EPL: helm # HEL/-PL
K*8S: k8s
KAO*UB: kube
KAOUB/K-LT: kubectl
K-8S: kubernetes
KAOUB/TPHET/AOES: kubernetes
KAOUB/TPHET/AOEZ: kubernetes
TPH*PBLGS: nginx # TPH-PBLGS: engines
```

## Haskell

```yaml
P-P/H-S: {^}.hs
HAFBG/EL: haskell # HAS/KEL
```

## HTML & CSS

```yaml
KR-SZ: css
KR*SZ: CSS
EPLS: {^em} # unit of measurement. EM/AEM/*EM/A*EM are all taken
P-P/H*PLT: {^}.html
H-PLT: html
EUPLG: img
P-BGS: {^px}
SKR-SZ: scss
SKR*SZ: SCSS
"*UL": ul
```

```yaml
EPL/ET: emmet
```

## Git

```yaml
TKPW-BGT: git checkout
TKPW*BGT: git checkout -b{^ ^}{MODE:SET_SPACE:-} # make a new branch, set to kebab case. Reset with R-R
TKPW-FP: git fetch # fetCH
TKPWEUT/HUB: github
TKPWUB: github
TKPWEUT/H*UB: GitHub
TKPW*UB: GitHub
P-P/TKPWEUT/EUG/TPHOR: .gitignore
TKPWEUT/HRAB: gitlab
TKPWHRAB: gitlab
TKPWEUT/HRA*B: GitLab
TKPWHRA*B: GitLab
TKPW-LG: git lg
TKPWEUT/HR-G: git lg # lg is a popular alias for a pretty git log
TKPW*L: git pull # TKPW-L: gallon
TKPW-RB: git push # puSH
TKPW*RB: git push -u origin HEAD # pushes a new branch
TKPW*TS: git status
PH*R: MR # PH-R: Mr., PHR: mister
P-R: PR
```

## JavaScript, JSON, web dev

```yaml
KHRO*G: console.log({^}
AOES/HREUPBT: eslint
TPAOEUR/PWA*EUS: firebase
TPAOEUR/STO*R: firestore
TPRAO*EFP: forEach
SKWR-S: js
SKWR-S/SKWR-S: JS
SKWR*FPB: JSON
SKWR-FPB: json # overwrites JSON
HRAR/SREL: laravel
HRA*R/SREL: Laravel
PH*PBD: mdn
TPHET/TPAOEU: netlify
TPH*ET/TPAOEU: Netlify
TPH-PL: npm # overwrites {&n-}
TPH-PL/TPH-PL: npm # overwrites {&n-}
TPH*UGT: nuxt
P-PL/2: pm2
P-PL/-67: pm2 # using keypad numbers dictionary
P-P/SRAO*U: {^}{>}.vue
SRAO*U: vue
SRAO*U/SRAO*U: Vue
SRAO*U/HREU/TKAEUD: vuelidate
SRAO*U/HREU/TKAEUT: vuelidate
SRAOUBGS: vuex
SROUBGS: vuex
```

## Markdown

Useful symbols to learn (all in emily symbols / [symbols.py](./symbols.py)):

- Open and closing *italics* `{*^}` `{^*}`
- Open and closing **bold** `{**^}` `{^**}`
- Open and closing `code` ``{`^}`` ``{^`}``
- Open and closing code blocks `{^```^}`
- Open quote `{^>}{-|}`
- Bullet points `{^-}{-|}`
- Various heading levels (1-4) `{^##}{-|}`. 5 and 6 are not supported in one stroke by the symbol dictionary, but you can easily do it in two.
- Horizontal rule `{^---^}`
- Various brackets

```yaml
KH-BGS: - [ ] # CHeckBoX: overwrites 'which cans' because of 'KH-BG: which can'
KH*BGS: - [X]
```

```yaml
HREFPB/TEU: eleventy
TPROPBT/PHA*ERT: frontmatter
TPROPBT/PHA*RT: frontmatter
SKWREBG/EUL: Jekyll
PHARBG/SKWROUPB: markdown # exists: mark + ^down
PHA*RBG/SKWROUPB: Markdown # exists: Mark + ^down
P-PLD: {^}{>}.md
P-P/PH-D: {^}{>}.md
TO*BG/TO*BG: Table of Contents
TO*BG: toc # table of contents
```

## Lua

```yaml
HRAOU/SKWRA: lua
HROEU: lua # trusty old OEU wildcard
```

## PHP

```yaml
ELS/EUF: elseif # ELS/TP: else if, ELS/TP* elsef (fingerspelling)
EPBD/EUF: endif
TPRAOEFP: foreach
```

```yaml
EUPBT/EL/TPEPBS: intelephense
SPWEL/TPEPBS: intelephense
PH-P: php
PH-P/PH-P: PHP # star version conflicts with fingerspelling
KP*/TKE/PWUG: xdebug
```

## Python

```yaml
TK-F: def # exists
TK-L: del
EL/TP: elif
KWAERGS: kwargs # like AERG: arg. KWARGS: kwargs exists
```

```yaml
PAO*EU: {>}py{^}
P-P/PAO*EU: {^}{>}.py
P-P/PAOEU: {^}{>}.py
P-P/PEU: {^}{>}.py
THO*PB: Python
THOPB: python # swapped python and Python
```

```yaml
PHAOEU/PAO*EU: mypy
PHEU/PAO*EU: mypy
PRAPLT/AOEUZ: parametrize
PRAPL/TRAOEUZ: parametrize
PA/RAPL/TRAOEUZ: parametrize # pytest.parametrize
KW-T: qt
```

## SQL

```yaml
P-P/SKW-L: .sql
```

# Vim

```yaml
AU/TKPWRAOUP: augroup
```

## WordPress

```yaml
WO*RP: WordPress
WORP: wordpress # overwrites WordPress (use WO*RP)
W-P: wp # overwrites WordPress (use WO*RP)
TKPWHEUPB: {^}wp/wp-admin # TKPHEUPB: admin, plus W
```

## Yaml

```yaml
P-P/KWRAFRL: {^}{>}.yaml
KWRAPL/-L: yaml
KWRAFRL: yaml # FR=M, like -FRP: -mp
P-P/KWR-FRL: {^}{>}.yml
```

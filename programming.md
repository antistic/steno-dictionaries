# Programming

Requires:
 - [plover-markdown-dictionary](https://github.com/antistic/plover-markdown-dictionary)

Other useful dictionaries:
 - Find symbols at [symbols.py](./symbols.py), which is my fork of [Emily's Symbols](https://github.com/EPLHREU/emily-symbols).
 - If you use vim, the attachment [fingerspelling dictionary](./fingerspelling.json) ([script](./scripts/fingerspelling.py)) may be useful.


Theory:
 - File extensions are `P-P` followed by the letters in the extension, and are lowercase.
 - Names have the lowercase variant (usually a command name) without a `*` and the brand name with a `*`. This is different to what's in the default Plover dictionary.

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
AERG: arg # A*RG is argh
RAE: array # A/RAEU
PWAOL: bool # exists
PWOERT/TP*S: btrfs
KPH-D: cmd
K-PLD: cmd
K-FG: config # exists as KAUPB/TP*EUG
KO*PBS: const
KRO*L: ctrl
KHOE: echo # overwrites Cho (use KHO or KHO*E)
SRAOEURPB: environ
TPAOEUL/PA*ET: filepath # using AE since you may still want TPAOEUL/PA*T: file path
TPA*UPBG: func # exists
HAO*EPTS: HTTPS
EUPBG: inc # overwrites Inc. (use AO*EPBG)
"*EUPBT": int # exists
SPW*: int # exists
TPHAF: nav
TPHA*F: nav # overwrites 1/2 (use HA*F)
TPHAUPL: num # TPHUPL is taken by number
P-P/P-FD: {^}.pdf
P-FD: pdf
RA*E: re
RUPB/TAO*EUPL: runtime
STK-BG: sdk
S-RBG: src # exists
SHR*: ssl
ST*D: std # overwrites standard deviation (use STAO*EFD)
ST*R: str # STR: center, ST-R: sister. STR*: centre by my British dictionary, so ST*R is what's left
S-FG: svg
T-FRP: tmp
TO/TKO*: todo
TUPL: tuple
P-P/T-GT: {^}{>}.txt
AO*ULT: util # AOULT: utility, AOU/TEUL: util
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
```

```yaml
K-LT: {^ctl}
TKPHO*PB: daemon
TKAEPL/O*PB: daemon
S*RB: zsh
HREUB/TPH*PT: libinput
```

## DevOps

```yaml
ARPB: arn
A*US: aws
A*US/A*US: AWS
A*US/A*US/A*US: Amazon Web Services
A*US/KHREU: aws-cli # A*US/KHR*EU: AWS CLI
KREUBGD: CI/CD
TKOFRBG: dockerfile
TKOT/TPAOEUL: dotfile
TKOT/TPAOEULS: dotfiles
TKOT/TPAOEULZ: dotfiles
EBGS/K-LT: eksctl
TPH*PBLGS: nginx # TPH-PBLGS: engines
"*EF": env
H*EPL: helm # HEL/-PL
K*8S: k8s
KAO*UB: kube
KAOUB/K-LT: kubectl
K-8S: kubernetes
KAOUB/TPHET/AOES: kubernetes
KAOUB/TPHET/AOEZ: kubernetes
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
```

## Git

```yaml
TKPWEUT/HR-G: git lg
TKPWHR-G: git lg
TKPW-RB: git push
P-P/TKPWEUT/EUG/TPHOR: .gitignore
P-R: PR
PH*R: MR # PH-R: Mr., PHR: mister
TKPWUB: github
TKPWEUT/HUB: github
TKPW*UB: GitHub
TKPWEUT/H*UB: GitHub
TKPWHRAB: gitlab
TKPWEUT/HRAB: gitlab
TKPWHRA*B: GitLab
TKPWEUT/HRA*B: GitLab
```

## JavaScript, JSON, web dev

```yaml
KHRO*G: console.log(
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
TPH-PL: npm # overwrites {&n-}
TPH-PL/TPH-PL: npm # overwrites {&n-}
TPHUBGT: Nuxt
TPHUGT: nuxt # overwrites nugget (use TPH*UGT)
TPH*UGT: nugget
P-PL/2: pm2
P-PL/34: pm2 # using keypad numbers dictionary (numbers.py)
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

- Open and closing _italics_ `{*^}` `{^*}`
- Open and closing **bold** `{**^}` `{^**}`
- Open and closing `code` `` {`^} `` `` {^`} ``
- Open and closing code blocks ` {^```^} `
- Open quote `{^>}{-|}`
- Bullet points `{^-}{-|}`
- Various heading levels (1-4) `{^##}{-|}`. 5 and 6 are not supported in one stroke by the symbol dictionary, but you can easily do it in two.
- Horizontal rule `{^---^}`
- Various brackets

```yaml
KH-BGS: - [ ] # CHeckBoX: overwrites 'which cans' because of 'KH-BG: which can'
```

```yaml
P-PLD: {^}{>}.md
P-P/PH-D: {^}{>}.md
PHARBG/SKWROUPB: markdown # exists: mark + ^down
PHA*RBG/SKWROUPB: Markdown # exists: Mark + ^down
```

## Lua

```yaml
HRAOU/SKWRA: lua # if you can think of a good one-stroke let me know
```

## PHP

```yaml
ELS/EUF: elseif # ELS/TP: else if, ELS/TP* elsef (fingerspelling)
EPBD/EUF: endif
TPRAOEFP: foreach
```

```yaml
PH-P: php
PH-P/PH-P: PHP # star version conflicts with fingerspelling
```

## Python

```yaml
EL/TP: elif
TK-F: def # exists
TK-L: del
KWAERGS: kwargs # like AERG: arg. KWARGS: kwargs exists
```

```yaml
P-P/PEU: {^}{>}.py
P-P/PAOEU: {^}{>}.py
P-P/PAO*EU: {^}{>}.py
PAO*EU: {>}py{^}
THOPB: python # swapped python and Python
THO*PB: Python
```

```yaml
PHEU/PAO*EU: mypy
PHAOEU/PAO*EU: mypy
PA/RAPL/TRAOEUZ: parametrize # pytest.parametrize
PRAPL/TRAOEUZ: parametrize
PRAPLT/AOEUZ: parametrize
KW-T: qt
```

## Yaml

```yaml
KWRAPL/-L: yaml
KWRAFRL: yaml # FR=M, like -FRP: -mp. Not technically Plover theory, but useful
P-P/KWR-FRL: {^}{>}.yml
P-P/KWRAFRL: {^}{>}.yaml
```

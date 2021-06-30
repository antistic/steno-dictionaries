# Programming

 - Requires [plover-markdown-dictionary](https://github.com/antistic/plover-markdown-dictionary) to use.
 - Find symbols at [symbols.py](./symbols.py), which is my fork of [Emily's Symbols](https://github.com/EPLHREU/emily-symbols).
 - If you use vim, the attachment [fingerspelling dictionary](./fingerspelling.json) ([script](./scripts/fingerspelling.py)) may be useful.

Theory:

 - File extensions are `P-P` followed by the letters in the extension, and are lowercase.
 - The names of languages have the lowercase variant (usually a command name) without a `*` and the brand name with a `*`. This is different to what's in the default Plover dictionary.

## General

Words

```yaml
AERG: arg # A*RG is argh
RAE: array # A/RAEU
APB/SEU: ansi
PWAOL: bool # exists
KO*PBS: const
K-FG: config # exists as KAUPB/TP*EUG
TPAOEUL/PA*ET: filepath
SPW*: int # exists
"*EUPBT": int # exists
TPHAUPL: num
S-RBG: src # exists
ST*R: str
T-FRP: tmp
TO/TKO*: todo
TUPL: tuple
AO*ULT: util # AOULT: utility, AOU/TEUL: util
```

Commands/Keys

```yaml
KPA: {-|} # exists as {}{-|}, which inserts a space with prefix strokes (e.g. a^)
KPA*: {^}{-|} # exists
KA*EPL: {MODE:CAMEL}  # as suggested in the wiki
STPH*BG: {MODE:LOWER}{MODE:SNAKE}   # as suggested in the wiki
R*EFT: {MODE:RESET}  # as suggested in the wiki
SK-P: "{#Escape}{MODE:RESET}" # eSKaPe, with reset. good for vim
S-P: {^ ^}{MODE:RESET}  # exists without reset. good for special modes on a single word
P-P: {^.^}{>} # add lowercase to next word since I'm usually using this for domain names and file extensions
```

## Command Line

 - Prefixed with `{>}` for lowercase.
 - When possible, tries to use `*` for consistency.
 - Doesn't use left attach since you might use the commands somewhere other than the start (e.g. when piping)

```yaml
(DELETED) K*D: {>}cd   # KR*D is 'CD', KR-D is 'considered'
KR-P: {>}cp  # exists. KR*P is used for fingerspelling
KPHOD: {>}chmod   # exists (without {>})
KHOEPB: {>}chown  # exists (wihout {>})
TKPWREP: {>}grep  # exists (without {>})
PH-BG/TKEUR: {>}mkdir # exists (without {>})
PH*BGD: {>}mkdir  # M*KDir
PH*F: {>}mv  # exists as '{>}{^mv}'
HR*S: {>}ls  # exists
PW-D: {>}pwd # exists (without {>})
R*F: {>}rf   # overwrites 'reticular formation'
R-PL: {>}rm  # overwrites 'rm'
R*PL: {>}rm  # * for consistency
R-PL/TKEUR: {>}rmdir
R*PLD: {>}rmdir  # R*MDir. Overwrites {&.r}
SKR-P: {>}scp # no * for consistency with cp
SKR*P: {>}scp # * for consistency with most else
S*ED: {>}sed
SH*: {>}ssh   # overwrites '{>}{&s}{&h}'
SOUD: sudo
P-P/SH: {^.sh}
P-P/SH*: {^.sh}
TKAEPL/O*PB: daemon
```

```yaml
K-LT: {^ctl}
S*RB: zsh
```

## DevOps

```yaml
KREUBGD: CI/CD
TKOFRBG: dockerfile
TKOT/TPAOEUL: dotfile
TKOT/TPAOEULS: dotfiles
TKOT/TPAOEULZ: dotfiles
"*EF": env
K-8S: kubernetes
H*EPL: helm # HEL/-PL
```

## HTML & CSS

```yaml
H-PLT: html
KR-SZ: css
KR*SZ: CSS
SKR-SZ: scss
SKR*SZ: SCSS
EPLS: {^em} # unit of measurement. EM/AEM/*EM/A*EM are all taken
```

## Git

```yaml
P-P/TKPWEUT/EUG/TPHOR: .gitignore
P-R: PR
TKPWUB: github
TKPWEUT/HUB: github
TKPW*UB: GitHub
TKPWEUT/H*UB: GitHub
TKPWHRAB: gitlab
TKPWEUT/HRAB: gitlab
TKPWHRA*B: GitLab
TKPWEUT/HRA*B: GitLab
```

## JavaScript & JSON


```yaml
TPH-PL: npm # the command. overwrites {&n-}
TPH*PL: NPM # the brand. overwrites New Mexico, which still exists under TPH*PL/TPH*PL and TPHU/PHEBGS/KOE
P-P/SKWR-FPB: {^}{>}.json
P-P/SKWR-S: {^}{>}.js
SKWR-FPB: json  # overwrites JSON
SKWR*FPB: JSON
P-PL/2: pm2
P-PL/#PH: pm2 # using keypad numbers dictionary (numbers.py)
HRAR/SREL: Laravel
SRAO*U: Vue
```

## Markdown

Useful symbols to learn:

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
KH-BGS: - [ ]  # CHeckBoX: currently mapped to 'which cans' because of 'KH-BG: which can'
```

```yaml
P-PLD: {^}{>}.md
P-P/PH-D: {^}{>}.md
PHARBG/SKWROUPB: markdown  # exists: mark + ^down
PHA*RBG/SKWROUPB: Markdown  # exists: Mark + ^down
```

## Python


```yaml
EL/TP: elif
TK-F: def  # exists
TK-L: del
KWAERGS: kwargs # like AERG: arg. KWARGS: kwargs exists
```


```yaml
P-P/PEU: {^}{>}.py
P-P/PAOEU: {^}{>}.py
P-P/PAO*EU: {^}{>}.py
PAO*EU: {>}py{^}
THOPB: python  # swapped python and Python
THO*PB: Python
```

```yaml
PHEU/PAO*EU: mypy
PA/RAPL/TRAOEUZ: parametrize # pytest.parametrize
PRAPL/TRAOEUZ: parametrize
KW-T: qt
```

## Yaml

```yaml
KWRAPL/-L: yaml
KWRAFRL: yaml # FR=M, like -FRP: -mp. Not technically Plover theory, but useful
```

## Misc

```yaml
SHR*: ssl
SR-S/KO*ED: VSCode
PWOERT/TP*S: btrfs
```

## Added by Plover

```yaml
PHAO*EU/PAO*EU: py
KR-D: {>}cd
SRAOEURPB: environ
```

# AI-Toolbox

Dépôt de skills IA partagés pour l'équipe. Compatible avec tous les agents supportés par l'écosystème [Agent Skills](https://agentskills.io/) (GitHub Copilot, Claude Code, Cursor, Codex, etc.).

## Installation rapide

Depuis la Forgejo interne :

```bash
npx skills add https://git.kopo/Kopo/tool-ai.git --all
```

Ou depuis le miroir GitHub :

```bash
npx skills add https://github.com/KopoCorp/AI-Toolbox.git --all
```

## Skills disponibles

| Skill | Source | Description |
|---|---|---|
| `kopo-smart-ai` | Interne | **Routeur** : aide l'agent à choisir le bon skill de ce dépôt selon la situation (aucune installation externe requise) |
| `kopo-website-skill` | Interne | Crée des sites web conformes à la charte Kopo V1.4 |
| `humanizer` | [blader/humanizer](https://github.com/blader/humanizer) | Supprime les signes d'écriture IA pour un texte plus naturel |
| `superpowers/` | [obra/superpowers](https://github.com/obra/superpowers) | **Suite de 14 skills** (pas un skill unique) : brainstorming, TDD, debugging systématique, revue de code, plans en micro-tâches, etc. Invocation qualifiée `superpowers:<sous-skill>`. Voir le détail dans le dossier. |
| `karpathy-guidelines` | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Garde-fous anti-pièges LLM (Karpathy) : pas de sur-ingénierie, changements chirurgicaux, clarifier avant de coder |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills) | L'agent challenge le brief avec des questions avant d'implémenter |
| `find-skills` | [vercel-labs/skills](https://github.com/vercel-labs/skills) | Permet à l'agent de découvrir et installer d'autres skills tout seul |
| `agent-browser` | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Donne un vrai navigateur à l'agent pour vérifier visuellement ce qu'il produit (nécessite `npm i -g agent-browser`) |

Les noms de dossier correspondent exactement au champ `name:` du `SKILL.md` de chacun — c'est ce nom-là (pas le nom du dépôt d'origine) que Claude Code utilise pour invoquer un skill, d'où l'importance de ne pas les rebaptiser arbitrairement.

`superpowers` est un dossier à part : c'est la seule suite multi-skills du dépôt (14 SKILL.md sous `superpowers/skills/*/`), avec ses propres hooks d'auto-déclenchement, invoquée par sous-skill (`superpowers:brainstorming`, `superpowers:test-driven-development`, ...). Les six autres lignes du tableau sont chacune un skill autonome avec un seul `SKILL.md` à la racine de son dossier. En cas de doute sur quel skill invoquer, `kopo-smart-ai` fait office de table de routage.

## Cloner le dépôt (pour les collaborateurs)

Tous les skills, y compris ceux d'origine externe, sont copiés directement dans le dépôt (pas de git submodules). Un clone classique suffit :

```bash
git clone https://git.kopo/Kopo/tool-ai.git
```

## Mettre à jour un skill externe

Ces skills sont vendored (copie figée d'une version en amont), pas liés en live. Pour mettre à jour `<skill>` :

```bash
git clone --depth 1 <url-du-repo-amont> /tmp/<skill>
rm -rf skills/<skill>
cp -r /tmp/<skill> skills/<skill>
rm -rf skills/<skill>/.git
git add skills/<skill>
git commit -m "chore: update <skill>"
```

## Structure

```
AI-Toolbox/
├── skills/
│   ├── kopo-smart-ai/            ← skill interne (routeur des skills ci-dessous)
│   ├── kopo-website-skill/       ← skill interne
│   ├── humanizer/                ← vendored (blader/humanizer)
│   ├── superpowers/              ← vendored (obra/superpowers) — suite de 14 skills
│   ├── karpathy-guidelines/      ← vendored (multica-ai/andrej-karpathy-skills)
│   ├── grill-me/                 ← vendored (mattpocock/skills)
│   ├── find-skills/              ← vendored (vercel-labs/skills)
│   └── agent-browser/            ← vendored (vercel-labs/agent-browser)
└── README.md
```

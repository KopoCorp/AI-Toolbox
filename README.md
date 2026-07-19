# AI-Toolbox

Dépôt de skills IA partagés pour l'équipe. Compatible avec tous les agents supportés par l'écosystème [Agent Skills](https://agentskills.io/) (GitHub Copilot, Claude Code, Cursor, Codex, etc.).

## Installation rapide

Depuis la Forgejo interne :

```bash
npx skills add https://git.kopo/Kopo/AI-Toolbox.git
```

Ou depuis le miroir GitHub :

```bash
npx skills add https://github.com/KopoCorp/AI-Toolbox.git
```

## Skills disponibles

| Skill | Source | Description |
|---|---|---|
| `kopo-website-skill` | Interne | Crée des sites web conformes à la charte Kopo V1.4 |
| `humanizer` | [blader/humanizer](https://github.com/blader/humanizer) | Supprime les signes d'écriture IA pour un texte plus naturel |
| `dev-methodology` | [obra/superpowers](https://github.com/obra/superpowers) | Méthodologie de dev complète : brainstorm avant le code, plans en micro-tâches, TDD |
| `llm-coding-guidelines` | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Garde-fous anti-pièges LLM (Karpathy) : pas de sur-ingénierie, changements chirurgicaux, clarifier avant de coder |
| `clarify-before-coding` | [mattpocock/skills](https://github.com/mattpocock/skills) | L'agent challenge le brief avec des questions (grill-me) avant d'implémenter |
| `find-skills` | [vercel-labs/skills](https://github.com/vercel-labs/skills) | Permet à l'agent de découvrir et installer d'autres skills tout seul |
| `agent-browser` | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Donne un vrai navigateur à l'agent pour vérifier visuellement ce qu'il produit |

## Cloner le dépôt (pour les collaborateurs)

Les skills externes sont liés via git submodules. Pour tout récupérer :

```bash
git clone --recursive https://git.kopo/Kopo/AI-Toolbox.git
```

Si le dépôt est déjà cloné sans `--recursive` :

```bash
git submodule update --init --recursive
```

## Structure

```
AI-Toolbox/
├── skills/
│   ├── kopo-website-skill/       ← skill interne
│   ├── humanizer/                ← submodule (blader/humanizer)
│   ├── dev-methodology/          ← submodule (obra/superpowers)
│   ├── llm-coding-guidelines/    ← submodule (multica-ai/andrej-karpathy-skills)
│   ├── clarify-before-coding/    ← submodule (mattpocock/skills)
│   ├── find-skills/              ← submodule (vercel-labs/skills)
│   └── agent-browser/            ← submodule (vercel-labs/agent-browser)
└── README.md
```

# AI-Toolbox

Dépôt de skills IA partagés pour l'équipe. Compatible avec tous les agents supportés par l'écosystème [Agent Skills](https://agentskills.io/) (GitHub Copilot, Claude Code, Cursor, Codex, etc.).

## Installation rapide

```bash
npx skills add https://git.kopo/Kopo/AI-Toolbox.git
```

## Skills disponibles

| Skill | Source | Description |
|---|---|---|
| `kopo-website-skill` | Interne | Crée des sites web conformes à la charte Kopo V1.4 |
| `humanizer` | [blader/humanizer](https://github.com/blader/humanizer) | Supprime les signes d'écriture IA pour un texte plus naturel |

## Cloner le dépôt (pour les collaborateurs)

Les skills externes sont liés via git submodules. Pour tout récupérer :

```bash
git clone --recursive https://git.kopo/Kopo/AI-Toolbox.git
```

Si le dépôt est déjà cloné sans `--recursive` :

```bash
git submodule update --init --recursive
```

## Mettre à jour les skills externes

```bash
git submodule update --remote
git add .
git commit -m "update: skills externes"
```

## Ajouter un nouveau skill externe

```bash
git submodule add https://github.com/<auteur>/<skill>.git skills/<skill>
git commit -m "feat: ajout skill <skill>"
```

## Structure

```
AI-Toolbox/
├── skills/
│   ├── kopo-website-skill/   ← skill interne (commité)
│   └── humanizer/            ← git submodule
└── README.md
```

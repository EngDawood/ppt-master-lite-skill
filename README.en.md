# ppt-master-lite-skill

A lite copy of the [`ppt-master`](https://github.com/hugohe3/ppt-master/tree/main/skills/ppt-master) skill by Hugo He (MIT). Only `skills/ppt-master` was taken from upstream, version 6.10.0.

## What was removed

| Removed | Size | Effect |
|---|---|---|
| `templates/icons/` (5 icon libraries, 12,027 SVG) | 49 MB | No bundled icons. Use your own SVGs under `<project>/icons/<lib>/` or skip icons. |
| `templates/sounds/` (CC0 sound effects) | 12 MB | No bundled sound effects. `sound_sync.py` has nothing to copy from. |

Total goes from 79 MB to about 19 MB. Everything else is untouched: `SKILL.md`, `workflows/`, `references/`, `scripts/`, brand, deck, layout and chart templates, `LICENSE`, `SPONSORS*.md`. The upstream `attribution_guard.py` integrity check passes.

## Install

As a plugin, add this repo as a marketplace source or clone it, then point Claude at it. As a plain skill, copy `skills/ppt-master` into your skills folder (`~/.claude/skills/ppt-master`).

Python dependencies: `pip install -r skills/ppt-master/requirements.txt`.

## Updating from upstream

Re-run a sparse checkout of `skills/ppt-master`, then delete `templates/icons` and `templates/sounds`. Do not edit `SKILL.md`, `LICENSE` or `SPONSORS*.md`, because the integrity guard checks them.

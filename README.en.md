# ppt-master-lite-skill

A lite copy of the [`ppt-master`](https://github.com/hugohe3/ppt-master/tree/main/skills/ppt-master) skill by Hugo He (MIT). Only `skills/ppt-master` was taken from upstream, version 6.10.0.

## What was removed

| Removed | Size | Effect |
|---|---|---|
| `templates/icons/` (5 icon libraries, 12,027 SVG) | 49 MB | No bundled icons. Use your own SVGs under `<project>/icons/<lib>/` or skip icons. |
| `templates/sounds/` (CC0 sound effects) | 12 MB | No bundled sound effects. `sound_sync.py` has nothing to copy from. |

Language trim (Arabic and English only):

| Removed | Effect |
|---|---|
| Chinese decks (`中国电信`, `中汽研`) and Chinese brands (`中国电信`, `中国电建`, `中汽研`) | `templates/decks` is empty. Brand identities in English (e.g. Tencent, Huawei) are kept. |
| Chinese social layouts (`xiaohongshu_post`, `moments_square`, `story_vertical`) | The layouts index lists the remaining layouts only. Canvas sizes such as `xiaohongshu` stay available. |
| Chinese-only image backends: Qwen, Zhipu, Volcengine, Tencent, ModelScope, SiliconFlow, MiniMax | Remaining: OpenAI, Gemini, BFL, Ideogram, Stability, fal, OpenRouter, Replicate. |
| Chinese-only TTS providers: Qwen, CosyVoice, MiniMax | Remaining: edge-tts, ElevenLabs, OpenAI. The curated edge voice list is now Arabic (ar-SA, ar-EG) and English (en-US, en-GB). |
| Chinese text in `.env.example` and the audio workflow templates | Replaced with English. |
| Tests that depended on removed assets | 14 tests removed. The rest of the suite passes, except one test that also fails upstream (`test_source_resource_links`). |

Not trimmed: the confirm UI (`scripts/confirm_ui`) still carries Chinese, Traditional Chinese and Japanese UI strings alongside English, and has no Arabic strings. `SPONSORS_CN.md` stays because the integrity guard requires it.

Total goes from 79 MB to about 18 MB. Everything else is untouched: `SKILL.md`, `workflows/`, `references/`, `scripts/`, brand, deck, layout and chart templates, `LICENSE`, `SPONSORS*.md`. The upstream `attribution_guard.py` integrity check passes.

## Install

As a plugin, add this repo as a marketplace source or clone it, then point Claude at it. As a plain skill, copy `skills/ppt-master` into your skills folder (`~/.claude/skills/ppt-master`).

Python dependencies: `pip install -r skills/ppt-master/requirements.txt`.

## Updating from upstream

Re-run a sparse checkout of `skills/ppt-master`, then delete `templates/icons` and `templates/sounds`. Do not edit `SKILL.md`, `LICENSE` or `SPONSORS*.md`, because the integrity guard checks them.

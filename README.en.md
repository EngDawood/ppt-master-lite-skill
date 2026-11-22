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

Not trimmed: the confirm UI (`scripts/confirm_ui`) still carries Chinese, Traditional Chinese and Japanese UI strings alongside English, and has no Arabic strings.

Sponsor pages removed: `SPONSORS.md` and `SPONSORS_CN.md` are deleted, together with the `sponsors` field in `SKILL.md`, the sponsor note in its rules, and the matching prompt-audit entries. To keep the skill runnable, `scripts/attribution_guard.py` no longer requires those files or that field. `LICENSE` (MIT, Copyright (c) 2025-2026 Hugo He) and the copyright, license and repository fields in `SKILL.md` are unchanged and still checked.

Feature trim: removed narration audio, TTS backends, video and subtitle scripts, AI image generation (`image_gen.py` and its provider backends) and the Gemini watermark remover. Web image search, speaker notes and animations stay. Size is now about 13 MB.

Install as a marketplace: `/plugin marketplace add EngDawood/ppt-master-lite-skill`, then `/plugin install ppt-master-lite@ppt-master-lite`.

Standalone cleanup: removed everything that only served the upstream repository or website: the test suite, `prompt_audit.py` and its manifest, `update_repo.py`, `generate_examples_index.py`, the maintenance smoke docs, the scripts index README and the image-comparison gallery. Links to removed files were turned into plain text. `SKILL.md` has a short "Lite Build" section telling the agent to pick "No base icons" and skip sounds. A real run (project init, SVG check, finalize, PPTX export) was verified.

Total goes from 79 MB to about 18 MB. Everything else is untouched: `workflows/`, `references/`, the remaining scripts and templates.

## Install

As a plugin, add this repo as a marketplace source or clone it, then point Claude at it. As a plain skill, copy `skills/ppt-master` into your skills folder (`~/.claude/skills/ppt-master`).

Python dependencies: `pip install -r skills/ppt-master/requirements.txt`.

## Updating from upstream

Re-run a sparse checkout of `skills/ppt-master`, then delete `templates/icons` and `templates/sounds`. Keep `LICENSE` and the copyright, license and repository fields in `SKILL.md` as they are, because the integrity guard checks them. Re-apply the guard change above if you pull a newer upstream `attribution_guard.py`.

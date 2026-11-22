# ppt-master-lite-skill

نسخة خفيفة من مهارة [`ppt-master`](https://github.com/hugohe3/ppt-master/tree/main/skills/ppt-master) للمطوّر Hugo He (رخصة MIT). أُخذ من المستودع الأصلي مجلد `skills/ppt-master` فقط، الإصدار 6.10.0.

## ما الذي حُذف

| المحذوف | الحجم | الأثر |
|---|---|---|
| `templates/icons/` (خمس مكتبات، 12,027 أيقونة SVG) | 49 ميجابايت | لا توجد أيقونات مضمّنة. استخدم ملفات SVG الخاصة بك داخل `<project>/icons/<lib>/` أو تجاهل الأيقونات. |
| `templates/sounds/` (مؤثرات صوتية CC0) | 12 ميجابايت | لا توجد مؤثرات صوتية مضمّنة. |

ينخفض الحجم من 79 إلى نحو 19 ميجابايت. بقية المحتوى كما هو: `SKILL.md` و`workflows` و`references` و`scripts` وقوالب العلامات والعروض والتخطيطات والمخططات، مع `LICENSE` وملفات `SPONSORS`. وفحص السلامة `attribution_guard.py` الأصلي ينجح.

## التثبيت

كإضافة: أضف هذا المستودع كمصدر أو انسخه. كمهارة مفردة: انسخ `skills/ppt-master` إلى مجلد المهارات (`~/.claude/skills/ppt-master`).

المتطلبات: `pip install -r skills/ppt-master/requirements.txt`.

## التحديث من المصدر

اسحب `skills/ppt-master` من جديد بـ sparse checkout ثم احذف `templates/icons` و`templates/sounds`. لا تعدّل `SKILL.md` ولا `LICENSE` ولا `SPONSORS*.md` لأن فحص السلامة يتحقق منها.

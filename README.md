# ppt-master-lite-skill

نسخة خفيفة من مهارة [`ppt-master`](https://github.com/hugohe3/ppt-master/tree/main/skills/ppt-master) للمطوّر Hugo He (رخصة MIT). أُخذ من المستودع الأصلي مجلد `skills/ppt-master` فقط، الإصدار 6.10.0.

## ما الذي حُذف

| المحذوف | الحجم | الأثر |
|---|---|---|
| `templates/icons/` (خمس مكتبات، 12,027 أيقونة SVG) | 49 ميجابايت | لا توجد أيقونات مضمّنة. استخدم ملفات SVG الخاصة بك داخل `<project>/icons/<lib>/` أو تجاهل الأيقونات. |
| `templates/sounds/` (مؤثرات صوتية CC0) | 12 ميجابايت | لا توجد مؤثرات صوتية مضمّنة. |

تقليص اللغات (العربية والإنجليزية فقط):

| المحذوف | الأثر |
|---|---|
| عروض صينية (`中国电信`، `中汽研`) وعلامات تجارية صينية (`中国电信`، `中国电建`، `中汽研`) | مجلد `templates/decks` فارغ. تبقى هويات العلامات بالإنجليزية (مثل Tencent وHuawei). |
| تخطيطات التواصل الصينية (`xiaohongshu_post` و`moments_square` و`story_vertical`) | يعرض الفهرس بقية التخطيطات فقط. تبقى مقاسات اللوحة مثل `xiaohongshu`. |
| مزوّدو الصور الصينيون فقط: Qwen وZhipu وVolcengine وTencent وModelScope وSiliconFlow وMiniMax | المتبقي: OpenAI وGemini وBFL وIdeogram وStability وfal وOpenRouter وReplicate. |
| مزوّدو الصوت الصينيون فقط: Qwen وCosyVoice وMiniMax | المتبقي: edge-tts وElevenLabs وOpenAI. وقائمة أصوات edge صارت عربية (ar-SA، ar-EG) وإنجليزية (en-US، en-GB). |
| النصوص الصينية في `.env.example` وقوالب سير العمل الصوتي | استُبدلت بالإنجليزية. |
| اختبارات تعتمد على ما حُذف | حُذف 14 اختبارًا. بقية الاختبارات تنجح عدا اختبار واحد يفشل في المصدر الأصلي أيضًا (`test_source_resource_links`). |

لم يُقلَّص: واجهة التأكيد (`scripts/confirm_ui`) ما زالت تحوي نصوصًا بالصينية والصينية التقليدية واليابانية مع الإنجليزية، ولا تحوي نصوصًا عربية. ويبقى `SPONSORS_CN.md` لأن فحص السلامة يشترطه.

حُذفت صفحات الرعاة: `SPONSORS.md` و`SPONSORS_CN.md` مع حقل `sponsors` في `SKILL.md` وملاحظة الرعاة في قواعده وما يقابلها في بيان تدقيق الموجّهات. ولكي تبقى المهارة قابلة للتشغيل لم يعد `scripts/attribution_guard.py` يشترط تلك الملفات ولا ذلك الحقل. يبقى `LICENSE` (MIT، حقوق Hugo He 2025-2026) وحقول الحقوق والرخصة والمستودع في `SKILL.md` دون تغيير، ولا يزال الفحص يتحقق منها.

تنظيف للاستقلالية: حُذف كل ما يخدم المستودع الأصلي أو موقعه فقط: مجموعة الاختبارات و`prompt_audit.py` وبيانه و`update_repo.py` و`generate_examples_index.py` ووثائق الفحوصات الصيانية وفهرس السكربتات ومعرض مقارنة الصور. حُوّلت الروابط إلى الملفات المحذوفة إلى نص عادي. وأُضيف في `SKILL.md` قسم قصير «Lite Build» يوجّه الوكيل لاختيار «بلا أيقونات» وتخطي الأصوات. وجُرّب تشغيل فعلي (إنشاء مشروع، فحص SVG، الإنهاء، تصدير PPTX).

ينخفض الحجم من 79 إلى نحو 18 ميجابايت. بقية المحتوى كما هو: `workflows` و`references` وبقية السكربتات والقوالب.

## التثبيت

كإضافة: أضف هذا المستودع كمصدر أو انسخه. كمهارة مفردة: انسخ `skills/ppt-master` إلى مجلد المهارات (`~/.claude/skills/ppt-master`).

المتطلبات: `pip install -r skills/ppt-master/requirements.txt`.

## التحديث من المصدر

اسحب `skills/ppt-master` من جديد بـ sparse checkout ثم احذف `templates/icons` و`templates/sounds`. أبقِ `LICENSE` وحقول الحقوق والرخصة والمستودع في `SKILL.md` كما هي لأن فحص السلامة يتحقق منها. وأعد تطبيق تعديل الفحص أعلاه إن سحبت نسخة أحدث من `attribution_guard.py`.

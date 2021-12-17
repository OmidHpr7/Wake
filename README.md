# Wake
Wake: Context-Sensitive Automatic Keyword Extraction Using Word2vec

# Abstract
<div dir="rtl">
 استخراج خودکار کلمات کلیدی متون کوتاه فارسی با استفاده از word2vec 

با رشد روز افزون اسناد و متون الکترونیکی به زبان فارسی، به کارگیری روش­هایی سریع و ارزان برای دسترسی بـه متـون مورد نظر از میان مجموعه وسیع این مستندات، اهمیت بیشتری می­یابد. برای رسیدن به این هدف، استخراج کلمات کلیدی که بیانگر مضمون اصلی متن باشند، روشی بسیار مؤثر است. تعداد تکرار یک کلمه در متن نمی­تواند نشان­دهنده­ اهمیت یک کلمه و کلیدی بودن آن باشد. همچنین در اکثر روش­های استخراج کلمات کلیدی مفهوم و معنای متن نادیده گرفته می­شوند. از طرفی دیگر بدون ساختار بودن متون جدید در اخبار و اسناد الکترونیکی، استخراج این کلمات را مشکل می­سازد. در این مقاله روشی بدون نظارت و خودکار برای استخراج این کلمات در زبان فارسی که دارای ساختار مناسبی نمی­باشد، پیشنهاد شده است که نه تنها احتمال رخ دادن کلمه در متن و تعداد تکرار آن را در نظر می­گیرد، بلکه با آموزش مدل word2vec روی متن، مفهوم و معنای متن را نیز درک می­کند. در روش پیشنهادی که روشی ترکیبی از دو مدل آماری و یادگیری ماشین می­باشد، پس از آموزش word2vec روی متن، کلماتی که با سایر کلمات دارای فاصله­ کمی بوده استخراج شده و سپس با استفاده از هم­رخدادی و فرکانس رابطه­ای آماری برای محاسبه امتیاز پیشنهاد شده است. درنهایت با استفاده از حدآستانه کلمات با امتیاز بالاتر به‌عنوان کلمه کلیدی در نظر گرفته می­شوند. ارزیابی­­ها بیانگر کارایی روش با معیار F برابر 53.92% و با 11% افزایش نسبت به دیگر روش‌های استخراج کلمات کلیدی می­باشد.
</div>

# Run
This project requires a data set as the context and target text (which is short text: between 500 and 1000 tokens).

In the code the name of the Context text is cntText and the name of target text is shortTxt. The main part of the program consists of two lines of code:

wake = Wake.wake(cntTxt , use_PreTrain_Model, word2vec_param, model_add)
key = wake.keyword_EXT(shortTxt,numKey)

word2vec_param is a tuple contains parameters for traning Word2vec: (window_size, min_count)
use_PreTrain_Model is a binary variable that indicates whether the pre-trained model is being used: if use_PreTrain_Model=1 -> using pretrain Model
model_add is the address of pretrain model that can be empty

# Example
In this project, text keywords are automatically extracted based on its context. For example for the following input text:
<div dir="rtl">
وزرای امور خارجه آمریکا و عربستان در پایان سفر مایک پامپئو به ریاض در کنفرانسی مطبوعاتی تاکید کردند که محور گفت وگوهایشان ایران و `` مقابله با سیاست های ایران در منطقه '' بوده است  .  به گزارش ایسنا ،  به نقل از شبکه اسکای نیوز عربی ،  مایک پامپئو ،  وزیر خارجه جدید آمریکا در این کنفرانس مطبوعاتی گفت : ما شراکت ویژه ای با عربستان داریم که این شراکت و همکاری در حال گسترش است  .  دیدارهای بسیار خوبی با همتای عربستانی خود و نیز پادشاه و دیگر مسئولان این کشور داشتم  .  رئیس جمهور ترامپ بسیار خوشحال می شود میزبان پادشاه عربستان و مسئولان اقتصادی این کشور در کاخ سفید باشد  .  وزیر امور خارجه آمریکا ادامه داد : امنیت عربستان یک اولویت اصلی برای ایالات متحده است و ما با عربستان کار می کنیم تا امنیت در این کشور ارتقا یابد  .  پامپئو در بخش دیگری از سخنانش به مساله ایران پرداخت و مدعی شد : ایران باعث ایجاد ناامنی و بی ثباتی در منطقه و بزرگترین حامی تروریسم در جهان است  .  این کشور با شبه نظامیان وابسته به خود در سوریه ،  عراق و یمن و نیز با حملات سایبری به ایجاد ناامنی دست می زند  .  باید بگویم برخلاف دولت قبلی ایالات متحده ما دست بسته نمی نشینیم  .  اطمینان می دهم ایران هیچگاه به سلاح اتمی دست نخواهد یافت  .  او ادامه داد : درباره توافق هسته ای با ایران نیز باید بگویم رفتار ایران بعد از این توافق بدتر شده است  .  همانگونه که رئیس جمهور ترامپ گفته است این توافق باید اصلاح شود و اگر اصلاح نشود و یا قابل اصلاح نباشد ما از آن خارج می شویم  .  پامپئو ادامه داد : باید جلوی اقدامات ایران از جمله کمک به حوثی ها گرفته شود  .  حوثی ها با پرتاب موشک و نیز به خطر انداختن امنیت دریانوردی ،  عربستان و امنیت منطقه را تهدید می کنند  .  ما به عربستان در مقابله با این تهدیدات کمک خواهیم کرد  .  همزمان نیز مذاکرات با نماینده سازمان ملل در یمن را پی می گیریم تا اوضاع در یمن که باعث ظهور و رشد القاعده شده ،   وخیم تر نشود  .  خطر علیه منطقه یقینا تهدید علیه ایالات متحده است  .  وزیر امور خارجه آمریکا به سفر ترامپ به عربستان نیز اشاره کرد و گفت : سفر ترامپ به منطقه یک سفر تاریخی بود که در آن یک سازمان مبارزه با تروریسم تشکیل شد  .  ما متعهد به پیگیری اقداماتمان در این راستا هستیم البته خاورمیانه و شرکایمان نباید منتظر آمریکا بمانند و اطمینان داریم که عربستان در مبارزه با تروریسم پیش قراول دیگر کشورها خواهد بود  .  مایک پامپئو در پایان سخنان خود با ستایش از اقدامات اصلاحی ولیعهد عربستان ،  به چشم انداز 2030 این کشور اشاره کرد و گفت که ایالات متحده آمریکا حامی برنامه های محمد بن سلمان ،  ولیعهد عربستان است و اصلاحات ایجاد شده در این کشور به ویژه در زمینه حقوق زنان را ستایش می کند  .  عادل الجبیر ،  وزیر امور خارجه عربستان نیز به عنوان میزبان همتای آمریکایی خود در آغاز این کنفرانس مطبوعاتی گفت که با پامپئو توافق کرده تا مانع `` خواسته های روزافزون ایران در منطقه '' شود  .  وی گفت : دو کشور بر سر مبارزه با `` اقدامات بی ثبات کننده ایران '' در منطقه توافق دارند  .  ما از سیاست های آمریکا در قبال ایران به طور کامل حمایت می کنیم که از جمله آن سیاست های ایالات متحده در قبال برنامه هسته ای ایران است  . 
</div>

The 10 keywords extracted by the model are:

('ایران', 4.05292034373375)

('عربستان', 4.193905604785485)

('کشور', 4.7680901504699245)

('آمریکا', 4.941453550088568)

('منطقه', 4.949306749139798)

('ایالات', 5.365563238340798)

('متحده', 5.444792335101005)

('توافق', 5.479569006927752)

('خارجه', 5.616200457615028)

('ترامپ', 5.829934633246103)

### Note
In this model, lower score means higher priority.

# Reference:
[Implemented article](https://journals.ihu.ac.ir/article_204763.html)

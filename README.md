1. قم بزيارة https://render.com وسجّل دخولك.
2. اضغط New → Web Service.
3. اختر Upload ZIP أو Deploy manually.
4. ارفع ملف ZIP الذي يحتوي على app.py وrequirements.txt.
5. ادخل:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
   - Instance Type: Free
6. بعد النشر ستظهر لك رابط HTTPS ثابت (مثال: https://mybot.onrender.com).
7. الآن اربطه بصفحتك في فيسبوك:
   - Facebook Developer → تطبيقك → Messenger → Settings.
   - Webhook URL: https://<your-render-url>/
   - VERIFY_TOKEN: myfbverify123
   - اختر الحقول fields: messages, messaging_postbacks, message_deliveries.
   - اضغط Verify and Save.
8. اربط الصفحة (Page) بالتطبيق وخذ Page Access Token (اللي استخدمناه في app.py).
9. اختبر البوت عبر إرسال رسالة من صفحتك على فيسبوك.
   - سيلقي الرد Echo: نفس الصورة أو النص اللي بعته.

# إعداد التعديل الشامل (مرة واحدة فقط)

التعديلات تُحفظ في Firebase Firestore (مجاني) ويقرأها كل زوار الموقع.

1. افتح https://console.firebase.google.com ← **Add project** (مثلاً `rafad-site`).
2. **Build ← Authentication ← Get started ← Email/Password ← Enable.**
   ثم تبويب **Users ← Add user**: بريدك وكلمة مرور قوية (هذا حساب المدير).
3. **Build ← Firestore Database ← Create database** (Production mode).
   ثم تبويب **Rules** والصق (غيّر البريد لبريد المدير) ثم **Publish**:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{db}/documents {
    match /site/content {
      allow read: if true;
      allow write: if request.auth != null
        && request.auth.token.email == "ADMIN@EMAIL.COM";
    }
  }
}
```
4. **Project settings (⚙) ← General ← Your apps ← Web (</>)** سجّل تطبيقًا وانسخ `apiKey` و `projectId`.
5. افتح `firebase-config.js` وضعهما.
6. ارفع كل الملفات (index.html, admin.html, site-content.js, firebase-config.js, …) إلى استضافتك.

## الدخول للوحة الإدارة
- اضغط **5 مرات سريعة** على شعار مدماك أسفل الصفحة، أو افتح `/admin.html` مباشرة (غير مرتبطة بأي رابط وعليها noindex).
- سجّل الدخول ← عدّل (الفريق / النصوص / الأرقام) ← **حفظ للموقع كامل**.

ملاحظة: الإدارة المخفية للراحة فقط؛ الأمان الفعلي من قواعد Firestore وحساب المدير.

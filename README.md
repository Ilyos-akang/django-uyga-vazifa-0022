# django-uyga-vazifa-0022
django-uyga-vazifa-0022 test
🎯 Vazifa nomi: “Mahsulotlar katalogi” mini-loyihasi

⸻
Githubda django-uyga-vazifa-0022 nomli repository yarating vs codega clone qiling va venv yaratib active qilib sozlang kegin.

1️⃣ Django app yaratish
 • Mavjud Django project ichida products nomli app yarating:

python manage.py startapp products

 • Appni settings.py dagi INSTALLED_APPS ga qo‘shing.

⸻

2️⃣ Model yaratish

products/models.py faylida quyidagi modelni yarating:

Product
 • name – CharField (max_length=100)
 • price – IntegerField
 • description – TextField
 • created_at – DateTimeField (auto_now_add=True)

⸻

3️⃣ Admin panelga qo‘shish
 • products/admin.py faylida Product modelini admin panelga ro‘yxatdan o‘tkazing.
 • Admin panelda:
 • name
 • price
 • created_at

ustunlari ko‘rinsin.

⸻

4️⃣ Migratsiya qilish

Quyidagi buyruqlarni bajaring:

python manage.py makemigrations
python manage.py migrate


⸻

5️⃣ Superuser yaratish

Admin panelga kirish uchun:

python manage.py createsuperuser


⸻

6️⃣ View yaratish

products/views.py da:
 • Barcha mahsulotlarni bazadan olib,
 • Templatega uzatuvchi view yozing.

Masalan:
 • product_list funksiyasi

⸻

7️⃣ URL sozlash
 • products/urls.py faylini yarating.
 • product_list view uchun URL yozing:

path('', product_list, name='product_list')

 • Asosiy project/urls.py da products URLlarini ulang.

⸻

8️⃣ Template yaratish

templates/products/product_list.html faylini yarating.

Template ichida:
 • Sahifa sarlavhasi bo‘lsin
 • Barcha mahsulotlar:
 • nomi
 • narxi
 • tavsifi
ko‘rinishda chiqarilsin.

⸻

9️⃣ Templatega ma’lumot chiqarish
 • Django template syntax ({{ }}, {% for %}) dan foydalaning.
 • Mahsulotlarni for loop orqali chiqarib bering.

⸻

🔟 Tekshirish
 • Admin panel orqali kamida 3 ta mahsulot qo‘shing.
 • Brauzerda:

http://127.0.0.1:8000/products/

manzilida mahsulotlar chiqayotganini tekshiring.

⸻

✅ Natija
 • App yaratildi
 • Model yaratildi
 • Admin panel ishlayapti
 • URL sozlandi
 • Template orqali ma’lumot chiqyapti
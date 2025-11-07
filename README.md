Proyek Portfolio Pribadi - Flask & MySQL Ini adalah proyek website portfolio pribadi yang dibuat untuk memenuhi tugas Responsi Pemrograman Web Praktik III. Proyek ini dibangun menggunakan Python dengan framework Flask dan terhubung ke database MySQL.

Website ini memiliki dua bagian utama:

Halaman Publik: Menampilkan profil, daftar skill, dan proyek. Panel Admin: Halaman dashboard yang dilindungi login untuk mengelola (CRUD) semua konten di halaman publik. Fitur Utama Halaman Publik: Menampilkan data profil, skill, dan proyek langsung dari database. Login Admin: Otentikasi admin manual menggunakan Flask Session. Manajemen Profil: Admin dapat mengubah nama, bio, dan foto profil. CRUD Proyek: Admin dapat menambah, mengedit, dan menghapus data proyek (termasuk upload gambar). CRUD Skill: Admin dapat menambah, mengedit, dan menghapus data skill (termasuk nama ikon Font Awesome). Upload Gambar: Fungsionalitas untuk meng-upload foto profil dan gambar proyek ke server. Teknologi yang Digunakan Back-end: Python, Flask Database: MySQL Driver Database: flask-mysqldb (dijalankan dengan PyMySQL untuk kompatibilitas Windows) Front-end: HTML5, Bootstrap 5, Font Awesome Templating: Jinja2

Cara Menjalankan Aplikasi

Clone Repository git clone https://github.com/username/portfolio-flask.git cd portfolio-flask

Buat Virtual Environment dan Install Dependencies python -m venv env env\Scripts\activate # untuk Windows

Halaman Home 
<img width="1884" height="984" alt="Screenshot 2025-11-07 163620" src="https://github.com/user-attachments/assets/e1ec5542-aef9-4448-a8fc-39a453b27b6c" />
<img width="1882" height="986" alt="Screenshot 2025-11-07 163642" src="https://github.com/user-attachments/assets/b6e79111-0f6e-411f-9c7e-0b5c520c594b" />

Halaman Admin
<img width="1890" height="990" alt="Screenshot 2025-11-07 163703" src="https://github.com/user-attachments/assets/264e3a69-9edc-43e8-b52f-e9bfa686b008" />
<img width="1886" height="987" alt="Screenshot 2025-11-07 163713" src="https://github.com/user-attachments/assets/c4e9907f-9a2a-4602-be8a-3123d42cb27e" />

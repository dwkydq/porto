Proyek Portfolio Pribadi - Flask & MySQL Ini adalah proyek website portfolio pribadi yang dibuat untuk memenuhi tugas Responsi Pemrograman Web Praktik III. Proyek ini dibangun menggunakan Python dengan framework Flask dan terhubung ke database MySQL.

Website ini memiliki dua bagian utama:

Tampilan Publik (index.html)
Ini adalah halaman yang dilihat oleh pengunjung.
Header Profil: Menampilkan Foto Profil, Nama ({{ user[3] }}), dan Bio ({{ user[4] }}) dari pemilik portofolio.
SKILLS: Bagian yang menampilkan daftar kemampuan yang dimiliki. Setiap skill memiliki Nama ({{ skill[1] }}), Level ({{ skill[2] }}), dan Ikon.
PROJECTS: Bagian yang menampilkan karya atau proyek yang telah diselesaikan. Setiap proyek memiliki Judul ({{ project[1] }}), Deskripsi ({{ project[2] }}), Gambar ({{ project[3] }}), dan tautan Unduh/Link ({{ project[4] }}).
Tombol Mode Admin: Tombol di bagian bawah halaman untuk masuk ke halaman login admin.

🔒 Dashboard Admin (admin.html, edit_profile.html, login.html)
Ini adalah area yang dilindungi kata sandi untuk mengelola konten website.
1. Header Admin (admin.html)
Menampilkan Salam ("Halo, Dwiky"), Foto Profil, dan Bio.
Terdapat tombol untuk Edit Profil (edit_profile) dan Log Out (logout).
2. Manajemen SKILLS (admin.html)
Menampilkan daftar skill yang ada.
Memiliki fungsi:
+ Tambah: Menampilkan form untuk menambah skill baru.
Edit: Menampilkan form untuk mengubah nama, level, dan ikon skill yang sudah ada.
Hapus: Untuk menghapus skill.
3. Manajemen PROJECTS (admin.html)
Menampilkan daftar proyek yang ada.
Memiliki fungsi:
+ Tambah: Menampilkan form untuk menambah proyek baru (Judul, Deskripsi, Link, Gambar).
Edit: Menampilkan form untuk mengubah detail proyek.
Hapus: Untuk menghapus proyek.
4. Edit Profil (edit_profile.html)
Halaman khusus untuk mengubah Nama, Bio, dan Foto Profil.
5. Login (login.html)
Halaman untuk memasukkan Username dan Password guna mengakses Dashboard Admin.


Cara Menjalankan Aplikasi

Clone Repository git clone https://github.com/dwky/porto-flask.git cd portfolio-flask

Buat Virtual Environment dan Install Dependencies python -m venv env env\Scripts\activate # untuk Windows

Halaman Home 
<img width="1884" height="984" alt="Screenshot 2025-11-07 163620" src="https://github.com/user-attachments/assets/e1ec5542-aef9-4448-a8fc-39a453b27b6c" />
<img width="1882" height="986" alt="Screenshot 2025-11-07 163642" src="https://github.com/user-attachments/assets/b6e79111-0f6e-411f-9c7e-0b5c520c594b" />

Halaman Admin
<img width="1890" height="990" alt="Screenshot 2025-11-07 163703" src="https://github.com/user-attachments/assets/264e3a69-9edc-43e8-b52f-e9bfa686b008" />
<img width="1886" height="987" alt="Screenshot 2025-11-07 163713" src="https://github.com/user-attachments/assets/c4e9907f-9a2a-4602-be8a-3123d42cb27e" />

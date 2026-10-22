# Cortez Web

Website latihan dengan Python (Flask), HTML, CSS, dan sedikit JavaScript.

## Persyaratan
- Python terpasang
- Visual Studio Code

## Menjalankan di Windows
1. Ekstrak ZIP ini.
2. Buka folder `cortez_web` di VS Code (`File > Open Folder`).
3. Buka terminal (`Terminal > New Terminal`).
4. Buat virtual environment:
   ```powershell
   python -m venv .venv
   ```
5. Aktifkan:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   Jika PowerShell memblokir aktivasi, gunakan Command Prompt terminal dan jalankan:
   ```bat
   .venv\Scripts\activate.bat
   ```
6. Instal Flask:
   ```powershell
   python -m pip install -r requirements.txt
   ```
7. Jalankan:
   ```powershell
   python app.py
   ```
8. Buka `http://127.0.0.1:5000` di browser.
9. Untuk menghentikan server, tekan `Ctrl+C` di terminal.

Catatan: form contoh memberikan konfirmasi, tetapi belum menyimpan pesan ke database. Server debug hanya untuk pengembangan lokal, bukan hosting publik.

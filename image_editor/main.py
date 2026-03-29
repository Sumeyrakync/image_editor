import os
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image


class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Yemeksepeti Görsel Düzenleyici v2")
        self.geometry("450x350")
        ctk.set_appearance_mode("dark")

        # Masaüstünde çıktı klasörünü hazırla
        self.output_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Yemeksepeti_Yukle")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Arayüz Elemanları
        self.label = ctk.CTkLabel(self, text="Resmi Buraya Sürükle\n(Dosya Masaüstüne Kaydolur)",
                                  width=400, height=200,
                                  fg_color="#1f538d", corner_radius=15)
        self.label.pack(pady=30, padx=20)

        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.resmi_isle)

        self.status_label = ctk.CTkLabel(self, text=f"Çıktı Klasörü: Masaüstü/Yemeksepeti_Yukle", text_color="gray",
                                         font=("Arial", 10))
        self.status_label.pack()

    def resmi_isle(self, event):
        # Dosya yolunu temizle (Bazı sistemlerde {} veya tırnak içinde gelir)
        path = event.data.strip('{}').strip('"')

        if not path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            self.status_label.configure(text="Hata: Geçersiz dosya formatı!", text_color="red")
            return

        try:
            # Resmi aç ve RGB'ye çevir
            img = Image.open(path).convert('RGB')

            # Boyutu 2000px genişliğe sabitle (1000px sınırını aşmak için)
            target_w = 2000
            w_ratio = (target_w / float(img.size[0]))
            target_h = int((float(img.size[1]) * float(w_ratio)))
            img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)

            # Yeni dosya adı oluştur
            base_name = os.path.basename(path).split('.')[0]
            final_path = os.path.join(self.output_dir, f"HAZIR_{base_name}.jpg")

            # Kaydet (Boyutu 200KB üstünde tutmak için kaliteyi ve örneklemeyi ayarla)
            img.save(final_path, "JPEG", quality=98, subsampling=0)

            size_kb = os.path.getsize(final_path) / 1024
            self.status_label.configure(text=f"BAŞARILI! Masaüstüne bak: {size_kb:.1f} KB", text_color="#00FF00")

            # Klasörü otomatik aç
            os.startfile(self.output_dir)

        except Exception as e:
            self.status_label.configure(text=f"Hata: {str(e)}", text_color="red")


if __name__ == "__main__":
    app = App()
    app.mainloop()
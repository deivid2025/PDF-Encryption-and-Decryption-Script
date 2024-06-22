from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm
import time

def decrypt_pdf(input_file, output_file, password):
    reader = PdfReader(input_file)

    if reader.is_encrypted:
        if reader.decrypt(password):
            writer = PdfWriter()

            total_pages = len(reader.pages)
            # Configurar tqdm para mostrar la barra de progreso general
            progress_bar = tqdm(total=total_pages, desc="Descifrando PDF", unit="páginas")

            # Configurar tqdm para la barra de progreso estilo "matrix"
            matrix_bar = tqdm(total=100, desc="Descifrando", unit="%", position=0)

            for page_num in range(total_pages):
                writer.add_page(reader.pages[page_num])

                # Actualizar la barra de progreso general
                progress_bar.update(1)

                # Actualizar la barra de progreso estilo "matrix"
                matrix_bar.update(1)
                time.sleep(0.02)  # Ajustar el tiempo de espera para el efecto deseado

            with open(output_file, "wb") as f:
                writer.write(f)

            progress_bar.close()
            matrix_bar.close()
            print(f"\nPDF descifrado guardado en: {output_file}")
        else:
            print("Error: Contraseña incorrecta. No se puede descifrar el PDF.")
    else:
        print("Error: El PDF no está cifrado.")

if __name__ == "__main__":
    encrypted_pdf = "encrypted-pdf.pdf"  # Nombre del PDF cifrado
    decrypted_pdf = "decrypted-pdf.pdf"  # Nombre del PDF descifrado
    password = "my-secret-password"  # Contraseña para descifrar el PDF cifrado

    decrypt_pdf(encrypted_pdf, decrypted_pdf, password)

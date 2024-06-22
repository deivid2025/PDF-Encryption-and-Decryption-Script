from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm

def encrypt_pdf(input_file, output_file, password):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    progress_bar = tqdm(total=len(reader.pages), desc="Cifrando PDF", unit="páginas")

    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])
        progress_bar.update(1)

    writer.encrypt(user_password=password, use_128bit=True)

    with open(output_file, "wb") as f:
        writer.write(f)

    progress_bar.close()
    print(f"\nPDF cifrado guardado en: {output_file}")

if __name__ == "__main__":
    input_pdf = "test.pdf"  # Nombre del PDF original
    encrypted_pdf = "encrypted-pdf.pdf"  # Nombre del PDF cifrado
    password = "my-secret-password"  # Contraseña para cifrar el PDF

    encrypt_pdf(input_pdf, encrypted_pdf, password)

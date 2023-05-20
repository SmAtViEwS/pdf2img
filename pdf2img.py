# img2pdf #
import os
os.system('pip install pyfiglet==0.7')

from pyfiglet import Figlet

figlet = Figlet(font="Standard")
print(figlet.renderText("SmAtViEwS"))

txt = "SMART VIEWS IMG 2 PDF TRANSFER"
print(txt)
print("PLEASE ALLOW THE STORAGE ACCESS OF TERMUX OR ANY TERMINAL YOU ARE USING.")
print("   ")

import img2pdf

def main():
    f = input('Enter img path :')
    try:
        with open(f, 'rb') as img:
            pdf_byts = img2pdf.convert(img)
    except FileNotFoundError:
        print('File not found.')
        return(main())

    k = input('Enter file name :')
    with open(k, 'wb') as pdf:
        pdf.write(pdf_byts)

    print('PDF file created successfully.')

if __name__ == '__main__':
    main()

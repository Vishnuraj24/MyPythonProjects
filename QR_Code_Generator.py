import pyqrcode
import png
link = "https://www.linkedin.com/in/kandukurivishnuraj/"
QR_Code = pyqrcode.create(link)
QR_Code.png("Linkedin_QR",scale=5)
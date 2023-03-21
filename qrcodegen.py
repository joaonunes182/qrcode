#pip install segno 
import segno
qrcode = segno.make_qr('https://youtube.com')
qrcode.save('youtube.png', scale='10')
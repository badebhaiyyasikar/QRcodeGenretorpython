import qrcode

#taking UPI ID As a input
upi_id = input("Enter UPI ID: ")

#upi://pay?pa=UPI_ID_&pm=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL bassed on the UPI ID and the payment app
#You can modify the payment app according to your needs

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Creat QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the QR code to image file
phonepe_qr.save('phonepe.png')
paytm_qr.save('paytm.png')
google_pay_qr.save('google_pay.png')

#display the QR codes (you may need to install pillow)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
print("bade_bhaiyya")

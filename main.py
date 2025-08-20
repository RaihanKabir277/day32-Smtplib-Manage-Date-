# print("day 32 starts here ........")

import smtplib

my_mail = "-------@gmail.com"  #give your gmail here
# connection = smtplib.SMTP("smtp.gmail.com")

with smtplib.SMTP("smtp.gmail.com") as connection:
    # ------ transport layer security ------
    connection.starttls()
    connection.login(user=my_mail, password="********") #your password paste here
    connection.sendmail(from_addr=my_mail, to_addrs="----@yahoo.com", msg="Subjects:Hello\n\nThis is my email.")


# connection.close()



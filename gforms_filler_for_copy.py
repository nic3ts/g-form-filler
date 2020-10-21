import requests
import random

url = 'https://docs.google.com/forms/d/e/1FAIpQLSf9e5tXHF6EFu6CyDnd2NxczhtbjL-ZdYQZ_MLHrDij06z4hg/formResponse'

answer1 = ['Αρσενικό', 'Θηλυκό']
answer2 = ['18-25', '26-30', '31-40', '41-50', '51-60', '61-70', '70+']
answer3 = ['Έγγαμος/η', 'Άγαμος/η', 'Διαζευγμένος/η']
answer4 = ['Φοιτητής', 'Ιδιωτικός υπάλληλος', 'Δημόσιος υπάλληλος', 'Ελεύθερος επαγγελματίας', 'Άνεργος', 'Συνταξιούχος']
answer5 = ['Ζω μόνος/η', 'Συγκατοικώ με φίλο/η ή τον/τη σύντροφο μου', 'Ζω με την πατρική μου οικογένεια', 'Έχω οικογένεια', 'Έχω οικογένεια με παιδιά']
answer6 = ['0', '1-450', '451-700', '701-1000', '1001-1500', '1501-2000', '2000+']
answer7 = ['0', '100-200', '200-300', '300-400', '400-500', '500+']
answer8 = ['0-100', '100-200', '200-300', '300-400', '400+']
answer9 = ['0-100', '100-200', '200-300', '300-400', '400-500', '500+']
answer10 = ['0-100', '100-200', '200-300', '300-400', '400+']
answer11 = ['0-100', '100-200', '200-300', '300-400', '400+']
answer12 = ['0-100', '100-200', '200-300', '300-400', '400+']


user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSf9e5tXHF6EFu6CyDnd2NxczhtbjL-ZdYQZ_MLHrDij06z4hg/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

for x in range (1000):

    fulo = random.randint(0,1)
    eidos_apasxolhshs = random.randint(0,4)

    if (eidos_apasxolhshs == 0):
        hlikia = random.randint(0,1)
        oikogeneiakh_kat = 1
        eidos_diamonhs = random.randint(0,2)
        esoda = random.randint(0,2)
        eksoda_enoikiashs = random.randint(0,3)
        eksoda_logariasmwn = random.randint(0,2)
        eksoda_supermarket = random.randint(0,2)
        eksoda_metakinhsewn = random.randint(0,1)
        eksoda_diaskedashs = random.randint(0,3)
        eksoda_alla = random.randint(0,1)
    else:
        hlikia = random.randint(0,6)
        oikogeneiakh_kat = random.randint(0,2)
        eidos_diamonhs = random.randint(0,4)
        esoda = random.randint(0,6)
        eksoda_enoikiashs = random.randint(0,5)
        eksoda_logariasmwn = random.randint(0,4)
        eksoda_supermarket = random.randint(0,5)
        eksoda_metakinhsewn = random.randint(0,4)
        eksoda_diaskedashs = random.randint(0,4)
        eksoda_alla = random.randint(0,4)

    form_data = {
                    'entry.632871401'   :  answer1[fulo],
                    'entry.514318258'   :  answer2[hlikia],
                    'entry.847492734'   :  answer3[oikogeneiakh_kat],
                    'entry.848442125'   :  answer4[eidos_apasxolhshs],
                    'entry.1582373587'  :  answer5[eidos_diamonhs],
                    'entry.341885911'   :  answer6[esoda],
                    'entry.274972187'   :  answer7[eksoda_enoikiashs],
                    'entry.1299272873'  :  answer8[eksoda_logariasmwn],
                    'entry.1948120245'  :  answer9[eksoda_supermarket],
                    'entry.449589248'   :  answer10[eksoda_metakinhsewn],
                    'entry.1060890948'  :  answer11[eksoda_diaskedashs],
                    'entry.1919127210'  :  answer12[eksoda_alla]
                }

    r = requests.post(url, data=form_data, headers=user_agent)
    print('POST ', x, ' successful')

# COPY OF
# https://docs.google.com/forms/d/e/1FAIpQLSf9e5tXHF6EFu6CyDnd2NxczhtbjL-ZdYQZ_MLHrDij06z4hg/viewform

# TEST ERWTHMATOLOGIO
# https://docs.google.com/forms/d/e/1FAIpQLSdX5VjVuH3ZB8B-_3x8AKGordpsYyhOrmJ2Z61p5_IOTV1RFw/viewform
# https://docs.google.com/forms/d/e/1FAIpQLSdX5VjVuH3ZB8B-_3x8AKGordpsYyhOrmJ2Z61p5_IOTV1RFw/formResponse

# 'entry.2048246044' : answer

# ====================================================================

# KOSTOS ZWHS STH SAMOS
# https://docs.google.com/forms/d/e/1FAIpQLSc_ZWnZkBzwywxKp5fa8xksfYnPnCeOuh6kA_fR5wojfDGQJg/viewform
# https://docs.google.com/forms/d/e/1FAIpQLSc_ZWnZkBzwywxKp5fa8xksfYnPnCeOuh6kA_fR5wojfDGQJg/formResponse

# COPY OF
# https://docs.google.com/forms/d/e/1FAIpQLSf9e5tXHF6EFu6CyDnd2NxczhtbjL-ZdYQZ_MLHrDij06z4hg/viewform


# https://docs.google.com/forms/d/e/1FAIpQLSdX5VjVuH3ZB8B-_3x8AKGordpsYyhOrmJ2Z61p5_IOTV1RFw/viewform?usp=pp_url&entry.2048246044=Option+2

from passporteye import read_mrz

mrzy = read_mrz("docpiv.jpg")

mrz_data = mrzy.to_dict()

print("Nationality: ", + mrz_data['nationality'])
print("Given name: " + mrz_data['name'])
print("Surname " + mrz_data['surname'])
print("Date of birth: " + mrz_data['date_of_birth'])
print("ID number: " + mrz_data['personal_number'])
print(" Sex :" + mrz_data['sex'])
print("Expiration date: " + mrz_data['expiration'])
print("Place of birth: " + mrz_data['place_of_birth'])
print(mrz_data, file=open('passportdata.csv', "a"))
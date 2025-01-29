course_id = input("Хичээлийн код: ")
course_name = input("Хичээлийн нэр: ")
credit = input("Хичээлийн кредит: ")

madlib1 = "Энэ хичээлийн код нь {}".format(course_id) + ", хичээлийн нэр нь {}".format(course_name) + \
        " бөгөөд уг хичээл нь {}".format(credit) + " кредитийн хичээл юм."

madlib2 = "Энэ хичээлийн код нь {}".format(course_id).upper() + ", хичээлийн нэр нь {}".format(course_name).title() + \
        " бөгөөд уг хичээл нь {}".format(credit) + " кредитийн хичээл юм."

print(madlib1)
print(madlib2)
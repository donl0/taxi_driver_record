def make_num_of_doc(num_of_user):
    len_pk = len(str(num_of_user))
    if len_pk < 10:
        num = '000000' + str(num_of_user)
    elif len_pk < 100:
        num = '00000' + str(num_of_user)
    elif len_pk < 1000:
        num = '0000' + str(num_of_user)
    elif len_pk < 10000:
        num = '000' + str(num_of_user)
    elif len_pk < 100000:
        num = '00' + str(num_of_user)
    elif len_pk < 1000000:
        num = '0' + str(num_of_user)
    else:
        num = str(num_of_user)
    return num
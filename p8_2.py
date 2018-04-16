def save_file(boy,girl,count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy.file.writelines(boy)
    girl.file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    ####################
    count = 1
    boy = []
    girl = []
    f = open(file_name)
    for each_line in f:
        if each_line[:6] != '== == == ':
            (role, line_spoken) = each_line.split(":", 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
           save_file(boy,girl,count)
            boy = []
            girl = []
            count += 1
    save_file(boy,girl,count)
    f.close()
split_file('record.txt')4
import sys

def parse_checkist(st):
    ll = len(st)
    for i in range(int(ll/2)):
        if st[i]!=st[ll-1-i]:
            return False
    return True

if __name__ == '__main__':
    try:
        ss = sys.argv[1]
    except IndexError:
        print("usage: python3 {} /path/to/file \n".format(sys.argv[0]))
        exit(64)
    dt = dict()
    cntr = 0
###ТЗ написано неоднозначно, было растолковано как "посчитать все полиндромы"
###"...состоящие из одних сиволов, имеющих пару и более"
    try:
        with open(ss, "r") as f:
            for line in f:
                if line[-1]=="\n":
###Если строка полиндрома заканчивается на символ переноса строки(а это все кроме последней)
###То удалим этот символ
###В python3 отсутствует проблема терминирующих нулей, их проверять не требуется
                    line = line[:len(line)-1]
#                print(line)

                if parse_checkist(line):
#                   print(line)
                    linesrt = str(sorted(list(set(line[:int(len(line)/2)+1]))))
###Преобразование: poly_str - исходная строка, содержащая в чистом виде полиндром
###set_of_chars - сет - набор уникальных символов, содержащийся в poly_str
###poly_str->set_of_chars(poly_str)->list_of_this_chars->sort_this_list->to_string
                    if linesrt in dt:
                    ##Есть ли уже в памяти поли из таких символов?
                        dt[linesrt]+=1
                        if dt[linesrt] == 2:
##Если есть такое, а пара найдена впервые, то счетчик не-одиночных сиволов увеличиваем на два
                            cntr += 2
                        else:
                            cntr+=1
###Иначе(3й,4й, etc...) - на один
                    else:
                        dt[linesrt] = 1
###Если полиндром с подобным набором найден впервые, используем автовивификацию по имени
    except OSError:
        print("Not such file\n")
        exit(42)
    print(cntr)

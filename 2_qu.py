import operator as op
def parser(line):
    s_list = line.split('/')
    str_dic_f = lambda x: {x[0]: str_dic_f(x[1:])} if x[1:] else x[0]
    return str_dic_f

def counter(sss):
    if sss:
        s = 1
        for i in sss.values():
            s+=cccc(i)
            return s
        else:
            return 0

if __name__ == '__main__':
    try:
        str_in = sys.argv[1]
    except IndexError:
        print("Usage: python3 {} /path/to/file".format(sys.argv[0]))
    
    str_dic_f = lambda x: {x[0]: str_dic_f(x[1:])} \
                    if x[1:] else {x[0]:{}}

    unite = lambda a, b: unite(a[list(b.keys())[0]], b[list(b.keys())[0]]) if \
                         list(b.keys())[0] in a else \
                         op.setitem(a, list(b.keys())[0], b[list(b.keys())[0]])
    ###impure func relatively to a###

        
    summary = {}
    with open(str_in, 'r') as f_in:
        for line in f_in:
            ##creating temporary path struct
            if line[0] == '/':
                line = line[1:]
            tmp = str_dic_f(line.split('/'))

            ##uniting it with summary paths
            unite(summary, tmp)
    summary_overall = {'ALL_FILES':summary}
    ###function creating structs
    rec_ret = lambda sss: [[{k:rec_ret(v)}, counter(v)+1] for k,v in sss.items()] if sss else {}
    
    print(summary_overall)

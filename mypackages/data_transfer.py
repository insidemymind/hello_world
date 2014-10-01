import math, os
from xlrd import open_workbook, cellname

def read_xls(filename):
    '''read from a xls file and make it into variable 'data' '''
    book = open_workbook(filename)
    data_all = []
    names = []
    for sheet_index in range(book.nsheets):
        sheet = book.sheet_by_index(sheet_index)
        names.append(sheet.name)
        data = []
        for row_index in range(sheet.nrows):
            data.append([])
            for col_index in range(sheet.ncols):
                v = sheet.cell(row_index,col_index).value
                if v != '':
                    ##this is only for the treatment without the suffix '-BD' or '-BL'##
                    # if row_index == 0 and v[-2] != 'B':
                    #     if sheet.name.split()[-1] == 'live':
                    #         v = v + '-BL'
                    #     elif sheet.name.split()[-1] == 'dead':
                    #         v = v + '-BD'
                    ##end here##
                    data[-1].append(v)
        data_all.append(data)
    return data_all, names


def data_transform(data, log):
    ''' transform the data from total number into individual worms with one's live days '''
    day = data[0][1:]
    curve_list = []
    status_list = []
    for i, condition in enumerate(data[1:]):
        condition = list(condition)
        if len(day) + 1 != len(condition):
            print data[0][0], condition
        curve = [condition[0],]
        status = [condition[0],]
        for x in range(1, len(condition) - 1):
            tmp = int(math.floor(float(condition[x])) - math.floor(float(condition[x+1])))
            if tmp < 0:
                print >>log, 'pretending death', condition
                print 'pretending death', tmp, condition[x], condition[x+1],condition, type(condition)
                condition[x+1] = condition[x]
            for k in range(tmp):
                curve.append(day[x-1])
                status.append('1')
        if len(curve) - 1 == int(condition[1]):
            stand = int(condition[1])
        else:
            ##this is for live worms at the end of an experiment##
            [curve.append(day[-1]) for x in range(int(condition[-1]))]
            [curve.append(day[-1]+2) for x in range(int(condition[-1]))]
            [status.append('1') for x in range(int(condition[-1]))]
            [status.append('0') for x in range(int(condition[-1]))]
            stand = int(condition[1]) + int(condition[-1])
            ##end up here##
        if len(curve) != len(status):
            print len(curve), len(status)
        curve_list.append(curve)
        status_list.append(status)
    return (curve_list, status_list)


def pipe(names, data, dirname='./', n='test'):
    '''
    names = name of each sheet, i.e. 'live', 'plate2'.
    data = a list of list <IMPORTANT!> each list has a name: 'day', 'CTL'.
    dirname = absolute dir is prefer.
    n = name of xls, i.e. name of this experiment.
    '''
    if not os.path.exists(dirname+n+'/1/'):
        os.makedirs(dirname+n+'/1/')
        os.makedirs(dirname+n+'/2/')
    with open(dirname + n+ '/' + 'filelist.txt', 'w') as f:
        for x in names:
            print >>f, dirname+ n+'/'+ x
    log = open(dirname+ n+'/'+ n +'.log', 'a')
    for index, sub in enumerate(data):
        name = names[index]
        out = open(dirname+ n+'/'+name +"-rowbyrow.txt",'a')
        status_out = open(dirname+ n+'/'+ name + '-status.txt', 'a')
        (curve_list, status_list) = data_transform(sub, log)
        for i in range(len(curve_list)):
            c = [str(k) for k in curve_list[i]]
            s = [str(k) for k in status_list[i]]
            print >>out, '\t'.join(c)
            print >>status_out, '\t'.join(s)
    # D:\Program Files\R\R-3.0.3patched\bin\

def main():
    ''' process the xls file with all the print function '''
    xlsnames = ['0310plate2']
    for n in xlsnames:
        data, names = read_xls('../input/'+ n +'.xls')


if __name__ == '__main__':
    main()

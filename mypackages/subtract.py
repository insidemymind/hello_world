# -*- coding: utf-8 -*-
# Subtract two images.
# Using threshold to get the binary image from the subtract image.

def two_convert(im, threshold, threshold2):
    lim = im.convert('L')
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        elif i > threshold2:
            table.append(0)
        else:
            table.append(255)
    bim = lim.point(table, '1')
    return bim


def clean(im):
    for i in iter(im.getdata()):
        if i != 0:
           break
    else:
        return 1
    return 0

def dead_or_live(object_list, im):
    if clean(im):
        return 'Clean\t0'
    live = []
    # print object_list
    for seq, ele in enumerate(object_list):
        for point in range(21):
            # print point, ele
            if im.getpixel((object_list[ele][point], object_list[ele][point+21])) != 0:
                live.append(seq+1)
                break
    count = len(live)
    live = ','.join([str(x) for x in live])
    return '\t'.join((live, str(count)))


def live_judge(name1, name2, object_list, save_flag, save_location=''):
    from PIL import Image,ImageChops

    im1 = Image.open(name1)
    im2 = Image.open(name2)
    im0 = ImageChops.subtract(im1, im2)
    im3 = two_convert(im0, 30,230)
    if save_flag:
        im3.save(save_location)
    return dead_or_live(object_list, im3)

def get_obj(obj_file_name):
    obj_dic = {}
    with open(obj_file_name) as obj_f:
        for line in obj_f:
            fields = line.split(',')
            img = int(fields[0])
            if img not in obj_dic:
                obj_dic[img] = []
            obj_dic[img].append([float(x) for x in fields[24:-1]])
    return obj_dic


def main(obj_dic, img_obj_map, well):
    """
    main function of subtract method
    """
    subtract_worm_count = []
    well = [int(dummy_i) for dummy_i in well.split('_')]

    # convert img_obj_map:
    obj_img_map = {}
    for dummy_k in img_obj_map:
        obj_img_map[img_obj_map[dummy_k]] = dummy_k

    for i in range(8, 49, 2): # i means Day
        if i == 12: # Day 12 is not included in this dataset
            continue
        elif i < 21: # month = 03
            name_general = 'D:/plate2_test_3/03%02d D%d' % (i+10, i)
        elif i : # month = 04
            name_general = 'D:/plate2_test_3/04%02d D%d' % (i-21, i)
        tmp = []

        for j in range(well[0], well[1]+1): # j means well
            name = '%dD%d' % (j, i)

            for k in(6, 3): # k means image
                image = name+'_%d' % k
                if image in obj_img_map:
                    name_com = name_general + '_%d_%d.tiff' % (j, k)
                    break
            name_org = name_general + '_%d_0.tiff' % (j)

            if obj_img_map[image] not in obj_dic:
                live = 'No_obj\t0'
            else:
                live = live_judge(name_org, name_com, \
                    obj_dic[obj_img_map[image]], False)
            # print i,j,k,live
            tmp.append(int(live.split('\t')[-1]))
        subtract_worm_count.append(tmp)
    return zip(*subtract_worm_count)


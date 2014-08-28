# -*- coding: utf-8 -*-

"""
get the number of live worms through two approaches:
first, by CPA counting the live worms;
second, by angle change
"""
import copy

def invalid_dict(filename, location_list):
    """
    read from the image_file to fetch
    image_dict: which image is available to calculate, return a dictionary of
    true or false.
    image_count: a dictionary of worms count in each well;
    image_object_map: e.g. 1:"195D8"
    """
    image_flag_dict = {}
    image_count = {}
    image_object_map = {}
    with open(filename) as image_f:
        count = 0
        flag_list = 0
        well_count = []
        for line in image_f:
            fields = line.split(",")
            if 'NULL' in fields:
                print 'NULL in fields', line
                continue

            # location_list = [Image_Metadata_ImageQCFlag integer, \
            # Image_Metadata_ObjectAreaQCFlag integer, Image_Metadata_Well \
            # TEXT, Image_Count_NonOverlappingWorms integer, ImageNumber\
            # INTEGER, Image_Metadata_Date TEXT,]
            flag_list += float(fields[location_list[0]]) + \
            float(fields[location_list[1]])
            well = int(fields[location_list[2]].strip('"'))
            count += 1
            well_count.append(float(fields[location_list[3]]))
            image_object_map[int(fields[location_list[4]])] = str(well) + \
            fields[location_list[5]].strip('"')+'_'+fields[location_list[6]]

            if count == 3:
                if well in image_flag_dict:
                    if flag_list == 0:
                        # if all the image in a set is qualified, agree that
                        # append means that the sequence is D10-->D28-->D8
                        image_flag_dict[well].append(True)
                    else:
                        image_flag_dict[well].append(False)
                else:
                    if flag_list == 0:
                        image_flag_dict[well] = [True]
                    else:
                        image_flag_dict[well] = [False]
                total = int(sorted(well_count)[1]) # total is the median either
                if well in image_count:
                    image_count[well].append(total)
                else:
                    image_count[well] = [total]
                flag_list = 0
                count = 0
                well_count = []
    return image_flag_dict, image_count, image_object_map


def merge_flags_and_counts(flags, counts):
    """
    merge the image flag and the well count
    according to the flag, decide whether to use the count or not
    """
    dummy_i = -1
    for well in flags:
        dummy_i += 1
        for index_i, bool_value in enumerate(flags[well]):
            if not bool_value:
                if type(counts) is dict:
                    counts[well][index_i] = None
                elif type(counts) is list:
                    counts[dummy_i][index_i] = None
                else:
                    print type(counts)
    return counts


def sequence(counts):
    """
    give the count the right sequence,
    that is D8-->D10-->D28.
    """
    for date in counts:
        counts[date] = [counts[date][-1]] + counts[date][:-1]
    return counts


def combine_eight_wells(counts):
    """
    show the total list of each treatment
    counts should be a list, rather than a dict,
    because list is more reliable in this condition.
    """
    if type(counts) is dict:
    # the old way for counts as a dict:
        index = 0
        treatment_all = []
        for key in counts:
            if index % 8 == 0:
                treatment = [0 for dummy_j in range(len(counts[195]))]
            index += 1
            # print len(counts[key])
            treatment = [(tmp_x + tmp_y) \
            for tmp_x, tmp_y in zip(treatment, counts[key])]
            if index % 8 == 0:
                treatment_all.append(treatment)
        # this step is special for the test data,
        # because the number of test data is 23 and cannot mod 8 == 0
        # treatment_all.append(treatment)
        # end
    elif type(counts) is list:
        # the new way for counts as a list of list:
        treatment_all = []
        for index in range(len(counts)):
            if index % 8 == 7:
                treatment_all.append([sum(ele) for ele in \
                    zip(*counts[index-7:index+1])])
    return treatment_all


def plot_data(name, data, day, text, \
    compare=False, data2='', day2='', text2='',\
    compare2=False, data3='', day3='', text3=''):
    """
    plotting data
    """
    import matplotlib.pyplot as plt
    count = -1
    plt.figure(figsize=(18, 5), dpi=100)
    for key in data:
        count += 1
        plt.subplot(1, 3, count+1)
        plt.plot(day, key, label=text)
        if compare:
            plt.plot(day2, data2[count], label=text2)
            plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, \
                ncol=2, mode="expand", borderaxespad=0.)
        if compare2:
            plt.plot(day3, data3[count], label=text3)
            plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, \
                ncol=3, mode="expand", borderaxespad=0.)
        plt.axis([day[0], day[-1], 0, 90])
        # plt.savefig('%s_%d' %(text, count))
        # plt.clf()
    plt.savefig('%s' %(name))
    plt.clf()


def subtract_count(obj_dic, img_obj_map, well):
    """
    use subtract module to count the worms after day 34.
    """
    import subtract
    return subtract.main(obj_dic, img_obj_map, well)


def combine_subtract_and_max(subtract_result, max_result, day, split_day):
    """
    combine the two result into one, depends on split_day
    """
    combine_result = copy.deepcopy(max_result)
    ini = day.index(split_day)
    for dummy_i in xrange(len(combine_result)):
        for dummy_j in xrange(ini, len(day)):
            combine_result[dummy_i][dummy_j] = \
            subtract_result[dummy_i][dummy_j]
    return combine_result


def read_idw_object_csv(filename, image_object_map, daylist, location_list, before_method, split_day, neighbor_flag, dead_filename):
    """
    read the IDW object file, count the live worm in each image,
    use the object with no Children_DeadWorms_Count,
    and count the median of 3 images of each well in each day.
    The order here is the right one: D8 -> D28.
    """
    def judge_fake(loc, lis, image_object_map, split_day):
        import intersection

        length = 88
        # read in the dead worm file --> dead worm x and y
        dead_loc = {}
        with open(dead_filename) as dead_f:
            for line in dead_f:
                fields = line.strip().split(',')
                img = int(fields[0])
                obj = int(fields[4])
                tmp_x, tmp_y, tmp_angle = [float(dummy_x) for dummy_x in \
                (fields[2], fields[3], fields[5])]
                if img not in dead_loc:
                    dead_loc[img] = {}
                try:
                    dead_loc[img][obj].append((tmp_x, tmp_y, tmp_angle))
                except KeyError:
                    dead_loc[img][obj] = \
                    [(tmp_x, tmp_y, tmp_angle)]
        fake = {}
        dist_limit = float(length)*float(length)*4/25 # square of dist
        for ele in lis:
            img, obj, children, closest = [int(dummy_x) for dummy_x in ele]
            if int(image_object_map[img].split('D')[1].split('_')[0]) >= split_day:
                # print int(image_object_map[img].split('D')[1])
                break
            if img not in fake:
                fake[img] = {}
            fake[img][obj] = children
            x1 = [loc[img][closest][0]] + [loc[img][closest][11]] + loc[img][closest][14:21] + loc[img][closest][1:11] + loc[img][closest][12:14]
            y1 = [loc[img][closest][21]] + [loc[img][closest][32]] + loc[img][closest][35:] + loc[img][closest][22:32] + loc[img][closest][33:35]
            for dead_line in dead_loc[img][obj]:
                if fake[img][obj] < 1:
                        break
                dead_line_seg = intersection.line_segment(dead_line[:2], dead_line[-1], length, 8)
                # NOTE: 88 & 8 are the parameters in the CP pipeline from IDW
                x2 = dead_line_seg[0:2]
                y2 = dead_line_seg[2:]
                for dummy_x in range(len(x1)-1):
                    if fake[img][obj] < 1:
                        break
                    inter_point = intersection.intersection(x1[dummy_x:dummy_x+2], y1[dummy_x:dummy_x+2], x2, y2)
                    if inter_point and intersection.dist_pnt_pnt(\
                        inter_point[0], inter_point[1], dead_line[0], \
                        dead_line[1]) > 22:
                    # float(length)*float(length)/100 >
                        fake[img][obj] -= 1
        return fake

    image_count = []
    well_count = {}
    well_count_seq = {}
    well_list = []
    locxy = {}
    judge_fake_list = []

    with open(filename) as object_f:
        for line in object_f:
            fields = line.split(',')
            # location_list = [image_num, Children_DeadWorms_Count, \
            # Neighbors_NumberOfNeighbors_Adjacent, \
            # Neighbors_FirstClosestObjectNumber_Adjacent, \
            # Worm_ControlPointX_1, ObjectNumber]
            if int(fields[location_list[0]]) not in locxy:
                locxy[int(fields[location_list[0]])] = {}
            locxy[int(fields[location_list[0]])]\
            [int(fields[location_list[5]])] = \
            [float(dummy_x) for dummy_x in fields[location_list[4]:-1]]
            if fields[location_list[1]] == '0':
                try:
                    image_count[int(fields[location_list[0]]) -1] += 1
                except IndexError:
                    image_count.append(1)
            elif neighbor_flag and fields[location_list[2]] != '0.0':
                # means the dead worm has neighbour(s), might be fake
                # print fields[location_list[2]]
                judge_fake_list.append((fields[location_list[0]], \
                    fields[location_list[5]], fields[location_list[1]],\
                    fields[location_list[3]]))
                # give a question list: image, object_num, \
                # children_num, closest_num
    if neighbor_flag:
        add_dict = judge_fake(locxy, judge_fake_list, image_object_map, split_day)
        for dummy_k in add_dict:
            for dummy_x in add_dict[dummy_k]:
                if add_dict[dummy_k][dummy_x] == 0:
                    image_count[dummy_k-1] += 1

    for dummy_k, worm_count in enumerate(image_count):
        try:
            well_count[image_object_map[dummy_k + 1].split('_')[0]].\
            append(worm_count)
        except KeyError:
            well_count[image_object_map[dummy_k + 1].split('_')[0]] = \
            [worm_count]

    for each in well_count:
        well, day = [dummy_i for dummy_i in each.split('D')]
        day = int(day.split('_')[0])
        well = int(well)
        if well not in well_count_seq:
            well_count_seq[well] = [0] * len(daylist)
        if int(day) < split_day:
            if before_method == 'max':
                well_count_seq[well][daylist.index(day)] = \
                max(well_count[each])
            elif before_method == 'median':
                well_count_seq[well][daylist.index(day)] = \
                sorted(well_count[each])[1]
            elif before_method == 'mean':
                well_count_seq[well][daylist.index(day)] = \
                sum(well_count[each])*1.0/len(well_count[each])
            else:
                raise Exception("unsupported method")
        else:
            well_count_seq[well][daylist.index(day)] = \
            min(well_count[each])
        # max : max(well_count[each])
        # median : sorted(well_count[each])[1]
        # mean : sum(well_count[each])*1.0/len(well_count[each])
        # min: min(well_count[each])
    for key in sorted(well_count_seq):
        well_list.append(well_count_seq[key])
    return well_list, locxy


def manual(filename):
    """
    give the manual result
    """
    # manual_count = [80, 78, 57, 79, 75, 58, 73, 60, 53, 74, 79, 59, \
    # 73, 79, 58, 68, 67, 61, 67, 61, 54, 64, 67, 53, 60, 70, 52, \
    # 66, 78, 46, 58, 60, 52, 49, 26, 58, 33, 31, 38, 26, 20, 37, \
    # 18, 9, 25, 13, 11, 20, 8, 10, 21, 7, 9, 19, 3, 0, 10]
    # manual_day = [8, 10, 14, 16, 18, 22, 24, 26, 28, \
    # 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
    # print len(manual_day)
    # manual_count_per_treatment = []
    # for dummy_i in range(3):
    #     manual_count_per_treatment.append(manual_count[dummy_i::3])
    # return manual_count_per_treatment, manual_day

    import xlrd

    xls = xlrd.open_workbook(filename)
    xls_names = xls.sheet_names()
    xls_names = [int(dummy_x.split('D')[-1]) for dummy_x in xls_names]
    manual_result = {}
    for i in range(0, len(xls_names)):
        table = xls.sheets()[i]
        for j in range(31, 49):
            for k in range(37, 45):
                if xls_names[i] not in manual_result:
                    manual_result[xls_names[i]] = []
                if table.cell(j, k).value == '':
                    tmp_value = 0
                else:
                    tmp_value = int(table.cell(j, k).value)
                manual_result[xls_names[i]].append(tmp_value)

    # 在指定的行上将数字逆序,因为显微镜的结果是S型的.
    for key in manual_result:
        for dummy_i in (0, 48, 96):
            for dummy_k in (0, 8, 16):
                manual_result[key][dummy_i+dummy_k:dummy_i+dummy_k+8] = \
                reversed(manual_result[key][dummy_i+dummy_k:dummy_i+dummy_k+8])
    return manual_result

def manual_treatment_count(manual_result, start_well, day):
    """
    get the manual result from the xls.file.
    """
    manual_treatment = []
    for dummy_i in range(len(manual_result[day[0]])/8):
        tmp_list = []
        for dummy_day in day:
            tmp_list.append(\
                sum(manual_result[dummy_day][dummy_i*8:(dummy_i+1)*8]))
        manual_treatment.append(tmp_list)
    # print manual_treatment, len(manual_treatment)
    return manual_treatment[(start_well-217)/24:(start_well-217)/24+3]

def compare_manual_with_idw(day, image_live, manual_count, start_well_ini, start_well, out_file):
    """
    compare manual result with IDW result.
    """
    # idw_count = copy.deepcopy(image_live)
    # for child_list in idw_count:
    #     del child_list[day.index(12)]
    # day_here = copy.deepcopy(day)
    # del day_here[2]
    # with open("manual_well_count.txt") as count_f:
    #     print 'day', 'well', 'manule', 'IDW', 'diff'
    #     line_number = -1
    #     diff_total = 0
    #     total = 0
    #     for line in count_f:
    #         line_number += 1
    #         fields = line.strip().split()
    #         for dummy_k, ele in enumerate(fields):
    #             ele = int(ele)
    #             correspoding = idw_count[8 * (line_number % 3) + dummy_k]\
    #             [line_number / 3]
    #             diff_total += abs(ele - correspoding)
    #             total += max(ele, correspoding)
    #             if abs(ele - correspoding) != 0:
    #                 print day_here[line_number / 3], \
    #                 193 + 8 * (line_number % 3) + dummy_k, \
    #                 ele, correspoding, ele - correspoding
    diff_total = 0
    total = 0
    out = open(out_file+'.txt', 'w')
    print >>out, "day well manual IDW diff"
    for dummy_i, per_well_count in enumerate(image_live):
        if dummy_i%8 == 0 and dummy_i != 0:
            print >>out, start_well+dummy_i, diff_total, \
            total, float(diff_total)/ total
            diff_total = 0
            total = 0
        for dummy_j, per_day in enumerate(per_well_count):
            # print day[dummy_j], start_well - start_well_ini+ dummy_i
            if per_day == None:
                continue
            man = \
            manual_count[day[dummy_j]][start_well - start_well_ini+ dummy_i]
            total += max(man, per_day)
            if man != per_day:
                diff_total += abs(man - per_day)
                print >>out, day[dummy_j], \
                start_well+dummy_i, man, per_day, man- per_day
    print >>out, start_well+dummy_i, diff_total, total, float(diff_total)/ total
    out.close()
    return diff_total, total

def smooth(counts, day, split_day):
    '''
    smooth the line for the living worms count
    '''
    bound = day.index(split_day)
    newcounts = []
    for count in counts:
        newcount = [count[0]]
        # before day34, save the larger count; after day34, save smaller
        for dummy_k in range(1, len(count)):
            if dummy_k < bound:
                if count[dummy_k] > count[dummy_k - 1]:
                    for dummy_i, each_newcount in enumerate(newcount[::-1]):
                        if each_newcount < count[dummy_k]:
                            # print dummy_i, newcount, count[dummy_k]
                            newcount[len(newcount) - 1 - dummy_i] = \
                            count[dummy_k]
                        else:
                            break
            else:
                if count[dummy_k] > newcount[-1]:
                    newcount.append(newcount[-1])
                    continue
            newcount.append(count[dummy_k])
        # make the line looks natural
        newcount_dict = {}
        for dummy_k in newcount:
            if dummy_k not in newcount_dict:
                newcount_dict[dummy_k] = 1
            else:
                newcount_dict[dummy_k] += 1
        order = sorted(newcount_dict.keys(), reverse=True)
        for eid, ele in enumerate(order):
            if newcount_dict[ele] > 2 and eid != 0 and eid != len(order)-1:
                step = int(round((order[eid-1]-order[eid+1])*1.0/newcount_dict[ele]))
                if step == 0:
                    step = 1
                tmp_list = range(order[eid+1]+1, order[eid-1], step)
                tmp_list.reverse()
                order[eid] = tmp_list[-1]
                if len(tmp_list) < newcount_dict[ele]:
                    tmp_list = tmp_list + [tmp_list[-1] for dummy_k in range(newcount_dict[ele] - len(tmp_list))]
                elif len(tmp_list) > newcount_dict[ele]:
                    tmp_list = tmp_list[:newcount_dict[ele]]
                assert len(tmp_list) == newcount_dict[ele]
                # except AssertionError:
                #     print tmp_list, newcount_dict[ele], len(tmp_list)
                newcount[newcount.index(ele):\
                newcount.index(ele)+newcount_dict[ele]] = tmp_list
        newcounts.append(newcount)
    return newcounts

def log_rank_test(days, counts, name, treatments):
    '''
    use log_rank_test module to generte result.
    '''
    import data_transfer
    count = copy.deepcopy(counts)
    day = copy.deepcopy(days)
    data = [day]
    [data.append(each_list) for each_list in count]
    dummy_i = -1
    for ele in zip(['day', treatments[0], treatments[1], treatments[2]], data):
        dummy_i += 1
        data[dummy_i].insert(0, ele[0])
    data_transfer.pipe(['dead'], [data], dirname='../', n=name)
    return None


def main(folder, filename, treatments_names):
    """
    main logic
    """
    # image file processing
    # run1: image: "../0813/217_240/SQL_1_1440_Image.CSV"
    image_file = "../0813/run1/%s/SQL_1_%d_Image.CSV" %(folder, filename)
    image_dict, image_total, image_object_map = invalid_dict(image_file, \
        (38, 39, 42, 6, 0, 35, 41))
    # print image_object_map
        # location_list = [Image_Metadata_ImageQCFlag integer, \
        # Image_Metadata_ObjectAreaQCFlag integer, Image_Metadata_Well TEXT, \
        # Image_Count_NonOverlappingWorms integer, ImageNumber\
        # INTEGER, Image_Metadata_Date TEXT,]
    # for track 0712 text: [37, 38, 41, 5, 0, 34]
    # for IDW 0723: [38, 39, 42, 6, 0, 35]
    # for current data: 265 images is not available
    # approximately 35% of all the images
    # day = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, \
    # 30, 32, 34, 36, 38, 40, 42, 44, 46, 48] # this is for plate2 run1
    day = range(8, 50, 2)
    del day[2]
    start_well_ini = 217
    start_well = int(folder.split('_')[0])
    print start_well
    # 0310plate1 11 days [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    # manual_count, manual_day = manual()
    manual_result = manual('../manual_result/20140310 384 plate 2 edited.xls')
    manual_day = day
    manual_count = manual_treatment_count(manual_result, start_well, day)
    # print manual_result


    # =========this is for the third strategy: Identify dead worms=========
    object_file = "../0813/run1/%s/SQL_1_%d_NonOverlappingWorms.CSV" \
    %(folder, filename)
    del image_total # image total count is not used in this approach
    split_day = 34
    image_live, locxy = read_idw_object_csv(object_file, image_object_map, \
        day, (0, 2, 8, 7, 51, 1), 'max', split_day+1, False, \
        "")
    # print image_live
        # location_list = [image_num, Children_DeadWorms_Count, \
        # Neighbors_NumberOfNeighbors_Adjacent, \
        # Neighbors_FirstClosestObjectNumber_Adjacent, \
        # Worm_ControlPointX_1, ObjectNumber]
    # "../0310plate2_0801_neighbor/SQL_1_1385_NonOverlappingWorms.CSV"
    # (0, 2, 8, 7, 31, 1), 'max', split_day+1, True, \
    #    "../0310plate2_0801_neighbor/SQL_1_1385_DeadWorms.CSV"
    # 0722 IDW [0,3]
    # 0723 IDW [0,2]
    # 0723 IDW (0, 7)

    # use subtract method:
    image_live_subtract = subtract_count(locxy, image_object_map, folder)
    combine_image_live = combine_subtract_and_max(image_live_subtract, \
        image_live, day, split_day)

    # mask the count per image:
    image_dict = sequence(image_dict)
    combine_image_live = merge_flags_and_counts(image_dict, combine_image_live)
    # print combine_image_live
    # compare_manual_with_idw(day, image_live, \
    #     manual_result, start_well_ini, start_well, \
    #     'IDW_%d_%d_%s_origin' %(start_well, split_day, 'max_subtract_mask'))
    # print image_live
    total = 0
    count = 0
    for dummy_i in xrange(len(combine_image_live)):
        for dummy_k in xrange(len(combine_image_live[dummy_i])):
            total += 1
            if combine_image_live[dummy_i][dummy_k] == None:
                count += 1
                combine_image_live[dummy_i][dummy_k] = \
                manual_result[day[dummy_k]][start_well-start_well_ini+dummy_i]
    print "mask:", count, total, float(count)/total
    # print combine_image_live

    # # this is for the 193 and 194 is not available in 0310plate2 dataset
    # for dummy_i in range(2):
    #     image_live.insert(0, [0]*len(day))
    # # end here

    # # comparison between each well
    # for dummy_i, dummy_j in zip([image_live, image_live_subtract, \
    #     combine_image_live], ('max', 'subtract', 'combine')):
    #     compare_manual_with_idw(day, dummy_i, \
    #     manual_result, start_well_ini, start_well, \
    #     'IDW_%d_%d_%s_origin' %(start_well, split_day, dummy_j))

    # plot original data
    # treatment_count = combine_eight_wells(image_live)
    treatment_count_combine = combine_eight_wells(combine_image_live)
    # treatment_count2 = combine_eight_wells(image_live_subtract)
    plot_data('IDW_%d_%d_mask_combine_origin' %(start_well, split_day), \
        treatment_count_combine, day, 'mask_combine',\
        True, manual_count, manual_day, 'manual')
    # plot_data('IDW_%d_%d_max_subtract_origin' %(start_well, split_day), \
    #     treatment_count, day, 'max',\
    #     True, manual_count, manual_day, 'manual', \
    #     True, treatment_count2, day, 'subtract')

    # overall comparison
    # with open("overall_comparison.txt", 'a') as comparison:
    #     print >>comparison, folder,\
    #     'max', treatment_count, '\n', \
    #     'subtract', treatment_count2, '\n', \
    #     'combine', treatment_count_combine

    # # plot smooth data
    # treatment_count = smooth(treatment_count, day, split_day)
    # treatment_count2 = smooth(treatment_count2, day, split_day)
    manual_count = smooth(manual_count, manual_day, split_day)
    treatment_count_combine = smooth(treatment_count_combine, day, split_day)
    plot_data('IDW_%d_%d_mask_combine_smooth' %(start_well, split_day), \
        treatment_count_combine, day, 'mask_combine',\
        True, manual_count, manual_day, 'manual')
    # plot_data('IDW_%d_%d_max_subtract_smooth' %(start_well, split_day), \
    #     treatment_count, day, 'max',\
    #     True, manual_count, manual_day, 'manual', \
    #     True, treatment_count2, day, 'subtract')


    # # log_rank_test data prepare using smooth data, generate the files for R
    log_rank_test(day, treatment_count_combine, '0817_logrank_%s' \
        % 'mask_combine', treatments_names)
    # for dummy_i, dummy_j in zip([manual_count, treatment_count, \
    #     treatment_count2, treatment_count_combine], \
    #     ('manual', 'max', 'subtract', 'combine')):
    #     log_rank_test(day, dummy_i, '0817_logrank_%s' % dummy_j, \
    #         treatments_names)



if __name__ == '__main__':
    FILELIST = (\
('217_240', 1440, \
('D(+)-Galactose-BD', 'D-(+)-Glucose-BD', 'D(+)-Mannose-BD')), \
('241_264', 1440, \
('D-Aspartate-BD', 'D-erythro-Dihydrosphingosine-BD', 'D-Gluconic acid-BD',)),\
('265_288', 1439, \
('D-Glucuronate-BD', 'D-Glucuronolactone-BD', 'D-Glutamate-BD',)), \
('289_312', 1440, \
('Urocanate-BD', 'DL-3-Hydroxy-3-methylglutaryl-BD', 'Dopamine-BD',)), \
('313_336', 1440, ('D-Ornithine', 'D-Sorbitol-BD', 'Ethanolamine-BD',)), \
('337_360', 1439, ('Folate-BD', 'Fumarate-BD', 'DMSO-BD',)),\
)
    for dummy_i in FILELIST:
        main(dummy_i[0], dummy_i[1], dummy_i[2])

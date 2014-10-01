def combine_eight_wells(count_list):
    """
    get the sum value of counts result
    @input
    [<well1>[day1, day2, day3, ..], <well2>[day1, day2, day3, ..]]
    @return
    [[sum_of_eight_well_on_day1, sum_on_day2, ..], ..]
    """
    treatment_all = []
    for index in range(len(count_list)):
        if index % 8 == 7:
            treatment_all.append([sum(ele) for ele in \
                zip(*count_list[index-7:index+1])])
    return treatment_all


def smooth(counts, day, split_day):
    '''
    smooth the line for the living worms count
    @input & return
    [[sum_of_eight_well_on_day1, sum_on_day2, ..], ..]
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


def plot_data(name, data, day, text, \
    compare=False, data2='', day2='', text2='',\
    compare2=False, data3='', day3='', text3=''):
    """
    plotting data
    """
    import matplotlib.pyplot as plt
    count = -1
    plt.figure()
    for key in data:
        count += 1
        # plt.subplot(1, 3, count+1)
        plt.plot(day, key, label=text)
        if compare:
            plt.plot(day2, data2[count], label=text2)
            plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, \
                ncol=2, mode="expand", borderaxespad=0.)
        # if compare2:
        #     plt.plot(day3, data3[count], label=text3)
        #     plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, \
        #         ncol=3, mode="expand", borderaxespad=0.)
        plt.axis([day[0], day[-1], 0, 90])
        plt.savefig('%s_%d' %(name, count))
        plt.clf()
    # plt.savefig('%s' %(name))
    # plt.clf()


def log_rank_test(days, counts, name, treatments):
    '''
    use log_rank_test module to generte result.
    '''
    import data_transfer
    import copy
    count = copy.deepcopy(counts)
    day = copy.deepcopy(days)
    data = [day]
    [data.append(each_list) for each_list in count]
    dummy_i = -1
    for ele in zip(treatments, data):
        dummy_i += 1
        data[dummy_i].insert(0, ele[0])
    data_transfer.pipe(['dead'], [data], dirname='./', n=name)
    return None

#get_nevts_inIx(inChannel)
"""
  Script to get number of events in each file for given Irequest 
"""

import re, string
import sys, os, subprocess
import time 
from string import Template
from time import gmtime, strftime

#ireq="I" + str($idChannel)
#iFile=$ixnfile
#index=$ind

def get_nevts_inIx(inChannel):

    #    inChannel = "106571"
    #ireq = "I106485"  qqH        total_number_of_events=439608   number_of_files=18
    #ireq = "I106486"  qqH        total_number_of_events=268672   number_of_files=11
    #ireq = "I106607"  Z_h        total_number_of_events=1747094  number_of_files=50
    #ireq = "I106608"  Z_h        total_number_of_events=1841069  number_of_files=50
    #ireq = "I106551"  WW_h       total_number_of_events=1074480  number_of_files=50 
    #ireq = "I106552"  WW_h       total_number_of_events=136357   number_of_files=7 
    #ireq = "I106563" sW_sl       total_number_of_events=119683   number_of_files=4
    #ireq = "I106564" sW_sl       total_number_of_events=1927011  number_of_files=50 
    #ireq = "I106565" sW_sl       total_number_of_events=119289   number_of_files=4
    #ireq = "I106566" sW_sl       total_number_of_events=85616    number_of_files=3
    #ireq = "I106559" sZe_sl      total_number_of_events=259756   number_of_files=6
    #ireq = "I106560" sZe_sl      total_number_of_events=459055   number_of_files=12
    #ireq = "I106561" sZe_sl      total_number_of_events=258958   number_of_files=6
    #ireq = "I106562" sZe_sl      total_number_of_events=316516   number_of_files=8
    #ireq = "I106571" sZnu_sl     total_number_of_events=456800   number_of_files=12
    #ireq = "I106572" sZnu_sl     total_number_of_events=130789   number_of_files=4
    #ireq = "I106573"  ZZ_h       total_number_of_events=1005427  number_of_files=50
    #ireq = "I106574"  ZZ_h       total_number_of_events=604971   number_of_files=30
    #ireq = "I106575"  ZZ_sl      total_number_of_events=1422143  number_of_files=40
    #ireq = "I106576"  ZZ_sl      total_number_of_events=713526   number_of_files=20
    #ireq = "I106577"  WW_sl      total_number_of_events=1919149  number_of_files=50
    #ireq = "I106578"  WW_sl      total_number_of_events=172733   number_of_files=5
    if inChannel == '106485' :
         nEvtsArray = [0,24418,24413,24369,24423,24411,24440,24370,24400,24424,24424, \
                         24391,24494,24422,24438,24446,24437,24448,24440]
    elif inChannel == '106486' :
         nEvtsArray = [0,24405,24395,24434,24405,24405,24401,24422,24466,24518,24387, \
                         24434]
    elif inChannel == '106607' :
         nEvtsArray = [0,35015,35037,34904,34937,34837,34854,34943,34849,34964,34902, \
                         34965,34960,34914,34998,34937,35019,34923,34979,34871,34875, \
                         34903,34993,34843,34960,34939,34887,34963,35001,35000,34916, \
                         34997,34913,35066,35003,34897,35062,34927,35033,34974,34935, \
                         34927,34977,34858,34998,34790,35018,34979,34828,34888,34936]
    elif inChannel == '106608' :
         nEvtsArray = [0,36926,36839,36741,36934,36710,36908,36772,36873,36895,36941, \
                         36773,36779,36752,36739,36855,36803,36715,36843,36852,36810, \
                         36819,36767,36853,36841,36835,36841,36846,36854,36813,36844, \
                         36786,36777,36809,36876,36890,36814,36694,36782,36813,36748, \
                         36885,36801,36761,36762,36777,36866,36945,36827,36943,36740]
    elif inChannel == '106551' :
         nEvtsArray = [0,21479,21509,21474,21492,21465,21540,21500,21474,21471,21516, \
                         21494,21549,21519,21474,21487,21503,21511,21466,21444,21502, \
                         21539,21467,21463,21480,21485,21460,21460,21473,21494,21442, \
                         21472,21516,21552,21461,21478,21501,21500,21539,21525,21492, \
                         21506,21423,21492,21457,21422,21519,21492,21502,21501,21498]
    elif inChannel == '106552' :
         nEvtsArray = [0,21576,21583,21541,21576,21597,21505,6979]
    elif inChannel == '106563' :
         nEvtsArray = [0,38993,38961,38945,2784 ]
    elif inChannel == '106564' :
         nEvtsArray = [0,38492,38565,38558,38527,38554,38518,38532,38533,38515,38484, \
                         38531,38544,38582,38563,38502,38509,38535,38534,38449,38556, \
                         38538,38589,38538,38529,38487,38579,38493,38464,38575,38510, \
                         38502,38615,38579,38518,38515,38630,38560,38572,38591,38558, \
                         38529,38520,38582,38553,38553,38470,38575,38591,38603,38510]
    elif inChannel == '106565' :
         nEvtsArray = [0,38922,38858,38968,2541 ]
    elif inChannel == '106566' :
         nEvtsArray = [0,38671,38678,8267 ]
    elif inChannel == '106559' :
         nEvtsArray = [0,44871,44898,44838,44827,44944,35378]
    elif inChannel == '106560' :
         nEvtsArray = [0,39661,39756,39761,39768,39781,39785,39758,39807,39871,39794, \
                         39868,21445]
    elif inChannel == '106561' :
         nEvtsArray = [0,44741,44877,44802,44895,44839,34804]
    elif inChannel == '106562' :
         nEvtsArray = [0,42188,42252,42258,42254,42283,42237,42174,20870]
    elif inChannel == '106571' :
         nEvtsArray = [0,38279,38238,38152,38195,38218,38153,38196,38176,38226,38257, \
                         38129,36581]
    elif inChannel == '106572' :
         nEvtsArray = [0,38424,38505,38441,15419]
    elif inChannel == '106573' :
         nEvtsArray = [0,20071,20094,20103,20081,20082,20136,20089,20125,20086,20162, \
                         20106,20081,20054,20121,20106,20102,20048,20118,20120,20076, \
                         20114,20132,20098,20161,20081,20111,20095,20118,20142,20122, \
                         20106,20125,20135,20083,20114,20115,20140,20075,20118,20077, \
                         20138,20149,20058,20104,20116,20125,20168,20082,20134,20130]
    elif inChannel == '106574' :
         nEvtsArray = [0,20468,20450,20541,20452,20488,20453,20476,20459,20470,20455, \
                         20430,20448,20454,20432,20439,20443,20465,20463,20451,20435, \
                         20497,20516,20439,20509,20445,20413,20470,20517,20440,11553]
    elif inChannel == '106575' :
         nEvtsArray = [0,36280,36248,36342,36298,36222,36253,36271,36196,36355,36348, \
                         36329,36363,36366,36266,36401,36359,36311,36312,36272,36285, \
                         36274,36298,36340,36292,36324,36317,36305,36304,36256,36393, \
                         36291,36333,36332,36302,36257,36330,36334,36388,36376,6020]
    elif inChannel == '106576' :
         nEvtsArray = [0,36876,36969,36863,36930,36927,36948,36964,36984,36919,36887, \
                         36926,36963,36937,36990,36834,36963,36920,36943,36904,11879]
    elif inChannel == '106577' :
         nEvtsArray = [0,38348,38473,38404,38374,38392,38405,38406,38441,38391,38445, \
                         38411,38410,38377,38379,38327,38438,38372,38332,38368,38379, \
                         38402,38405,38292,38372,38292,38320,38506,38371,38318,38403, \
                         38408,38351,38375,38418,38328,38357,38408,38400,38413,38456, \
                         38328,38383,38253,38380,38380,38408,38365,38385,38397,38403]
    elif inChannel == '106578' :
         nEvtsArray = [0,38501,38559,38456,38500,18717]
    else:
         print "get_nevts_inIx: Wrong Channel Id !!!!" , inChannel
         quit()

    nfiles= len(nEvtsArray)
    print "get_nevts_inIx: nfiles ",nfiles, "inChannel=", inChannel

    return nEvtsArray

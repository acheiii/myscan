# coding=utf-8
# @Author   : zpchcbd HG team
# @blog     : https://www.cnblogs.com/zpchcbd/
# @Time     : 2021-11-23 20:45

# PROXY

HTTP_PROXY = 'http://127.0.0.1:7890'

# SPEED

CONCURRENCY = 500

# REGEXP

REGEXP_TITLE_STRING = r'<title>(?P<result>[^<]+)</title>'

REGEXP_PARAM_STRING = r''

# SQL Injection

SQL_COMMON_FALG_SIGN = '@@'

SQL_HTML_FLAG_SIGN = '.htm'

SQL_SHTML_FLAG_SIGN = '.shtm'

ERROR_PAYLOAD_XML = 'dict/payload/errors.xml'

BOOL_PAYLOAD_XML = 'dict/payload/bool.xml'

HIGH_RADIO = -1

LOW_RADIO = 2

# PORT

TOP_1000_BANNER_PORT = [80, 8983, 161, 23, 9001, 8069, 10050, 10051, 1080, 15672, 443, 8161, 5335, 5336, 2381, 4848,
                        489, 7001, 110, 9300, 4567, 50000,
                        3389, 3390, 33890, 3388,  # top rdp
                        22, 2222, 22222, 2022,  # top ssh
                        15000, 6379, 8089, 20880, 8000,  # top redis
                        21, 2121,  # top ftp
                        2181,  # top zookeeper
                        5984, 2375, 16992, 16993, 33899, 179, 1026, 2000, 8443, 445, 139, 1099, 3312, 3690, 4440,
                        143, 53, 135, 8080, 22, 5901, 5432, 27017, 7809, 9200, 50070, 50075,
                        3306, 3307, 3310, 3333, 10000,  # top mysql
                        1433, 1434,  # top mssql
                        11211, 1723, 111, 995, 993, 5900, 1025, 1720, 548, 113, 81, 6001,
                        32768, 554, 26, 49152, 2001, 515, 8008, 49154, 1027, 5666, 646, 5000,
                        5631, 631, 49153, 8081, 2049, 88, 79, 5800, 106, 2121, 1110, 49155, 6000, 513,
                        990, 5357, 49156, 543, 544, 5101, 144, 7, 389, 8009, 9999, 5009, 7070, 5190, 3000,
                        1900, 3986, 13, 1029, 9, 5051, 6646, 49157, 1028, 873, 1755, 2717, 4899, 9100,
                        119, 37, 1000, 3001, 5001, 82, 10010, 1030, 9090, 2107, 1024, 2103, 6004, 1801,
                        5050, 19, 8031, 1041, 255, 1048, 1049, 1053, 1054, 1056, 1064, 3703, 17, 808, 3689,
                        1031, 1044, 1071, 100, 9102, 2869, 4001, 5120, 8010, 9000, 2105, 636, 1038,
                        2601, 1, 7000, 1066, 1069, 625, 311, 280, 254, 4000, 1761, 5003, 2002, 1998, 2005,
                        1032, 1050, 6112, 1521, 2161, 6002, 2401, 902, 4045, 787, 7937, 1058, 2383, 1033,
                        1040, 1059, 5555, 1494, 3, 593, 2301, 3268, 7938, 1022, 1234, 1035, 1036, 1037,
                        1074, 8002, 464, 497, 1935, 2003, 6666, 6543, 24, 1352, 3269, 1111, 407, 500,
                        20, 2006, 1034, 1218, 3260, 4444, 264, 33, 2004, 1042, 42510, 999, 3052, 1023,
                        222, 1068, 888, 7100, 1717, 992, 2008, 2007, 8082, 512, 1043, 2009, 5801, 1700,
                        7019, 50001, 4662, 2065, 42, 2602, 9535, 5100, 2604, 4002, 5002, 1047, 1051, 1052,
                        1055, 1060, 1062, 1311, 3283, 4443, 5225, 5226, 6059, 6789, 8651, 8652, 8701, 9415,
                        9593, 9594, 9595, 20828, 23502, 32769, 33354, 35500, 52869, 55555, 55600,
                        64623, 64680, 65000, 65389, 1067, 13782, 366, 5902, 9050, 85, 1002, 5500, 1863, 1864,
                        5431, 8085, 10243, 45100, 49999, 51103, 49, 90, 6667, 1503, 6881, 27000, 340, 1500, 8021,
                        5566, 8088, 8899, 9071, 5102, 6005, 9101, 163, 5679, 146, 648, 1666, 83, 3476, 5004,
                        5214, 8001, 8083, 8084, 9207, 14238, 30, 912, 12345, 2030, 2605, 6, 541, 4, 1248, 3005,
                        8007,
                        306, 880, 2500, 1086, 1088, 2525, 4242, 8291, 9009, 52822, 900, 6101, 2809, 7200, 211, 800,
                        987, 1083, 12000, 705, 711, 20005, 6969, 13783, 1045, 1046, 1061, 1063, 1070, 1072, 1073,
                        1075, 1077, 1078, 1079, 1081, 1082, 1085, 1093, 1094, 1096, 1098, 1100, 1104, 1106,
                        1107, 1108, 1148, 1169, 1272, 1310, 1687, 1718, 1783, 1840, 2100, 2119, 2135, 2144, 2160,
                        2190, 2260, 2399, 2492, 2607, 2718, 2811, 2875, 3017, 3031, 3071, 3211, 3300, 3301,
                        3323, 3325, 3351, 3404, 3551, 3580, 3659, 3766, 3784, 3801, 3827, 3998, 4003, 4126, 4129,
                        4449, 5222, 5269, 5633, 5718, 5810, 5825, 5877, 5910, 5911, 5925, 5959, 5960, 5961, 5962,
                        5987, 5988, 5989, 6123, 6129, 6156, 6389, 6580, 6901, 7106, 7625, 7777, 7778, 7911, 8086,
                        8181, 8222, 8333, 8400, 8402, 8600, 8649, 8873, 8994, 9002, 9011, 9080, 9220, 9290, 9485,
                        9500, 9502, 9503, 9618, 9900, 9968, 10002, 10012, 10024, 10025, 10566, 10616, 10617, 10621,
                        10626, 10628, 10629, 11110, 13456, 14442, 15002, 15003, 15660, 16001, 16016, 16018, 17988,
                        19101, 19801, 19842, 20000, 20031, 20221, 20222, 21571, 22939, 24800, 25734, 27715, 28201,
                        30000, 30718, 31038, 32781, 32782, 34571, 34572, 34573, 40193, 48080, 49158, 49159,
                        49160, 50003, 50006, 50800, 57294, 58080, 60020, 63331, 65129, 691, 212, 1001, 1999, 2020,
                        2998, 6003, 7002, 50002, 32, 2033, 3372, 99, 425, 749, 5903, 43, 458, 5405, 6106, 6502,
                        7007,
                        13722, 1087, 1089, 1124, 1152, 1183, 1186, 1247, 1296, 1334, 1580, 1782, 2126, 2179, 2191,
                        2251,
                        2522, 3011, 3030, 3077, 3261, 3493, 3546, 3737, 3828, 3871, 3880, 3918, 3995, 4006, 4111,
                        4446,
                        5054, 5200, 5280, 5298, 5822, 5859, 5904, 5915, 5922, 5963, 7103, 7402, 7435, 7443, 7512,
                        8011,
                        8090, 8100, 8180, 8254, 8500, 8654, 9091, 9110, 9666, 9877, 9943, 9944, 9998, 10004, 10778,
                        15742,
                        16012, 18988, 19283, 19315, 19780, 24444, 27352, 27353, 27355, 32784, 49163, 49165, 49175,
                        50389, 50636, 51493, 55055, 56738, 61532, 61900, 62078, 1021, 9040, 666, 700, 84, 545,
                        1112, 1524, 2040, 4321, 5802, 38292, 49400, 1084, 1600, 2048, 2111, 3006, 6547, 6699, 9111,
                        16080, 555, 667, 720, 801, 1443, 1533, 2106, 5560, 6007, 1090, 1091, 1114, 1117, 1119,
                        1122, 1131,
                        1138,
                        1151, 1175, 1199, 1201, 1271, 1862, 2323, 2393, 2394, 2608, 2725, 2909, 3003, 3168, 3221,
                        3322,
                        3324, 3517, 3527, 3800, 3809, 3814, 3826, 3869, 3878, 3889, 3905, 3914, 3920, 3945,
                        3971,
                        4004, 4005, 4279, 4445, 4550, 4567, 4900, 5033, 5080, 5087, 5221, 5440, 5544, 5678,
                        5730,
                        5811, 5815, 5850, 5862, 5906, 5907, 5950, 5952, 6025, 6510, 6565, 6567, 6689, 6692, 6779,
                        6792,
                        6839, 7025, 7496, 7676, 7800, 7920, 7921, 7999, 8022, 8042, 8045, 8093, 8099, 8200, 8290,
                        8292,
                        8300, 8383, 9003, 9081, 9099, 9418, 9575, 9878, 9898, 9917, 10003, 10180, 10215,
                        11111,
                        12174, 12265, 14441, 15004, 16000, 16113, 17877, 18040, 18101, 19350, 25735, 26214, 27356,
                        30951, 32783, 32785, 40911, 41511, 44176, 44501, 49161, 49167, 49176, 50300, 50500, 52673,
                        52848, 54045, 54328, 55056, 56737, 57797, 60443, 70, 417, 714, 722, 777, 981, 1009,
                        4224,
                        4998, 6346, 301, 524, 668, 765, 2041, 5999, 10082, 259, 1007, 1417, 1984, 2038, 2068,
                        4343,
                        6009, 7004, 44443, 109, 687, 726, 911, 1461, 2035, 4125, 6006, 7201, 9103, 125, 481, 683,
                        903,
                        1011, 1455, 2013, 2043, 2047, 6668, 6669, 256, 406, 843, 2042, 2045, 5998, 9929, 31337,
                        44442,
                        1092, 1095, 1102, 1105, 1113, 1121, 1123, 1126, 1130, 1132, 1137, 1141, 1145, 1147, 1149,
                        1154,
                        1164, 1165, 1166, 1174, 1185, 1187, 1192, 1198, 1213, 1216, 1217, 1233, 1236, 1244, 1259,
                        1277,
                        1287, 1300, 1301, 1309, 1322, 1328, 1556, 1641, 1688, 1719, 1721, 1805, 1812, 1839, 1875,
                        1914,
                        1971, 1972, 1974, 2099, 2170, 2196, 2200, 2288, 2366, 2382, 2557, 2800, 2910, 2920, 2968,
                        3007,
                        3013, 3050, 3119, 3304, 3376, 3400, 3410, 3514, 3684, 3697, 3700, 3824, 3846, 3848,
                        3859,
                        3863, 3870, 3872, 3888, 3907, 3916, 3931, 3941, 3957, 3963, 3968, 3969, 3972, 3990, 3993,
                        3994,
                        4009, 4040, 4080, 4096, 4143, 4147, 4200, 4252, 4430, 4555, 4600, 4658, 4875, 4949, 5040,
                        5063,
                        5074, 5151, 5212, 5223, 5242, 5279, 5339, 5353, 5501, 5807, 5812, 5818, 5823, 5868, 5869,
                        5899,
                        5905, 5909, 5914, 5918, 5938, 5940, 5968, 5981, 6051, 6060, 6068, 6203, 6247, 6500, 6504,
                        6520,
                        6550, 6600]

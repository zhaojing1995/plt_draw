#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:data.py
@TIME:2019/9/26 15:40
@DES:
'''

gradually_5_15={
    "title":"gradually_5_15",
    "length": 9,
    "mAP" :       [28.2, 30.5, 36.7, 40.0, 47.0, 51.5, 52.7, 54.0,54.1],
    "top1" :      [33.3, 34.8, 43.2, 46.3, 54.4, 59.8, 60.3, 62.8,63.4],
    "top5" :      [50.0, 52.4, 58.4, 62.5, 70.8, 75.8, 76.5, 78.2,78.2],
    "top10" :     [56.0, 59.8, 63.7, 68.9, 76.1, 80.1, 82.5, 82.2,82.8],
    "top20" :     [63.4, 65.7, 69.7, 74.8, 80.8, 85.6, 87.0, 85.9,86.8],
    "label_pre" : [40.8, 43.5, 48.3, 51.3, 56.6, 59.6, 61.6, 62.3,62.7],
    "select_pre" : [94.59, 93.84, 89.95, 86.10, 81.2, 74.48, 65.15, 62.32,62.65],
    "train_pre": [100.0, 99.36, 97.59, 94.96, 91.31, 86.09, 78.72, 74.98, 74.54],
    "select_percent":[0.0, 5.02, 14.19, 26.04, 40.03, 55.96, 73.49, 92.64, 100.0],
    "select_num": [0, 75, 212, 389, 598, 836, 1098, 1384, 1494]
}

gradually_5_13={
    "title":"gradually_5_13",
    "length": 12,
    "mAP" :       [30.2,31.3,35.3,40.8,44.0,49.0,50.3,53.5,54.1,56.0,54.8,55.6],
    "top1" :      [35.9,35.9,40.6,47.3,50.3,57.0,59.4,62.5,62.8,65.4,63.4,64.5],
    "top5" :      [52.1,54.7,56.7,63.8,67.7,72.2,74.1,77.8,77.5,79.1,78.2,78.5],
    "top10" :     [59.4,60.4,63.0,69.7,72.8,76.5,78.5,81.8,81.5,83.6,83.5,82.3],
    "top20" :     [65.0,66.0,70.4,74.6,77.2,81.6,83.0,84.9,85.8,86.6,86.9,86.5],
    "label_pre" : [42.3,42.7,46.9,53.6,56.3,58.2,61.6,63.3,64.1,64.5,64.7,65.3],
    "select_pre" : [95.59,93.99,95.18,92.04,90.08,87.74,83.46,77.58,71.36,64.56,64.73,65.26],
    "train_pre": [100.0, 99.36, 98.98, 97.53, 96.1, 94.27, 91.29, 87.13, 82.4, 76.97, 76.01, 76.32],
    "select_percent":[0.0, 5.02, 12.32, 20.88, 30.32, 40.56, 51.41, 62.78, 74.7, 87.01, 99.8, 100.0],
    "select_num":[0, 75, 184, 312, 453, 606, 768, 938, 1116, 1300, 1491, 1494]
}

gradually_5_10={
    "title":"gradually_5_10",
    "length": 21,
    "p":10,
    "mAP" :        [29.4,30.1,34.0,39.4,40.6,42.2,45.8,47.2,46.9,49.2,51.3,52.1,53.3,56.2,56.4,58.6,56.7,57.1,57.2,56.2,57.6],
    "top1" :       [34.5,34.8,39.7,45.0,47.2,49.4,53.1,54.4,54.7,57.7,59.0,62.0,62.1,66.4,66.4,67.1,65.8,66.8,65.8,65.4,67.2],
    "top5" :       [49.0,52.0,56.7,62.0,63.4,64.5,69.7,71.2,72.4,71.9,76.9,75.8,78.2,79.9,79.2,81.2,78.8,81.1,80.3,80.2,80.5],
    "top10" :      [56.1,60.7,63.1,68.2,69.4,69.9,75.5,75.9,76.8,78.1,80.8,80.6,82.8,83.5,83.5,84.5,82.8,84.6,84.3,84.6,83.8],
    "top20" :      [63.0,66.5,68.8,73.4,76.1,75.5,81.3,81.1,80.5,82.9,83.5,84.0,85.3,87.3,87.7,87.6,87.2,87.9,88.7,87.5,88.2],
    "label_pre" :  [41.8,42.8,45.3,50.1,51.8,54.8,56.0,57.8,57.8,60.0,62.7,62.6,64.7,65.3,66.7,68.1,67.5,67.8,68.2,68.3,68.5],
    "select_pre" : [91.89,91.95,92.86,94.97,96.25,95.09,94.64,93.47,91.34,90.23,88.43,87.50,86.61,84.69,82.05,80.00,77.15,74.18,71.32,68.27,68.54],
    "train_pre": [100.0, 99.1, 98.71, 98.71, 98.8, 98.23, 97.83, 97.14, 96.0, 95.2, 94.0, 93.24, 92.43, 91.1, 89.24, 87.66, 85.56, 83.37, 81.14, 78.75, 78.55],
    "select_percent":[0.0, 5.02, 10.04, 15.06, 20.01, 25.03, 30.05, 35.01, 40.03, 45.05, 50.0, 55.02, 60.04, 65.06, 70.01, 75.03, 80.05, 85.01, 90.03, 95.05, 100.0],
    "select_num":[0, 75, 150, 225, 299, 374, 449, 523, 598, 673, 747, 822, 897, 972, 1046, 1121, 1196, 1270, 1345, 1420, 1494]
}

gradually_5_k15={
    "title":"gradually_5_k15",
    "length": 22,
    "mAP" :       [29.0,28.4,30.8,32.8,34.7,36.5,39.8,42.9,47.3,48.4,49.3,51.2,53.5,53.9,55.8,58.1,56.1,58.2,57.3,56.5,57.2,57.5],
    "top1" :      [35.0,33.2,36.0,38.6,40.7,41.2,46.4,49.6,54.0,57.8,57.8,60.7,63.5,63.8,64.7,67.4,65.2,67.0,66.5,65.2,66.4,67.4],
    "top5" :      [51.4,52.6,51.1,54.3,58.5,58.3,63.7,65.2,70.5,71.1,74.4,74.9,76.6,78.3,79.6,81.2,80.1,81.3,81.1,80.5,80.5,82.3],
    "top10" :     [57.3,58.1,56.7,61.0,63.2,64.2,69.1,70.4,76.2,76.6,79.3,79.2,80.6,81.8,84.2,85.5,85.6,85.8,84.8,83.5,85.6,85.6],
    "top20" :     [62.7,64.7,62.3,67.0,68.4,71.7,74.4,76.1,81.2,82.2,84.0,83.9,84.9,85.9,87.2,88.5,88.6,89.3,88.3,87.0,89.2,88.3],
    "label_pre" : [39.4,41.2,41.9,43.4,47.3,49.7,50.9,54.8,58.6,59.8,60.8,61.9,64.5,66.1,66.8,66.8,67.5,68.1,67.8,68.3,68.3,68.3],
    "select_pre" : [100.0,93.94,95.95,96.15,95.5,95.04,92.53,91.81,90.91,89.77,88.09,85.70,83.87,80.96,77.96,75.17,72.71,70.53,69.15,68.57,68.39,68.34],
    "train_pre": [100.0, 99.86, 99.73, 99.61, 99.28, 98.89, 97.77, 97.12, 96.27, 95.33, 94.06, 92.31, 90.86, 88.7, 86.43, 84.21, 82.25, 80.48, 79.34, 78.75, 78.48, 78.42],
    "select_percent":[0.0, 0.6, 2.28, 5.02, 8.77, 13.45, 18.94, 25.17, 31.93, 39.09, 46.52, 54.02, 61.38, 68.54, 75.3, 81.46, 86.88, 91.57, 95.25, 97.93, 99.53, 100.0],
    "select_num": [0, 9, 34, 75, 131, 201, 283, 376, 477, 584, 695, 807, 917, 1024, 1125, 1217, 1298, 1368, 1423, 1463, 1487, 1494]
}


gradually_11_15={  #ef 1.1  q 1.5
    "title":"gradually_11_15",
    "length": 22,
    "mAP" :       [28.8,29.7,33.2,34.7,33.8,36.3,37.6,39.7,42.5,44.8,46.9,48.6,50.9,52.6,53.9,55.9,57.6,57.5,58.8,57.3,58.0,56.6],
    "top1" :      [33.6,34.9,38.7,39.3,38.9,42.9,43.0,46.0,48.3,51.3,54.0,55.8,59.8,61.5,64.1,65.5,67.0,67.0,67.9,66.4,67.5,65.8],
    "top5" :      [48.7,50.4,55.3,56.0,54.8,58.5,60.4,63.0,64.1,68.2,75.6,72.2,73.6,76.4,77.9,79.9,80.1,79.9,81.2,79.8,79.6,80.1],
    "top10" :     [54.7,56.4,61.3,62.1,61.7,64.7,67.1,67.2,71.8,73.2,75.6,77.6,78.9,80.3,81.9,83.2,84.3,83.5,85.9,84.3,83.9,84.2],
    "top20" :     [61.7,64.2,67.9,68.1,66.4,68.9,73.4,72.6,77.4,78.5,81.1,83.2,82.6,85.2,85.0,85.9,87.6,87.7,89.2,86.5,87.6,87.5],
    "label_pre" : [40.8,40.2,45.6,46.7,43.8,48.5,49.9,50.8,52.6,55.2,57.8,59.4,61.4,63.3,64.1,66.2,65.8,67.1,67.8,68.4,68.4,68.5],
    "select_pre" : [94.12,95.74,97.67,96.21,92.39,91.74,92.79,94.09,92.34,92.69,90.83,90.79,89.88,87.34,85.24,83.56,80.21,76.67,73.2,69.32,68.41,68.47],
    "train_pre":[100.0, 99.86, 99.73, 99.49, 98.68, 98.19, 98.09, 98.11, 97.3, 97.12, 96.07, 95.7, 94.95, 93.35, 91.81, 90.46, 88.08, 85.49, 82.79, 79.75, 78.59, 78.51],
    "select_percent":[0.0, 1.14, 3.15, 5.76, 8.84, 12.32, 16.2, 20.41, 24.9, 29.72, 34.81, 40.16, 45.78, 51.61, 57.63, 63.92, 70.41, 77.11, 84.07, 91.16, 98.39, 100.0],
    "select_num":[0, 17, 47, 86, 132, 184, 242, 305, 372, 444, 520, 600, 684, 771, 861, 955, 1052, 1152, 1256, 1362, 1470, 1494]


}

gradually_55_25={  #ef 0.055  q 2.5
    "title":"gradually_55_25",
    "length": 22,
    "mAP" :       [29.0,27.4,31.2,30.1,29.4,28.9,33.2,32.3,35.0,36.6,39.1,43.5,44.0,46.3,47.6,48.7,51.0,54.7,55.7,56.2,55.8,56.4],
    "top1" :      [34.8,32.3,36.2,35.6,34.9,34.0,37.5,38.3,40.3,42.2,44.3,50.0,49.9,53.7,56.3,56.8,61.5,63.4,64.4,65.8,65.5,65.5],
    "top5" :      [51.0,48.0,53.7,52.0,50.4,48.1,56.8,53.8,56.8,59.8,63.0,67.5,69.7,69.4,71.8,75.1,74.4,77.9,78.5,79.1,78.3,78.5],
    "top10" :     [57.4,54.6,59.7,58.7,56.8,54.6,62.8,61.5,61.7,64.5,68.2,73.4,74.5,74.1,78.1,79.6,78.6,81.9,83.0,83.0,82.5,82.9],
    "top20" :     [65.8,60.5,66.1,65.2,64.2,60.7,67.1,67.1,67.7,70.9,74.4,77.4,78.3,79.8,80.9,83.6,83.3,86.8,87.7,86.0,87.0,86.0],
    "label_pre" : [40.9,38.0,43.6,40.3,39.9,40.2,45.8,43.8,46.2,48.5,51.1,54.6,54.1,56.7,58.2,61.3,61.9,65.7,65.5,66.0,66.0,65.9],
    "select_pre" :[100.0,100.0,100.0,96.30,95.65,98.63,97.2,95.3,95.00,94.23,95.15,94.63,93.21,92.21,89.82,86.34,83.06,80.0,73.24,66.87,66.0,65.93],
    "train_pre" :[100.0, 100.0, 100.0, 99.86, 99.73, 99.87, 99.61, 99.26, 99.06, 98.67, 98.65, 98.26, 97.48, 96.67, 95.25, 93.09, 90.74, 88.35, 83.46, 78.5, 76.98, 76.78],
    "select_percent":[0.0, 0.07, 0.33, 0.87, 1.81, 3.08, 4.89, 7.16, 9.97, 13.39, 17.4, 22.09, 27.44, 33.53, 40.36, 47.99, 56.36, 65.6, 75.64, 86.55, 98.39, 100.0],
    "select_num":[0, 1, 5, 13, 27, 46, 73, 107, 149, 200, 260, 330, 410, 501, 603, 717, 842, 980, 1130, 1293, 1470, 1494]
}


gradually_223_05={  #ef 22.3  q 0.5
    "title":"gradually_223_05",
    "length": 22,
    "mAP" :       [29.9,38.3,43.6,45.7,48.1,50.3,51.6,53.9,54.1,55.2,54.2,55.8,55.6,57.5,57.3,58.6,57.1,55.4,56.8,56.9,56.9,56.4],
    "top1" :      [35.0,43.4,49.6,53.0,56.1,58.3,61.0,64.1,63.7,65.2,63.8,66.0,65.5,67.4,67.0,68.5,67.4,64.0,66.2,66.2,66.1,65.8],
    "top5" :      [48.9,61.1,68.1,69.8,72.6,74.2,77.1,77.2,77.6,77.8,78.6,78.8,78.3,80.3,79.2,81.9,79.3,78.2,80.3,78.2,78.3,79.1],
    "top10" :     [56.4,67.9,72.4,75.6,77.8,79.8,79.9,81.1,81.5,81.9,82.8,83.2,83.6,85.0,83.9,85.3,82.9,81.2,83.3,82.6,83.0,83.8],
    "top20" :     [64.4,72.8,76.9,80.9,82.2,83.5,84.0,85.6,85.2,84.9,86.2,85.6,86.9,88.2,87.2,88.7,86.3,85.0,87.0,86.9,86.6,86.9],
    "label_pre" : [41.3,50.5,53.9,56.6,59.6,61.5,63.2,64.0,63.5,66.1,65.9,67.0,66.9,67.3,67.5,67.9,68.2,68.1,68.5,68.5,68.5,68.5],
    "select_pre" :[81.14,86.86,86.68,86.81,86.98,87.03,86.73,85.58,83.70,83.02,82.17,80.61,79.03,77.79,76.3,74.72,73.22,71.36,70.13,68.72,68.54,68.47],
    "train_pre" :[100.0, 95.75, 94.63, 93.98, 93.64, 93.3, 92.82, 91.92, 90.64, 90.01, 89.29, 88.1, 86.91, 85.98, 84.81, 83.59, 82.46, 81.02, 80.01, 78.89, 78.6, 78.51],
    "select_percent":[0.0, 22.36, 31.59, 38.69, 44.65, 49.87, 54.69, 59.04, 63.12, 66.93, 70.55, 73.96, 77.31, 80.46, 83.47, 86.41, 89.22, 91.97, 94.65, 97.26, 99.73, 100.0],
    "select_num":[0, 334, 472, 578, 667, 745, 817, 882, 943, 1000, 1054, 1105, 1155, 1202, 1247, 1291, 1333, 1374, 1414, 1453, 1490, 1494]
}

gradually_30_04={  #ef 30  q 0.4
    "title":"gradually_30_04",
    "length": 22,
    "mAP" :       [28.9, 36.2, 40.8, 45.2, 48.4, 51.6, 52.4, 50.8, 56.1, 54.9, 55.2, 55.6, 54.3, 54.8, 57.5, 57.1, 55.3, 56.9, 55.7, 56.9, 55.5, 56.9],
    "top1" :      [34.0, 42.5, 47.0, 52.3, 56.0, 59.5, 61.4, 58.5, 65.0, 64.4, 63.4, 64.4, 63.7, 63.8, 67.4, 66.5, 65.0, 66.5, 65.2, 66.4, 64.7, 66.8],
    "top5" :      [49.3, 60.1, 62.7, 70.2, 72.2, 74.1, 75.4, 75.9, 79.6, 77.1, 80.1, 79.2, 78.6, 77.5, 80.5, 80.3, 79.5, 79.9, 78.1, 79.2, 79.8, 78.8],
    "top10" :     [56.3, 66.4, 68.9, 74.9, 75.9, 79.6, 78.9, 80.3, 83.9, 81.5, 83.3, 82.2, 82.3, 81.6, 85.5, 83.9, 83.5, 84.5, 82.8, 83.2, 83.9, 82.9],
    "top20" :     [62.4, 71.9, 75.4, 79.6, 81.1, 84.6, 83.8, 85.5, 86.6, 85.9, 86.0, 86.0, 85.8, 85.6, 88.3, 87.6, 86.3, 88.2, 85.9, 87.0, 86.6, 86.5],
    "label_pre" : [39.7, 49.1, 52.0, 56.1, 58.9, 61.0, 62.2, 63.1, 64.3, 63.9, 64.5, 65.5, 65.0, 65.8, 66.7, 67.3, 67.1, 67.3, 67.3, 67.5, 67.6, 67.6],
    "select_pre" :[72.83, 77.36, 78.3, 81.05, 82.32, 82.14, 81.99, 80.78, 79.91, 78.6, 77.86, 76.57, 75.38, 74.24, 73.36, 72.63, 71.28, 70.11, 68.82, 67.77, 67.6, 67.6],
    "train_pre" :[100.0, 91.14, 90.03, 90.56, 90.63, 90.17, 89.75, 88.8, 88.05, 86.98, 86.32, 85.31, 84.38, 83.46, 82.72, 82.09, 81.03, 80.1, 79.08, 78.22, 77.97, 77.91],
    "select_percent":[0.0, 30.05, 39.63, 46.59, 52.28, 57.16, 61.45, 65.39, 68.94, 72.29, 75.37, 78.31, 81.12, 83.73, 86.28, 88.69, 90.96, 93.24, 95.38, 97.46, 99.46, 100.0],
    "select_num":[0, 449, 592, 696, 781, 854, 918, 977, 1030, 1080, 1126, 1170, 1212, 1251, 1289, 1325, 1359, 1393, 1425, 1456, 1486, 1494]
}

AP_bs_50={
    "title": "AP_bs_50",
    "length": 83,
    "mAP":  [29.34, 30.83, 33.86, 31.19, 33.61, 34.77, 35.22, 35.37, 36.34, 36.52, 35.58, 37.93, 39.02, 38.45, 39.47, 39.77, 41.56, 42.22, 43.76, 42.78, 44.56, 44.1, 44.89, 45.7, 47.01, 47.6, 46.58, 49.19, 49.59, 47.94, 48.91, 50.16, 49.3, 49.59, 51.47, 52.04, 51.9, 53.95, 53.53, 51.85, 53.11, 52.4, 55.06, 54.46, 54.23, 54.9, 54.86, 56.99, 56.26, 56.47, 55.72, 55.62, 56.77, 57.37, 57.4, 57.86, 55.59, 57.89, 58.16, 57.61, 58.13, 58.5, 57.12, 58.95, 57.13, 60.5, 59.21, 59.34, 57.76, 58.18, 60.52, 58.33, 58.03, 59.06, 58.61, 59.07, 59.3, 58.6, 60.01, 58.93, 57.68, 58.48, 57.72],
    "top1": [34.05, 35.9, 39.03, 35.9, 39.74, 40.88, 41.31, 40.46, 41.74, 42.45, 41.6, 44.44, 45.01, 43.73, 45.73, 46.58, 48.15, 48.72, 51.14, 50.0, 51.57, 51.0, 52.71, 53.85, 55.13, 55.98, 55.56, 57.69, 59.12, 55.7, 57.12, 59.12, 58.26, 57.98, 61.4, 61.54, 61.11, 63.82, 63.53, 62.11, 63.25, 61.82, 63.96, 64.25, 64.81, 64.39, 64.81, 66.81, 66.67, 66.1, 65.53, 65.95, 66.1, 67.52, 66.81, 67.95, 64.96, 68.09, 66.52, 66.81, 67.52, 67.38, 67.66, 67.66, 66.52, 70.09, 68.8, 69.37, 67.81, 67.52, 69.66, 67.81, 67.24, 68.23, 67.95, 69.66, 68.66, 68.09, 69.37, 67.81, 66.67, 66.95, 67.81],
    "top5": [],
    "top10": [],
    "top20": [],
    "label_pre": [40.43, 41.97, 45.05, 42.64, 45.11, 46.52, 46.12, 48.06, 47.79, 49.8, 47.46, 49.87, 50.07, 49.26, 50.6, 52.21, 52.48, 52.41, 53.82, 53.61, 55.76, 56.09, 55.35, 59.3, 57.43, 60.37, 57.7, 59.71, 60.11, 60.11, 60.84, 61.31, 61.11, 61.04, 62.32, 64.06, 63.59, 64.86, 63.72, 63.39, 63.92, 65.6, 66.53, 65.33, 65.66, 66.4, 65.33, 67.07, 67.94, 68.01, 66.8, 66.67, 68.41, 68.27, 67.47, 68.21, 68.07, 69.21, 69.21, 69.21, 69.75, 69.14, 68.61, 69.48, 69.48, 69.81, 70.08, 69.81, 69.75, 70.48, 70.55, 70.35, 70.28, 70.35, 70.21, 70.35, 70.55, 70.62, 70.55, 70.68, 70.75, 70.62, 70.55],
    "select_pre":[98.0, 97.06, 96.51, 97.12, 97.54, 95.71, 95.57, 96.59, 96.91, 94.81, 95.65, 96.77, 96.24, 97.18, 97.02, 96.25, 97.04, 97.19, 96.52, 96.68, 96.59, 96.5, 96.64, 96.55, 96.27, 96.6, 96.72, 96.64, 96.75, 96.5, 95.93, 95.89, 95.37, 95.34, 95.32, 95.15, 94.7, 94.83, 94.69, 94.68, 94.42, 93.4, 93.18, 92.6, 92.4, 92.09, 91.46, 90.96, 91.03, 90.56, 89.79, 88.84, 88.74, 88.65, 88.45, 87.6, 87.15, 86.52, 86.11, 85.52, 85.31, 84.23, 83.36, 82.85, 81.95, 81.48, 81.26, 80.41, 79.67, 79.1, 78.4, 77.48, 76.52, 76.03, 75.18, 74.43, 73.84, 73.05, 72.28, 71.67, 70.87, 70.62, 70.55],
    "train_pre": [100.0, 99.73, 99.61, 99.62, 99.63, 99.27, 99.17, 99.3, 99.32, 98.77, 98.91, 99.14, 98.95, 99.17, 99.09, 98.8, 99.02, 99.04, 98.77, 98.79, 98.72, 98.65, 98.67, 98.61, 98.46, 98.56, 98.59, 98.52, 98.55, 98.41, 98.12, 98.07, 97.79, 97.74, 97.7, 97.58, 97.32, 97.36, 97.25, 97.21, 97.11, 96.54, 96.38, 96.02, 95.87, 95.66, 95.26, 94.94, 94.93, 94.62, 94.12, 93.52, 93.47, 93.36, 93.2, 92.63, 92.31, 91.88, 91.56, 91.15, 90.96, 90.23, 89.62, 89.29, 88.65, 88.29, 88.09, 87.47, 86.93, 86.49, 85.96, 85.29, 84.63, 84.23, 83.59, 83.01, 82.54, 81.93, 81.34, 80.89, 80.27, 80.02, 79.96],
    "select_percent": [0.0, 3.35, 4.55, 5.76, 6.96, 8.17, 9.37, 10.58, 11.78, 12.99, 14.19, 15.39, 16.6, 17.8, 19.01, 20.21, 21.42, 22.62, 23.83, 25.03, 26.24, 27.44, 28.65, 29.85, 31.06, 32.26, 33.47, 34.67, 35.88, 37.08, 38.29, 39.49, 40.7, 41.9, 43.11, 44.31, 45.52, 46.72, 47.93, 49.13, 50.33, 51.54, 52.74, 53.95, 55.15, 56.36, 57.56, 58.77, 59.97, 61.18, 62.38, 63.59, 64.79, 66.0, 67.2, 68.41, 69.61, 70.82, 72.02, 73.23, 74.43, 75.64, 76.84, 78.05, 79.25, 80.46, 81.66, 82.86, 84.07, 85.27, 86.48, 87.68, 88.89, 90.09, 91.3, 92.5, 93.71, 94.91, 96.12, 97.32, 98.53, 99.73, 100.0],
    "select_num": [0, 50, 68, 86, 104, 122, 140, 158, 176, 194, 212, 230, 248, 266, 284, 302, 320, 338, 356, 374, 392, 410, 428, 446, 464, 482, 500, 518, 536, 554, 572, 590, 608, 626, 644, 662, 680, 698, 716, 734, 752, 770, 788, 806, 824, 842, 860, 878, 896, 914, 932, 950, 968, 986, 1004, 1022, 1040, 1058, 1076, 1094, 1112, 1130, 1148, 1166, 1184, 1202, 1220, 1238, 1256, 1274, 1292, 1310, 1328, 1346, 1364, 1382, 1400, 1418, 1436, 1454, 1472, 1490, 1494]
}

EF_5_q_1pro={
    "title": "EF_5_q_1pro",
    "length": 21,
    "mAP": [30.1, 29.66, 31.89, 35.67, 38.41, 43.55, 44.52, 45.12, 47.01, 49.86, 49.7, 51.89, 53.91, 54.32, 55.39, 57.07, 54.84, 55.91, 56.95, 55.36, 56.31],
    "top1": [34.33, 34.33, 36.75, 41.45, 43.3, 51.28, 50.43, 52.56, 54.13, 58.26, 58.26, 61.82, 64.25, 64.39, 64.67, 66.38, 64.39, 65.38, 65.38, 64.96, 65.24],
    "top5": [],
    "top10": [],
    "top20": [],
    "label_pre": [41.16, 42.9, 43.51, 47.32, 50.47, 54.95, 55.09, 56.56, 58.43, 59.77, 61.04, 62.65, 63.99, 64.93, 64.66, 65.39, 66.0, 66.27, 66.4, 66.53, 66.67],
    "select_pre": [85.0, 97.06, 93.6, 87.95, 88.89, 91.14, 92.08, 91.86, 91.3, 86.71, 84.05, 84.95, 83.56, 82.6, 74.32, 74.66, 70.22, 67.3, 66.44, 66.53, 66.67],
    "train_pre": [100.0, 99.61, 98.83, 96.98, 96.6, 96.84, 96.87, 96.49, 95.92, 93.45, 91.72, 91.86, 90.74, 89.84, 84.61, 84.37, 81.19, 78.9, 77.92, 77.57, 77.32],
    "select_percent": [0.0, 5.02, 10.04, 15.06, 20.01, 25.03, 30.05, 35.01, 40.03, 45.05, 50.0, 55.02, 60.04, 65.06, 70.01, 75.03, 80.05, 85.01, 90.03, 95.05, 100.0],
    "select_num": [0, 75, 150, 225, 299, 374, 449, 523, 598, 673, 747, 822, 897, 972, 1046, 1121, 1196, 1270, 1345, 1420, 1494]
}

EF_5_q_1pro2={
    "title": "EF_5_q_1pro2",
    "length": 21,
    "mAP": [28.01, 28.96, 30.89, 31.83, 35.74, 37.8, 41.44, 44.43, 45.99, 47.25, 47.64, 49.45, 50.6, 50.58, 53.19, 52.44, 53.5, 54.71, 52.93, 56.58, 52.86],
    "top1": [34.19, 33.48, 35.9, 37.18, 41.45, 43.87, 48.58, 52.99, 53.56, 55.84, 55.7, 59.12, 59.4, 60.4, 62.11, 61.68, 63.53, 63.39, 61.54, 65.38, 62.25],
    "top5": [],
    "top10": [],
    "top20": [],
    "label_pre": [38.82, 41.9, 42.44, 43.44, 45.72, 49.26, 53.35, 56.09, 56.22, 57.03, 58.5, 61.45, 61.78, 62.78, 63.12, 62.65, 63.05, 63.45, 63.59, 63.99, 64.06],
    "select_pre": [73.91, 75.32, 74.6, 63.22, 62.97, 69.89, 67.84, 69.49, 70.88, 70.04, 68.79, 69.93, 68.86, 68.75, 65.95, 66.99, 66.06, 64.22, 63.59, 63.99, 64.06],
    "train_pre": [100.0, 97.55, 95.42, 91.05, 88.91, 89.5, 87.4, 86.94, 86.54, 85.31, 83.85, 83.73, 82.49, 81.84, 79.58, 79.65, 78.61, 76.93, 76.06, 75.87, 75.55],
    "select_percent": [0.0, 5.02, 10.04, 15.06, 20.01, 25.03, 30.05, 35.01, 40.03, 45.05, 50.0, 55.02, 60.04, 65.06, 70.01, 75.03, 80.05, 85.01, 90.03, 95.05, 100.0],
    "select_num": [0, 75, 150, 225, 299, 374, 449, 523, 598, 673, 747, 822, 897, 972, 1046, 1121, 1196, 1270, 1345, 1420, 1494]
}


EF70_11_15={  #data1.1_1.5.10_15_15-25-50.txt
    "title": "EF70_11_15",
    "length": 22,
    "mAP": [31.96, 31.73, 32.85, 36.34, 37.08, 40.52, 40.85, 43.97, 45.04, 49.65, 50.26, 52.5, 53.92, 56.7, 57.94, 59.25, 61.09, 60.48, 62.54, 62.63, 60.85, 61.56],
    "top1": [36.18, 36.04, 38.6, 42.17, 42.02, 46.72, 47.44, 51.0, 51.99, 57.69, 59.26, 61.68, 62.54, 67.09, 67.52, 68.23, 69.8, 69.52, 71.79, 71.79, 69.8, 70.09],
    "label_pre": [45.11, 45.45, 46.18, 48.39, 49.8, 53.48, 53.35, 56.09, 57.9, 61.11, 60.71, 64.12, 65.73, 67.14, 68.14, 69.14, 69.81, 71.15, 71.35, 71.69, 71.55, 71.55],
    "select_pre": [100.0, 97.87, 96.51, 96.97, 97.28, 97.52, 97.38, 97.58, 96.85, 96.15, 95.67, 94.59, 93.64, 92.1, 89.11, 87.07, 84.29, 80.81, 77.09, 72.65, 71.55, 71.55],
    "train_pre": [100.0, 99.86, 99.73, 99.62, 99.52, 99.44, 99.26, 99.21, 98.88, 98.43, 98.12, 97.47, 96.83, 95.86, 93.99, 92.52, 90.54, 88.03, 85.29, 81.93, 80.71, 80.6],
    "select_percent": [0.0, 1.14, 3.15, 5.76, 8.84, 12.32, 16.2, 20.41, 24.9, 29.72, 34.81, 40.16, 45.78, 51.61, 57.63, 63.92, 70.41, 77.11, 84.07, 91.16, 98.39, 100.0],
    "select_num": [0, 17, 47, 86, 132, 184, 242, 305, 372, 444, 520, 600, 684, 771, 861, 955, 1052, 1152, 1256, 1362, 1470, 1494]
}


EF70_50_10={ #data5.0_1.0.10_14_17-07-25
    "title": "EF70_50_10",
    "length": 21,
    "mAP": [34.22, 34.17, 36.88, 41.46, 42.45, 45.66, 46.38, 48.56, 52.57, 53.96, 54.6, 56.01, 58.21, 58.83, 59.39, 61.41, 61.42, 59.56, 61.31, 62.12, 60.74],
    "top1": [40.17, 39.6, 42.31, 47.86, 47.58, 52.28, 53.13, 54.84, 60.54, 63.11, 63.96, 65.38, 66.67, 68.38, 68.52, 71.08, 70.37, 68.38, 70.23, 71.65, 69.52],
    "label_pre": [47.39, 48.93, 48.39, 51.47, 54.69, 55.49, 57.43, 59.64, 62.38, 65.06, 65.46, 66.53, 67.74, 67.47, 68.61, 69.54, 69.48, 69.75, 69.68, 69.95, 69.95],
    "select_pre": [97.33, 96.0, 95.56, 95.32, 95.45, 95.32, 93.88, 92.81, 92.27, 91.57, 90.27, 88.85, 86.93, 85.47, 83.94, 81.19, 78.9, 75.76, 72.75, 69.95, 69.95],
    "train_pre": [100.0, 99.61, 99.18, 98.81, 98.6, 98.33, 97.57, 96.9, 96.38, 95.85, 94.96, 93.96, 92.62, 91.52, 90.39, 88.43, 86.67, 84.38, 82.07, 79.88, 79.55],
    "select_percent": [0.0, 5.02, 10.04, 15.06, 20.01, 25.03, 30.05, 35.01, 40.03, 45.05, 50.0, 55.02, 60.04, 65.06, 70.01, 75.03, 80.05, 85.01, 90.03, 95.05, 100.0],
    "select_num": [0, 75, 150, 225, 299, 374, 449, 523, 598, 673, 747, 822, 897, 972, 1046, 1121, 1196, 1270, 1345, 1420, 1494]
}

EF70_223_05={ #data22.3_0.5.10_16_09-41-32
    "title": "EF70_223_05",
    "length": 22,
    "mAP": [30.57, 41.54, 45.75, 49.42, 51.9, 53.77, 55.64, 57.11, 58.13, 57.98, 60.11, 58.96, 60.19, 60.53, 59.89, 60.84, 60.9, 61.64, 60.67, 61.19, 62.36, 60.46],
    "top1": [35.04, 47.44, 51.57, 56.7, 59.97, 62.25, 64.53, 66.52, 67.66, 66.95, 69.94, 68.23, 69.52, 69.52, 69.52, 69.94, 69.23, 69.94, 69.8, 70.66, 72.22, 69.94],
    "label_pre": [45.11, 52.21, 56.96, 60.04, 62.99, 64.52, 64.99, 67.2, 67.34, 67.47, 67.74, 68.01, 69.01, 68.74, 69.21, 69.54, 69.54, 69.61, 69.61, 69.68, 69.75, 69.75],
    "select_pre": [89.22, 90.04, 89.62, 89.81, 89.8, 88.74, 88.1, 87.17, 86.5, 85.48, 83.44, 82.08, 80.87, 79.55, 78.0, 76.29, 74.6, 72.91, 71.3, 69.87, 69.75, 69.75],
    "train_pre": [100.0, 96.72, 95.83, 95.39, 94.96, 94.19, 93.55, 92.8, 92.22, 91.42, 90.03, 88.99, 88.1, 87.08, 85.89, 84.6, 83.34, 82.03, 80.81, 79.68, 79.43, 79.42],
    "select_percent": [0.0, 22.36, 31.59, 38.69, 44.65, 49.87, 54.69, 59.04, 63.12, 66.93, 70.55, 73.96, 77.31, 80.46, 83.47, 86.41, 89.22, 91.97, 94.65, 97.26, 99.73, 100.0],
    "select_num": [0, 334, 472, 578, 667, 745, 817, 882, 943, 1000, 1054, 1105, 1155, 1202, 1247, 1291, 1333, 1374, 1414, 1453, 1490, 1494]
}

EFnorm_50_10={ #data5.0_1.0.10_19_14-58-12.txt
    "title": "EFnorm_50_10",
    "length": 21,
    "mAP": [30.38, 29.09, 33.76, 37.15, 40.23, 41.68, 43.47, 46.34, 48.34, 49.18, 51.02, 53.65, 52.66, 55.16, 54.76, 56.71, 54.9, 55.93, 55.56, 57.34, 55.47],
    "top1": [35.75, 34.05, 38.89, 42.59, 45.58, 47.15, 49.72, 53.99, 56.55, 57.12, 60.97, 62.82, 61.68, 64.81, 64.39, 66.52, 64.39, 65.81, 64.67, 66.67, 65.1],
    "label_pre": [41.7, 42.44, 45.25, 47.93, 51.61, 53.55, 53.08, 55.96, 58.97, 60.51, 62.18, 63.99, 62.92, 64.12, 65.13, 64.93, 66.33, 65.86, 66.06, 65.8, 65.86],
    "select_pre": [92.0, 93.33, 92.0, 94.98, 92.78, 92.43, 91.2, 91.14, 90.79, 89.29, 87.35, 86.4, 84.47, 82.7, 80.2, 77.42, 74.8, 71.67, 68.87, 65.8, 65.86],
    "train_pre": [100.0, 99.23, 98.59, 98.71, 97.8, 97.3, 96.52, 96.16, 95.69, 94.69, 93.44, 92.65, 91.24, 89.9, 88.1, 86.07, 84.09, 81.74, 79.53, 77.1, 76.73],
    "select_percent": [0.0, 5.02, 10.04, 15.06, 20.01, 25.03, 30.05, 35.01, 40.03, 45.05, 50.0, 55.02, 60.04, 65.06, 70.01, 75.03, 80.05, 85.01, 90.03, 95.05, 100.0],
    "select_num": [0, 75, 150, 225, 299, 374, 449, 523, 598, 673, 747, 822, 897, 972, 1046, 1121, 1196, 1270, 1345, 1420, 1494]
}


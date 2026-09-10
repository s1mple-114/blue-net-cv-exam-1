# 题目变量定义(请勿修改)
text1 = "welcome to OpenCV computer vision is fun we use python and numpy"

text2 = []

list1 = [
    "IMG_001.jpg",
    "IMG_002.JPG",
    "IMG_003.png",
    "IMG_004.jpeg",
    "VID_001.mp4",
    "VID_002.mov",
    "DATA_001.csv",
    "DATA_002.json",
    "notes.txt",
    "temp_001.tmp",
    "temp_002.tmp",
    "mask_001.png",
    "result_001.jpg",
    "raw_001.raw",
    "raw_002.raw",
]

""" --------------在下面完成剩余代码,实现题目要求--------------------
 1. 将 text1 中的每个单词转换为首字母大写,其余字母小写;
    但 "OpenCV"保持原样,处理后的单词按顺序追加到列表 text2 中
 2. 删除 list1 中所有以 .tmp 或 .raw 结尾的文件名
 3. 用集合统计删除后 list1 中出现过多少种不同的扩展名(不区分大小写),
 4. 将 text2,list1 和不同扩展名的数量打印输出  !!! 注意text2需要连续
 text2打印效果 :Welcome To OpenCV Computer Vision Is Fun We Use Python And Numpy """
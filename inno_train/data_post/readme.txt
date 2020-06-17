insert_rawdata()
#上传爬虫爬取数据的方法
#上传数据格式为ds，context，topic，分别为时间、文本、话题，
#上传的数据格式如该目录下rawdata.csv一样，注意列名称必须是ds,context,topic
#李哲荀用

insert_emotionval()
##上传原始数据经过二次处理后数据和最终预测结果的方法
#上传数据格式为ds，emotion_val，topic，predict分别代表时间、话题情感值、话题、该行数据是否为预测值
#上传的数据格式如该目录下rawdata.csv一样，注意列名称必须是ds,context,topic，predict
# predict只有0、1两个属性，0代表这行数据不是预测得到的，1代表这行数据是预测得到的，只取0或1，杨涛处理后的真实数据是1，杨秀辉预测的预测数据是0
#杨涛、杨秀辉用
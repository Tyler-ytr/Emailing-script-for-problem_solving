#殷天润制作
#使用说明:在批好的作业的文件夹下面: python py_email.py即可

import  yagmail
import os
def get_id(filename):
	for index in range(0,len(filename)-1):
		if filename[index]=='1' and (filename[index+1]=='9' or filename[index+1]=='7'):
			print(filename[index:index+9])
			return filename[index:index+9]



user='171240xxx@smail.nju.edu.cn'
passwd="passwd"
smtp_host="smtp.exmail.qq.com"
mail=yagmail.SMTP(user=user,password=passwd,host=smtp_host,port=465)
path="./"
filelist=os.listdir(path)
# 遍历输出每一个文件的名字和类型
for item in filelist:
    # 输出指定后缀类型的文件
		if(item.endswith('.pdf')):
			file=item
			uid=get_id(item)
			uid_email=uid+"@smail.nju.edu.cn"
			print(uid_email)
			mail.send(to=[uid_email],subject='问题求解批改_殷天润', contents='批改见附件',   attachments=[file] )   			






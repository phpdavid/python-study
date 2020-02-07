from urllib.request import urlretrieve
import csv

# # 下载文件
# # urlretrieve('http://175.6.32.4:88/soft/lnmp/backup.sh','backup-test.sh')
# rf = open('admin_user_20200203.csv', 'r')
# reader = csv.reader(rf)
# # print(next(reader))
# writ_line = next(reader)
# wf = open('admin_user_20200203.csv', 'a')
# writer = csv.writer(wf)
# writer.writerow(next(reader))
# writer.writerow(next(reader))
# wf.flush()
# with后面接的对象返回的结果赋值给f。此例当中open函数返回的文件对象赋值给了f.with会自已获取上下文件的异常信息。
with open('admin_user_20200203.csv', 'r') as rf:
    reader = csv.reader(rf)
    with open('admin_user_20200203_new.csv', 'w') as wf:
        writer = csv.writer(wf)
        reader_header = next(reader)
        next(reader)
        writer.writerow(reader_header)
        for line in reader:
            if line[0] == 'user_id':
                break
            if int(line[0]) > 10 and int(line[10]) > 10000:
                writer.writerow(line)
print('end')

# douban_backup
豆瓣读过的书的记录备份

代码功能实现(books.py)：

将Douban 读过的书的记录保存到 ex/douban.xlsx 文件和 db/douban.db 数据库中。

需要在douban_config.py 文件中填写配置信息：

1.豆瓣登录的用户名和密码
``` python
douban_id = '[豆瓣登录id(邮箱名)]'
douban_pwd = '[豆瓣登录密码]'
```

2.webdriver的绝对路径：
``` python
driver_path = r'G:\Python\software\chromedriver.exe'
```
3.数据库文件douban.db的绝对路径和表格文件douban.xlsx的绝对路径：
``` python
db_file = r'G:\Python\code2\douban\db\douban.db'
ex_file = r'G:\Python\code2\douban\ex\douban.xlsx'
```

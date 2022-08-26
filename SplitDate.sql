# mysql 取日期字段中的年月 
# eg : bill_date字段的值为2013.03.02,提取 2013.03

# 方法一 DATE_FORMAT
# 缺陷：有些日期格式本身就是年月，这样的数据会出现问题,如 2014.03
SELECT DATE_FORMAT(bill_date,'%Y.%m') as '日期',bill_date as '原数据' from acb_bill

# 方法二 截取
# left(str, length)函数 【从左开始截取,right()从右开始截取】
# substring(str, pos,[length]) 函数 【str:被截取字符串 pos:从第几位开始截取 length:截取长度（如未设置，则为从截取位到末尾）】
# substring_index(str, delim, count)【被截取字符串，关键字，关键字出现的次数】


SELECT left(bill_date,7) as '日期',bill_date as '原数据' from acb_bill

SELECT substring(bill_date,1,7) as '日期',bill_date as '原数据' from acb_bill

SELECT substring_index(bill_date,',',2) as '日期',bill_date as '原数据' from acb_bill
# 如 2014.03 格式数据没有第二个“.”，则返回整个字符串 2014.03

# 转载自 https://blog.csdn.net/weixin_43697585/article/details/109620585
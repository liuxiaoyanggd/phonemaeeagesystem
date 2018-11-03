from phone import Phone
from admin import Admin
def welcome():
    print('--------------------------------')
    print('手机信息管理系统')
    print('1.手机录入')
    print('2.根据手机品牌查询手机信息')
    print('3.查询全部手机信息')
    print('4.根据手机编号修改手机价格')
    print('5.根据手机编号删除手机记录')
    print('6.退出')
    print('--------------------------------')

if __name__ == '__main__':
    p = Admin()
    while True:
        welcome()
        bh=int(input('请输入您选择的编号'))
        if bh==1:#添加手机信息
            p.add_phone()
        elif bh==2:#根据品牌查信息
            p.cha()
        elif bh==3:#查看所有手机信息
            p.show_all()
        elif bh==4:#由编号修改价格
            p.update()
        elif bh==5:#由编号删除信息
            p.rm()
        elif bh==6:#退出
            break
        else:
            print('您输入有误,请重新输入')
            continue


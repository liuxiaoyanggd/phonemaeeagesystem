from phone import Phone
phone_id=[] #手机编号
class Admin:
    def __init__(self):
        self.phone = {}  # 手机信息
    def add_phone(self):
        print(len(phone_id)+1)
        brand=input('请输入手机品牌')
        model=input('请输入手机型号')
        price=float(input('请输入手机价格'))
        count=int(input('请输入手机数量'))
        version=input('请输入手机版本')
        phone_id.append(len(phone_id)+1)
        p=Phone(brand,model,price,count,version)
        self.phone[len(phone_id)]=p
        print('添加成功')
    def show_all(self):
        print('序号\t品牌\t型号\t价格\t数量\t版本')
        for i,j in self.phone.items():
            print('{:^4}\t{:^3}\t{:^4}\t{:^4}\t{:^4}\t{:^4}'.format(i,j.brand,j.model,j.price,j.count,j.version))
    def update(self):
        while True:
            bh=int(input('请输入您要修改信息的手机编号'))
            if bh not in phone_id:
                print('没有这个手机,请重新输入')
                continue
            attr=input('请输入您要更改的属性(price or count)')
            content = float(input('请输入您要修改的内容'))
            if attr=='price':
                self.phone[bh].price=content
                print('价格修改成功,当前价格为%d'%self.phone[bh].price)
                break
            elif attr=='count':
                content=int(content)
                self.phone[bh].count=content
                print('价格修改成功,当前数量为%d' % self.phone[bh].count)
                break
            else:
                print('请输入正确的属性')
                continue
            break
    def rm(self):
        while True:
            bh=int(input('请输入您要删除信息的手机编号'))
            if bh not in phone_id:
                print('没有这个手机,请重新输入')
                continue
            else:
                del self.phone[bh]
                print('删除成功')
                phone_id.pop(bh)
                break
    def cha(self):
        pp=input(('请输入您要查询的品牌'))
        for i in self.phone.values():
            if i.brand==pp:
                print('品牌\t型号\t价格\t数量\t版本')
                print('{:^3}\t{:^4}\t{:^4}\t{:^4}\t{:^4}'.format(i.brand, i.model, i.price, i.count, i.version))
            else:
                print('没有此品牌')








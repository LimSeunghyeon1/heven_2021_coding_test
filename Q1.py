'''
시작 시각 : 14시
종료 시각 : 15시 30분
'''
import copy ##ㅠㅠ

class Cake:
    def __init__(self,name,price,ingredient):
        self.name=name
        self.price=price
        self.ingredient=ingredient


class Shop:
    def __init__(self):
        self.ingredient=dict()
        self.product=dict()

    def buy_ingredient(self, buy_dict): #buy ingredient_ 구매한 재료들
        for key,val in buy_dict.items():
            if key in self.ingredient:
                self.ingredient[key]+=val
            else: #when there's no matches
                self.ingredient[key]=val



    def current_ingredient(self):
        print("현재 보유한 재료는 ",end='')
        for key,val in self.ingredient.items():
            print(f"{key}({val}개)",end=' ')
        print('입니다.')

    def make_cake(self, cake): #cake(name,price,ingre)
        error=dict()  #[모자란 재료: 개수]
        cop=copy.deepcopy(self.ingredient)##error 날때를 위해 미리 복사
        #print('cop:',cop)
        for key,val in cake.ingredient.items():

            if key not in self.ingredient: #재료가 없을때
                error[key]=val #error에 추가
            else:

                if (self.ingredient[key]-val)<0:
                    error[key]=-self.ingredient[key]+val
                    del self.ingredient[key]
                elif (self.ingredient[key]-val)==0:
                    del self.ingredient[key]
                else:
                     self.ingredient[key]-=val

        if error==dict(): #ingredient is enough
            if cake in self.product:
                self.product[cake]+=1
            else:
                self.product[cake]=1
            print(cake.name,"1개 완성!")
        else: #not enough ingredient
            for key, val in error.items():
                print(f"{key}재료가 {val}개",end=' ')
            print("부족해요!")
            self.ingredient=copy.deepcopy(cop)


class Pos:
    def __init__(self,cake_shop): #cake_shop=shop의 객체
        self.shop=cake_shop
        self.money=0


    def current_cakes(self):
        print("현재 재고는")
        for key,val in self.shop.product.items():
            print(key.name,':',val)

    def sell_cake(self, cakename):
        for cake in self.shop.product: #product: cake class & 개수
            if cake.name==cakename:
                self.shop.product[cake]-=1
                self.money+=cake.price #판매금액 더해주기
                if self.shop.product[cake]<=0:
                    del self.shop.product[cake]
                print(cakename,"판매 완료. 현재 남은",cakename,"개수는",self.shop.product.get(cake,0),"입니다.")

                return
        print(cakename,"재고가 없습니다.")


    def print_current_money(self):
        print("현재 판매 금액은 총",self.money,'입니다.')
        pass


cheesecake = Cake("Cheese Cake", 6900, {'cheese': 2, 'egg': 2, 'butter': 2})
chococake = Cake("Chocolate Cake", 5900, {'chocolate': 2, 'egg': 2, 'butter': 2})
carrotcake = Cake("Carrot Cake", 5500, {'carrot': 2, 'walnut': 2, 'egg': 1, 'butter': 1})
creamcake = Cake("Fresh Cream Cake", 4500, {'cream': 3, 'egg': 1, 'butter': 1})
swpotatocake = Cake("Sweet Potato Cake", 6500, {'sweet potato': 3, 'egg': 2, 'butter': 1})

cake_shop = Shop()
cake_shop.buy_ingredient({'cheese': 5, 'carrot': 3, 'sweet potato': 3, 'egg': 10, 'butter': 10})
cake_shop.current_ingredient()
cake_shop.buy_ingredient({'chocolate': 3, 'walnut': 2, 'egg': 12, 'butter': 12})
cake_shop.current_ingredient()

print("\nMAKE CAKE")
cake_shop.make_cake(creamcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(chococake)
print(cake_shop.ingredient)
cake_shop.make_cake(swpotatocake)
print(cake_shop.ingredient)
cake_shop.current_ingredient()

pos = Pos(cake_shop)
print()
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Chocolate Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')

print()
pos.print_current_money()

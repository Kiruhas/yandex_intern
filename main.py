class Dish:
  def __init__(self, parameters):
    self.name = parameters[0]
    self.count_need = parameters[1]
    self.ingridients = parameters[2]

class Ingridient:
  def __init__(self, parameters):
    self.name = parameters[0]
    self.massa = parameters[1]
    self.izmer = parameters[2]

class Prices:
  def __init__(self, parameters):
    self.name = parameters[0]
    self.price = parameters[1]
    self.count = parameters[2]
    self.izmer = parameters[3]

class Bju:
  def __init__(self, parameters):
    self.name = parameters[0]
    self.count = parameters[1]
    self.izmer = parameters[2]
    self.bel = parameters[3]
    self.jir = parameters[4]
    self.ugl = parameters[5]
    self.energy = parameters[6]

def get_dishes(count_dishes, dishes, ingridients):
  for i in range(0, int(count_dishes)):
    dish = input().split(" ")
    dish_ingridients = []
    for j in range(0, int(dish[2])):
      ingr = input().split(" ")
      if ingr[0] in ingridients:
        ingridients[ingr[0]] += int()
      
      ingridient = Ingridient([ingr[0], ingr[1], ingr[2]])
      dish_ingridients.append(ingridient)
    dishes.append(Dish([dish[0], dish[1], dish_ingridients]))

def get_prices(count_ingridients, prices):
  for i in range(0, int(count_ingridients)):
    ingr = input().split(" ")
    prices.append(Prices([ingr[0], ingr[1], ingr[2], ingr[3]]))

def get_bju(count_ingridients, bju):
  for i in range(0, int(count_ingridients)):
    ingr = input().split(" ")
    bju.append(Bju([ingr[0], ingr[1], ingr[2], ingr[3], ingr[4], ingr[5], ingr[6]]))

def main():
  dishes = []
  ingridients = []
  prices = []
  bju = []
  get_dishes(input(), dishes, ingridients)
  get_prices(input(), prices)
  get_bju(input(), bju)

  # output_dishes()
  # output_prices()

def output_dishes():
  print("\n----------DISHES RESULT-----------\n")
  for a in range(0, len(dishes)):
    print(dishes[a].name + " " + dishes[a].count_need)
    for b in range(0, len(dishes[a].ingridients)):
      print(dishes[a].ingridients[b].name + " " + dishes[a].ingridients[b].massa + " " + dishes[a].ingridients[b].izmer)

def output_prices():
  print("\n----------PRICES RESULT-----------\n")
  for a in range(0, len(prices)):
    print(prices[a].name + " " + prices[a].price + " " + prices[a].count + " " + prices[a].izmer)

if __name__ == "__main__":
  main()

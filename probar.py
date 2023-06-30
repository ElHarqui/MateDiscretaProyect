class restaurante( ): 
  def __init__(self,name = 'HOLS',cocina = 'ADIO'):
    self.restaurant_name =  name
    self.cuisine_name = cocina
  def describe_restaurant(self):
    return f"El nombre del restaurante es {self.restaurant_name} y su tipo de cocina es {self.cuisine_name}"
  #def open_restaurant(self):
    
try:
  gaaa = restaurante()
  print(gaaa.restaurant_name)
  #print(gaaa)
except Exception as a:
  print(a)
  print("ERROR") 
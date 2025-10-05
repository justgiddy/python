# Assignment 1: Design Your Own Class! 🏗️
class Smartphone:
    """A class representing a smartphone with various features"""
    
    def __init__(self, brand, model, storage_gb, battery_mah, price):
        # Public attributes
        self.brand = brand
        self.model = model
        
        # Protected attributes (encapsulation)
        self._storage_gb = storage_gb
        self._battery_mah = battery_mah
        
        # Private attributes (encapsulation)
        self.__price = price
        self.__is_locked = True
        self.__pin = "1234"  # Default PIN
        
    # Public methods
    def make_call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}")
        
    def send_message(self, number, message):
        print(f"💬 Sending message to {number}: {message}")
        
    def take_photo(self):
        print(f"📸 Photo taken with {self.brand} {self.model}'s camera!")
        
    def get_specs(self):
        return f"{self.brand} {self.model} - {self._storage_gb}GB, {self._battery_mah}mAh"
    
    # Encapsulation methods for private attributes
    def unlock(self, pin):
        if pin == self.__pin:
            self.__is_locked = False
            print("🔓 Phone unlocked!")
        else:
            print("❌ Incorrect PIN!")
            
    def lock(self):
        self.__is_locked = True
        print("🔒 Phone locked!")
        
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("✅ PIN changed successfully!")
        else:
            print("❌ Incorrect current PIN!")
            
    def get_price(self):
        return f"${self.__price}"
    
    def set_discount(self, discount_percent):
        if 0 <= discount_percent <= 50:
            self.__price = self.__price * (1 - discount_percent/100)
            print(f"🎉 Discount applied! New price: ${self.__price:.2f}")
        else:
            print("❌ Invalid discount percentage!")


# Inheritance layer - GamingPhone inherits from Smartphone
class GamingPhone(Smartphone):
    """A specialized smartphone for gaming with enhanced features"""
    
    def __init__(self, brand, model, storage_gb, battery_mah, price, refresh_rate, cooling_system):
        # Call parent constructor
        super().__init__(brand, model, storage_gb, battery_mah, price)
        
        # Additional attributes specific to gaming phones
        self.refresh_rate = refresh_rate  # Hz
        self.cooling_system = cooling_system
        self.__game_mode = False
        
    # Polymorphism - overriding parent method
    def get_specs(self):
        base_specs = super().get_specs()
        return f"{base_specs}, {self.refresh_rate}Hz, {self.cooling_system} cooling"
    
    # Additional methods specific to gaming phones
    def enable_game_mode(self):
        self.__game_mode = True
        print("🎮 Game Mode enabled! Enhanced performance activated!")
        
    def disable_game_mode(self):
        self.__game_mode = False
        print("📱 Game Mode disabled!")
        
    def play_game(self, game_name):
        if self.__game_mode:
            print(f"🎯 Playing {game_name} in ultra-smooth {self.refresh_rate}Hz!")
        else:
            print(f"🎯 Playing {game_name} - enable Game Mode for better performance!")


# Demonstration
def demonstrate_smartphone_class():
    print("📱 SMART PHONE CLASS DEMONSTRATION")
    print("=" * 50)
    
    # Create regular smartphone
    iphone = Smartphone("Apple", "iPhone 15", 128, 4000, 999)
    print(iphone.get_specs())
    iphone.make_call("555-1234")
    iphone.take_photo()
    
    # Demonstrate encapsulation
    iphone.unlock("1234")
    iphone.change_pin("1234", "5678")
    print(f"Phone price: {iphone.get_price()}")
    iphone.set_discount(10)
    
    print("\n" + "🎮 GAMING PHONE DEMONSTRATION" + "=" * 50)
    
    # Create gaming phone
    gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 512, 6000, 1299, 165, "Vapor Chamber")
    print(gaming_phone.get_specs())  # Polymorphism in action!
    gaming_phone.enable_game_mode()
    gaming_phone.play_game("Call of Duty Mobile")
    gaming_phone.make_call("555-5678")  # Inherited method

# Activity 2: Polymorphism Challenge! 🎭
from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    
    @abstractmethod
    def move(self):
        """Abstract method that must be implemented by all subclasses"""
        pass
    
    def honk(self):
        print("🚗 Beep beep!")
        
    def get_info(self):
        return f"{self.name} (Max speed: {self.max_speed} km/h)"

# Concrete implementations with different move() behaviors
class Car(Vehicle):
    def __init__(self, name, max_speed, fuel_type):
        super().__init__(name, max_speed)
        self.fuel_type = fuel_type
    
    def move(self):
        print(f"🚗 {self.name} is driving on the road at up to {self.max_speed} km/h!")
        
    def honk(self):
        print("🚗 Honk honk! Car horn sounding!")

class Plane(Vehicle):
    def __init__(self, name, max_speed, wingspan):
        super().__init__(name, max_speed)
        self.wingspan = wingspan
    
    def move(self):
        print(f"✈️ {self.name} is flying in the sky at up to {self.max_speed} km/h!")
        
    def take_off(self):
        print(f"🛫 {self.name} is taking off with {self.wingspan}m wingspan!")

class Boat(Vehicle):
    def __init__(self, name, max_speed, boat_type):
        super().__init__(name, max_speed)
        self.boat_type = boat_type
    
    def move(self):
        print(f"🚤 {self.name} is sailing on water at up to {self.max_speed} km/h!")
        
    def anchor(self):
        print(f"⚓ {self.name} is dropping anchor!")

class Bicycle(Vehicle):
    def __init__(self, name, max_speed, gears):
        super().__init__(name, max_speed)
        self.gears = gears
    
    def move(self):
        print(f"🚴 {self.name} is pedaling on the path at up to {self.max_speed} km/h!")
        
    def ring_bell(self):
        print("🔔 Ring ring! Bicycle bell ringing!")

class Rocket(Vehicle):
    def __init__(self, name, max_speed, fuel_capacity):
        super().__init__(name, max_speed)
        self.fuel_capacity = fuel_capacity
    
    def move(self):
        print(f"🚀 {self.name} is launching into space at up to {self.max_speed} km/h!")
        
    def countdown(self):
        print("🔟 9... 8... 7... 6... 5... 4... 3... 2... 1... LIFTOFF! 🚀")

# Function demonstrating polymorphism
def vehicle_parade(vehicles):
    """Demonstrates polymorphism by calling move() on different vehicle types"""
    print("\n🎪 VEHICLE PARADE - POLYMORPHISM IN ACTION!")
    print("=" * 60)
    
    for vehicle in vehicles:
        print(f"\n{vehicle.get_info()}")
        vehicle.move()  # Same method, different behaviors!
        vehicle.honk()  # Some override this too!
        
        # Type-specific methods
        if isinstance(vehicle, Plane):
            vehicle.take_off()
        elif isinstance(vehicle, Boat):
            vehicle.anchor()
        elif isinstance(vehicle, Bicycle):
            vehicle.ring_bell()
        elif isinstance(vehicle, Rocket):
            vehicle.countdown()

# Enhanced demonstration with user interaction
def interactive_vehicle_demo():
    """Interactive demonstration of polymorphism"""
    
    # Create various vehicles
    vehicles = [
        Car("Tesla Model S", 250, "Electric"),
        Plane("Boeing 747", 920, 68.5),
        Boat("Speedboat 5000", 80, "Speedboat"),
        Bicycle("Mountain Bike Pro", 45, 21),
        Rocket("Falcon Heavy", 28000, "1,500 tons")
    ]
    
    while True:
        print("\n🚗 VEHICLE POLYMORPHISM DEMO 🚀")
        print("1. See all vehicles move")
        print("2. Select a specific vehicle")
        print("3. Race simulation")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            vehicle_parade(vehicles)
            
        elif choice == '2':
            print("\nAvailable vehicles:")
            for i, vehicle in enumerate(vehicles, 1):
                print(f"{i}. {vehicle.get_info()}")
            
            try:
                vehicle_choice = int(input("\nSelect a vehicle (1-5): ")) - 1
                if 0 <= vehicle_choice < len(vehicles):
                    selected_vehicle = vehicles[vehicle_choice]
                    print(f"\n🎯 Selected: {selected_vehicle.get_info()}")
                    selected_vehicle.move()
                    
                    # Show type-specific actions
                    if isinstance(selected_vehicle, Car):
                        print("💡 This car uses eco-friendly fuel!" if selected_vehicle.fuel_type == "Electric" else "⛽ This car uses conventional fuel.")
                    elif isinstance(selected_vehicle, Plane):
                        print(f"✈️ Impressive {selected_vehicle.wingspan}m wingspan!")
                    elif isinstance(selected_vehicle, Bicycle):
                        print(f"🚴 This bike has {selected_vehicle.gears} gears for all terrains!")
                        
                else:
                    print("❌ Invalid selection!")
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == '3':
            print("\n🏁 RACE SIMULATION - READY, SET, GO! 🏁")
            for vehicle in vehicles:
                vehicle.move()
            print("\n🎉 All vehicles completed the race in their own unique ways!")
            
        elif choice == '4':
            print("👋 Thanks for exploring polymorphism!")
            break
            
        else:
            print("❌ Invalid choice! Please try again.")

# Run both demonstrations
if __name__ == "__main__":
    print("🎯 PYTHON OOP ASSIGNMENTS DEMONSTRATION")
    print("=" * 50)
    
    # Run Assignment 1
    demonstrate_smartphone_class()
    
    print("\n" + "=" * 50)
    
    # Run Activity 2
    interactive_vehicle_demo()

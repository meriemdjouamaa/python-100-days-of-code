
# Using Positional Arguments
def greet_with(name, location):
    
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jack Bauer", "Nairobi")

# Using Keyword Arguments
def greet_with(name, location):
    
    print(f"Hello {name}")
    print(f"What is it like in {location}?")    


    greet_with(location="Nairobi", name="Jack Bauer")
# Newton's Laws of Motion - Simple Calculator

mass = 5  # kg
force = 6  # N

# Newton's First Law: F = 0 -> no acceleration
print("=== NEWTON'S FIRST LAW ===")
if force == 0:
    print("No net force, object remains at rest or moves at constant velocity")
else:
    print(f"Net force = {force} N, object will accelerate")

# Newton's Second Law: F = m * a
print("\n=== NEWTON'S SECOND LAW ===")
acceleration = force / mass
print(f"F = m * a")
print(f"a = F / m = {force} / {mass} = {acceleration} m/s²")

# Newton's Third Law: Action-Reaction
print("\n=== NEWTON'S THIRD LAW ===")
reaction_force = -force
print(f"Action force = {force} N")
print(f"Reaction force = {reaction_force} N")

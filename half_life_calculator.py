import math

# ---- Apni drug ke hisaab se numbers badlo ----
initial_dose = 500       # mg, shuru mein kitni dawa thi
half_life = 6            # hours, dawa aadhi hone mein kitna time lagta hai
time_elapsed = 18        # hours, dawa lene ke baad kitna time hua
# ----------------------------------------------

# Formula: bacha hua = shuru wali dose x (1/2)^(time / half-life)
remaining = initial_dose * (0.5 ** (time_elapsed / half_life))

# Elimination rate constant (k) = 0.693 / half-life
k = math.log(2) / half_life

print("Initial dose:", initial_dose, "mg")
print("Half-life:", half_life, "hours")
print("Time elapsed:", time_elapsed, "hours")
print("Drug remaining:", round(remaining, 2), "mg")
print("Percent remaining:", round(remaining / initial_dose * 100, 2), "%")
print("Elimination rate constant (k):", round(k, 4), "per hour")

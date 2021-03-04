import package.list_ops as lo
import package.dict_ops as do

weights = [65, 90, 42, 76]
heights = [1.65, 1.78, 1.59, 1.80]
heights_sq = lo.multiply(heights, heights)
print((heights_sq))

bmi = lo.divide(weights, heights_sq)
print("BMI:", bmi)

print("\n")
w_names = ["RM", "Suga", "Jin", "V"]
h_names = ["Jimin", "RM", "Suga", "Jin"]
weights = dict(zip(w_names, weights))
print("weights", weights)
#딕셔너리 만드는 방법
heights = dict(zip(h_names, heights))
print("heights", heights)

heights_sq = do.multiply(heights, heights)
print("heights_sq", heights_sq)
bmi = do.divide(weights, heights_sq)
print("BMI:", bmi)
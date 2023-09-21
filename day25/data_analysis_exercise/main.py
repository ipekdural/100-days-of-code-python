import pandas

data = pandas.read_csv("Squirrel_Data.csv")  # creating a DataFrame

gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(f"""
Gray: {gray}
Black: {black}
Cinnamon={cinnamon}
""")

data_dict={
    "Fur Color":["Gray","Black","Cinnamon"],
    "Count": [gray,black,cinnamon]
}
data_dict_frame=pandas.DataFrame(data_dict)
data_dict_frame.to_csv("squirrel_count.csv") # create a csv file
print(data_dict_frame)
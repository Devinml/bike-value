import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('results_DO_NOT_DELETE.csv',error_bad_lines=False)
df = df.reset_index()

df.rename(columns= {'index': 'Title',
                   'Title': 'Condition',
                    'Condition': 'Material',
                    "Material": "Frame Size",
                    'Frame Size':'Wheel Size',
                    'Wheel Size': 'Front Travel',
                    'Front Travel': 'Rear Travel',
                    'Rear Travel':'Price',
                    'Price' : 'City',
                    'City' : 'State/Prov',
                    'State/Prov':'Country',
                    'Country':'Description',
                    'Description': 'Date'
                    
                   },inplace=True)

df.drop('Date Posted',inplace=True,axis = 1)
df.groupby('Wheel Size').count()

def Check_Material(string):
    if string == 'Aluminium' or string == 'Carbon Fiber' or string == 'Chromoly' or string== 'Steel' or string =='Titanium':
        return True
    else:
        return False

def Check_Wheel(string):
    if '275' in string or string == '29' or string == '26':
        return True
    else:
        return False

def remove_resonable_trades(input_string):
    if 'CAD' in input_string or 'USD' in input_string:
        return True
    else:
        return False

def convert_string_int(input_string):
    nums = '1234567890'
    string = ''
    for char in input_string:
        if char in nums:
            string+= char
        else:
            return 
    return int(string)
def convert_to_us(input_string):
    if 'CAD' in input_string:
        return int(convert_string_int(input_string)*.71)
    else:
        return convert_string_int(input_string)

df = df[df['Material'].apply(lambda x : Check_Material(x))]
df = df[df['Wheel Size'].apply(lambda z: Check_Wheel(z))]
df = df[df['Front Travel'] != '0 mm Hardtail' ]
df['Front Travel'] = df['Front Travel'].apply(lambda x : convert_string_int(x))
df['Rear Travel'] = df['Rear Travel'].apply(lambda x : convert_string_int(x))
df = df[df['Price'].apply(lambda x : remove_resonable_trades(x))]
df.dropna()
df['Price'] = df['Price'].apply(lambda x : convert_to_us(x))


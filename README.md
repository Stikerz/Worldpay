# Worldpay

## Setup:

- Create virtualenv(Optional) using python 3.7
- Run pip install -r requirements.txt

## Usage
`main.py` takes either 2 required arguments and 3 optional:

It returns an image file in the `visuals` dir and prints out statistical
 information from the specified data file.

All parameters:


```
	'--help', '-h':   // Prints help
	'--path', '-p':  String // Specify a particular data frame (Required)
	'--column', '-c': String // Specify a particular column (Required)
	'--day', '-d': stores_true,  // Specify time window day
	'--month', '-m': stores_false, // Specify time window month (Default True)
	'--week', '-w': stores_true,  // Specify time window week
```

Example:
   
```bash
    python main.py -p "RoadSafetyData_2015/Accidents_2015.csv" -c "Number_of_Casualties" -d -w
```

scalability/limitations:
 
 
future features:
## Testing
- Run python tests/anylysis_test.py # Run test

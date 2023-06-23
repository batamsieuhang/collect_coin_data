from results import print_results
import sys

# Variables
time_value = sys.argv[1:(len(sys.argv)-2)]
url = "https://ckcoin.top/Spot/Up"
sort_value = int(sys.argv[len(sys.argv)-2])
time_delay =int(sys.argv[len(sys.argv)-1])


print_results(url,time_value,sort_value,time_delay)



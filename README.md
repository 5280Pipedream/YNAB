# YNAB 4

Convert bank CSV to YNAB 4 CSV format using python

A simple python script to convert CSV files downloaded from supported banks to the import format supported for YNAB 4.

## Supported Banks

- Charles Schwab

  Only works with posted transations. The pending transactions are removed from the CSV during conversion.

- Chase
- Capital One

### Slow desktop performance fix

YNAB4 will import bank items with incorrect dates and this will cause performance issues. Someone created a ruby script to fix the issue.

[Reddit Post](https://www.reddit.com/r/ynab/comments/8h1oqx/ynab4_slow_desktop_performance_fix/)

```ruby
require  'json'

file = 'path/to/Budget.yfull'

data = JSON.parse(File.read(file))

startCount = data["monthlyBudgets"].size
data["monthlyBudgets"].delete_if { |month|
    month["monthlySubCategoryBudgets"].empty?
}

endCount = data["monthlyBudgets"].size

print "Deleted #{startCount - endCount} empty months was #{startCount} now #{endCount}"

File.write(file, data.to_json)

print "\n"
```

Modify the script as needed and save it in a \*.rb file type. Run the file by typing `ruby <fileName.rb>`

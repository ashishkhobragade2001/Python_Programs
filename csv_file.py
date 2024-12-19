import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (replace 'chromedriver' with the path to your WebDriver)
driver = webdriver.Chrome()

# Open the webpage where the test cases are displayed
driver.get("http://example.com/test-results")  # Replace with the actual URL

# Prepare a list to store test case data
test_cases = []

# Locate the table with test results (replace with actual locator)
# For example, assuming each row has:
# - Test case name in the first column
# - Status in the second column
# - Execution time in the third column
# - Failure reason (if any) in the fourth column
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    test_case = {
        "Test Case Name": cells[0].text,
        "Execution Status": cells[1].text,
        "Execution Time": cells[2].text
    }
    
    # If test case failed, add the failure reason
    if test_case["Execution Status"].lower() == "failed":
        test_case["Failure Reason"] = cells[3].text
    else:
        test_case["Failure Reason"] = ""
    
    test_cases.append(test_case)

# Save the data to a CSV file
csv_file = "test_results.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Test Case Name", "Execution Status", "Execution Time", "Failure Reason"])
    writer.writeheader()
    writer.writerows(test_cases)

print(f"Test results saved to {csv_file}")

# Close the browser
driver.quit()

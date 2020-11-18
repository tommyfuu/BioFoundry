
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


# open the tm calculator headlessly
options = webdriver.chrome.options.Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://tmcalculator.neb.com/#!/batch")

time.sleep(1)

# set the enzyme to phusion
driver.find_element_by_xpath(
    "/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/form/div/div[1]/div/select[1]").send_keys("P\n")

# set the primer input
# driver.find_element_by_id("batchinput").send_keys(
#     "P1fwd; GGAGAGGGTGAAGGTGATGC; P1rev; ATCACTTGCGGTTGCCAGTA \n P2fwd; GGAGAGGGTGAAGGTGATGC; P2rev; ATCACTTGCGGTTGCCAGTA")
driver.find_element_by_id("batchinput").send_keys(
    'primerPair0Left; GGAGAGGGTGAAGGTGATGC; primerPair0Right; ATCACTTGCGGTTGCCAGTA\nprimerPair1Left; GGAGAGGGTGAAGGTGATGC; primerPair1Right; CGGGATGCGGTTTGATTTCC\nprimerPair2Left; GGAGAGGGTGAAGGTGATGC; primerPair2Right; TATTGTCAGGCACGACGACC\nprimerPair3Left; AGTGGAGAGGGTGAAGGTGA; primerPair3Right; ATCACTTGCGGTTGCCAGTA\nprimerPair4Left; TCAGTGGAGAGGGTGAAGGT; primerPair4Right; ATCACTTGCGGTTGCCAGTA\n')
# .sendKeys("wuba")

# blur the focus to produce outputs
driver.execute_script("document.getElementById('batchinput').blur()")


# tableHeader = driver.find_element_by_class_name("batchresultstablex")
# all_children_by_css = tableHeader.find_elements_by_css_selector("*")
# #all_children_by_xpath = tableHeader.find_elements_by_xpath(".//*")
# print("Table", str(all_children_by_xpath))

# fetch the result table
rows = driver.find_elements_by_css_selector(
    "table.batchresultstablex>tbody>tr")

table = [[col.get_attribute("innerHTML").splitlines(
) for col in row.find_elements_by_css_selector("td")] for row in rows]

# turn into a dictionary for easier manipulation
NEBprimerDict = {}
for primer in table:
    currentPrimerName = primer[0][0]
    currentPrimerSeq = primer[1][0]
    currentPrimerTm = primer[2][0]
    currentPrimerTa = primer[2][0]
    NEBprimerDict.update(
        {currentPrimerName: [currentPrimerSeq, currentPrimerTm]})
print(NEBprimerDict)


time.sleep(100000)

# driver.close()

# PATH=$(pwd):$PATH python3 NEBWebscraper.py

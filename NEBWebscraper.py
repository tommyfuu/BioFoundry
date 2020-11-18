
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


def primerDictToNEBPrimerSeq(primerDict):
    """turn a primer dict from primer3 in fastCloningPrimer to the NEB readdable format"""
    NEBPrimerString = ""
    for primerPairName, primerPairInfo in primerDict.items():
        currentLPrimerName = str(primerPairName) + "Left"
        currentLPrimerSeq = primerPairInfo[0][2]
        currentRPrimerName = str(primerPairName) + "Right"
        currentRPrimerSeq = primerPairInfo[1][2]
        NEBPrimerString += currentLPrimerName + "; " + currentLPrimerSeq + \
            "; " + currentRPrimerName + "; " + currentRPrimerSeq + "\n"
    return NEBPrimerString


def NEBWebscraper(primersSeq, phusionprimerOptTm):
    """Use NEB to check the melting temperature and annealing temperature of all primers"""
    # open the tm calculator headlessly
    options = webdriver.chrome.options.Options()
    options.headless = True
    cwd = os.getcwd() + '/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=cwd)
    driver.get("https://tmcalculator.neb.com/#!/batch")

    time.sleep(1)

    # set the enzyme to phusion
    driver.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div/div/div/div[2]/div[1]/form/div/div[1]/div/select[1]").send_keys("P\n")

    # set the primer input
    driver.find_element_by_id("batchinput").send_keys(
        primersSeq)
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

    # close the chrome driver
    driver.close()

    # turn into a dictionary for easier manipulation
    NEBprimerDict = {}
    # NEBprimerL = []
    # NEBprimerCleanL = []
    for primerIndex in range(len(table)):
        if primerIndex % 2 == 0:
            # left primer
            Lprimer = table[primerIndex]
            currentLPrimerName = Lprimer[0][0]
            currentLPrimerSeq = Lprimer[1][0][1:]
            currentLPrimerTm = Lprimer[2][0]
            currentLPrimerTa = float(Lprimer[3][0])

            # right primers
            Rprimer = table[primerIndex+1]
            currentRPrimerName = Rprimer[0][0]
            currentRPrimerSeq = Rprimer[1][0][1:]
            currentRPrimerTm = Rprimer[2][0]
            currentRPrimerTa = float(Rprimer[3][0])
            # primer pair name
            primerPairName = currentLPrimerName[-4:]
            phusionPrimerLowerBound = float(phusionprimerOptTm)-5
            phusionPrimerUpperBound = float(phusionprimerOptTm)+5
            print(phusionPrimerLowerBound)
            print(phusionPrimerUpperBound)
            if (currentLPrimerTa > phusionPrimerLowerBound) and (currentLPrimerTa < phusionPrimerUpperBound):
                if (currentRPrimerTa > phusionPrimerLowerBound) and (currentRPrimerTa < phusionPrimerUpperBound):
                    NEBprimerDict.update(
                        {primerPairName: [['left', currentLPrimerTa, currentLPrimerSeq], ['right', currentRPrimerTa, currentRPrimerSeq]]})
                # NEBprimerL.append(
                #     [currentPrimerName, currentPrimerTm, currentPrimerTa, currentPrimerSeq])
                # NEBprimerCleanL.append([currentPrimerName, currentPrimerSeq])
    # print(NEBprimerDict)
    return NEBprimerDict
    # time.sleep(100000)

# driver.close()

# PATH=$(pwd):$PATH python3 NEBWebscraper.py

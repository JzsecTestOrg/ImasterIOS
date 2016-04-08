# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback

def tradeTab(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('tab', 'trade', 'tradeTab', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件tradeTab未找到\n" + traceback.format_exc())

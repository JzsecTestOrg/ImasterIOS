# -*- coding: GBK -*-
__author__ = 'xuwen'

import unittest
from TestCases import welcome, register
from CommonMethods import generateLog, globalData, checkMail, Data, driverInit, driverQuit, dataBase, result



class Register(unittest.TestCase):
        def setUp(self):
            globalData.MODULE = 'init'
            driverInit.deviceSetup(self)


        def tearDown(self):
            driverQuit.driverQuit(self)


        def test_register(self):
            globalData.MODULE = 'welcome'
            welcome.welcome(self)
            globalData.MODULE = 'register'
            try:
            # for i in range(17, Data.getCasenumber('register')):
                register.register(self, 30)
                generateLog.generate_log()
                globalData.LOG = ''
            except:
                generateLog.generate_log()
                globalData.LOG = ''




def suite():
    RegisterTestSuite = unittest.makeSuite(Register, 'test')
    return RegisterTestSuite

def log():
    generateLog.generate_log()



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #注册
    runner.run(suite())

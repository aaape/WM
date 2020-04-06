import unittest
from selenium import webdriver

implicility_wait
# 在setUp方法中加入隐式等待时间10S，webdriver找不到该元素将会等待10S,超过10S将会抛出NoSuchElementExpection的异常
# 适用于异步需求 ，当网络延迟或AJAX请求，DOM没有 加载出来
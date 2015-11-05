#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import wx
import os
import sys
import socket

reload(sys)
sys.setdefaultencoding('utf8')
socket.setdefaulttimeout(2.0)

from threading import Thread
#from wx.lib.pubsub import Publisher

########################################################################
__myversion = "bate 2.0"
__author = "jasonzhang"
########################################################################
class TestThread(Thread):
    """Test Worker Thread Class."""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)      
        #self.start()    # start the thread
 
    #----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
   
 
    #----------------------------------------------------------------------
    def postTime(self, amt):
        """
        Send time to GUI
        """
        amtOfTime = (amt + 1) * 10
        Publisher().sendMessage("update", amtOfTime)
 
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self, name):
        wx.Frame.__init__(self, None, wx.ID_ANY, name, size=(300,300))
        self.SetSize((400, 300))
        panel = wx.Panel(self, -1)
        label1 = wx.StaticText(panel, -1, u"输入文件: ")
        label2 = wx.StaticText(panel, -1, u"输出文件: ")
       
        self.sizeCtrl = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY, size=wx.Size(200, -1))
        self.posCtrl = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY, size = wx.Size(200, -1))
       
        self.InputBtn = wx.Button(panel, label = u"浏览")
        self.InputBtn.Bind(wx.EVT_BUTTON, self.onInput)
        self.OutputBtn = wx.Button(panel, label = u"浏览")
        self.OutputBtn.Bind(wx.EVT_BUTTON, self.onOutput)
        self.OnBeginBtn = wx.Button(panel, label="START!")
        self.OnBeginBtn.Bind(wx.EVT_BUTTON, self.onBegin)
        self.SettingBtn = wx.Button(panel, label = u"设置")
        self.SettingBtn.Bind(wx.EVT_BUTTON, self.onSetting)
       
        space = wx.StaticText(panel, -1, "")
       
       
        self.panel = panel

        # Use some sizers for layout of the widgets
        sizer = wx.GridBagSizer(vgap=3, hgap=3)
#        sizer = wx.FlexGridSizer(3, 3, 5, 5)
        sizer.Add(label1, pos=(0,0))
        sizer.Add(self.sizeCtrl, pos=(0,1))
        sizer.Add(self.InputBtn, pos=(0,2))
        sizer.Add(label2, pos=(1,0))
        sizer.Add(self.posCtrl, pos=(1,1))
        sizer.Add(self.OutputBtn, pos=(1,2))
        sizer.Add(self.OnBeginBtn, pos=(2,1), span=wx.DefaultSpan,flag = wx.CENTER)
        sizer.Add(self.SettingBtn, pos=(2,2), span=wx.DefaultSpan,flag = wx.CENTER)
       

        border = wx.BoxSizer()
        border.Add(sizer, 0, wx.ALL, 15)
        panel.SetSizerAndFit(border)
        self.Fit()
       
    def onInput(self, event):
        file_wildcard = "All files(*.*)|*.*"
        dlg = wx.FileDialog(self, u"输入文件",
                            os.getcwd(),
                            style = wx.OPEN,
                            wildcard = file_wildcard)
        filename = ""
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
        dlg.Destroy()
        self.sizeCtrl.SetValue(filename)
       
    def onOutput(self, event):
        file_wildcard = "All files(*.*)|*.*"
        dlg = wx.FileDialog(self, u"输入文件",
                            os.getcwd(),
                            style = wx.OPEN,
                            wildcard = file_wildcard)
        filename = ""
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
        dlg.Destroy()
        self.posCtrl.SetValue(filename)
       
 
    #----------------------------------------------------------------------
    def onBegin(self, event):
        """
        Runs the thread
        """
        self.thread_arr = []
        for i in range(2):
            mythread = TestThread()
            self.thread_arr.append(mythread)
        for i in range(2):
            self.thread_arr[i].start()
        for i in range(2):
            self.thread_arr[i].join()       
        #self.displayLbl.SetLabel("Thread started!")
        #self.btn = event.GetEventObject()
        #self.btn.Disable()
        
    def onSetting(self):
        pass
        
 
    #----------------------------------------------------------------------
    def updateDisplay(self, msg):
        """
        Receives data from thread and updates the display
        """
        t = msg.data
        if isinstance(t, int):
            self.displayLbl.SetLabel("Time since thread started: %s seconds" % t)
        else:
            self.displayLbl.SetLabel("%s" % t)
            self.btn.Enable()
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm(u"竞品关键字查询 %s"%(__myversion)).Show()
    app.MainLoop()
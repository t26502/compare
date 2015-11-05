#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx
import socket
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

###########################################
__author = u'jasonzhang'
__version = u'bate 2.0'
###########################################

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        self.width = 325
        self.height = 150
        super(MyFrame, self).__init__(parent, title = title, size = (self.width, self.height), style = wx.MINIMIZE_BOX|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.CAPTION)
        self.InitUi()
        self.Centre()
        self.Show()
        self._enableflag = True
        self._setflag = True
        
    def InitUi(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 7)
        
        spacelabel = wx.StaticText(panel)
        sizer.Add(spacelabel, pos = (0, 0), flag = wx.TOP, border = 0)
        labelinput = wx.StaticText(panel, label = u"输入: ")
        sizer.Add(labelinput, pos = (1, 0), flag = wx.TOP|wx.LEFT, border = 8)
        
        self.textinput = wx.TextCtrl(panel, size = wx.Size(200, -1))
        sizer.Add(self.textinput, pos=(1, 1), span = (1, 3), flag = wx.TOP|wx.EXPAND, border = 5)
        
        self.btninput = wx.Button(panel, label = u"浏览", size = wx.Size(60, -1))
        sizer.Add(self.btninput, pos = (1, 4),flag = wx.TOP|wx.RIGHT, border = 8)
        self.btninput.Bind(wx.EVT_BUTTON, self.onInut)
        
        labeloutput = wx.StaticText(panel, label = u"输出: ")
        sizer.Add(labeloutput, pos = (2, 0), flag = wx.TOP|wx.LEFT, border = 8)
                
        self.textoutput = wx.TextCtrl(panel, size = wx.Size(200, -1))
        sizer.Add(self.textoutput, pos=(2, 1), span = (1, 3), flag = wx.TOP|wx.EXPAND, border = 5)
                
        self.btnoutput = wx.Button(panel, label = u"浏览", size = wx.Size(60, -1))
        sizer.Add(self.btnoutput, pos = (2, 4),flag = wx.TOP|wx.RIGHT, border = 8)
        self.btnoutput.Bind(wx.EVT_BUTTON, self.onOutput)
        
        self.btnbegin = wx.Button(panel, label = u"START!")
        sizer.Add(self.btnbegin, pos = (3,2), flag = wx.TOP|wx.EXPAND, border = 8)
        self.btnbegin.Bind(wx.EVT_BUTTON, self.onBegin)
        
        
        
        self.btnhelp = wx.Button(panel, label = u'?', size = wx.Size(30, -1))
        sizer.Add(self.btnhelp, pos = (3, 0), flag = wx.TOP|wx.LEFT, border = 8)
        
        self.btnsetting = wx.Button(panel, label = u"设置", size = wx.Size(60, -1))
        sizer.Add(self.btnsetting, pos = (3, 4), flag = wx.TOP|wx.RIGHT, border = 8)
        self.btnsetting.Bind(wx.EVT_BUTTON, self.onSetting)
        
        sb = wx.StaticBox(panel, label = "Setting")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.mutiplebox = wx.CheckBox(panel, label = u'多线程')
        self.mutiplebox.SetValue(True)
        boxsizer.Add(self.mutiplebox, flag=wx.LEFT|wx.TOP, border=5)
        sizer.Add(boxsizer, pos = (1, 5), span = (2,2), flag = wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
        
        panel.SetSizer(sizer)
        
    def onInut(self, event):
        file_wildcard = "All files(*.*)|*.*|Txt files(*.txt)|*.txt"
        dlg = wx.FileDialog(self, u"输入文件",
                    os.getcwd(),
                    style = wx.OPEN,
                    wildcard = file_wildcard)
        filename = "123"
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
        dlg.Destroy()
        self.textinput.SetValue(filename)
        
    def onOutput(self, event):
        file_wildcard = "All files(*.*)|*.*|Txt files(*.txt)|*.txt"
        dlg = wx.FileDialog(self, u"输出文件",
                        os.getcwd(),
                        style = wx.OPEN,
                        wildcard = file_wildcard)
        filename = ""
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
        dlg.Destroy()
        self.textoutput.SetValue(filename)
        
    def lockbtn(self):
        if self._enableflag == True:
            self.textinput.Disable()
            self.textoutput.Disable()
            self.btnbegin.Disable()
            self.btnhelp.Disable()
            self.btninput.Disable()
            self.btnoutput.Disable()
            self.btnsetting.Disable()
            self._enableflag = False
        else:
            self.textinput.Enable()
            self.textoutput.Enable()
            self.btnbegin.Enable()
            self.btnhelp.Enable()
            self.btninput.Enable()
            self.btnoutput.Enable()
            self.btnsetting.Enable()
            self._enableflag = True
    def onSetting(self, event):
        if self._setflag == True:
            self.Size = wx.Size(450, -1)
            self._setflag = False
            self.btnsetting.Label=u"收起"
        else:
            self.Size = wx.Size(self.width, -1)
            self._setflag = True
            self.btnsetting.Label=u'设置'
        
    
    def onBegin(self, event):
        self.lockbtn()
        self.Size = wx.Size(-1, 400)
        
        self.lockbtn()
        
    
if __name__ == "__main__":
    app = wx.App()
    MyFrame(None, title = u"竞品查询")
    
    app.MainLoop()
        
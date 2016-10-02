# -*- coding: utf-8 -*-
#!/usr/bin/python
"""wxPython program to display all the running processes by """
import wx 
import psutil
class MyFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self, None, -1, U"14Lab1_2--进程列表", size=(1024, 650))
    #icon = wx.EmptyIcon()
    #icon.CopyFromBitmap(wx.Bitmap("task.ico", wx.BITMAP_TYPE_ANY))
    #self.SetIcon(icon)
    panel = wx.Panel(self, -1)
    wx.StaticText(panel, -1, u"进程ID：    模块名：", pos=(0, 0))
    wx.StaticText(panel, -1, u"进程ID：    模块名：", pos=(250, 0))
    wx.StaticText(panel, -1, u"进程ID：    模块名：", pos=(500, 0))
    wx.StaticText(panel, -1, u"进程ID：    模块名：", pos=(750, 0))
    posy = 20 
    i = 0
    for proc in psutil.process_iter():
        #reference: http://pythonhosted.org/psutil/#processes
        # psutil.get_pid_list() does not work in my computer
        try:
            pinfo = proc.as_dict()
            wx.StaticText(panel, -1, "%05x      %s"%(pinfo['pid'],pinfo['name']), pos=((i%4)*250, posy))
            i += 1
        except psutil.NoSuchProcess: pass
        if i % 4 == 0:
            posy += 20

if __name__ == '__main__':
  app = wx.App()
  frame = MyFrame()
  frame.Show(True)
  app.MainLoop()

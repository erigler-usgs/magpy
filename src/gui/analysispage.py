#!/usr/bin/env python

try:
    from magpy.stream import *
    from magpy.absolutes import *
    from magpy.transfer import *
    from magpy.database import *
except:
    from stream import *
    from absolutes import *
    from transfer import *
    from database import *

import wx

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

from wx.lib.pubsub import Publisher


class AnalysisPage(wx.Panel):
    #def __init__(self, parent):
    #    wx.Panel.__init__(self,parent,-1,size=(100,100))
    def __init__(self, *args, **kwds):
        wx.Panel.__init__(self, *args, **kwds)
        self.filterlist = ['flat','barthann','bartlett','blackman','blackmanharris','bohman','boxcar','cosine','flattop','hamming','hann','nuttall','parzen','triang','gaussian','wiener','spline','butterworth']
        self.filterlength = ['second','minute','hour','day','month','year','userdefined']
        self.comp = ['xyz', 'hdz', 'idf']
        self.createControls()
        self.doLayout()
        
    # Widgets
    def createControls(self):
        self.head1Label = wx.StaticText(self, label="Information:")
        self.head2Label = wx.StaticText(self, label="Basic methods:")
        self.head3Label = wx.StaticText(self, label="Filtering:")
        self.head4Label = wx.StaticText(self, label="Further functions:")
        # 1. Section
        self.samplingrateLabel = wx.StaticText(self, label="Samp. period (sec):")
        self.samplingrateTextCtrl = wx.TextCtrl(self, value="--",size=(120,30))
        self.amountLabel = wx.StaticText(self, label="N of data point:")
        self.amountTextCtrl = wx.TextCtrl(self, value="--",size=(120,30))
        self.typeLabel = wx.StaticText(self, label="Datatype:")
        self.typeTextCtrl = wx.TextCtrl(self, value="--",size=(120,30))
        self.keysLabel = wx.StaticText(self, label="Used keys:")
        self.keysTextCtrl = wx.TextCtrl(self, value="--",size=(120,30))
        self.samplingrateTextCtrl.Disable()
        self.amountTextCtrl.Disable()
        self.typeTextCtrl.Disable()
        self.keysTextCtrl.Disable()

        # 2. Section
        self.outlierButton = wx.Button(self,-1,"Remove outlier",size=(120,30))
        self.outlieroptionsButton = wx.Button(self,-1,"Options",size=(120,30))
        self.derivativeButton = wx.Button(self,-1,"Derivative",size=(120,30))
        self.fitButton = wx.Button(self,-1,"Fit",size=(120,30))
        self.offsetButton = wx.Button(self,-1,"Offsets",size=(120,30))
        self.activityButton = wx.Button(self,-1,"Activity",size=(120,30))
        # 3. Section
        self.selectfilterLabel = wx.StaticText(self, label="Select type:")
        self.selectfilterComboBox = wx.ComboBox(self, choices=self.filterlist,
            style=wx.CB_DROPDOWN, value=self.filterlist[14])
        self.selectlengthLabel = wx.StaticText(self, label="Select length:")
        self.selectlengthComboBox = wx.ComboBox(self, choices=self.filterlength,
            style=wx.CB_DROPDOWN, value=self.filterlength[0])
        self.filterButton = wx.Button(self,-1,"Filter!",size=(120,30))

 
    def doLayout(self):
        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=8, cols=2, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        # Add the controls to the sizers:
        for control, options in \
                [(self.head1Label, noOptions),
                  emptySpace,
                 (self.samplingrateLabel, noOptions),
                 (self.samplingrateTextCtrl, expandOption),
                 (self.amountLabel, noOptions),
                 (self.amountTextCtrl, expandOption),
                 (self.typeLabel, noOptions),
                 (self.typeTextCtrl, expandOption),
                 (self.keysLabel, noOptions),
                 (self.keysTextCtrl, expandOption),
                  emptySpace,
                  emptySpace,
                 # section 2
                 (self.head2Label, noOptions),
                  emptySpace,
                 (self.outlierButton, dict(flag=wx.ALIGN_CENTER)),
                 (self.outlieroptionsButton, dict(flag=wx.ALIGN_CENTER)),
                 (self.derivativeButton, dict(flag=wx.ALIGN_CENTER)),
                  emptySpace,
                 (self.fitButton, dict(flag=wx.ALIGN_CENTER)),
                  emptySpace,
                 (self.offsetButton, dict(flag=wx.ALIGN_CENTER)),
                  emptySpace,
                 (self.activityButton, dict(flag=wx.ALIGN_CENTER)),
                  emptySpace,
                 # section 3
                 (self.head3Label, noOptions),
                  emptySpace,
                 (self.selectfilterLabel, noOptions),
                 (self.selectfilterComboBox, expandOption),
                 (self.selectlengthLabel, noOptions),
                 (self.selectlengthComboBox, expandOption),
                  emptySpace,
                 (self.filterButton, dict(flag=wx.ALIGN_CENTER)),
                 (self.head4Label, noOptions),
                  emptySpace,
                 # end 
                  emptySpace,
                  emptySpace,
                  emptySpace,
                  emptySpace]:
            gridSizer.Add(control, **options)

        for control, options in \
                [(gridSizer, dict(border=5, flag=wx.ALL))]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)


 

import cv2, os, simplejson as json
from confapp import conf
from pyforms_gui.controls.control_button import ControlButton


class Module(object):

    def __init__(self):
        """
        This implements the Path edition functionality
        """
        super(Module, self).__init__()

        self.toolbar.append(ControlButton('Import Git Repo', icon=conf.ANNOTATOR_ICON_IMPORTDB))
        self.toolbar.append(ControlButton('Sync Git', icon=conf.ANNOTATOR_ICON_SYNC))

    ######################################################################################
    #### IO FUNCTIONS ####################################################################
    ######################################################################################


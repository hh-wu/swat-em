# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from swat_em.datamodel import datamodel







def test_image_export():

    def clean_up():
        try:
            os.remove('plot_layout.png')
            os.remove('plot_star.png')
            os.remove('plot_wf.png')
            os.remove('plot_MMK.png')
        except:
            pass
    
    data = datamodel()
    data.genwdg(Q = 12, P = 2, m = 3, w = -1, layers = 1, turns = 1000)
    data.analyse_wdg()
    
    print('Test image export')
    clean_up() # clear old data
    
    data.plot_layout('plot_layout.png', res = [1200, 900])
    assert os.path.isfile('plot_layout.png')
    
    data.plot_star('plot_star.png', res = [800, 600])
    assert os.path.isfile('plot_star.png')
    
    data.plot_windingfactor('plot_wf.png', mechanical = False, res = [800, 600])
    assert os.path.isfile('plot_wf.png')
    
    data.plot_MMK('plot_MMK.png', res = [800, 600], phase = 0)
    assert os.path.isfile('plot_MMK.png')

    clean_up() # clear data
    

if __name__ == '__main__':
    test_image_export()






# -*- coding: utf-8 -*-
""" main.py """

from configs.config import CFG
from model.GW_SkyLocator import GW_SkyLocator


def run():
    """Builds model, loads data, trains and evaluates"""
    for i in range(1):
        
        CFG["train"]["output_filename"] = 'skymaps/BBH/Injection_run_BBH_3_det_design_test_Gaussian_KDE_test_GPU_'+str(i)+'.hdf'
    
        print(CFG["train"]["output_filename"])
        
        model = GW_SkyLocator(CFG)
        model.load_data()
    #    model.load_test_data
        model.construct_model()
        model.construct_flow(training=True)
        model.train()
        model.obtain_probability_density()
        


if __name__ == '__main__':
    run()
  
            

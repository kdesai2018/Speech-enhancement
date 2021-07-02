import os
from os.path import isfile, join, isdir
import subprocess
import shutil  
# import rosbag

data_dir = 'noisy-sawyer-data/'
output_data_dir = 'cleaned-sawyer-data'

users = [d for d in os.listdir(data_dir) if isdir(join(data_dir,d))]
task_name = ['/box', '/cutting']
task_type = ['/kt', '/video']
file_name = ['/audio.wav', '/env.wav']

# python main.py --mode prediction --weights_folder weights --dir_save_prediction cleaned-sawyer-data/ --audio_dir_prediction noisy-sawyer-data/ --audio_input_prediction
# <NAME OF FILE IN NOISE-SAWYER-DATA/> --audio_output_prediction cleaned_sawyer_audio.wav

cmd1 = "python main.py --mode prediction --weights_folder weights --dir_save_prediction cleaned-sawyer-data/ --audio_dir_prediction noisy-sawyer-data/ --audio_input_prediction "
cmd2 = " --audio_output_prediction "
# loop through users
for user in users:
    for tn in task_name:
        for tt in task_type:
            for fn in file_name:
                curr = user+tn+tt+fn
                spl = fn.split('.')
                o_fn = spl[0]+'-cleaned'+'.wav'
                out_curr = user+tn+tt+o_fn
                file_to_make = output_data_dir+'/'+user+tn+tt
                # os.system('mkdir -p '+file_to_make)
                os.system(cmd1+curr+cmd2+out_curr)
                # exit(0)
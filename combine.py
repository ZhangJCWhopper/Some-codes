import wave
import random
import os
import subprocess
random.seed(128)

def expand_noise(dir):
    noises = filter(lambda a: a.endswith(".wav"), os.listdir(dir))
    os.chdir(dir)
    for n in noises:
        r = random.randint(1,10)
        cmd = ["sox"]
        for _ in range(r):
            cmd.append(n)
    cmd.append("../noises/"+n)
    subprocess.call(cmd)


def data_aug(dir):
    #data augmentation
    global noises
    noises = map(lambda f: os.path.join("noises", f), os.listdir("noises"))
    #full path of long noise files
    temp_dir = os.path.abspath("tmp")
    if not os.path.isdir(temp_dir):
        os.mkdir(temp_dir)
    def process_file(f):
        #f should be in full relative path
        print f
        w = wave.open(f)
        frame_num = w.getnframes()

        noise_num = random.randint(2, 5)
        for _ in xrange(noise_num):
            noise = random.choice(noises)
            noise_w = wave.open(noise)
            noise_frame_num = noise_w.getnframes()
            clip_start = noise_frame_num-frame_num
            clip_len = frame_num
            if clip_start <0:
                clip_len = noise_frame_num
                clip_start = 0
            #sox in.wav out.wav trim {start}s {len}s
            trim_noise_cmd = ["sox", noise, os.path.join(temp_dir, str(_)+".wav"), "trim", "{0}s".format(clip_start), "{0}s".format(clip_len)]
            subprocess.call(trim_noise_cmd)
        #sox -m autio.wav noise.wav noise2.wav out.wav
        combine_cmd = ["sox", "-m", f]
        combine_cmd += [os.path.join(temp_dir, str(_)+".wav") for _ in xrange(noise_num) ] 
        combine_cmd +=  [f.replace("/original/", "/processed/")]
        subprocess.call(combine_cmd)
        for _ in xrange(noise_num):
            os.remove(os.path.join(temp_dir, str(_)+".wav"))
        return " ".join(combine_cmd)

    for r, ds, fs in os.walk(dir):
        for d in ds:
            new_d = (os.path.join(r, d) ).replace("/original/", "/processed/") 
            if not os.path.isdir(new_d):
                os.makedirs(new_d)
        for f in fs:
            if f.endswith(".wav"):
                print process_file(os.path.join(r, f))
            else:
                copy_cmd = ["cp", f, f.replace("/original/", "/processed/")]
                subprocess.call(copy_cmd)
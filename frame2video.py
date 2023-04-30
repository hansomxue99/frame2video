import cv2
import os
from tqdm import tqdm

def main():    
    frame_path = ".//frame"
    frame_len = len(os.listdir(frame_path))
    frame1 = cv2.imread('.//frame//001.png')

    fps = 30          # fps
    size = (frame1.shape[1], frame1.shape[0]) # video size
    video = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'XVID'), fps, size)
    
    for i in tqdm(range(frame_len)):      
        image_path = frame_path + "//%03d.png" % (i+1)
        img = cv2.imread(image_path)
        video.write(img)
    print('finished')
    video.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
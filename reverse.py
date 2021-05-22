#==============================================#
#    Github: http://github.com/Hotdogishot     #
#=============================================#
import cv2
def reverse(inputVideo, outputVideo, fps):
    # load all video frames
    vidcap = cv2.VideoCapture(inputVideo)
    success,image = vidcap.read()
    frames = []
    while success:
        frames.append(image)  
        success, image = vidcap.read()

    # reverse frames
    height, width, layers = frames[0].shape
    size = (width,height)
    out = cv2.VideoWriter(outputVideo,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frames)-1, -1, -1):
        out.write(frames[i])
    out.release()

if __name__ == "__main__":
    inputVideo = "./Never_Gonna_Give_You_Up.mp4"
    outputVideo = "./output.avi"
    fps = 25.0
    reverse(inputVideo, outputVideo, fps)

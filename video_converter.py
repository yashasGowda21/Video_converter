import cv2
from converter import Converter
import logging
logging.basicConfig(level=logging.INFO)

logging.info("Converting annotated video")
# Converting video to h264 codec format
conv = Converter()
# Video file that needs to be converted
def video_converter(video_file):
    """
    Args: 
    video_file: mp4 file path
    """
    info = conv.probe(video_file)
    # new compressed file
    cap = cv2.VideoCapture()
    source_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    source_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = cap.get(cv2.CAP_PROP_FPS)
    shape = (source_h, source_w)
    converted_video = '/'.join(
        video_file.split('/')[:-1])+'/compressed_video.mp4'
    convert = conv.convert(video_file, converted_video, {
        'format': 'mp4',
        'audio': {
            'codec': 'aac',
            'samplerate': 11025,
            'channels': 2
        },
        'video': {
            'codec': 'h264',
            'width': source_w,
            'height': source_h,
            'fps': fps
        }})
    for timecode in convert:
        logging.info(f'\rConverting ({timecode:.2f}) ...')


if __name__ == "__main__":
    video_file_path = input("Enter video_file path : ")
    video_converter(video_file_path)
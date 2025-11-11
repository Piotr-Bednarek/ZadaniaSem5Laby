import wave
import cv2
import numpy as np

def bmp_to_wav(bmp_path, wav_path, sample_rate=44100):
    """
    Convert a BMP image to a WAV audio file.
    The pixel data is interpreted as audio samples.
    """
    # Read the BMP image
    img = cv2.imread(bmp_path)
    
    if img is None:
        raise ValueError(f"Could not read image from {bmp_path}")
    
    # Get image dimensions (OpenCV returns BGR by default)
    height, width = img.shape[:2]
    pixels = img
    
    # Flatten the pixel array (height x width x 3) to 1D array
    audio_data = pixels.flatten()
    
    # Convert to 16-bit signed integers for WAV format
    # Scale from 0-255 to -32768 to 32767
    audio_data = ((audio_data.astype(np.float32) - 127.5) * 256).astype(np.int16)
    
    # Write WAV file
    with wave.open(wav_path, 'w') as wav_file:
        # Set parameters: nchannels, sampwidth, framerate, nframes, comptype, compname
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 2 bytes per sample (16-bit)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data.tobytes())
    
    # Store metadata for reconstruction
    channels = img.shape[2] if len(img.shape) == 3 else 1
    return width, height, channels

def wav_to_bmp(wav_path, bmp_path, width, height, channels=3):
    """
    Convert a WAV audio file back to a BMP image.
    Requires the original image dimensions to reconstruct properly.
    """
    # Read WAV file
    with wave.open(wav_path, 'r') as wav_file:
        # Read all frames
        frames = wav_file.readframes(wav_file.getnframes())
        # Convert bytes to numpy array of 16-bit integers
        audio_data = np.frombuffer(frames, dtype=np.int16)
    
    # Convert back from 16-bit audio range to 8-bit pixel range
    pixel_data = ((audio_data.astype(np.float32) / 256) + 127.5).astype(np.uint8)
    
    # Calculate expected size
    expected_size = width * height * channels
    
    # Trim or pad if necessary
    if len(pixel_data) > expected_size:
        pixel_data = pixel_data[:expected_size]
    elif len(pixel_data) < expected_size:
        # Pad with zeros if data is shorter
        pixel_data = np.pad(pixel_data, (0, expected_size - len(pixel_data)))
    
    # Reshape back to image dimensions
    if channels == 3:
        pixel_data = pixel_data.reshape((height, width, 3))
    elif channels == 1:
        pixel_data = pixel_data.reshape((height, width))
    else:
        pixel_data = pixel_data.reshape((height, width, channels))
    
    # Save image using OpenCV
    cv2.imwrite(bmp_path, pixel_data)

# Example usage
if __name__ == "__main__":
    # Convert BMP to WAV
    input_bmp = "input.bmp"
    output_wav = "output.wav"
    
    #bmp_to_wav('beachgs.bmp',output_wav)
    wav_to_bmp('toconvert.wav','new.bmp',600,400,channels=1)
    

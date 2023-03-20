from pydub import AudioSegment
import os

i = 0

for dirname, _, filenames in os.walk("m4afiles"):
    for filename in filenames:
        m4a_file = os.path.join(dirname, filename)

        start_pos = m4a_file.find('/', 7)
        end_pos = m4a_file.rfind('/')

        alpha = m4a_file[start_pos + 1:end_pos]

        if (i != 0):
            if (before_alpha != alpha):
                i = 1
            else:
                i += 1
        else:
            i += 1

        before_alpha = alpha

        # print(start_pos, end_pos, imsi_breed)

        wav_filename = "wavfiles/" + str(alpha) + str(i) + ".wav"
        # print(wav_filename)
        track = AudioSegment.from_file(m4a_file, format='m4a')
        file_handle = track.export(wav_filename, format='wav')

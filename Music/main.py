import librosa

filename = librosa.util.example_audio_file()

y, sr = librosa.load(filename)

hop_length = 64
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length)

print 'Extimated tempo: %0.2f beats per minute' % tempo

beat_times = librosa.frames_to_time(beat_frames, sr=sr, hop_length=hop_length)

print 'Saving output to beat_times.csv'

librosa.output.times_csv('beat_times.csv', beat_times)
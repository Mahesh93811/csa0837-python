def count_segments(s):

    segments = s.split()
    return len(segments)

string = "Hello, how are you?"
segment_count = count_segments(string)
print(f"Number of segments: {segment_count}")

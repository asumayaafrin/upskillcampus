files = [
    "photo.jpg",
    "notes.pdf",
    "movie.mp4",
    "resume.docx",
    "image.png",
    "song.mp3"
]

images = []
documents = []
videos = []
others = []

for file in files:

    if file.endswith((".jpg", ".jpeg", ".png")):
        images.append(file)

    elif file.endswith((".pdf", ".docx", ".txt")):
        documents.append(file)

    elif file.endswith((".mp4", ".mkv")):
        videos.append(file)

    else:
        others.append(file)

print("Images Folder:")
print(images)

print("\nDocuments Folder:")
print(documents)

print("\nVideos Folder:")
print(videos)

print("\nOthers Folder:")
print(others)

print("\nFile Organization Completed!")
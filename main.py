from fastapi import FastAPI, File, UploadFile, Response
import database

app = FastAPI()

@app.post("/upload/")
async def upload(video: UploadFile = File(...)):
    video_id = fs.put(video.file, filename=video.filename)
    return {
        "status": "uploaded sucessfully",
        "video_id": str(video_id)
    }

@app.get("/stream/")
async def stream(video_id: str):
    video = fs.get(video_id)
    return Response(content=video, media_type="video/mp4")

@app.get("download/")
async def download(video_id: str):
    video = fs.get(video_id)
    return Response(
        content=video,
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={video.filename}"}
    )

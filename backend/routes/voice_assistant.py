from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from backend.utils.audio_utils import extract_audio_from_video, transcribe_audio, generate_voice_response
import uuid
import os

router = APIRouter()

@router.post("/voice-assistant", summary="Send voice/video and get product info")
async def voice_shopping_assistant(file: UploadFile = File(...)):
    temp_dir = "temp_audio"
    os.makedirs(temp_dir, exist_ok=True)

    file_id = str(uuid.uuid4())
    input_path = os.path.join(temp_dir, f"{file_id}_{file.filename}")
    output_path = os.path.join(temp_dir, f"{file_id}.wav")

    # Save file temporarily
    with open(input_path, "wb") as f:
        f.write(await file.read())

    try:
        # 1. Extract audio from video (if video)
        await extract_audio_from_video(input_path, output_path)

        # 2. Transcribe audio to text
        transcript = await transcribe_audio(output_path)

        # 3. Process transcript as product question
        response_text = f"Umeuliza kuhusu: {transcript}. Hii bidhaa inapatikana kwenye stock yetu."

        # 4. Convert response to voice
        voice_path = await generate_voice_response(response_text, file_id)

        return {
            "message": response_text,
            "voice_reply_url": f"/static/responses/{file_id}.mp3"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

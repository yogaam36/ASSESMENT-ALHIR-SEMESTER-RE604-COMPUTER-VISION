import requests
import base64
import os
import csv
from difflib import SequenceMatcher

LMSTUDIO_URL = "http://localhost:1234/v1/chat/completions"
PROMPT = "What is the license plate number shown in this image? Respond only with the plate number."

IMAGE_DIR = "test"  # ganti sesuai nama folder gambar kamu
CSV_GT_PATH = "ground_truth.csv"
CSV_OUTPUT_PATH = "Hasil_Prediksi.csv"

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def send_to_lmstudio(image_path, prompt):
    encoded_image = encode_image_to_base64(image_path)
    payload = {
        "model": "llava-v1.5-7b-llamafile",  # ganti sesuai nama model aktif di LMStudio
        "prompt": prompt,
        "images": [encoded_image],
        "stream": False
    }
    response = requests.post(LMSTUDIO_URL, json=payload)
    result = response.json()
    return result.get("response", "").strip()

def cer_score(prediction, ground_truth):
    matcher = SequenceMatcher(None, ground_truth, prediction)
    opcodes = matcher.get_opcodes()
    S = D = I = 0
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == 'replace':
            S += max(i2 - i1, j2 - j1)
        elif tag == 'delete':
            D += (i2 - i1)
        elif tag == 'insert':
            I += (j2 - j1)
    N = len(ground_truth)
    return round((S + D + I) / N, 4) if N > 0 else 1.0

def main():
    results = []

    with open(CSV_GT_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            image_name = row["image"]
            gt = row["ground_truth"]
            image_path = os.path.join(IMAGE_DIR, image_name)

            if not os.path.exists(image_path):
                print(f"Image not found: {image_name}")
                continue

            print(f"Processing {image_name}...")
            pred = send_to_lmstudio(image_path, PROMPT)
            cer = cer_score(pred, gt)

            print(f"GT: {gt} | Pred: {pred} | CER: {cer}")
            results.append({
                "image": image_name,
                "ground_truth": gt,
                "prediction": pred,
                "CER_score": cer
            })

    # Simpan hasil ke CSV
    with open(CSV_OUTPUT_PATH, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["image", "ground_truth", "prediction", "CER_score"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Hasil disimpan di {CSV_OUTPUT_PATH}")

if __name__ == "__main__":
    main()
